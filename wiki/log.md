# OSS Security KB — Ingest Log

*Append-only. Each entry starts with `## [YYYY-MM-DD]` for grep-ability.*
*Usage: `grep "^## \[" wiki/log.md | tail -10`*

---

## [2026-04-07] bootstrap | Repository initialized
Initial repo created. SCHEMA.md, README.md, index.md scaffolded. Ecosystems: npm, rust, dotnet, python, go, homebrew, kubernetes, linux.

## [2026-04-07] ingest | path-to-regexp (npm)
Source: GitHub Issue #433 filed by travis-burmaster on 2026-03-31. Manual code review of parse() function. Found: (1) trailing backslash appends literal "undefined" to path token — route becomes /testundefined silently; (2) null byte passthrough — \x00 not stripped from path strings. Pages updated: wiki/npm/path-to-regexp.md, wiki/index.md.

## [2026-04-07] ingest | jsonwebtoken (npm)
Source: GitHub Issue #1021 filed by travis-burmaster on 2026-03-31. Manual code review of verify() and the clockTolerance option. Found: setting clockTolerance to Number.MAX_SAFE_INTEGER bypasses exp (expiry) claim verification entirely — expired tokens accepted indefinitely. Pages updated: wiki/npm/jsonwebtoken.md, wiki/index.md.
