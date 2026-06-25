# Advisory Review — 2026-06-25 06:00 UTC

Pass targeting under-covered Rust (15→17) and Go (16→17) ecosystems.
OSV.dev API blocked (HTTP 403); all advisory content sourced from rustsec/advisory-db and github/advisory-database via raw.githubusercontent.com and mcp__github__search_code.

## Targets

### rust/axum (new page)
- crates.io API: https://crates.io/api/v1/crates/axum — version 0.8.9, ~361.7M total / ~89.5M 90-day downloads
- crates.io API: https://crates.io/api/v1/crates/axum-core — version 0.5.6
- rustsec/advisory-db search: 1 result — crates/axum-core/RUSTSEC-2022-0055.md
- Raw advisory: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/axum-core/RUSTSEC-2022-0055.md
  → CVE-2022-3212 / GHSA-m77f-652q-wwp4; no default body size limit DoS; patched axum ≥ 0.5.16 / axum-core ≥ 0.2.8
- github/advisory-database search: no additional axum advisories found beyond GHSA-m77f-652q-wwp4
- Additional context: RUSTSEC-2021-0135 and RUSTSEC-2022-0043 (tower-http file-disclosure) noted as related but on a different crate

### rust/rustls-webpki (new page)
- rustsec/advisory-db search: 5 advisory files in crates/rustls-webpki/ plus 1 in crates/webpki/
- Raw advisory: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/rustls-webpki/RUSTSEC-2023-0053.md
  → CPU DoS in cert path building; exponential time; patched ≥ 0.100.2 / ≥ 0.101.4
- Raw advisory: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/rustls-webpki/RUSTSEC-2026-0049.md
  → GHSA-pwjx-qhcg-rvj4; CRL distribution point matching bug; revocation bypass under UnknownStatusPolicy::Allow; patched ≥ 0.103.10
- Raw advisory: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/rustls-webpki/RUSTSEC-2026-0098.md
  → GHSA-965h-392x-2mh5; URI name constraints ignored; patched ≥ 0.103.12 / ≥ 0.104.0-alpha.6
- Raw advisory: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/rustls-webpki/RUSTSEC-2026-0099.md
  → GHSA-xgp8-3hg3-c2mh; DNS wildcard name constraint bypass; patched ≥ 0.103.12 / ≥ 0.104.0-alpha.6
- Raw advisory: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/rustls-webpki/RUSTSEC-2026-0104.md
  → CRL parsing panic DoS pre-auth via empty BIT STRING in onlySomeReasons; patched ≥ 0.103.13 / ≥ 0.104.0-alpha.7
- Raw advisory: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/webpki/RUSTSEC-2023-0052.md
  → GHSA-8qv2-5vq6-g2g7; predecessor crate webpki same CPU DoS; patched ≥ 0.22.2
- crates.io API: https://crates.io/api/v1/crates/rustls-webpki — version 0.103.13, ~601.5M total / ~156.8M 90-day downloads

### go/gopkg.in/yaml.v3 (new page)
- github/advisory-database search: 1 result for gopkg.in/yaml.v3
- Raw advisory: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-hp87-p4gw-j4gq/GHSA-hp87-p4gw-j4gq.json
  → CVE-2022-28948; Unmarshal panic on malformed YAML; High CVSS 7.5 / CWE-502; fixed v3.0.1; Go vuln alias GO-2022-0272
- pkg.go.dev: gopkg.in/yaml.v3 — v3.0.1 current, 34,113 importers, released 2022-05-27
- Also researched gopkg.in/yaml.v2 advisories: GHSA-r88r-gmrh-7j83/CVE-2021-4235, GHSA-6q6q-88xp-6f2r/CVE-2022-3064, GHSA-wxc4-f4m6-wwqv/CVE-2019-11254 (noted in posture section, yaml.v2 warrants a future page)
