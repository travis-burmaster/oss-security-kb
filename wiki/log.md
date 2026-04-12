## [2026-04-07] bootstrap | repository structure
Initialized canonical wiki scaffolding: master index, append-only log, page template, CONTRIBUTING.md, and SECURITY.md.

## [2026-04-07] seed-pages | lodash, minimist, semver (npm)
Added first three high-value npm package pages with advisory-mapped baseline coverage and open questions. Updated wiki/index.md and wiki/npm/index.md.

## [2026-04-07] research-pass | npm seed package evidence
Expanded evidence and posture notes for lodash, minimist, and semver using advisory/search-backed sources. Added stronger context about recurring bug classes, exploitability, and follow-up audit questions.

## [2026-04-08] ingest | axios (npm)
Added axios package page documenting the 2026 compromised publish / supply-chain incident, safe downgrade targets, and open research questions around incident response and downstream exposure.

## [2026-04-11] advisory-review | requests (PyPI), google.golang.org/grpc (Go)
Ran a public-information-only review pass against two baseline stubs and upgraded both pages to advisory-mapped status. Curated Requests credential / redirect / TLS verification advisories and grpc-go transport / metadata / authorization findings using OSV, GitHub Security Advisories, upstream release notes, and CVE references. Updated `wiki/python/index.md`, `wiki/go/index.md`, and the master index descriptors to reflect the deeper coverage.

## [2026-04-11] advisory-review | Newtonsoft.Json (NuGet), jsonwebtoken (npm), koa-router (npm), serde (crates.io)
Ran a public-information-only review pass across one .NET page, one npm page refresh, and two gap candidates. Upgraded `Newtonsoft.Json` from baseline stub to advisory-mapped status using OSV, GitHub Security Advisories, the CVE record, and upstream issue / PR / fix / release history for the deeply nested JSON denial-of-service issue fixed in 13.0.1, including release-note-backed hardening context around `MaxDepth`. Refreshed `jsonwebtoken` so the page now reflects the accepted GHSA/CVE set around verification semantics, explicitly marks CVE-2022-23529 as rejected, and keeps the filed `clockTolerance` issue separate from published advisories. Also checked `koa-router` and `serde` for package-specific advisory history in OSV and GitHub advisory listings, but found no clean new package-level disclosures worth forcing into the KB in that pass.

## [2026-04-12] advisory-review | express (npm), koa-router (npm), serde (crates.io)
Ran a public-information-only review pass against three candidates using OSV package queries and GitHub repository advisory listings saved under `raw/advisory-review-2026-04-12/`. Public evidence showed multiple package advisories for `express`, while `koa-router` and `serde` returned no package-scoped OSV matches and no repository security advisories in this pass. The requested local Claude CLI synthesis step could not complete because the installed CLI returned a 401 authentication error, so no evidence-backed package-page edits were forced from this pass. Fixed unresolved merge conflict markers that had landed in `wiki/index.md` and `wiki/log.md` on `main`, and preserved the gathered evidence files for the next review.

## [2026-04-12] cleanup | index, npm index, template
Resolved leftover merge-conflict markers in `wiki/index.md` and `wiki/log.md`, preserving the useful details from both sides of the prior advisory-review history. Promoted `axios` into the npm seed-page section so ecosystem navigation matches its existing advisory-mapped page state, and aligned `wiki/TEMPLATE.md` status values with the public schema for cleaner future page generation.
