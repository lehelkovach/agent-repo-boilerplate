# Agent Operations Log

Append meaningful agent activity here in reverse chronological order. Keep entries concise
and factual so future agents and human maintainers can understand what changed, how it was
verified, and what remains.

## 2026-05-29 - Document Cursor agent write policy

- Agent: Cursor cloud coding agent
- Scope: Repository agent permissions guidance
- Actions: Added repo-level guidance that Cursor agents with write credentials may branch,
  commit, push, and prepare pull requests, with direct `main` pushes reserved for explicit
  maintainer requests.
- Verification: Reviewed `AGENTS.md`, `README.md`, and operations log diff; documentation-only
  change, no automated tests available.
- Follow-ups: GitHub/Cursor access for additional human users must still be granted through
  the platform settings; repository files cannot grant credentials.

## 2026-05-28 - Seed coding-agent boilerplate

- Agent: Cursor cloud coding agent
- Scope: Repository boilerplate documentation
- Actions: Added standard coding-agent entry points: `.AGENTS`, `AGENTS.md`,
  `.agent/base-agent.md`, `docs/AGENT-OPERATIONS-LOG.md`, and refreshed `README.md`.
- Verification: Reviewed generated files and `git diff`/`git status`; documentation-only
  change, no automated tests available.
- Follow-ups: None currently known.
