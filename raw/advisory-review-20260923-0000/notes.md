# Advisory Review Pass — 2026-09-23 00:00 UTC

## Scope
Targeting Rust/crates.io and Maven/Java ecosystems.

## Packages Researched

### rust/borsh
- crates.io API: https://crates.io/api/v1/crates/borsh
- rustsec advisory-db search: path:crates/borsh repo:rustsec/advisory-db
- Advisory fetched: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/borsh/RUSTSEC-2023-0033.md
- GHSA alias: https://github.com/advisories/GHSA-fjx5-qpf4-xjf2
- GitHub repo: https://github.com/near/borsh-rs

### maven/io.undertow/undertow-core
- GitHub advisory database search: "io.undertow:undertow-core" repo:github/advisory-database
- Search for 2024 advisories: path:advisories/github-reviewed/2024
- Advisories fetched (raw.githubusercontent.com):
  - GHSA-h6p6-fc4w-cqhx (CVE-2014-7816)
  - GHSA-3f57-w2rp-72fc (CVE-2016-7046)
  - GHSA-3x7h-5hfr-hvjm (CVE-2017-2670)
  - GHSA-5gg7-5wv8-4gcj (CVE-2017-12165)
  - GHSA-cccf-7xw3-p2vr (CVE-2020-10719)
  - GHSA-fj7c-vg2v-ccrm (CVE-2021-3690)
  - GHSA-339q-62wm-c39w (CVE-2021-3859)
  - GHSA-m4mm-pg93-fv78 (CVE-2023-1108)
  - GHSA-3jrv-jgp8-45v3 (CVE-2023-4639)
  - GHSA-ch7q-gpff-h9hp (CVE-2024-3653)
  - GHSA-22c5-cpvr-cfvq (CVE-2024-4109) — WITHDRAWN, not included
- GitHub repository: https://github.com/undertow-io/undertow
- Total advisories in database: ~40 (10 mapped in this pass)

## APIs Used
- crates.io: accessible
- OSV.dev: blocked (HTTP 403)
- Maven Central stats: unavailable (no simple public API)
