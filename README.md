# Agent Repo Boilerplate

This repository is organized as a minimal coding-agent boilerplate. The root stays simple:
`README.md` explains the layout, and `.AGENT/` contains the agent prompt, template, log, and
support files.

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
	d) `.AGENT/dev-notes.md` stores future-facing notes for inter-agent communication,
	   agentic environment variables, and support-file conventions.

## How to Use This Boilerplate

1) Start With the Template
	a) Copy or generate `.AGENT/agent.md` from `.AGENT/.agent-template.md`.
	b) Keep the base-agent section generic so downstream forks can reuse it.
	c) Add repository-specific directions below the `#### Below: Repository-Specific
	   Directions` heading in `.AGENT/agent.md`.

2) Customize the Agent Prompt
	a) Put common prompting that should apply to every repository in the base-agent section.
	b) Put repo-specific rules, behavior, commands, and priorities below the base section.
	c) Organize rules in priority order so agents can resolve conflicts predictably.

3) Maintain the Action Log
	a) Update `.AGENT/agent-action-log.md` for non-trivial agent work.
	b) Record what changed, how it was verified, and any follow-ups.
	c) Keep entries in reverse chronological order.

## Current Status

This repo currently contains documentation-only boilerplate. Add project-specific source code,
tooling, verification commands, and agent infrastructure details as the repository evolves.
