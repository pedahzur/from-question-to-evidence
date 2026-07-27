#!/usr/bin/env python3
"""Validate a literature-discovery candidate register."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys

import yaml


SCHEMA = Path(__file__).resolve().parents[1] / "references/candidate-register-schema.yml"


def validate(path: Path) -> list[str]:
    schema = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    expected_fields = schema["fields"]
    required = schema["required"]
    allowed_verification = set(schema["verification_status"])
    allowed_scope = set(schema["scope_signal"])
    prohibited = set(schema["prohibited_fields"])
    errors: list[str] = []

    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        actual_fields = reader.fieldnames or []
        if actual_fields != expected_fields:
            missing = [field for field in expected_fields if field not in actual_fields]
            extra = [field for field in actual_fields if field not in expected_fields]
            if missing:
                errors.append(f"header: missing fields: {', '.join(missing)}")
            if extra:
                errors.append(f"header: unexpected fields: {', '.join(extra)}")
            if not missing and not extra:
                errors.append("header: fields are not in the declared order")
        if prohibited.intersection(actual_fields):
            errors.append("header: contains a prohibited final-eligibility field")

        seen_ids: set[str] = set()
        rows = list(reader)
        if not rows:
            errors.append("register: contains no candidate rows")

        for line_number, row in enumerate(rows, start=2):
            for field in required:
                if not (row.get(field) or "").strip():
                    errors.append(f"line {line_number}: {field} is required")

            candidate_id = (row.get("candidate_id") or "").strip()
            if candidate_id in seen_ids:
                errors.append(f"line {line_number}: duplicate candidate_id {candidate_id}")
            seen_ids.add(candidate_id)

            status = (row.get("verification_status") or "").strip()
            if status and status not in allowed_verification:
                errors.append(
                    f"line {line_number}: invalid verification_status {status}"
                )

            scope = (row.get("scope_signal") or "").strip()
            if scope and scope not in allowed_scope:
                errors.append(f"line {line_number}: invalid scope_signal {scope}")

            duplicate_of = (row.get("duplicate_of") or "").strip()
            if duplicate_of and duplicate_of == candidate_id:
                errors.append(f"line {line_number}: duplicate_of points to itself")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate an auditable literature candidate-register CSV."
    )
    parser.add_argument("register", type=Path)
    args = parser.parse_args()

    if not args.register.is_file():
        print(f"register not found: {args.register}")
        return 1

    errors = validate(args.register)
    if errors:
        for error in errors:
            print(error)
        return 1

    print(f"candidate register passed: {args.register}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
