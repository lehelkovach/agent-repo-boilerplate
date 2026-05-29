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
	b) Generic prompting belongs in `.AGENT/.agent-template.md` and should be mirrored into
	   `.AGENT/agent.md`.
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
	a) Keep common prompting in `.AGENT/.agent-template.md`.
	b) Keep repository-specific operational rules in `.AGENT/agent.md` below the base-agent
	   section.

2) Support File Placement
	a) Agent support files should remain inside `.AGENT/`.
	b) The root directory should remain easy to scan, with `README.md` as the human-facing
	   entry point.
