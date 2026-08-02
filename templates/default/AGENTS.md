# Agent Instructions for {{REPOSITORY_NAME}}

## Before working

- Read this file, the repository README, the relevant issue or task, and any more-specific
  `AGENTS.md` files in the directory tree.
- Inspect the current branch and working tree. Preserve unrelated work.
- Confirm the task's acceptance criteria, owned files, and verification commands.

## Workflow

- Use one branch or worktree per task. Keep changes small enough to review.
- Use the repository's existing conventions and dependencies before introducing new ones.
- Record active work, ownership, and acceptance criteria in the issue or task tracker.
- Record architectural decisions in `docs/decisions/` when the repository uses ADRs.
- Put implementation evidence, commands run, residual risks, and the next action in the
  pull request or task record.

## Continuity

- Use `.AGENT/RUNBOOK.md` for stable startup and verification guidance that does not
  belong in this file.
- If work must pass to another session before a pull request exists, copy
  `.AGENT/handoffs/HANDOFF-TEMPLATE.md` to a uniquely named task file.
- Never coordinate concurrent agents through one shared queue or append-only action log.
  Git branches, worktrees, issues, commits, and pull requests are the durable record.

## Safety

- Never discard unrelated changes or rewrite history without explicit authorization.
- Never print or commit credentials, tokens, personal data, or machine-local settings.
- Run the narrowest relevant checks first, then broader checks required by the repository.
- State exactly what was and was not verified.
