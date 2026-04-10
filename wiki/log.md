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

