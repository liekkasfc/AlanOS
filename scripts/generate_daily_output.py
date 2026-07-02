#!/usr/bin/env python3
"""Render one manual-first Alan OS daily action packet from local JSON records."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ACTIVE_BET_STATUSES = {"planned", "active"}
ENTITY_PREFIXES = (
    "information_gap",
    "validation_record",
    "validation_plan",
    "rejection_signal",
    "revenue_signal",
    "todays_bet",
    "alan_memory",
    "alan_context",
    "opportunity",
    "signal",
)


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: invalid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return data


def infer_entity(path: Path) -> str | None:
    name = path.name
    for prefix in ENTITY_PREFIXES:
        if name.startswith(prefix):
            return prefix
    return None


def load_records(records_dir: Path) -> dict[str, list[dict[str, Any]]]:
    if not records_dir.exists() or not records_dir.is_dir():
        raise ValueError(f"records directory not found: {records_dir}")

    records: dict[str, list[dict[str, Any]]] = {prefix: [] for prefix in ENTITY_PREFIXES}
    for path in sorted(records_dir.glob("*.json")):
        entity = infer_entity(path)
        if entity:
            records[entity].append(load_json(path))
    return records


def index_by_id(records: list[dict[str, Any]], entity: str) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for record in records:
        record_id = record.get("id")
        if not isinstance(record_id, str) or not record_id:
            raise ValueError(f"{entity} record missing string id")
        if record_id in indexed:
            raise ValueError(f"duplicate {entity} id: {record_id}")
        indexed[record_id] = record
    return indexed


def select_one_bet(records: dict[str, list[dict[str, Any]]], date: str) -> dict[str, Any]:
    bets = [
        bet
        for bet in records["todays_bet"]
        if bet.get("date") == date and bet.get("status") in ACTIVE_BET_STATUSES
    ]
    if not bets:
        raise ValueError(f"no active Today's Bet found for {date}")
    if len(bets) > 1:
        ids = ", ".join(str(bet.get("id", "<missing id>")) for bet in bets)
        raise ValueError(f"more than one active Today's Bet found for {date}: {ids}")
    return bets[0]


def require_record(indexed: dict[str, dict[str, Any]], record_id: str, entity: str) -> dict[str, Any]:
    try:
        return indexed[record_id]
    except KeyError as exc:
        raise ValueError(f"missing {entity} record: {record_id}") from exc


def find_first(records: list[dict[str, Any]], key: str, value: str) -> dict[str, Any] | None:
    for record in records:
        if record.get(key) == value:
            return record
    return None


def bullet_list(items: list[Any]) -> str:
    if not items:
        return "- None recorded."
    return "\n".join(f"- {item}" for item in items)


def inline_list(items: list[Any]) -> str:
    return ", ".join(str(item) for item in items) if items else "None recorded"


def scalar(value: Any, fallback: str = "Not recorded") -> str:
    if value is None or value == "":
        return fallback
    return str(value)


def load_alan_context(records_dir: Path, memory_context_path: Path) -> dict[str, Any]:
    records_context_path = records_dir / "alan_context.json"
    if records_context_path.exists():
        return load_json(records_context_path)
    if memory_context_path.exists():
        return load_json(memory_context_path)
    return {}


def render_daily_output(
    records: dict[str, list[dict[str, Any]]],
    date: str,
    alan_context: dict[str, Any] | None = None,
) -> str:
    bet = select_one_bet(records, date)

    opportunities = index_by_id(records["opportunity"], "opportunity")
    gaps = index_by_id(records["information_gap"], "information_gap")
    signals = index_by_id(records["signal"], "signal")

    opportunity = require_record(opportunities, scalar(bet.get("opportunity_id")), "opportunity")
    gap = require_record(gaps, scalar(opportunity.get("information_gap_id")), "information_gap")
    evidence_signals = [
        require_record(signals, signal_id, "signal")
        for signal_id in gap.get("evidence_signal_ids", [])
    ]

    plan = find_first(records["validation_plan"], "todays_bet_id", scalar(bet.get("id")))
    record = None
    if plan:
        record = find_first(records["validation_record"], "validation_plan_id", scalar(plan.get("id")))

    revenue_by_id = index_by_id(records["revenue_signal"], "revenue_signal")
    rejection_by_id = index_by_id(records["rejection_signal"], "rejection_signal")
    revenue_signals = []
    rejection_signals = []
    if record:
        revenue_signals = [
            require_record(revenue_by_id, signal_id, "revenue_signal")
            for signal_id in record.get("revenue_signal_ids", [])
        ]
        rejection_signals = [
            require_record(rejection_by_id, signal_id, "rejection_signal")
            for signal_id in record.get("rejection_signal_ids", [])
        ]

    alan_context = alan_context or {}
    memory = records["alan_memory"][0] if records["alan_memory"] else {}

    action_steps = bullet_list(plan.get("action_steps", []) if plan else [])
    channels = inline_list(plan.get("channels", []) if plan else [])
    evidence = bullet_list(
        [
            f"{signal['id']}: {signal.get('summary', 'No summary recorded')}"
            for signal in evidence_signals
        ]
    )
    revenue_lines = bullet_list(
        [
            f"{signal['id']} ({signal.get('strength', 'unknown')}): {signal.get('evidence', '')}"
            for signal in revenue_signals
        ]
    )
    rejection_lines = bullet_list(
        [
            f"{signal['id']} ({signal.get('rejection_type', 'unknown')}): {signal.get('lesson', '')}"
            for signal in rejection_signals
        ]
    )

    context_constraints = (
        bullet_list(alan_context.get("constraints", []))
        if alan_context
        else "- No Alan Context recorded."
    )
    memory_biases = bullet_list(memory.get("next_biases", []))

    return f"""# Daily Action Packet

Date: {date}

## 今日唯一验证动作
ID: `{bet['id']}`

Action: {bet['action']}

Target personas: {inline_list(bet.get('target_personas', []))}

Timebox: {bet.get('timebox_minutes')} minutes

Expected signal: {bet['expected_signal']}

Give-up rule: {bet['give_up_rule']}

Success criteria: {scalar(bet.get('success_criteria'))}

Notes: {scalar(bet.get('notes'))}

## 为什么选它
Opportunity: `{opportunity['id']}` - {opportunity['offer']}

Customer segment: {opportunity['customer_segment']}

Buyer: {opportunity['buyer']}

Pain: {opportunity['pain']}

Revenue hypothesis: {opportunity['revenue_hypothesis']}

InformationGap: `{gap['id']}` - {gap['name']}

Why now: {gap['why_now']}

Riskiest assumption: {scalar(opportunity.get('riskiest_assumption'))}

Alan constraints:
{context_constraints}

## 执行计划
Plan ID: `{scalar(plan.get('id') if plan else None)}`

Hypothesis: {scalar(plan.get('hypothesis') if plan else None)}

Channels: {channels}

Target count: {scalar(plan.get('target_count') if plan else None)}

Action steps:
{action_steps}

Script:
{scalar(plan.get('script') if plan else None)}

Success threshold: {scalar(plan.get('success_threshold') if plan else None)}

Plan give-up rule: {scalar(plan.get('give_up_rule') if plan else None)}

Risk notes: {scalar(plan.get('risk_notes') if plan else None)}

## 证据与疑点
Evidence Signals:
{evidence}

Window risk: {scalar(gap.get('window_risk'))}

Lifecycle stage: {scalar(opportunity.get('lifecycle_stage'))}

Known RevenueSignals:
{revenue_lines}

Known RejectionSignals:
{rejection_lines}

AlanMemory next biases:
{memory_biases}

## 回填记录提示
- Record actions taken, people contacted, and time spent.
- Record RevenueSignals: booked calls, budget-confirming replies, paid requests, deposits, paid pilots, or buyer referrals.
- Record RejectionSignals: silence, not urgent, no budget, wrong buyer, already solved, price objection, timing objection, or scope mismatch.
- Record the lesson before opening a new research path.
- Update AlanMemory with one specific future selection bias.
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render one daily Alan OS action packet from local prepared JSON records."
    )
    parser.add_argument(
        "--sample-dir",
        "--records-dir",
        dest="records_dir",
        type=Path,
        default=Path("data/sample"),
        help="Directory containing local prepared JSON records.",
    )
    parser.add_argument("--date", required=True, help="Date for Today's Bet, in YYYY-MM-DD.")
    parser.add_argument(
        "--memory-context",
        type=Path,
        default=Path("memory/alan_context.json"),
        help="Fallback persistent Alan Context file.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        records = load_records(args.records_dir)
        alan_context = load_alan_context(args.records_dir, args.memory_context)
        print(render_daily_output(records, args.date, alan_context), end="")
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
