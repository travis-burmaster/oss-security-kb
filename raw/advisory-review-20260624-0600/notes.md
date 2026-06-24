# Advisory Review Pass — 2026-06-24 06:00 UTC

## Targets Selected
- `rust/actix-web` (actix-web crate + actix-http + actix-files ecosystem) — no existing KB page; high-profile Rust web framework with known advisory history
- `rust/rand` — no existing KB page; ~1.3B total downloads; fresh 2026 unsoundness advisory RUSTSEC-2026-0097

## URLs Consulted

### rustsec/advisory-db (GitHub MCP code search + raw.githubusercontent.com)
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/actix-web/RUSTSEC-2018-0019.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/actix-http/RUSTSEC-2020-0048.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/rand/RUSTSEC-2026-0097.md

### github/advisory-database (raw.githubusercontent.com)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/01/GHSA-9qj6-4rfq-vm84/GHSA-9qj6-4rfq-vm84.json  (CVE-2018-25024 Critical CVSS 9.8)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/08/GHSA-v3j6-xf77-8r9c/GHSA-v3j6-xf77-8r9c.json  (CVE-2020-35901 High CVSS 9.1)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/08/GHSA-8928-2fgm-6x9x/GHSA-8928-2fgm-6x9x.json  (CVE-2021-38512 High CVSS 7.5)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/02/GHSA-8v2v-wjwg-vx6r/GHSA-8v2v-wjwg-vx6r.json  (actix-files info exposure Moderate)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/02/GHSA-gcqf-3g44-vc9p/GHSA-gcqf-3g44-vc9p.json  (actix-files empty Range DoS Moderate)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/04/GHSA-xhj4-vrgc-hr34/GHSA-xhj4-vrgc-hr34.json  (actix-http CL.TE smuggling Medium CVSS 4.0)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/04/GHSA-cq8v-f236-94qc/GHSA-cq8v-f236-94qc.json  (rand unsoundness Low)

### GitHub code search (advisory-db discovery)
- mcp__github__search_code: `actix-web repo:rustsec/advisory-db path:crates`
- mcp__github__search_code: `rand repo:rustsec/advisory-db path:crates/rand`
- mcp__github__search_code: `actix-web repo:github/advisory-database path:advisories`
- mcp__github__search_code: `GHSA-cq8v-f236-94qc repo:github/advisory-database path:advisories`

### crates.io API
- https://crates.io/api/v1/crates/actix-web  (total: 71,285,016; recent-90d: 8,607,527; current: 4.14.0)
- https://crates.io/api/v1/crates/rand       (total: 1,298,527,728; recent-90d: 307,936,560; current: 0.10.1)

## OSV.dev
- Blocked (HTTP 403) — not used; all advisory content sourced from rustsec/advisory-db and github/advisory-database.

## Pages Written
- wiki/rust/actix-web.md — advisory-mapped — 8 vulnerability rows
- wiki/rust/rand.md — advisory-mapped — 1 vulnerability row

## Index Updates
- wiki/rust/index.md: 13 → 15 entries
- wiki/index.md: 197 → 199 pages, date 2026-06-24
- wiki/log.md: 2026-06-24 entry prepended
