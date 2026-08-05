# Advisory Review Notes — 2026-08-05

## Pass targets

- `rust/sqlx` (new page)
- `rust/tonic` (new page)

## Sources consulted

### rust/sqlx

- `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/sqlx/RUSTSEC-2024-0363.md` — primary advisory content
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/08/GHSA-xmrp-424f-vfpx/GHSA-xmrp-424f-vfpx.json` — GHSA record (Moderate, no CVSS, no CVE)
- `https://crates.io/api/v1/crates/sqlx` — download stats (126,238,086 total; 31,914,244 recent/90d → ~2.5M/week); max_version 0.9.0
- `mcp__github__search_code`: "sqlx repo:rustsec/advisory-db" → 3 results; only RUSTSEC-2024-0363.md in crates/sqlx/ applies; RUSTSEC-2020-0010 (tiberius) and RUSTSEC-2024-0421 (idna) are false positives
- `mcp__github__search_code`: "sqlx repo:github/advisory-database path:advisories/github-reviewed" → 4 results; GHSA-xmrp-424f-vfpx is the only sqlx-crate advisory; GHSA-wvq5-72qp-grjw (symphonycms), GHSA-wr69-g62g-2r9h (apache derby), GHSA-7rpj-hg47-cx62 (h2database) are false positives

### rust/tonic

- `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/tonic/RUSTSEC-2024-0376.md` — primary advisory content
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/10/GHSA-4jwc-w2hc-78qv/GHSA-4jwc-w2hc-78qv.json` — GHSA record (Moderate, CVSS 3.1: 5.3, CVE-2024-47609, CWE-755)
- `https://crates.io/api/v1/crates/tonic` — download stats (347,760,435 total; 80,795,771 recent/90d → ~6.3M/week); max_version 0.14.6
- `mcp__github__search_code`: "tonic repo:rustsec/advisory-db" → 3 results; only RUSTSEC-2024-0376.md in crates/tonic/ applies; RUSTSEC-2021-0112 (tectonic_xdv) and RUSTSEC-2021-0108 (ckb) are false positives
- `mcp__github__search_code`: "tonic repo:github/advisory-database path:advisories/github-reviewed" → 12 results; only GHSA-4jwc-w2hc-78qv applies to tonic (crates.io); 11 false positives from: rustfs, tectonic_xdv (×2), ml-dsa, hackney, zebrad, fission (Go), ckb, netty-codec-redis, aws-sdk-rust packages

## OSV.dev API

Blocked (HTTP 403) per environment policy. All advisory content sourced from rustsec/advisory-db and github/advisory-database via WebFetch on raw.githubusercontent.com.

## Findings summary

| Crate | Advisory | Severity | Category | Fixed |
|-------|----------|----------|----------|-------|
| sqlx | RUSTSEC-2024-0363 / GHSA-xmrp-424f-vfpx | Moderate | Format injection / integer overflow | ≥ 0.8.1 |
| tonic | RUSTSEC-2024-0376 / CVE-2024-47609 / GHSA-4jwc-w2hc-78qv | Moderate (CVSS 5.3) | DoS / improper error handling | ≥ 0.12.3 |
