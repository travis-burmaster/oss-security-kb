# Advisory Review — 2026-09-13 08:00 UTC

## Pass Summary

Ecosystems targeted: Rust/crates.io, Go
Packages added: rust/http, go/github.com/lestrrat-go/jwx
OSV.dev: blocked (HTTP 403) — not used

---

## Target 1: rust/http (hyperium/http crate)

**Selection rationale:** >1B total downloads; foundational dependency of hyper, reqwest, axum,
warp, tower-http, tonic, actix-web; under-covered despite ecosystem centrality.

**Sources consulted:**
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/http/RUSTSEC-2019-0033.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/http/RUSTSEC-2019-0034.md
- https://crates.io/api/v1/crates/http (download stats, latest version)
- mcp__github__search_code query: `repo:rustsec/advisory-db path:crates/http`
- mcp__github__search_code query: `repo:rustsec/advisory-db "package = \"http\"" path:crates`

**Advisories confirmed:**
- RUSTSEC-2019-0033 / CVE-2019-25008 / CVE-2020-25574: High CVSS 7.5 AV:N — integer overflow in HeaderMap::reserve() via next_power_of_two() wrapping to zero → infinite probing DoS; fixed 0.1.20
- RUSTSEC-2019-0034 / CVE-2019-25009: Critical CVSS 9.8 — HeaderMap::Drain double-free + data race unsoundness; fixed 0.1.20

**Stats:** crates.io total 1,005,012,247 downloads; 90-day recent 232,756,669 (~18.1M/week est.); latest stable 1.5.0

**Excluded:** No additional advisories found beyond the 2019 pair for 0.1.x, 0.2.x, or 1.x lines.

---

## Target 2: go/github.com/lestrrat-go/jwx

**Selection rationale:** Dominant Go JOSE/JWT implementation; 4 confirmed GHSA advisories
discovered via mcp__github__search_code; used in identity and auth middleware.

**Sources consulted:**
- mcp__github__search_code query: `repo:github/advisory-database "lestrrat-go/jwx" path:advisories/github-reviewed`
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/06/GHSA-rm8v-mxj3-5rmq/GHSA-rm8v-mxj3-5rmq.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/12/GHSA-7f9x-gw85-8grf/GHSA-7f9x-gw85-8grf.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/01/GHSA-pvcr-v8j8-j5q3/GHSA-pvcr-v8j8-j5q3.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/03/GHSA-hj3v-m684-v259/GHSA-hj3v-m684-v259.json
- https://pkg.go.dev/github.com/lestrrat-go/jwx/v2?tab=importedby (returned 0 — likely crawl gap; treated as unknown)
- mcp__github__search_code query: `repo:lestrrat-go/jwx go.mod` (confirmed v4 design docs exist)

**Advisories confirmed:**
1. GHSA-rm8v-mxj3-5rmq (2023-06): Moderate — AES-CBC JWE padding oracle; fixed v1.2.26/v2.0.11
2. GHSA-7f9x-gw85-8grf / CVE-2023-49290 (2023-12): Moderate CVSS 5.3 — p2c PBKDF2 DoS; fixed v1.2.27/v2.0.18
3. GHSA-pvcr-v8j8-j5q3 / CVE-2024-21664 (2024-01): Moderate CVSS 7.5 — nil-ptr dereference DoS in jws.Parse(); fixed v1.2.28/v2.0.19
4. GHSA-hj3v-m684-v259 / CVE-2024-28122 (2024-03): Moderate CVSS 7.5 — JWE decompression bomb DoS; fixed v1.2.29/v2.0.21

**Stats:** Import count unknown (pkg.go.dev unreliable for this module this pass); v3/v4 in active development as of mid-2026 per design docs in repo

---

## Index changes

- wiki/rust/index.md: 41 → 42 pages (added rust/http)
- wiki/go/index.md: 33 → 34 pages (added go/github.com/lestrrat-go/jwx)
- wiki/index.md: 288 → 290 pages; Rust section (41)→(42); Go section (33)→(34); header date updated
- wiki/log.md: entry prepended
