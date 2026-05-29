# Agent Runbook

Persistent startup operations and standing checks for agents working in this repository.
Agents should read this file at the start of each run after reading `.AGENT/agent.md`.

## Recurring Startup Operations

1) Refresh Agent Context
	a) Read `.AGENT/agent.md`, `.AGENT/dev-notes.md`, `.AGENT/agent-run.md`,
	   `.AGENT/agent-run-once.md`, and the latest relevant entries in
	   `.AGENT/agent-action-log.md`.
	b) Check the current branch and working tree before editing.
	c) Preserve existing user or agent work.

2) Process One-Shot Queue
	a) Review `.AGENT/agent-run-once.md` for active one-time operations.
	b) Complete active run-once items before starting unrelated work when safe.
	c) Remove completed items from `.AGENT/agent-run-once.md`.
	d) Append completed or blocked run-once results to `.AGENT/agent-action-log.md` with
	   timestamp, agent name, role, branch, scope, verification, and follow-ups.

3) Prompt Feedback Loop
	a) If the maintainer gives a new standing instruction, persist it in the correct
	   `.AGENT/` file rather than leaving it only in chat context.
	b) Re-read `.AGENT/agent.md` after changing prompt instructions.
	c) Log prompt, runbook, and run-once changes in `.AGENT/agent-action-log.md`.

4) Branch Synchronization
	a) Keep shared `.AGENT/` state synced to `main` when explicitly instructed or when the
	   workflow allows direct `main` updates.
	b) Use feature branches for review, concurrent work, or changes that may conflict.
	c) Avoid creating competing edits to `.AGENT/agent-run-once.md`; consume one-shot items
	   carefully and preserve other agents' pending work.

## Active Recurring Items

1) Maintain Boilerplate Cohesion
	a) Keep `.AGENT/.agent-template.md` and `.AGENT/agent.md` aligned for generic base-agent
	   behavior.
	b) Keep repository-specific behavior only in `.AGENT/agent.md` below the repository
	   directions heading.
