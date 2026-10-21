# Agent Repository Instructions

This repository maintains a vendor-neutral template for continuity across coding-agent
sessions. The distributable files live under `templates/default/`; do not treat the root
repository instructions as the downstream template.

## Working agreement

- Read `README.md`, the relevant issue or PR, and the current Git state before editing.
- Work on one focused branch or worktree per task. Do not push directly to protected
  branches unless explicitly instructed.
- Keep durable repository guidance in `AGENTS.md`. Keep active task ownership and
  acceptance criteria in an issue, and verification evidence in the PR.
- Create one `.AGENT/handoffs/<issue>-<task>.md` file only when another session needs
  continuity before a PR exists. Never use a shared append-only activity log.
- Write every audit, diagnosis, measurement or review to
  `.AGENT/reports/YYYY-MM-DD-<slug>.md` and index it in `.AGENT/reports/README.md`. The
  template ships that directory; downstream repositories keep their reports there.
- Preserve existing repository-specific instructions and unrelated user changes.
- Never print or commit secrets. Record required secret names only.

## Verification

Run these checks after changing behavior:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_template.py
git diff --check
```

The installer must remain dry-run by default, idempotent, standard-library only, and safe
for repositories that already contain `AGENTS.md` or legacy `.AGENT/` files.

## Scope boundary

This project is an initializer and migration utility, not an orchestration runtime. Do not
add an agent server, autonomous spawning, Slack/webhook integration, IAC Bus client, or a
required external task-management dependency.

## Cursor Cloud specific instructions

- Pure Python 3 standard library only: there are no third-party dependencies, no lockfile,
  and nothing to `pip install`. The startup update script is intentionally a no-op check.
- There is no server, build step, or dev server. The "application" is the CLI installer
  `scripts/apply_template.py`, which defaults to a dry run; pass `--apply` to write files.
  Exercise it end to end against a throwaway directory, e.g.
  `python3 scripts/apply_template.py /tmp/target --apply` then
  `python3 scripts/validate_template.py /tmp/target`.
- Lint/test/whitespace checks are the three commands under `## Verification` above.
