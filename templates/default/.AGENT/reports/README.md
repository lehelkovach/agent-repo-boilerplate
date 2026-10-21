# Reports

Audits, diagnoses, measurements and reviews that a session produced for a
person to read later: what was asked, what was looked at, what was found, and
what it means. The maintainer and later sessions read this directory to see
what was already established, and when, before measuring again.

A report written only in chat is gone when the session ends. One filed under
`docs/` reads as policy and drifts. This directory is the evidence shelf.

## Rules

- One report per file, named `YYYY-MM-DD-<slug>.md`: the date of the work and a
  lower-case, hyphenated slug.
- Start with the header block below, then the body.
- Say what was read, measured or run, and what was not. A result that was not
  observed is not a result.
- Never include secrets, tokens, card data or a third party's personal data.
  Name a secret only by its variable name.
- A report is evidence, not policy. When a finding changes how the repository
  is worked on, put the rule in `AGENTS.md` or the relevant document and link
  the report from there.
- Do not rewrite an old report. A follow-up is a new report that links back.
- Add a row to the index below in the same change, newest first.

Each report is its own file, so sessions working in parallel never conflict
here. This is not an activity log: nothing is appended to an existing report.

## Header block

```markdown
# <Title>

- **Date:** YYYY-MM-DD
- **Asked by:** <who asked, or "self-initiated">
- **Question:** <one sentence>
- **Scope:** <repositories, files, hosts, time window>
- **Method:** <read the code / measured on <host> / ran <command>>
- **Verdict:** <one or two sentences>
- **Follow-up:** <pull request, issue, task, or "none">
```

## Index

| Date | Report | Question | Verdict |
|---|---|---|---|
