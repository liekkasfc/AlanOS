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


def validate_records(records_dir: Path, schema_dir: Path) -> list[str]:
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
            errors.append(f"{path}: no matching schema found")
            continue
        try:
            record = load_json(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        errors.extend(validate_record(path, record, schemas[entity]))
    return errors


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
            continue
        try:
            record = load_json(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        errors.extend(validate_ready_record(path, entity, record))
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
        help="Also check whether records are ready for real execution.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        errors = validate_records(args.records_dir, args.schema_dir)
        if not errors and args.ready:
            errors = validate_readiness(args.records_dir, args.schema_dir)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    if args.ready:
        print(f"ready {args.records_dir}")
    else:
        print(f"validated {args.records_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
