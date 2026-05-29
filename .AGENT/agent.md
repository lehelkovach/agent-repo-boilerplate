# Agent Prompt

This file was created from `.AGENT/.agent-template.md`. The base-agent section is generic
across repositories and may be customized after forking.

## Base-Agent Section

1) Mission
	a) Deliver small, reviewable improvements while preserving repository integrity.
	b) Read available context before acting, including `.AGENT/agent.md`, the README, and
	   any task-specific files.
	c) Make focused changes, verify them, and leave clear handoff notes.

2) Operating Loop
	a) Inspect repository state, branch, and current changes before editing.
	b) Identify the smallest safe change that satisfies the task.
	c) Use existing project conventions, tools, and file organization.
	d) Run targeted verification before broad or expensive checks.
	e) Update `.AGENT/agent-action-log.md` for meaningful setup, implementation,
	   verification, or handoff events.
	f) Commit and prepare work for review when the workflow or maintainer request requires
	   it.

3) Repository Safety
	a) Preserve existing user work and never discard unrelated changes.
	b) Do not expose or commit secrets, credentials, tokens, or machine-specific
	   configuration.
	c) Avoid adding dependencies unless the task clearly requires them.
	d) Keep generated or boilerplate edits scoped to the requested files.
	e) Do not rewrite history or force push unless explicitly instructed.

4) Default Engineering Behavior
	a) Prefer repository-local patterns over new abstractions.
	b) Favor readable, maintainable code over cleverness.
	c) Add tests for behavior changes when a test framework exists.
	d) Explain skipped verification with the reason and residual risk.
	e) Escalate blockers with concrete evidence and suggested next steps.

5) Agent Action Log Usage
	a) Treat `.AGENT/agent-action-log.md` as the authoritative activity log for agent work.
	b) Add an entry for non-trivial setup, implementation, verification, migration,
	   permission, or handoff work.
	c) Keep entries in reverse chronological order.
	d) Update "Verification" from pending to actual commands or manual checks before
	   finishing a task.
	e) Record follow-ups as "None currently known" when there are no known gaps.
	f) Use this entry shape:

	   ```markdown
	   ## YYYY-MM-DD - Short title

	   1) Agent
	   	a) <agent name or tool>
	   2) Scope
	   	a) <files, subsystem, or issue>
	   3) Actions
	   	a) <what changed>
	   4) Verification
	   	a) <commands or manual checks>
	   5) Follow-ups
	   	a) <known gaps or none>
	   ```

6) Support Files
	a) Keep agent support files inside `.AGENT/`.
	b) Use `.AGENT/dev-notes.md` for future agent infrastructure notes, including
	   inter-agent communication rules and agentic environment variables.
	c) Keep root-level files minimal; by default, only `README.md` should live at the root
	   alongside the `.AGENT/` directory and version-control metadata.

#### Below: Repository-Specific Directions

1) Highest Priority Rules
	a) This repository is a coding-agent boilerplate. Keep the organization clear and
	   portable for downstream forks.
	b) Keep tracked root-level content limited to `README.md` and the `.AGENT/` directory.
	c) Do not restore root-level `.AGENTS`, `AGENTS.md`, `.agent/`, or `docs/` boilerplate
	   locations unless explicitly requested.

2) Cursor Agent Write Policy
	a) Cursor coding agents with repository write credentials may create branches, edit
	   files, commit, push, and prepare pull requests for maintainer-requested work.
	b) Agents may push directly to `main` only when explicitly instructed to do so.
	c) Otherwise, use a focused feature branch and leave work ready for human review.

3) Boilerplate Customization
	a) Treat `.AGENT/.agent-template.md` as the source template for new forks.
	b) Create or refresh `.AGENT/agent.md` from the template, then customize this
	   repository-specific section below the base-agent content.
	c) Keep common prompting in the base-agent section; keep project-only rules in this
	   repository-specific section.

4) Verification
	a) This repository currently contains documentation-only boilerplate.
	b) Use file review, `git diff`, `git diff --check`, and `git status` as the primary
	   verification steps until automated checks are introduced.

5) Known Gaps
	a) No automated tests, build system, or package manager are configured yet.
	b) Future inter-agent communication and agentic environment variables are placeholders
	   tracked in `.AGENT/dev-notes.md`.
