# Agent Prompt

This file is both the canonical boilerplate prompt and the live repo prompt. In this source
repository, `origin/main` preserves the default version. In target repositories, copy
`.AGENT/agent.md` from this repo, then customize the repository-specific section below.

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

3) Startup and Run Files
	a) At the start of a new agent run, read `.AGENT/agent.md`, `.AGENT/agent-run.md`,
	   `.AGENT/agent-run-once.md`, `.AGENT/dev-notes.md`, and the latest relevant entries
	   in `.AGENT/agent-action-log.md`.
	b) Treat `.AGENT/agent-run.md` as the persistent runbook for recurring startup
	   operations and standing checks.
	c) Treat `.AGENT/agent-run-once.md` as the one-shot queue for startup operations that
	   should run once and then be removed from that file.
	d) When a run-once item is completed, delete that item from `.AGENT/agent-run-once.md`,
	   then append the completed operation to `.AGENT/agent-action-log.md` with timestamp,
	   agent name, agent role, scope, result, verification, and follow-ups.
	e) If a run-once item cannot be completed, leave it in `.AGENT/agent-run-once.md` with
	   a short blocked note and append the blocker to the action log.
	f) Re-read `.AGENT/agent.md` after processing run-once items because those actions may
	   have updated the prompt or repository-specific directions.

4) Prompt Feedback Loop
	a) When a maintainer gives a new standing instruction, decide whether it belongs in
	   `.AGENT/agent.md`, `.AGENT/agent-run.md`, `.AGENT/agent-run-once.md`,
	   `.AGENT/dev-notes.md`, or only the current task notes.
	b) Add generic instructions that should apply to every fork to the base-agent section of
	   `.AGENT/agent.md` in this source repo, where version control preserves the canonical
	   default.
	c) Add repository-specific rules to `.AGENT/agent.md` below `#### Below:
	   Repository-Specific Directions` and keep them ordered by priority.
	d) Add recurring operational instructions to `.AGENT/agent-run.md`.
	e) Add one-time startup operations to `.AGENT/agent-run-once.md`.
	f) Log every prompt, runbook, or run-once change in `.AGENT/agent-action-log.md`.
	g) Prefer keeping shared `.AGENT/` state synced on `main`; use feature branches for
	   review or concurrent work when direct `main` updates could cause conflicts.
	h) When a new instruction requires the agent to pivot or update its own operating
	   behavior, write the new behavior into `.AGENT/agent.md` before relying on it.
	i) Commit and push the `.AGENT/agent.md` update so the new programming is durable and
	   available to future agents.
	j) Bootstrap the change by starting or requesting a replacement agent in the same repo
	   and instructing it to read the updated `.AGENT/agent.md` from the pushed branch.
	k) Treat the replacement agent as the active agent for the changed behavior; the current
	   agent should finish only the handoff, logging, verification, commit, and push needed
	   to make the replacement safe.

5) Agent Identity and Roles
	a) Identify yourself in action-log entries by agent name or tool, role, and branch.
	b) Use "master repo agent" for the primary agent coordinating repository-level prompt,
	   runbook, and synchronization changes.
	c) Use "worker sub-agent" for delegated agents working on narrower tasks.
	d) If multiple agents touch `.AGENT/` files, preserve each agent's log entries and avoid
	   overwriting another agent's queued work.

6) Repository Safety
	a) Preserve existing user work and never discard unrelated changes.
	b) Do not expose or commit secrets, credentials, tokens, or machine-specific
	   configuration.
	c) Avoid adding dependencies unless the task clearly requires them.
	d) Keep generated or boilerplate edits scoped to the requested files.
	e) Do not rewrite history or force push unless explicitly instructed.

7) Default Engineering Behavior
	a) Prefer repository-local patterns over new abstractions.
	b) Favor readable, maintainable code over cleverness.
	c) Add tests for behavior changes when a test framework exists.
	d) Explain skipped verification with the reason and residual risk.
	e) Escalate blockers with concrete evidence and suggested next steps.

8) Agent Action Log Usage
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

	   1) Timestamp
	    a) YYYY-MM-DD HH:MM UTC
	   2) Agent
	   	a) <agent name or tool>
	   3) Role
	    a) <master repo agent, sub-agent, or other role>
	   4) Branch
	    a) <branch name>
	   5) Scope
	   	a) <files, subsystem, or issue>
	   6) Actions
	   	a) <what changed>
	   7) Verification
	   	a) <commands or manual checks>
	   8) Follow-ups
	   	a) <known gaps or none>
	   ```

9) Optional Prompt Command Library
	a) The commented blocks below work like default Linux config-file options.
	b) To activate an option, remove the surrounding `<!--` and `-->`, then edit the text
	   for the repository.
	c) Keep broadly reusable prompt commands in this base-agent section. Move project-only
	   variations to the repository-specific section below.

<!--
9.1) Optional: Add Diagnostic Logging
	a) Section Label: Logging
	b) Description: Ask the agent to add focused logs around changed control flow, errors,
	   and external boundaries.
	c) Prompt: Add useful logging throughout the touched code paths using the repository's
	   existing logging style. Keep logs structured where possible, avoid secrets or PII,
	   and include enough context to debug failures without noisy per-iteration spam.
-->

<!--
9.2) Optional: Add Test Coverage
	a) Section Label: Tests
	b) Description: Ask the agent to add or improve automated coverage for changed behavior.
	c) Prompt: Add targeted test coverage for new or changed behavior. Prefer existing test
	   frameworks, fixtures, and naming conventions. Include regression coverage for fixed
	   bugs and document any behavior that cannot be tested automatically.
-->

<!--
9.3) Optional: Strengthen Error Handling
	a) Section Label: Error Handling
	b) Description: Ask the agent to make failure modes clearer and safer.
	c) Prompt: Review touched code paths for unclear errors, swallowed exceptions, and weak
	   validation. Improve error messages and handling without hiding failures or adding
	   broad catch-all behavior.
-->

<!--
9.4) Optional: Update Human Documentation
	a) Section Label: Documentation
	b) Description: Ask the agent to update README, usage notes, or inline docs affected by
	   the change.
	c) Prompt: Update human-facing documentation for any changed setup, usage, commands,
	   configuration, or operational behavior. Keep documentation concise and aligned with
	   the implemented behavior.
-->

<!--
9.5) Optional: Run a Security Pass
	a) Section Label: Security
	b) Description: Ask the agent to inspect touched code for common security issues.
	c) Prompt: Review touched files for secret exposure, unsafe input handling, injection
	   risks, over-broad permissions, and insecure defaults. Fix issues in scope and list
	   any residual risks in the handoff.
-->

<!--
9.6) Optional: Reduce Technical Debt
	a) Section Label: Refactoring
	b) Description: Ask the agent to simplify nearby code when it directly supports the
	   requested change.
	c) Prompt: Simplify duplicated or confusing code encountered in the touched area when
	   it directly supports the task. Keep refactors small, behavior-preserving, and covered
	   by existing or added verification.
-->

10) Support Files
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
	c) Keep legacy root-level agent prompt files out of this boilerplate unless explicitly
	   requested.
	d) Treat the present-day primary use case as Cursor agents seeding or updating
	   `.AGENT/` in target repositories, then customizing those files for each repo.

2) Cursor Agent Write Policy
	a) Cursor coding agents with repository write credentials may create branches, edit
	   files, commit, push, and prepare pull requests for maintainer-requested work.
	b) Agents may push directly to `main` only when explicitly instructed to do so.
	c) Otherwise, use a focused feature branch and leave work ready for human review.

3) Boilerplate Customization
	a) Treat `.AGENT/agent.md` on `origin/main` as the source template for new forks and
	   target-repo updates.
	b) Copy or refresh `.AGENT/agent.md` from this source, then customize this
	   repository-specific section below the base-agent content.
	c) Keep common prompting in the base-agent section; keep project-only rules in this
	   repository-specific section.
	d) When updating an existing repo from this boilerplate, preserve that repo's
	   repository-specific directions, action log, run-once queue, and dev notes unless the
	   maintainer asks to reset them.

4) Verification
	a) This repository currently contains documentation-only boilerplate.
	b) Use file review, `git diff`, `git diff --check`, and `git status` as the primary
	   verification steps until automated checks are introduced.

5) Known Gaps
	a) No automated tests, build system, or package manager are configured yet.
	b) Future inter-agent communication and agentic environment variables are placeholders
	   tracked in `.AGENT/dev-notes.md`.
