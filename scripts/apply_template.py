#!/usr/bin/env python3
"""Safely install or upgrade the agent continuity template."""

from __future__ import annotations

import argparse
import shutil
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = PROJECT_ROOT / "templates" / "default"
LEGACY_FILES = (
    Path(".AGENT/agent.md"),
    Path(".AGENT/agent-action-log.md"),
    Path(".AGENT/agent-run.md"),
    Path(".AGENT/agent-run-once.md"),
    Path(".AGENT/dev-notes.md"),
)
LEGACY_MARKER = "#### Below: Repository-Specific Directions"


@dataclass(frozen=True)
class Action:
    kind: str
    source: Path | None
    destination: Path
    content: str | None = None
    detail: str = ""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def render(content: str, target: Path) -> str:
    name = target.resolve().name or "repository"
    return content.replace("{{REPOSITORY_NAME}}", name)


def migrated_instructions(legacy_agent: Path) -> str:
    if not legacy_agent.is_file():
        return ""
    content = read_text(legacy_agent)
    if LEGACY_MARKER not in content:
        return ""
    custom = content.split(LEGACY_MARKER, 1)[1].strip()
    if not custom:
        return ""
    return (
        "\n\n## Migrated v1 repository instructions\n\n"
        "The following repository-specific guidance was preserved by the v2 upgrader. "
        "Review and consolidate it into the sections above when convenient.\n\n"
        f"{custom}\n"
    )


def plan(target: Path) -> list[Action]:
    target = target.resolve()
    if not target.is_dir():
        raise ValueError(f"target is not a directory: {target}")

    actions: list[Action] = []
    for source in sorted(path for path in TEMPLATE_ROOT.rglob("*") if path.is_file()):
        relative = source.relative_to(TEMPLATE_ROOT)
        destination = target / relative
        content = render(read_text(source), target)
        if relative == Path("AGENTS.md") and not destination.exists():
            content += migrated_instructions(target / ".AGENT" / "agent.md")

        if destination.exists() or destination.is_symlink():
            if (
                destination.is_file()
                and not destination.is_symlink()
                and read_text(destination) == content
            ):
                continue
            actions.append(
                Action(
                    "preserve",
                    source,
                    destination,
                    detail="existing content differs; manual merge required",
                )
            )
        else:
            actions.append(Action("write", source, destination, content=content))

    archive_root = target / ".AGENT" / "archive" / "v1"
    for relative in LEGACY_FILES:
        source = target / relative
        destination = archive_root / relative.name
        if source.is_symlink():
            actions.append(
                Action(
                    "preserve",
                    source,
                    source,
                    detail="legacy path is a symlink; inspect it manually",
                )
            )
            continue
        if not source.is_file():
            continue
        if destination.exists() or destination.is_symlink():
            if (
                destination.is_file()
                and not destination.is_symlink()
                and read_text(destination) == read_text(source)
            ):
                continue
            actions.append(
                Action(
                    "preserve",
                    source,
                    destination,
                    detail="archive already exists with different content",
                )
            )
        else:
            actions.append(
                Action(
                    "archive",
                    source,
                    destination,
                    detail="legacy source remains in place for a reversible migration",
                )
            )
    return actions


def apply(actions: list[Action]) -> None:
    for action in actions:
        if action.kind == "write":
            action.destination.parent.mkdir(parents=True, exist_ok=True)
            action.destination.write_text(action.content or "", encoding="utf-8")
        elif action.kind == "archive":
            action.destination.parent.mkdir(parents=True, exist_ok=True)
            if action.source is None:
                raise ValueError("archive action is missing a source")
            shutil.copy2(action.source, action.destination)


def display(actions: list[Action], applying: bool) -> None:
    if not actions:
        print("No changes required.")
        return
    mode = "APPLY" if applying else "DRY-RUN"
    for action in actions:
        suffix = f" ({action.detail})" if action.detail else ""
        print(f"{mode} {action.kind.upper():8} {action.destination}{suffix}")
    if not applying:
        print("Dry run only. Re-run with --apply to write changes.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install or safely upgrade the agent continuity template."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        type=Path,
        help="repository directory (default: current directory)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="perform planned writes; without this flag the command is a dry run",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        actions = plan(args.target)
    except ValueError as error:
        print(f"ERROR: {error}")
        return 2
    display(actions, args.apply)
    if args.apply:
        apply(actions)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
