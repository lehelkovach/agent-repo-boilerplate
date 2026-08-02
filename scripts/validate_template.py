#!/usr/bin/env python3
"""Validate the source template or an installed target."""

from __future__ import annotations

import argparse
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = PROJECT_ROOT / "templates" / "default"
REQUIRED = (
    Path("AGENTS.md"),
    Path(".AGENT/RUNBOOK.md"),
    Path(".AGENT/handoffs/HANDOFF-TEMPLATE.md"),
    Path(".cursor/rules/agent-conventions.mdc"),
)
FORBIDDEN_PHRASES = (
    "agent-action-log.md",
    "agent-run-once.md",
    "SLACK_WEBHOOK_URL",
    "start a replacement agent",
)


def validate(root: Path, source_template: bool) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")

    for relative in REQUIRED:
        path = root / relative
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        for phrase in FORBIDDEN_PHRASES:
            if phrase in content:
                errors.append(f"{relative} contains deprecated phrase: {phrase}")

    agents = root / "AGENTS.md"
    if agents.is_file() and source_template:
        content = agents.read_text(encoding="utf-8")
        if "{{REPOSITORY_NAME}}" not in content:
            errors.append("source AGENTS.md is missing {{REPOSITORY_NAME}} placeholder")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate agent boilerplate files.")
    parser.add_argument(
        "target",
        nargs="?",
        type=Path,
        help="installed repository to validate; omit to validate the source template",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.target.resolve() if args.target else TEMPLATE_ROOT
    errors = validate(root, source_template=args.target is None)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print(f"PASS: validated {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
