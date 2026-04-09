# Contributing

Thanks for helping build the OSS Security Knowledge Base.

## What this project values

This KB is trying to answer a specific question:

> Has this package actually been reviewed for security, by whom, when, and with what findings?

That means we care about **coverage**, **evidence**, and **clarity** more than hype.

## Contribution types

You can contribute by:
- adding a new package stub
- improving an existing package page
- ingesting an audit report, issue, CVE write-up, or researcher post
- correcting package metadata or download stats
- improving the schema, tooling, or site structure

## Evidence standards

Prefer primary sources whenever possible:
- maintainer issues / PRs
- CVE pages / OSV links
- audit reports
- researcher writeups
- security advisories

Clearly distinguish between:
- **confirmed findings**
- **reported but unverified claims**
- **audit coverage with no public findings**

Do not overstate. “No findings published” is not the same thing as “secure.”

## Package page rules

Use the canonical format described in `SCHEMA.md`.

Every package page should make it obvious:
- what package this is
- what ecosystem it belongs to
- whether anyone has audited it
- what was found
- what is still unknown
- where the information came from

## Naming and organization

Create package pages under the correct ecosystem directory in `wiki/`:
- `wiki/npm/`
- `wiki/rust/`
- `wiki/dotnet/`
- `wiki/python/`
- `wiki/go/`
- `wiki/homebrew/`
- `wiki/kubernetes/`
- `wiki/linux/`

## When adding or updating a page

Also update:
- `wiki/index.md`
- the ecosystem index when one exists (for example `wiki/npm/index.md`)
- `wiki/log.md`

## Tone

Be precise, skeptical, and boring in a good way.

Good:
- “No audits on record.”
- “One manual partial-source review documented in 2024.”
- “Known prototype pollution history; current status unclear.”

Bad:
- “Totally safe.”
- “Battle-tested, no issues.”
- “Looks clean.”

## Pull requests

A good PR should explain:
- what packages/pages changed
- what sources were added
- whether this is stub generation, audit ingest, or schema/tooling work

If you are contributing a security finding about an upstream project, include links to the original disclosure or reporting thread whenever possible.
