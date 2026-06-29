#!/usr/bin/env python3
"""Create one local manual validation workspace for a date."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any


RECORD_FILES = {
    "signal": "signal.json",
    "information_gap": "information_gap.json",
    "opportunity": "opportunity.json",
    "todays_bet": "todays_bet.json",
    "validation_plan": "validation_plan.json",
    "validation_record": "validation_record.json",
    "revenue_signal": "revenue_signal.json",
    "rejection_signal": "rejection_signal.json",
    "alan_memory": "alan_memory.json",
}


def compact_date(date: str) -> str:
    return date.replace("-", "")


def timestamp(date: str) -> str:
    return f"{date}T00:00:00Z"


def validate_date(date: str) -> None:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        raise ValueError(f"date must use YYYY-MM-DD format: {date}")


def template_records(date: str) -> dict[str, dict[str, Any]]:
    compact = compact_date(date)
    now = timestamp(date)
    signal_id = f"sig_{compact}_001"
    gap_id = f"gap_{compact}_001"
    opportunity_id = f"opp_{compact}_001"
    bet_id = f"bet_{compact}_001"
    plan_id = f"plan_{compact}_001"
    record_id = f"record_{compact}_001"
    revenue_id = f"rev_{compact}_001"
    rejection_id = f"rej_{compact}_001"

    return {
        "signal": {
            "id": signal_id,
            "created_at": now,
            "updated_at": now,
            "source": "manual_review",
            "confidence": 0,
            "status": "draft",
            "captured_at": now,
            "title": "TODO: captured signal title",
            "raw_content": "TODO: paste the manually reviewed source claim",
            "summary": "TODO: summarize the buyer pain or market change",
            "tags": [],
            "language": "en"
        },
        "information_gap": {
            "id": gap_id,
            "created_at": now,
            "updated_at": now,
            "source": "manual_signal_review",
            "confidence": 0,
            "status": "draft",
            "name": "TODO: information gap name",
            "description": "TODO: describe the temporary asymmetric gap",
            "evidence_signal_ids": [signal_id],
            "who_has_the_gap": "TODO: who feels or knows this early",
            "who_needs_the_gap_closed": "TODO: who needs this solved",
            "why_now": "TODO: why timing matters today",
            "window_start": date,
            "window_risk": "TODO: what could close or invalidate the gap",
            "notes": "Manual placeholder; edit before rendering a real daily packet."
        },
        "opportunity": {
            "id": opportunity_id,
            "created_at": now,
            "updated_at": now,
            "source": gap_id,
            "confidence": 0,
            "status": "draft",
            "information_gap_id": gap_id,
            "customer_segment": "TODO: reachable customer segment",
            "buyer": "TODO: buyer or decision maker",
            "pain": "TODO: concrete pain",
            "offer": "TODO: manual service-first offer",
            "revenue_hypothesis": "TODO: why someone might pay",
            "distribution_path": "TODO: reachable manual path",
            "lifecycle_stage": "Birth",
            "pricing_guess": "TODO: first manual price guess",
            "riskiest_assumption": "TODO: assumption Today's Bet should test"
        },
        "todays_bet": {
            "id": bet_id,
            "created_at": now,
            "updated_at": now,
            "source": opportunity_id,
            "confidence": 0,
            "status": "planned",
            "opportunity_id": opportunity_id,
            "date": date,
            "action": "TODO: one action Alan will execute today",
            "timebox_minutes": 60,
            "expected_signal": "TODO: revenue or rejection signal expected from real people",
            "give_up_rule": "TODO: when to stop, follow up, pivot, or record rejection",
            "target_personas": [],
            "success_criteria": "TODO: minimum useful signal",
            "notes": "Do not build before buyer validation."
        },
        "validation_plan": {
            "id": plan_id,
            "created_at": now,
            "updated_at": now,
            "source": bet_id,
            "confidence": 0,
            "status": "planned",
            "todays_bet_id": bet_id,
            "opportunity_id": opportunity_id,
            "hypothesis": "TODO: what this action tests",
            "action_steps": [
                "TODO: identify reachable people",
                "TODO: send or make the manual offer",
                "TODO: record every reply, objection, referral, and silence"
            ],
            "target_count": 0,
            "timebox_minutes": 60,
            "success_threshold": "TODO: minimum useful validation signal",
            "script": "TODO: outreach, offer, or interview script",
            "channels": [],
            "give_up_rule": "TODO: stop rule for the plan",
            "risk_notes": "Avoid product work before buyer signal."
        },
        "validation_record": {
            "id": record_id,
            "created_at": now,
            "updated_at": now,
            "source": plan_id,
            "confidence": 0,
            "status": "draft",
            "validation_plan_id": plan_id,
            "executed_at": now,
            "actions_taken": [],
            "outcome": "TODO: what happened",
            "lesson": "TODO: what Alan learned",
            "people_contacted": 0,
            "responses": [],
            "revenue_signal_ids": [],
            "rejection_signal_ids": [],
            "next_action": "TODO: next action after recording",
            "time_spent_minutes": 0
        },
        "revenue_signal": {
            "id": revenue_id,
            "created_at": now,
            "updated_at": now,
            "source": record_id,
            "confidence": 0,
            "status": "active",
            "validation_record_id": record_id,
            "signal_type": "serious_reply",
            "strength": "weak",
            "evidence": "TODO: payment-adjacent evidence",
            "buyer": "TODO: buyer or referrer",
            "next_step": "TODO: next step toward payment",
            "notes": "Post-execution placeholder; optional until execution produces a real RevenueSignal."
        },
        "rejection_signal": {
            "id": rejection_id,
            "created_at": now,
            "updated_at": now,
            "source": record_id,
            "confidence": 0,
            "status": "active",
            "validation_record_id": record_id,
            "rejection_type": "silence",
            "lesson": "TODO: what the rejection or silence teaches",
            "stated_reason": "TODO: stated reason if any",
            "implicit_reason": "TODO: inferred reason if any",
            "segment": "TODO: affected segment",
            "objection": "TODO: objection or silence",
            "follow_up_date": date,
            "notes": "Post-execution placeholder; optional until execution produces a real RejectionSignal."
        },
        "alan_memory": {
            "id": f"memory_{compact}",
            "created_at": now,
            "updated_at": now,
            "source": record_id,
            "confidence": 0,
            "status": "active",
            "period": date,
            "validated_patterns": [],
            "rejected_patterns": [],
            "lessons": [],
            "strong_segments": [],
            "weak_segments": [],
            "money_dna_updates": [],
            "weekly_revenue_signals": [],
            "next_biases": []
        }
    }


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def copy_sample_records(day_dir: Path, date: str, sample_dir: Path) -> None:
    for entity, target_name in RECORD_FILES.items():
        source = sample_dir / f"{entity}.sample.json"
        if not source.exists():
            raise ValueError(f"missing sample record: {source}")
        target = day_dir / target_name
        shutil.copyfile(source, target)
        if entity == "todays_bet":
            data = json.loads(target.read_text(encoding="utf-8"))
            data["date"] = date
            write_json(target, data)


def create_workspace(date: str, daily_root: Path, from_sample: bool, sample_dir: Path) -> Path:
    validate_date(date)
    day_dir = daily_root / date
    if day_dir.exists():
        raise ValueError(f"daily workspace already exists: {day_dir}")
    day_dir.mkdir(parents=True)

    if from_sample:
        copy_sample_records(day_dir, date, sample_dir)
    else:
        records = template_records(date)
        for entity, filename in RECORD_FILES.items():
            write_json(day_dir / filename, records[entity])
    return day_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a local manual Alan OS daily validation workspace."
    )
    parser.add_argument("--date", required=True, help="Daily workspace date in YYYY-MM-DD format.")
    parser.add_argument(
        "--daily-root",
        type=Path,
        default=Path("data/daily"),
        help="Root directory for daily manual records.",
    )
    parser.add_argument(
        "--from-sample",
        action="store_true",
        help="Copy data/sample records as examples instead of empty manual templates.",
    )
    parser.add_argument(
        "--sample-dir",
        type=Path,
        default=Path("data/sample"),
        help="Sample record directory used only with --from-sample.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        day_dir = create_workspace(args.date, args.daily_root, args.from_sample, args.sample_dir)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Created daily workspace: {day_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
