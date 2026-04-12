## [2026-04-07] bootstrap | repository structure
Initialized canonical wiki scaffolding: master index, append-only log, page template, CONTRIBUTING.md, and SECURITY.md.

## [2026-04-07] seed-pages | lodash, minimist, semver (npm)
Added first three high-value npm package pages with advisory-mapped baseline coverage and open questions. Updated wiki/index.md and wiki/npm/index.md.

## [2026-04-07] research-pass | npm seed package evidence
Expanded evidence and posture notes for lodash, minimist, and semver using advisory/search-backed sources. Added stronger context about recurring bug classes, exploitability, and follow-up audit questions.

## [2026-04-08] structure-pass | npm indexes + routing-related stubs
Updated `wiki/index.md` and `wiki/npm/index.md` so they reflect all current npm pages, including previously unindexed `jsonwebtoken` and `path-to-regexp`. Added baseline stub pages for `express` and `koa-router` to turn related-page redlinks into concrete future audit targets. Clarified baseline stub conventions in `SCHEMA.md`.

## [2026-04-08] ingest | axios (npm)
Added axios package page documenting the 2026 compromised publish / supply-chain incident, safe downgrade targets, and open research questions around incident response and downstream exposure.

## [2026-04-09] seed-pages | requests (python), serde (rust)
Added first non-npm seed pages so the KB now has concrete Python and Rust coverage anchors. Created `wiki/python/index.md` and `wiki/rust/index.md`, then added baseline stubs for `requests` and `serde` with ecosystem-specific next-step questions and cross-links suitable for future markdown-first site navigation.

## [2026-04-09] guidance-pass | schema + contributor instructions
Updated `SCHEMA.md` so the documented package format matches the current template style (`Current Status`, `Open Questions`) and clarified that ecosystem index pages are first-class navigation surfaces. Updated `CONTRIBUTING.md` to remind contributors to maintain ecosystem indexes alongside the master index and log.

## [2026-04-10] seed-pages | grpc-go (go), kube-apiserver (kubernetes)
Added first Go and Kubernetes seed pages so two previously empty ecosystems now have concrete anchors. Created `wiki/go/index.md` and `wiki/kubernetes/index.md`, then added baseline stubs for `google.golang.org/grpc` and `kube-apiserver` with disclosure references, ecosystem-specific follow-up questions, and site-friendly cross-links.

## [2026-04-10] contributor-guidance | Go module path naming
Updated `CONTRIBUTING.md` to clarify that Go pages can use nested import-path-based filenames (for example `wiki/go/google.golang.org/grpc.md`) to keep future markdown-first site routing aligned with canonical module names.

## [2026-04-11] seed-pages | Newtonsoft.Json (NuGet), openssl@3 (Homebrew), openssl (Linux)
Added first package pages for three previously empty ecosystem buckets: `.NET / NuGet`, `Homebrew`, and `Linux`. Created ecosystem landing pages for each, then added baseline stubs for `Newtonsoft.Json`, `openssl@3`, and upstream `openssl` with cross-links, evidence-backed metadata, and open questions aimed at future distro normalization and site-friendly navigation.

## [2026-04-11] advisory-review | requests (PyPI), google.golang.org/grpc (Go)
Ran a public-information-only review pass against two baseline stubs and upgraded both pages to advisory-mapped status. Curated Requests credential / redirect / TLS verification advisories and grpc-go transport / metadata / authorization findings using OSV, GitHub Security Advisories, upstream release notes, and CVE references. Updated `wiki/python/index.md`, `wiki/go/index.md`, and the master index descriptors to reflect the deeper coverage.

## [2026-04-11] advisory-review | Newtonsoft.Json (NuGet), jsonwebtoken (npm), koa-router (npm)
Ran a public-information-only review pass on two high-value package pages and one gap candidate. Upgraded `Newtonsoft.Json` from stub to advisory-mapped with the nested-input DoS issue fixed in 13.0.1 and added release-note-backed hardening context around `MaxDepth`. Refreshed `jsonwebtoken` so the page now reflects the accepted GHSA/CVE set around verification semantics, explicitly marks CVE-2022-23529 as rejected, and keeps the filed `clockTolerance` issue separate from published advisories. Reviewed `koa-router` as a gap candidate but did not force page changes because the public evidence gathered in this pass did not justify a substantive update.

## [2026-04-12] advisory-review | express (npm), koa-router (npm), serde (crates.io)
Ran a public-information-only review pass against three candidates using OSV package queries and GitHub repository advisory listings saved under `raw/advisory-review-2026-04-12/`. Public evidence showed multiple package advisories for `express`, while `koa-router` and `serde` returned no package-scoped OSV matches and no repository security advisories in this pass. The requested local Claude CLI synthesis step could not complete because the installed CLI returned a 401 authentication error, so no evidence-backed package-page edits were forced from this pass. Fixed unresolved merge conflict markers that had landed in `wiki/index.md` and `wiki/log.md` on `main`, and preserved the gathered evidence files for the next review.
