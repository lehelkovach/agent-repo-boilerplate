# Agent Repo Boilerplate

A small, vendor-neutral initializer for repositories that need reliable continuity across
coding-agent sessions. It standardizes discoverable instructions and handoffs while leaving
task tracking, Git history, pull requests, and live orchestration in their proper systems.

## What v2 provides

- a concise root `AGENTS.md` template recognized by modern coding agents;
- a stable `.AGENT/RUNBOOK.md` and one handoff file per task;
- a `.AGENT/reports/` directory, one dated file per audit, diagnosis, measurement or
  review, with an index the maintainer and later sessions read;
- an optional Cursor adapter;
- a dry-run-first, idempotent Python installer and v1 upgrader;
- migration that preserves existing instructions and archives v1 state;
- tests proving fresh installation, idempotency, safe preservation, v1 migration, and
  conflict-free handoffs from parallel worktrees.

It deliberately does not provide an orchestration server, agent runtime, Slack integration,
autonomous spawning, or a required task tracker. Use Issues or an optional tool such as Beads
for durable task state; use IAC Bus or another dedicated service for live coordination.

## Install or preview

Preview the default template in another repository:

```sh
python3 scripts/apply_template.py /path/to/repository
```

Apply it only after reviewing the plan:

```sh
python3 scripts/apply_template.py /path/to/repository --apply
```

The installer never silently overwrites a differing file. Existing `AGENTS.md` content is
reported for manual merge, and recognized v1 files are copied to `.AGENT/archive/v1/` before
the maintainer removes them.

## Installed layout

```text
AGENTS.md
.AGENT/
  RUNBOOK.md
  handoffs/
    HANDOFF-TEMPLATE.md
  reports/
    README.md
.cursor/
  rules/
    agent-conventions.mdc
```

The source files are under `templates/default/`; the root `AGENTS.md` governs development of
this repository itself.

## Continuity model

1. Put durable repository policy in `AGENTS.md`.
2. Put active task state, ownership, and acceptance criteria in an issue or task system.
3. Use one branch and worktree per task.
4. Put implementation and verification evidence in commits and pull requests.
5. Use a uniquely named handoff file only when state must cross sessions before a PR exists.
6. Move architectural history into ADRs rather than a generic activity log.
7. File every audit, diagnosis, measurement or review as `.AGENT/reports/<date>-<slug>.md`
   and index it there; it is evidence, and policy derived from it goes to `AGENTS.md`.

See [the v1 migration guide](docs/MIGRATION_V1_TO_V2.md) for the exact mapping and upgrade
behavior.

## Verify

```sh
python3 scripts/validate_template.py
python3 -m unittest discover -s tests -v
git diff --check
```

The project uses only the Python standard library.
