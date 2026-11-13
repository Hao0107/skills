#!/usr/bin/env python3
"""Deterministic helper script template for an Agent Skill.

Contract:
- Non-interactive; arguments via argparse.
- Result: JSON on stdout matching assets/output-schema.json.
- Errors: message on stderr and non-zero exit (1 = input not found, 2 = processing failed).
"""
import argparse
import json
import sys
from pathlib import Path

SKILL_NAME = "skill-template"


def process_target(input_path: Path, option: str, dry_run: bool) -> dict:
    if not input_path.exists():
        print(f"[ERROR] Target path not found: '{input_path}'", file=sys.stderr)
        sys.exit(1)

    try:
        # Replace with real logic. Honor dry_run: never modify files when True.
        results = [
            {
                "item_id": "example-check",
                "status": "PASS",
                "message": f"Processed with option '{option}'",
                "suggested_action": "",
            }
        ]
    except Exception as exc:  # noqa: BLE001
        print(f"[ERROR] Processing failed: {exc}", file=sys.stderr)
        sys.exit(2)

    failed = [r for r in results if r["status"] == "FAIL"]
    return {
        "skill_name": SKILL_NAME,
        "execution_status": "FAIL" if failed else "PASS",
        "summary": f"{len(results) - len(failed)}/{len(results)} checks passed.",
        "input_target": str(input_path),
        "results": results,
        "artifacts_created": [],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=f"Helper script for {SKILL_NAME}.")
    parser.add_argument("--input", "-i", required=True, help="Path to input file or directory.")
    parser.add_argument("--option", "-o", default="default", help="Optional parameter.")
    parser.add_argument("--dry-run", action="store_true", help="Do not modify any files.")
    args = parser.parse_args()

    output = process_target(Path(args.input), args.option, args.dry_run)
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
