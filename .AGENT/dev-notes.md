# Agent Dev Notes

Development notes for future agent support files and agent infrastructure. These notes are
placeholders until the repository adopts concrete inter-agent services.

## Future Inter-Agent Communication

1) Communication Rules
	a) Define message formats before agents exchange task state.
	b) Include sender agent UUID, recipient or channel, timestamp, task scope, and expected
	   response behavior.
	c) Record durable decisions in `.AGENT/agent-action-log.md` rather than relying only on
	   transient bus messages.

2) Agentic Environment Variables
	a) `IAC_BUS_HOST`: Placeholder host or IP address for a future inter-agent
	   communication bus.
	b) `IAC_BUS_PORT`: Placeholder port for the future inter-agent communication bus.
	c) `AGENT_UUID`: Placeholder UUID registered for the current agent runtime.
	d) `AGENT_REPO_SLUG`: Placeholder repository owner/name value for agent registration.
	e) `AGENT_RUN_ID`: Placeholder run identifier for correlating logs and bus messages.

3) Registration Notes
	a) Future agents may register their UUID, capabilities, repository scope, and current
	   branch with an IAC bus when that service exists.
	b) Registration should never require committing secrets or machine-local credentials.
	c) Any required local-only values should be documented here as names and purpose, not as
	   live values.

## Agent Runtime Coordination

1) Run Files
	a) `.AGENT/agent-run.md` is the persistent runbook for recurring startup operations.
	b) `.AGENT/agent-run-once.md` is the one-shot queue for startup operations that should
	   be removed after completion.
	c) Agents should append completed or blocked one-shot work to
	   `.AGENT/agent-action-log.md` before finishing.

2) Prompt Feedback
	a) New maintainer instructions that should persist beyond the current chat should be
	   written into the appropriate `.AGENT/` file.
	b) Generic prompting belongs in the base-agent section of `.AGENT/agent.md`.
	c) Repository-only prompting belongs below the repository-specific section of
	   `.AGENT/agent.md`.

3) Synchronization Notes
	a) Shared `.AGENT/` state is easiest to coordinate when it is kept current on `main`.
	b) Feature branches are safer for review or concurrent edits, but agents should avoid
	   letting long-lived branches diverge in prompt, runbook, or run-once queue files.
	c) When merging prompt updates, preserve other agents' log entries and pending
	   run-once items.

## Open Design Notes

1) Template Evolution
	a) Treat `.AGENT/agent.md` on `origin/main` as the canonical template and live prompt.
	b) Keep repository-specific operational rules below the base-agent section.
	c) Avoid a separate template file unless future packaging needs one for generation.

2) Support File Placement
	a) Agent support files should remain inside `.AGENT/`.
	b) The root directory should remain easy to scan, with `README.md` as the human-facing
	   entry point.

## Future Distribution and Setup

1) Product Direction
	a) This repo may evolve from a copyable boilerplate into an installable setup tool.
	b) The tool should initialize `.AGENT/`, copy or refresh `.AGENT/agent.md` from this
	   source repo, and guide the maintainer through a setup conversation.
	c) The setup flow should support choosing an agent brand or target environment, such as
	   Cursor, GitHub Copilot coding agent, Claude-style agents, Codex-style agents, or a
	   generic Markdown-only mode.
	d) The main function before that packaging exists is Cursor-driven setup: a Cursor agent
	   uses this repo as the source, adds or updates `.AGENT/` in a target repo, and then
	   customizes the target repo's prompt, run files, action log, and dev notes.
	e) Updates to existing repos should preserve repo-specific sections and operational
	   history while refreshing generic boilerplate content.

2) npm Global CLI Option
	a) Possible command shape: `npm install -g agent-repo-boilerplate`.
	b) Possible setup command: `agent-repo init` or `agent-boilerplate init`.
	c) The CLI could ask questions, copy `.AGENT/` files, activate optional prompt blocks,
	   and write agent-brand adapter instructions when requested.
	d) npm may be a good fit if the setup tool is primarily a cross-platform developer CLI.

3) Python/pip CLI Option
	a) Possible command shape: `pipx install agent-repo-boilerplate` or
	   `pip install agent-repo-boilerplate`.
	b) Possible setup command: `agent-repo init`.
	c) Python may be a good fit if future smoke tests, repo scans, or template transforms
	   stay script-heavy.

4) Git Bootstrap Option
	a) Possible command shape: clone this repo, then copy `.AGENT/` into a target repo.
	b) Possible one-liner shape: fetch an install script from a pinned tag and run it from
	   the target repository root.
	c) Git-only setup keeps the project simple before a package manager is chosen.
	d) Any bootstrap script should be auditable, version-pinned, and safe to run without
	   secrets.

5) Agent-Led Setup Conversation
	a) Future setup can be driven by an agent prompt rather than only a CLI.
	b) The maintainer could tell their agent: "Install the agent boilerplate, ask me setup
	   questions, choose the Cursor adapter, and commit the result."
	c) The agent should ask about repo type, preferred agent brand, direct-main versus PR
	   workflow, logging expectations, test requirements, and inter-agent coordination.
	d) The completed setup should update `.AGENT/agent.md`, `.AGENT/agent-run.md`,
	   `.AGENT/dev-notes.md`, and `.AGENT/agent-action-log.md`.
	e) For Cursor specifically, the setup conversation should support both "create a new
	   repo with this `.AGENT/` boilerplate" and "continue an existing repo by updating its
	   `.AGENT/` boilerplate from this source."

6) Open Decisions
	a) Choose whether npm, pip/pipx, git-only bootstrap, or an agent-led setup prompt should
	   be the first supported install path.
	b) Define package name, command name, versioning policy, and template migration behavior.
	c) Decide whether brand-specific adapters stay as commented blocks inside `.AGENT/` or
	   can optionally generate platform files outside `.AGENT/`.
