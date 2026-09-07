# Advisory Review Pass — 2026-09-07T00:00Z

## Targets

- `npm/mongoose` (MongoDB ODM for Node.js)
- `rust/tracing` (async-Rust structured logging / instrumentation framework, tokio-rs org)

## Rationale

- `mongoose`: No existing wiki page; 12 GHSA advisories in github/advisory-database with at least 9 directly on the mongoose package (vs. companion packages). High npm download counts and widespread use as the MongoDB ODM in Express-based applications.
- `rust/tracing`: No existing wiki page; 1 RustSec advisory (RUSTSEC-2023-0078) found in rustsec/advisory-db. ~14.1M/week est. downloads; foundational dep for tokio, axum, hyper, tonic, and the Rust cloud-native ecosystem.

## Sources Consulted

### npm/mongoose
- `mcp__github__search_code` query: `"npm" "mongoose" "affected" repo:github/advisory-database path:advisories` — 12 results
- Raw GHSA JSON files fetched via WebFetch from `raw.githubusercontent.com/github/advisory-database/main/advisories/...`:
  - GHSA-r5xw-q988-826m (2020-09): Remote memory exposure, Moderate, no CVE
  - GHSA-8687-vv9j-hgph (2019-10): CVE-2019-17426, _bsontype bypass, Critical
  - GHSA-f825-f98c-gj3g (2022-07): CVE-2022-2564, Schema.path() prototype pollution, High
  - GHSA-h8hf-x3f4-xwgp (2022-08): CVE-2022-24304, Schema.path() prototype pollution, Critical CVSS 9.8
  - GHSA-9m93-w8w6-76hh (2023-07): CVE-2023-3696, prototype pollution in findByIdAndUpdate, Critical
  - GHSA-rc4v-99cr-pjcm (2023-10): Excluded — for `@seal-security/mongoose-fixed` (third-party fork), not mongoose itself
  - GHSA-m7xq-9374-9rvx (2024-12): CVE-2024-53900, $where operator JS injection, High CVSS 9.8
  - GHSA-vg7j-7cwx-8wgw (2025-01): CVE-2025-23061, incomplete fix for CVE-2024-53900, Critical
  - GHSA-p92x-r36w-9395 (2021-09): Excluded — for `mpath` (mongoose dependency), not mongoose itself
  - GHSA-cgjx-mwpx-47jv (2018-10): Excluded — for `express-restify-mongoose` (separate package), not mongoose
  - GHSA-wpg9-53fq-2r8h (2026-05): CVE-2026-42334, sanitizeFilter $nor bypass, High CVSS 9.1
  - GHSA-664h-wqgq-64gw (2026-07): CVE-2026-73562, prototype pollution in update casting, Moderate CVSS 3.1
- GitHub Security Advisories page: https://github.com/Automattic/mongoose/security/advisories (WebFetch)
- npm registry API (api.npmjs.org): BLOCKED — download stats marked "unknown"
- crates.io API: not applicable (npm package)

### rust/tracing
- `mcp__github__search_code` query: `tracing repo:rustsec/advisory-db path:crates/tracing` — 1 result: RUSTSEC-2023-0078
- Raw advisory fetched via WebFetch: `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/tracing/RUSTSEC-2023-0078.md`
- crates.io API: `https://crates.io/api/v1/crates/tracing` — latest 0.1.44, total 825,860,252 downloads, recent 183,385,475 (~90 day window → ~14.1M/week est.)
- GitHub repository: https://github.com/tokio-rs/tracing

## Advisory Counts

| Package | Ecosystem | New Page | Advisories Mapped |
|---------|-----------|----------|-------------------|
| mongoose | npm | yes | 9 |
| tracing | Rust/crates.io | yes | 1 |

## Index Updates

- wiki/npm/index.md: +1 entry (mongoose, advisory-mapped)
- wiki/rust/index.md: +1 entry (tracing, advisory-mapped)
- wiki/index.md: npm 93→94, Rust 39→40, total 282→284, date 2026-09-05→2026-09-07
- wiki/log.md: 2 new entries prepended
