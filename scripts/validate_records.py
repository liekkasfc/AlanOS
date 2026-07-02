#!/usr/bin/env python3
"""Validate local Alan OS JSON records against local schemas."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_TIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
PLACEHOLDER_RE = re.compile(
    r"^\s*$|\b(TODO|TBD|PLACEHOLDER|REPLACE ME|FILL ME|FILL IN)\b",
    re.IGNORECASE,
)
PRE_EXECUTION_ENTITIES = {
    "signal",
    "information_gap",
    "opportunity",
    "todays_bet",
    "validation_plan",
}
POST_EXECUTION_ENTITIES = {
    "validation_record",
    "revenue_signal",
    "rejection_signal",
    "alan_memory",
}
LINK_ENTITIES = PRE_EXECUTION_ENTITIES | POST_EXECUTION_ENTITIES
RecordEntry = tuple[Path, dict[str, Any]]


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: invalid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return data


def load_schemas(schema_dir: Path) -> dict[str, dict[str, Any]]:
    schemas: dict[str, dict[str, Any]] = {}
    for path in sorted(schema_dir.glob("*.schema.json")):
        entity = path.name.removesuffix(".schema.json")
        schemas[entity] = load_json(path)
    if not schemas:
        raise ValueError(f"no schema files found in {schema_dir}")
    return schemas


def infer_entity(path: Path, schemas: dict[str, dict[str, Any]]) -> str | None:
    for entity in sorted(schemas, key=len, reverse=True):
        if path.name == f"{entity}.json" or path.name.startswith(f"{entity}."):
            return entity
    return None


def type_name(value: Any) -> str:
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    if value is None:
        return "null"
    return type(value).__name__


def matches_type(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return (isinstance(value, int) or isinstance(value, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    return True


def validate_field(field: str, value: Any, rule: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    expected_type = rule.get("type")
    if isinstance(expected_type, str) and not matches_type(value, expected_type):
        errors.append(f"{field}: expected {expected_type}, got {type_name(value)}")
        return errors

    enum = rule.get("enum")
    if isinstance(enum, list) and value not in enum:
        allowed = ", ".join(str(item) for item in enum)
        errors.append(f"{field}: expected one of [{allowed}], got {value!r}")

    if matches_type(value, "number"):
        minimum = rule.get("minimum")
        maximum = rule.get("maximum")
        if isinstance(minimum, (int, float)) and value < minimum:
            errors.append(f"{field}: expected >= {minimum}, got {value}")
        if isinstance(maximum, (int, float)) and value > maximum:
            errors.append(f"{field}: expected <= {maximum}, got {value}")

    if expected_type == "array" and isinstance(value, list):
        item_rule = rule.get("items")
        if isinstance(item_rule, dict):
            for index, item in enumerate(value):
                errors.extend(validate_field(f"{field}[{index}]", item, item_rule))

    field_format = rule.get("format")
    if field_format == "date" and isinstance(value, str) and not DATE_RE.fullmatch(value):
        errors.append(f"{field}: expected date format YYYY-MM-DD, got {value!r}")
    if field_format == "date-time" and isinstance(value, str) and not DATE_TIME_RE.fullmatch(value):
        errors.append(f"{field}: expected date-time format YYYY-MM-DDTHH:MM:SSZ, got {value!r}")

    return errors


def validate_record(path: Path, record: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in schema.get("required", []):
        if field not in record:
            errors.append(f"{field}: missing required field")

    for field, rule in schema.get("properties", {}).items():
        if field in record and isinstance(rule, dict):
            errors.extend(validate_field(field, record[field], rule))
    return [f"{path}: {error}" for error in errors]


def validate_records(
    records_dir: Path,
    schema_dir: Path,
    entity_filter: set[str] | None = None,
) -> list[str]:
    if not records_dir.exists() or not records_dir.is_dir():
        raise ValueError(f"records directory not found: {records_dir}")
    schemas = load_schemas(schema_dir)
    errors: list[str] = []
    json_paths = sorted(records_dir.glob("*.json"))
    if not json_paths:
        raise ValueError(f"no JSON records found in {records_dir}")

    for path in json_paths:
        entity = infer_entity(path, schemas)
        if entity is None:
            if entity_filter is None:
                errors.append(f"{path}: no matching schema found")
            continue
        if entity_filter is not None and entity not in entity_filter:
            continue
        try:
            record = load_json(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        errors.extend(validate_record(path, record, schemas[entity]))
    return errors


def load_records_by_entity(
    records_dir: Path,
    schema_dir: Path,
    entity_filter: set[str] | None = None,
) -> dict[str, list[RecordEntry]]:
    if not records_dir.exists() or not records_dir.is_dir():
        raise ValueError(f"records directory not found: {records_dir}")
    schemas = load_schemas(schema_dir)
    json_paths = sorted(records_dir.glob("*.json"))
    if not json_paths:
        raise ValueError(f"no JSON records found in {records_dir}")

    records: dict[str, list[RecordEntry]] = {}
    for path in json_paths:
        entity = infer_entity(path, schemas)
        if entity is None:
            continue
        if entity_filter is not None and entity not in entity_filter:
            continue
        records.setdefault(entity, []).append((path, load_json(path)))
    return records


def contains_todo(value: Any) -> bool:
    return isinstance(value, str) and "TODO" in value.upper()


def is_placeholder(value: Any) -> bool:
    return not isinstance(value, str) or PLACEHOLDER_RE.search(value) is not None


def iter_string_fields(value: Any, field_path: str = "") -> list[tuple[str, str]]:
    fields: list[tuple[str, str]] = []
    if isinstance(value, str):
        fields.append((field_path, value))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            path = f"{field_path}[{index}]" if field_path else f"[{index}]"
            fields.extend(iter_string_fields(item, path))
    elif isinstance(value, dict):
        for key, item in value.items():
            path = f"{field_path}.{key}" if field_path else key
            fields.extend(iter_string_fields(item, path))
    return fields


def add_ready_error(errors: list[str], path: Path, field: str, message: str) -> None:
    errors.append(f"{path}: {field}: {message}")


def validate_ready_record(path: Path, entity: str, record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field, value in iter_string_fields(record):
        if contains_todo(value):
            add_ready_error(errors, path, field, "contains TODO placeholder")

    if entity == "todays_bet":
        if is_placeholder(record.get("action")):
            add_ready_error(errors, path, "action", "must be filled before execution")
        target_personas = record.get("target_personas")
        if (
            not isinstance(target_personas, list)
            or not target_personas
            or any(is_placeholder(persona) for persona in target_personas)
        ):
            add_ready_error(errors, path, "target_personas", "must include at least one reachable persona")
        if is_placeholder(record.get("expected_signal")):
            add_ready_error(errors, path, "expected_signal", "must be filled before execution")
        if is_placeholder(record.get("give_up_rule")):
            add_ready_error(errors, path, "give_up_rule", "must be filled before execution")

    if entity == "validation_plan":
        target_count = record.get("target_count")
        if not isinstance(target_count, int) or isinstance(target_count, bool) or target_count <= 0:
            add_ready_error(errors, path, "target_count", "must be greater than 0")
        if is_placeholder(record.get("script")):
            add_ready_error(errors, path, "script", "must be filled before execution")
        action_steps = record.get("action_steps")
        if not isinstance(action_steps, list) or not action_steps:
            add_ready_error(errors, path, "action_steps", "must include executable steps")
        elif any(is_placeholder(step) for step in action_steps):
            add_ready_error(errors, path, "action_steps", "must not contain TODO placeholders")
    return errors


def validate_readiness(records_dir: Path, schema_dir: Path) -> list[str]:
    errors: list[str] = []
    for entity, entries in load_records_by_entity(records_dir, schema_dir, PRE_EXECUTION_ENTITIES).items():
        for path, record in entries:
            errors.extend(validate_ready_record(path, entity, record))
    return errors


def validate_result_record(path: Path, entity: str, record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field, value in iter_string_fields(record):
        if contains_todo(value):
            add_ready_error(errors, path, field, "contains TODO placeholder")

    if entity == "validation_record":
        actions_taken = record.get("actions_taken")
        if (
            not isinstance(actions_taken, list)
            or not actions_taken
            or any(is_placeholder(action) for action in actions_taken)
        ):
            add_ready_error(errors, path, "actions_taken", "must record at least one executed action")
        if is_placeholder(record.get("outcome")):
            add_ready_error(errors, path, "outcome", "must be filled after execution")
        if is_placeholder(record.get("lesson")):
            add_ready_error(errors, path, "lesson", "must be filled after execution")
        time_spent = record.get("time_spent_minutes")
        if not isinstance(time_spent, int) or isinstance(time_spent, bool) or time_spent <= 0:
            add_ready_error(errors, path, "time_spent_minutes", "must be greater than 0")
        revenue_signal_ids = record.get("revenue_signal_ids")
        rejection_signal_ids = record.get("rejection_signal_ids")
        if not isinstance(revenue_signal_ids, list):
            revenue_signal_ids = []
        if not isinstance(rejection_signal_ids, list):
            rejection_signal_ids = []
        if not revenue_signal_ids and not rejection_signal_ids:
            add_ready_error(
                errors,
                path,
                "revenue_signal_ids/rejection_signal_ids",
                "must include at least one recorded signal",
            )

    if entity == "alan_memory":
        next_biases = record.get("next_biases")
        if (
            not isinstance(next_biases, list)
            or not next_biases
            or any(is_placeholder(bias) for bias in next_biases)
        ):
            add_ready_error(errors, path, "next_biases", "must include at least one future selection bias")
    return errors


def validate_result(records_dir: Path, schema_dir: Path) -> list[str]:
    errors: list[str] = []
    for entity, entries in load_records_by_entity(records_dir, schema_dir, POST_EXECUTION_ENTITIES).items():
        for path, record in entries:
            errors.extend(validate_result_record(path, entity, record))
    return errors


def record_id(record: dict[str, Any]) -> str | None:
    value = record.get("id")
    return value if isinstance(value, str) and value else None


def build_id_index(records: dict[str, list[RecordEntry]]) -> dict[str, set[str]]:
    indexed: dict[str, set[str]] = {}
    for entity, entries in records.items():
        ids = {record_id(record) for _, record in entries}
        indexed[entity] = {value for value in ids if value is not None}
    return indexed


def add_link_error(
    errors: list[str],
    path: Path,
    field: str,
    target_entity: str,
    target_id: Any,
) -> None:
    errors.append(f"{path}: {field}: referenced {target_entity} not found: {target_id!r}")


def require_link(
    errors: list[str],
    path: Path,
    record: dict[str, Any],
    field: str,
    target_entity: str,
    ids_by_entity: dict[str, set[str]],
) -> None:
    target_id = record.get(field)
    if not isinstance(target_id, str) or target_id not in ids_by_entity.get(target_entity, set()):
        add_link_error(errors, path, field, target_entity, target_id)


def require_link_list(
    errors: list[str],
    path: Path,
    record: dict[str, Any],
    field: str,
    target_entity: str,
    ids_by_entity: dict[str, set[str]],
) -> None:
    target_ids = record.get(field, [])
    if target_ids is None:
        return
    if not isinstance(target_ids, list):
        add_link_error(errors, path, field, target_entity, target_ids)
        return
    for target_id in target_ids:
        if not isinstance(target_id, str) or target_id not in ids_by_entity.get(target_entity, set()):
            add_link_error(errors, path, field, target_entity, target_id)


def validate_links(records_dir: Path, schema_dir: Path) -> list[str]:
    records = load_records_by_entity(records_dir, schema_dir, LINK_ENTITIES)
    ids_by_entity = build_id_index(records)
    errors: list[str] = []

    for path, record in records.get("information_gap", []):
        require_link_list(errors, path, record, "evidence_signal_ids", "signal", ids_by_entity)
    for path, record in records.get("opportunity", []):
        require_link(errors, path, record, "information_gap_id", "information_gap", ids_by_entity)
    for path, record in records.get("todays_bet", []):
        require_link(errors, path, record, "opportunity_id", "opportunity", ids_by_entity)
    for path, record in records.get("validation_plan", []):
        require_link(errors, path, record, "todays_bet_id", "todays_bet", ids_by_entity)
        require_link(errors, path, record, "opportunity_id", "opportunity", ids_by_entity)
    for path, record in records.get("validation_record", []):
        require_link(errors, path, record, "validation_plan_id", "validation_plan", ids_by_entity)
    for path, record in records.get("revenue_signal", []):
        require_link(errors, path, record, "validation_record_id", "validation_record", ids_by_entity)
    for path, record in records.get("rejection_signal", []):
        require_link(errors, path, record, "validation_record_id", "validation_record", ids_by_entity)
    for path, record in records.get("alan_memory", []):
        require_link_list(errors, path, record, "weekly_revenue_signals", "revenue_signal", ids_by_entity)
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate local Alan OS JSON records against local JSON schema files."
    )
    parser.add_argument("--records-dir", type=Path, required=True, help="Directory of local JSON records.")
    parser.add_argument(
        "--schema-dir",
        type=Path,
        default=Path("schemas"),
        help="Directory containing *.schema.json files.",
    )
    parser.add_argument(
        "--ready",
        action="store_true",
        help="Check pre-execution records for an executable Today's Bet.",
    )
    parser.add_argument(
        "--result",
        action="store_true",
        help="Check post-execution records for a recorded validation result.",
    )
    parser.add_argument(
        "--links",
        action="store_true",
        help="Check relationships between local records.",
    )
    return parser.parse_args()


def selected_entity_filter(args: argparse.Namespace) -> set[str] | None:
    if not args.ready and not args.result and not args.links:
        return None

    selected: set[str] = set()
    if args.ready:
        selected.update(PRE_EXECUTION_ENTITIES)
    if args.result:
        selected.update(POST_EXECUTION_ENTITIES)
    if args.links:
        selected.update(LINK_ENTITIES)
    return selected


def success_message(args: argparse.Namespace, records_dir: Path) -> str:
    messages: list[str] = []
    if args.links:
        messages.append("links valid")
    if args.ready:
        messages.append("ready")
    if args.result:
        messages.append("result valid")
    if not messages:
        return f"validated {records_dir}"
    return f"{', '.join(messages)} {records_dir}"


def main() -> int:
    args = parse_args()
    try:
        errors = validate_records(args.records_dir, args.schema_dir, selected_entity_filter(args))
        if not errors and args.links:
            errors.extend(validate_links(args.records_dir, args.schema_dir))
        if not errors and args.ready:
            errors.extend(validate_readiness(args.records_dir, args.schema_dir))
        if not errors and args.result:
            errors.extend(validate_result(args.records_dir, args.schema_dir))
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(success_message(args, args.records_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
