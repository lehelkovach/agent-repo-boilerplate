# AGENTS.md

Repository-wide operating instructions for autonomous coding agents.

## Project Overview

This repository is seeded from the coding-agent boilerplate. It is intended to be a
lightweight starting point for projects that want predictable agent onboarding,
shared operating conventions, and an auditable activity log.

## Agent Entry Points

- Read this file before making changes.
- Use `.agent/base-agent.md` as the baseline role and workflow prompt.
- Record meaningful work in `docs/AGENT-OPERATIONS-LOG.md`.
- Keep `README.md` useful for human readers and link agent-specific details from there.

## Working Rules

- Preserve existing user changes. Do not revert unrelated edits.
- Prefer small, focused commits with descriptive messages.
- Keep generated or boilerplate edits scoped to the requested files unless more context is
  required.
- Use the repository's existing tools, package manager, and style once a project stack is
  introduced.
- Avoid adding dependencies unless the task requires them.
- Never commit secrets, credentials, tokens, or machine-specific configuration.

## Verification

When changing code or project configuration, run the narrowest meaningful checks first,
then broaden as risk increases. If no automated checks exist yet, verify the relevant files
manually and document that limitation in the operations log or handoff notes.

## Documentation Expectations

- Update `README.md` when human setup, usage, or project scope changes.
- Update `AGENTS.md` when agent workflow, commands, or repository conventions change.
- Append to `docs/AGENT-OPERATIONS-LOG.md` for non-trivial implementation, setup, test, or
  handoff events.

## Operations Log Format

Use concise entries in reverse chronological order:

```markdown
## YYYY-MM-DD - Short title

- Agent: <name or tool>
- Scope: <files, subsystem, or issue>
- Actions: <what changed>
- Verification: <commands or manual checks>
- Follow-ups: <known gaps or none>
```
