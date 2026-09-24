# Advisory Review — 2026-09-24 06:11 UTC

## Targets

- **Maven: `org.hibernate:hibernate-core`** — dominant Java ORM, not yet covered
- **Rust: `atty`** — widely used terminal-detection crate, unmaintained, RUSTSEC advisory

## Sources Consulted

### org.hibernate:hibernate-core

- https://github.com/advisories/GHSA-8grg-q944-cch5 (CVE-2019-14900, SQL injection SELECT/GROUP BY)
  - Raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/02/GHSA-8grg-q944-cch5/GHSA-8grg-q944-cch5.json
- https://github.com/advisories/GHSA-j8jw-g6fq-mp7h (CVE-2020-25638, SQL injection SQL comments)
  - Raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/02/GHSA-j8jw-g6fq-mp7h/GHSA-j8jw-g6fq-mp7h.json
- https://github.com/advisories/GHSA-2p5w-cvg5-gc5c (CVE-2026-0603, InlineIdsOrClauseBuilder SQL injection)
  - Raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/01/GHSA-2p5w-cvg5-gc5c/GHSA-2p5w-cvg5-gc5c.json
- https://github.com/advisories/GHSA-rmrm-75hp-phr2 (CVE-2020-10693) — confirmed targets `hibernate-validator`, not `hibernate-core`; excluded
- https://github.com/advisories/GHSA-fg4q-ccq8-3r5q (CVE-2024-39677) — confirmed targets NHibernate (NuGet), not org.hibernate:hibernate-core; excluded
- mcp__github__search_code: query `hibernate-core repo:github/advisory-database` → 4 results, 2 excluded as above
- hibernate.org blocked by network egress policy; GitHub API blocked for raw repository data
- Maven Central download API (search.maven.org) blocked; download stats marked "unknown"
- GitHub repository: https://github.com/hibernate/hibernate-orm (no SECURITY.md found)

### atty (Rust)

- https://rustsec.org/advisories/RUSTSEC-2021-0145.html
- Raw advisory: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/atty/RUSTSEC-2021-0145.md (fetched successfully)
  - Classification: Informational/unsound
  - Affected: all versions (no patch)
  - Aliases: GHSA-g98v-hv3f-hcfr
- crates.io API: https://crates.io/api/v1/crates/atty
  - max_version: 0.2.14; total_downloads: 353,083,733; recent_downloads: 30,124,924
- mcp__github__search_code: query `RUSTSEC-2021-0145 repo:rustsec/advisory-db` → confirmed path `crates/atty/RUSTSEC-2021-0145.md`
- GitHub repository: https://github.com/softprops/atty

## Network Policy Notes

- OSV.dev API (api.osv.dev): blocked HTTP 403
- Maven Central (search.maven.org): blocked
- hibernate.org: blocked
- GitHub API (api.github.com): HTTP 403 (requires auth)
- raw.githubusercontent.com: accessible
- crates.io API: accessible

## Pages Written

- `wiki/maven/org.hibernate/hibernate-core.md` (new, advisory-mapped, 3 advisories)
- `wiki/rust/atty.md` (new, advisory-mapped, 1 advisory)

## Index Updates

- `wiki/rust/index.md`: added atty entry (43→44 entries)
- `wiki/maven/index.md`: added hibernate-core entry (36→37 entries)
- `wiki/index.md`: added borsh (backfill from 2026-09-23 pass), atty, undertow-core (backfill), hibernate-core; fixed Rust (42→44), Maven (35→37), total (295→299)
- `wiki/log.md`: prepended entry
