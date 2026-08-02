# Migrating from v1 to v2

Version 2 makes root `AGENTS.md` the discoverable source of durable repository policy and
uses Git-native records for work in progress. It removes the need for every concurrent
agent to edit one queue or activity log.

## Mapping

| v1 | v2 |
|---|---|
| `.AGENT/agent.md` | Root `AGENTS.md` |
| `.AGENT/agent-run.md` | `.AGENT/RUNBOOK.md` |
| `.AGENT/agent-run-once.md` | Issue or task with acceptance criteria |
| `.AGENT/agent-action-log.md` | Commits, issue updates, and PR verification |
| Shared branch coordination | One branch and worktree per task |
| Runtime/webhook placeholders | IAC Bus or another dedicated coordinator, outside this repo |

## Safe upgrade

Preview changes first:

```sh
python3 scripts/apply_template.py /path/to/repository
```

Apply the plan:

```sh
python3 scripts/apply_template.py /path/to/repository --apply
```

The upgrader:

- does not write anything unless `--apply` is present;
- never replaces an existing `AGENTS.md` or other differing template file;
- copies recognized v1 files to `.AGENT/archive/v1/` without deleting the originals;
- copies the repository-specific section of v1 `.AGENT/agent.md` into a newly created
  `AGENTS.md`;
- can be run repeatedly without producing further changes.

If an existing `AGENTS.md` differs, the command reports `PRESERVE`. Merge any still-relevant
v1 repository instructions manually, confirm the new policy is complete, and then remove
legacy files in a separate reviewed commit. Git history remains the authoritative activity
record.

## Concurrent-agent protocol

1. Create or claim an issue/task with acceptance criteria and owned file scope.
2. Create a dedicated branch and worktree.
3. Commit coherent increments and keep verification in the issue or PR.
4. Use a uniquely named `.AGENT/handoffs/<issue>-<task>.md` only if continuity is needed
   before a PR exists.
5. Merge through a PR and remove temporary handoffs after their state is durable elsewhere.

Beads or another task graph may be added by an individual repository, but v2 has no required
task-system dependency.
