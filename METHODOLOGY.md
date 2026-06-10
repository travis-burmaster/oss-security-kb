# Methodology

This knowledge base is LLM-maintained. That phrase invites a fair question: *can you trust LLM-generated security content?* This document explains exactly what the LLM does, what it doesn't do, and how to verify any claim on any page yourself.

## Two kinds of content, two trust levels

Every package page carries a `Current Status` field that tells you which kind of content you're reading.

### 1. Advisory mapping (`advisory-mapped`, `baseline stub`) — verifiable lookup work

The bulk of the wiki. For each package, the LLM:

1. Queries public, authoritative sources: [OSV.dev](https://osv.dev), [GitHub Security Advisories](https://github.com/advisories), NVD, and the package's own security policy and release notes.
2. Maps each published advisory to the page's vulnerability table: CVE/GHSA ID, severity, affected and fixed versions, with a link to the primary source.
3. Pulls registry metadata (download counts, repository, security contact) from registry APIs.

**No security judgment is generated here.** This is structured transcription of records that already exist. Every row links to its primary source — if a row has no link, that's a bug; please [open an issue](https://github.com/travis-burmaster/oss-security-kb/issues).

The honest failure modes of this tier are *omission* (an advisory the pass didn't surface) and *staleness* (a fix version superseded after the page was written). Pages state the date of their last pass; treat them as a floor, not a ceiling.

### 2. Source review (`audit-ingested`) — human-verified findings

A small number of pages (e.g. Express, koa-router, js-yaml) include findings from actual source-code review. For these:

- The audit scope is stated precisely: exact version, commit hash, files and line counts reviewed, and what was *out* of scope.
- Each finding cites file and line numbers so anyone can check the claim against the source.
- Findings are assessed against the project's *own published threat model* where one exists.
- Findings that warrant disclosure go through the project's documented security contact **before** they appear here, and the page records the maintainers' response — including "disputed" or "working as intended." A disputed finding stays labeled as disputed; we don't present contested claims as settled vulnerabilities.
- "Confirmed safe" entries (things we looked for and did not find) are listed alongside bugs. Absence of findings is data, but it is never claimed as proof a package is clean — see the findings vocabulary in [SCHEMA.md](SCHEMA.md) (`none found`, never "clean").

## What the LLM is never trusted to do

- Invent vulnerabilities or severities without a linked primary source or an in-scope, line-cited code reference.
- Mark an audit as having happened without a citable source document in `raw/` or a public link.
- Claim a package is "secure" or "audited-clean." The strongest claim this KB makes is *"here is who looked, when, at what, and what they reported."*

## How to verify a page

1. Check `Current Status` to know which tier you're reading.
2. Follow the source links — every vulnerability row and audit-history row has one.
3. Compare against the OSV link on the page (`https://osv.dev/list?ecosystem=...`), which is always the live record.
4. Check `wiki/log.md` — every change to the wiki is logged, append-only, with its source.

## Corrections

If a page misstates your package's history, you have two fast paths:

- **Open an issue** — corrections from maintainers are prioritized over everything else.
- **Open a PR** — see [CONTRIBUTING.md](CONTRIBUTING.md); maintainer corrections don't require the full evidence workflow, just a pointer to the authoritative record.
