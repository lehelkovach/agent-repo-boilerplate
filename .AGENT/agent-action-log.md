# Agent Action Log

Append meaningful agent activity here in reverse chronological order. Keep entries concise
and factual so future agents and human maintainers can understand what changed, how it was
verified, and what remains.

## 2026-05-29 - Reorganize agent boilerplate

1) Agent
	a) Cursor cloud coding agent
2) Scope
	a) Repository boilerplate organization
3) Actions
	a) Moving agent boilerplate into `.AGENT/`, adding template-driven `agent.md`, moving
	   the action log, adding dev notes, removing the old `docs/`, `.agent/`, `.AGENTS`,
	   and root `AGENTS.md` locations, and refreshing the root README.
4) Verification
	a) Reviewed new `.AGENT/` files, root README, repository tree, `git diff --check`,
	   `git diff --stat`, and `git status`; documentation-only change, no automated tests
	   available.
5) Follow-ups
	a) None currently known.

## 2026-05-29 - Document Cursor agent write policy

1) Agent
	a) Cursor cloud coding agent
2) Scope
	a) Repository agent permissions guidance
3) Actions
	a) Added repo-level guidance that Cursor agents with write credentials may branch,
	   commit, push, and prepare pull requests, with direct `main` pushes reserved for
	   explicit maintainer requests.
4) Verification
	a) Reviewed `AGENTS.md`, `README.md`, and operations log diff; documentation-only
	   change, no automated tests available.
5) Follow-ups
	a) GitHub/Cursor access for additional human users must still be granted through the
	   platform settings; repository files cannot grant credentials.

## 2026-05-28 - Seed coding-agent boilerplate

1) Agent
	a) Cursor cloud coding agent
2) Scope
	a) Repository boilerplate documentation
3) Actions
	a) Added standard coding-agent entry points: `.AGENTS`, `AGENTS.md`,
	   `.agent/base-agent.md`, `docs/AGENT-OPERATIONS-LOG.md`, and refreshed `README.md`.
4) Verification
	a) Reviewed generated files and `git diff`/`git status`; documentation-only change,
	   no automated tests available.
5) Follow-ups
	a) None currently known.
