# Agent Repo Boilerplate

This repository is a minimal boilerplate for giving coding agents a consistent operating
surface inside a Git repository. It does not provide an application runtime, package
manager, CI system, or agent orchestration server. Its scope is the repo-local files that
help agents understand how to start, what prompt to follow, where to record work, and how to
persist new standing instructions for future runs.

The root stays intentionally small: `README.md` explains the boilerplate, and `.AGENT/`
contains the agent prompt, template, action log, run files, and support notes.

## What This Helps Agents Do Today

1) Start Consistently
	a) Agents have a known first-read location: `.AGENT/agent.md`.
	b) Recurring startup behavior is documented in `.AGENT/agent-run.md`.
	c) One-time startup actions are queued in `.AGENT/agent-run-once.md`.

2) Preserve Prompt Feedback
	a) Maintainer instructions that should apply beyond the current chat can be written into
	   `.AGENT/agent.md`, `.AGENT/.agent-template.md`, or the run files.
	b) Generic base-agent prompting stays reusable for forks.
	c) Repo-specific behavior stays below the repository-specific section in
	   `.AGENT/agent.md`.

3) Improve Handoffs
	a) Agents record meaningful setup, implementation, verification, and blocked work in
	   `.AGENT/agent-action-log.md`.
	b) Log entries include timestamp, agent name, role, branch, scope, verification, and
	   follow-ups.
	c) Master repo agents and sub-agents can coordinate through shared `.AGENT/` files.

4) Stay Vendor-Neutral
	a) The boilerplate is plain Markdown.
	b) Commercial-agent-specific instructions can be added as commented optional blocks
	   without forcing a platform-specific root file layout.
	c) Cursor, Copilot, Claude, Codex-style, or other agents can be pointed at the same
	   `.AGENT/agent.md` entry point.

## Repository Organization

1) Root Directory
	a) `README.md` is the human-facing overview and organization guide.
	b) `.AGENT/` contains all coding-agent boilerplate and support files.
	c) No root-level agent prompt files or `docs/` folder are used by default.

2) `.AGENT/` Directory
	a) `.AGENT/.agent-template.md` is the reusable template for new forks.
	b) `.AGENT/agent.md` is created from the template and then customized for this
	   repository.
	c) `.AGENT/agent-action-log.md` records meaningful agent setup, implementation,
	   verification, and handoff activity.
	d) `.AGENT/agent-run.md` stores recurring startup operations and standing checks.
	e) `.AGENT/agent-run-once.md` stores one-time startup operations that agents remove
	   after completion and record in the action log.
	f) `.AGENT/dev-notes.md` stores future-facing notes for inter-agent communication,
	   agentic environment variables, and support-file conventions.

## How to Use This Boilerplate

1) Add the Boilerplate to a Repo
	a) In the root directory of the main origin repository, keep `README.md` at root and
	   place all agent support files under `.AGENT/`.
	b) If starting fresh, copy this repository's `.AGENT/` directory into the target repo.
	c) Do not add separate root-level agent prompt files unless a specific platform requires
	   an adapter later.

2) Create the Repo Agent Prompt
	a) From the root of the target repo, create `.AGENT/agent.md` from
	   `.AGENT/.agent-template.md`.
	b) Example:

	   ```sh
	   cp .AGENT/.agent-template.md .AGENT/agent.md
	   ```

	c) Keep the base-agent section generic so downstream forks can reuse it.
	d) Add repository-specific directions below the `#### Below: Repository-Specific
	   Directions` heading in `.AGENT/agent.md`.

3) Instruct Agents on Startup
	a) Tell each coding agent to start by reading `.AGENT/agent.md`.
	b) The agent prompt then instructs the agent to read `.AGENT/agent-run.md`,
	   `.AGENT/agent-run-once.md`, `.AGENT/dev-notes.md`, and recent
	   `.AGENT/agent-action-log.md` entries.
	c) Example startup instruction:

	   ```text
	   Before working, read .AGENT/agent.md and follow its startup instructions.
	   Process .AGENT/agent-run.md and .AGENT/agent-run-once.md, then update
	   .AGENT/agent-action-log.md with meaningful work and verification.
	   ```

4) Customize the Agent Prompt
	a) Put common prompting that should apply to every repository in the base-agent section.
	b) Put repo-specific rules, behavior, commands, and priorities below the base section.
	c) Organize rules in priority order so agents can resolve conflicts predictably.

5) Maintain the Action Log
	a) Update `.AGENT/agent-action-log.md` for non-trivial agent work.
	b) Record what changed, how it was verified, and any follow-ups.
	c) Keep entries in reverse chronological order.

6) Use Run Files for Agent OS Behavior
	a) Put recurring startup behavior in `.AGENT/agent-run.md`.
	b) Put one-time startup operations in `.AGENT/agent-run-once.md`.
	c) Agents should process run-once items, remove completed items from the queue, and log
	   the result with timestamp, agent name, role, branch, and verification.

7) Keep Prompt Feedback Persistent
	a) When maintainers give new standing instructions, add them to the appropriate
	   `.AGENT/` file so future agents can pick them up.
	b) Keep generic base-agent behavior in the template and generated prompt.
	c) Keep repository-specific behavior in `.AGENT/agent.md`.

## Current Status

This repo currently contains documentation-only boilerplate. Add project-specific source code,
tooling, verification commands, and agent infrastructure details as the repository evolves.
