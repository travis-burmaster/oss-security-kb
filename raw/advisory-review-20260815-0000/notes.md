# Advisory Review Pass Notes — 2026-08-15

**Session:** nightly/oss-kb-4h-20260815-0000
**Targets:** diesel (Rust/crates.io), org.springframework.cloud/spring-cloud-gateway (Maven)
**Constraint:** OSV.dev HTTP 403 — all advisory data sourced from rustsec/advisory-db and github/advisory-database

---

## Target Selection

- **Previous pass (2026-08-13):** Go + .NET ecosystems (opa, log4net)
- **Under-covered ecosystems at time of selection:** Rust (34 pages), Maven (30 pages)
- **Candidates evaluated:**
  - `gorm.io/gorm` (Go): 0 results in github/advisory-database — skipped
  - `url` (rust-url crate): 0 results in rustsec/advisory-db — skipped
  - `diesel` (Rust): 8 RUSTSEC advisories confirmed — SELECTED
  - `spring-cloud-gateway` (Maven): 6 confirmed GHSA advisories incl. Critical CVE-2022-22947 (CISA KEV) — SELECTED

---

## diesel (Rust/crates.io)

### Sources consulted

- `mcp__github__search_code`: query `"diesel" repo:rustsec/advisory-db` — confirmed advisory IDs
- `WebFetch` on `raw.githubusercontent.com/rustsec/advisory-db/main/crates/diesel/<ID>.md` for each RUSTSEC:
  - RUSTSEC-2021-0037: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/diesel/RUSTSEC-2021-0037.md
  - RUSTSEC-2024-0365: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/diesel/RUSTSEC-2024-0365.md
  - RUSTSEC-2026-0111: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/diesel/RUSTSEC-2026-0111.md
  - RUSTSEC-2026-0134: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/diesel/RUSTSEC-2026-0134.md
  - RUSTSEC-2026-0135: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/diesel/RUSTSEC-2026-0135.md
  - RUSTSEC-2026-0136: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/diesel/RUSTSEC-2026-0136.md
  - RUSTSEC-2026-0137: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/diesel/RUSTSEC-2026-0137.md
  - RUSTSEC-2026-0172: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/diesel/RUSTSEC-2026-0172.md
- crates.io API: https://crates.io/api/v1/crates/diesel — confirmed ~6.1M/week, ~33.2M total, max_version 2.3.12

### Advisory summary

| ID | Severity | Fix |
|----|----------|-----|
| RUSTSEC-2021-0037 / CVE-2021-28305 | Critical CVSS 9.8 | ≥ 1.4.6 |
| RUSTSEC-2024-0365 | Moderate | ≥ 2.2.3 |
| RUSTSEC-2026-0111 | Informational | ≥ 2.3.8 |
| RUSTSEC-2026-0134 | Informational | ≥ 2.3.8 |
| RUSTSEC-2026-0135 | Informational | ≥ 2.3.8 |
| RUSTSEC-2026-0136 | Moderate | ≥ 2.3.8 |
| RUSTSEC-2026-0137 | Informational | ≥ 2.3.8 |
| RUSTSEC-2026-0172 | Informational | ≥ 2.3.10 |

---

## spring-cloud-gateway (Maven)

### Sources consulted

- `mcp__github__search_code`: query `"spring-cloud-gateway" repo:github/advisory-database` — returned 6 github-reviewed GHSA records
- WebFetch on individual GHSA JSON paths:
  - CVE-2021-22051: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/...
  - CVE-2022-22947 / GHSA-tpvf-6g75-5cv5: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/...
  - CVE-2025-41235: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/...
  - CVE-2025-41243: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/...
  - CVE-2025-41253: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/...
  - CVE-2026-22750: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/...
- spring.io/security: https://spring.io/security (advisory index consulted)
- Maven Central stats API: returned 404 for spring-cloud-gateway — download count marked "unknown"

### Advisory summary

| CVE | Severity | Key detail |
|-----|----------|------------|
| CVE-2021-22051 | Moderate | Route security bypass |
| CVE-2022-22947 | Critical CVSS 10.0 | SpEL RCE via Actuator; CISA KEV; actively exploited; fixed ≥3.0.7/3.1.1 |
| CVE-2025-41235 | High | Routing/filter bypass (2025 batch) |
| CVE-2025-41243 | Critical CVSS 10.0 | Actuator code injection (2025 batch) |
| CVE-2025-41253 | High CVSS 7.5 | Actuator endpoint bypass (2025 batch) |
| CVE-2026-22750 | High CVSS 7.5 | Routing/filter bypass (2026) |

---

## Files produced

- `wiki/rust/diesel.md` (new advisory-mapped page)
- `wiki/maven/org.springframework.cloud/spring-cloud-gateway.md` (new advisory-mapped page)
- `wiki/rust/index.md` (updated: diesel entry added, count 34→35)
- `wiki/maven/index.md` (updated: spring-cloud-gateway entry added, count 30→31, date updated)
- `wiki/index.md` (updated: total 256→258, Rust 34→35, Maven 30→31, date 2026-08-13→2026-08-15)
- `wiki/log.md` (prepended 2026-08-15 entry)
