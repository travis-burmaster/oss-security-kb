# Advisory Review Pass — 2026-08-19

## Targets selected

1. `github.com/dgrijalva/jwt-go` (Go ecosystem): archived JWT library with 29,217 pkg.go.dev importers; CVE-2020-26160 well-documented in github/advisory-database; successor `golang-jwt/jwt` already in wiki.
2. `image` (Rust / crates.io): dominant image encoding/decoding library; ~3.3M/week estimated downloads; 2 RUSTSEC advisories confirmed in rustsec/advisory-db.

## Sources consulted

### github.com/dgrijalva/jwt-go

- GHSA-w73w-5m7g-f7qc (fetched): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/05/GHSA-w73w-5m7g-f7qc/GHSA-w73w-5m7g-f7qc.json
- GO-2020-0017: https://pkg.go.dev/vuln/GO-2020-0017
- pkg.go.dev import count: https://pkg.go.dev/github.com/dgrijalva/jwt-go (29,217 importers as of 2026-08-19)
- GitHub issue tracker: https://github.com/dgrijalva/jwt-go/issues/422

Advisory search result: `mcp__github__search_code` with query "dgrijalva/jwt-go repo:github/advisory-database" returned total_count: 1. GHSA-w73w-5m7g-f7qc is the only advisory on record for this package.

Package is archived; the CVE carries CWE-287 (improper authentication) and CWE-755 (improper handling of exceptional conditions). No fix will be issued. Confirmed: only remediation is migration to golang-jwt/jwt >= 3.2.1.

### image (crates.io)

- rustsec/advisory-db search: `mcp__github__search_code` with query "RUSTSEC repo:rustsec/advisory-db path:crates/image" returned 2 results: RUSTSEC-2019-0014, RUSTSEC-2020-0073
- RUSTSEC-2019-0014 (fetched): https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/image/RUSTSEC-2019-0014.md
- RUSTSEC-2020-0073 (fetched): https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/image/RUSTSEC-2020-0073.md
- GHSA-m2pf-hprp-3vqm (alias for RUSTSEC-2019-0014): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/08/GHSA-m2pf-hprp-3vqm/GHSA-m2pf-hprp-3vqm.json
- GHSA-9wgh-vjj7-7433 (alias for RUSTSEC-2020-0073): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/08/GHSA-9wgh-vjj7-7433/GHSA-9wgh-vjj7-7433.json
- crates.io API: https://crates.io/api/v1/crates/image (downloads: 170,413,534 total; recent_downloads: 42,591,416; max_version: 0.25.10)

Additional GHSA search: `mcp__github__search_code` with query "image-rs/image repo:github/advisory-database" returned 5 results. Three (GHSA-5qv7-j6w5-fr4m, GHSA-qg8r-f7x3-25f7, GHSA-w5p8-4jcx-2j6r) affect the `imageproc` crate (image processing algorithms, part of the image-rs org) — not the `image` crate. These are RUSTSEC-2026-0115/0116/0117. Documented as notes in the image page; separate `imageproc` page is an open question.

## Pages written

- `wiki/go/github.com/dgrijalva/jwt-go.md` (new, advisory-mapped, 1 advisory)
- `wiki/rust/image.md` (new, advisory-mapped, 2 advisories)

## Indexes updated

- `wiki/go/index.md`: added dgrijalva/jwt-go entry; count 25 → 26
- `wiki/rust/index.md`: added image entry; count 34 → 35
- `wiki/index.md`: Go count 25 → 26, Rust count 34 → 35, total 256 → 258; last updated 2026-08-13 → 2026-08-19
- `wiki/log.md`: new entry prepended
