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

## Open Design Notes

1) Template Evolution
	a) Keep common prompting in `.AGENT/.agent-template.md`.
	b) Keep repository-specific operational rules in `.AGENT/agent.md` below the base-agent
	   section.

2) Support File Placement
	a) Agent support files should remain inside `.AGENT/`.
	b) The root directory should remain easy to scan, with `README.md` as the human-facing
	   entry point.
