# Agent Repo Boilerplate

This repository contains a minimal coding-agent boilerplate for projects that want
predictable autonomous-agent onboarding and handoff practices.

## Included Files

- `.AGENTS` - compact manifest pointing agents to the repository guidance.
- `AGENTS.md` - repository-wide instructions for coding agents.
- `.agent/base-agent.md` - baseline operating prompt for coding agents.
- `docs/AGENT-OPERATIONS-LOG.md` - append-only log for meaningful agent activity.
- `README.md` - human-facing overview of the repository.

## Using This Boilerplate

1. Read `AGENTS.md` before delegating work to a coding agent.
2. Customize `.agent/base-agent.md` with project-specific workflow expectations.
3. Keep `docs/AGENT-OPERATIONS-LOG.md` current when agents make non-trivial changes.
4. Add project setup, test, and deployment instructions here as the repository grows.

## Cursor Agent Access

Cursor agents that are launched with write credentials for this repository may create
branches, commit, push, and prepare pull requests. Direct pushes to `main` should only happen
when the repository owner or maintainers explicitly request them.

## Status

The repository is currently seeded with documentation-only boilerplate. Add project-specific
source code, tooling, and verification commands as they become available.
