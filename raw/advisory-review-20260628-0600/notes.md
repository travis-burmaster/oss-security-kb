# Advisory Review — 2026-06-28 0600 UTC

## Scope

Three packages selected for this pass, prioritising under-covered Rust ecosystem and a gap in .NET database-client coverage:

1. `rust/smallvec` (crates.io) — high-download Rust utility crate with 5 known RustSec advisories
2. `rust/time` (crates.io) — widely used date/time crate with 2 known RustSec advisories
3. `dotnet/Npgsql` (NuGet) — de facto standard .NET PostgreSQL client with 1 GHSA advisory

## Sources Consulted

### rust/smallvec
- `mcp__github__search_code` on `rustsec/advisory-db` (path:crates/smallvec) — returned 5 advisory files
- `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/smallvec/RUSTSEC-2018-0003.md`
- `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/smallvec/RUSTSEC-2018-0018.md`
- `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/smallvec/RUSTSEC-2019-0009.md`
- `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/smallvec/RUSTSEC-2019-0012.md`
- `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/smallvec/RUSTSEC-2021-0003.md`
- `https://crates.io/api/v1/crates/smallvec` — ~929.97M total downloads, ~197.37M recent (90d); max_stable_version: 1.15.2

### rust/time
- `mcp__github__search_code` on `rustsec/advisory-db` (path:crates/time) — returned 2 advisory files
- `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/time/RUSTSEC-2020-0071.md`
- `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/time/RUSTSEC-2026-0009.md`
- `https://crates.io/api/v1/crates/time` — ~737.94M total downloads, ~139.31M recent (90d); max_stable_version: 0.3.51 (released 2026-06-22)

### dotnet/Npgsql
- `mcp__github__search_code` on `github/advisory-database` (Npgsql ecosystem NuGet) — returned 1 advisory file (GHSA-x9vc-6hfv-hg8c)
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/05/GHSA-x9vc-6hfv-hg8c/GHSA-x9vc-6hfv-hg8c.json` — CVE-2024-32655, CVSS 9.1, all major branches affected through 8.0.2, patched May 2024
- `https://www.nuget.org/packages/Npgsql` — 871.2M total downloads; latest stable 10.0.3 (2026-05-27)

## Notes

- OSV.dev API blocked (HTTP 403) per known environment constraint; all advisory content sourced from rustsec/advisory-db and github/advisory-database directly
- No inventions; every vulnerability row is backed by a named RustSec or GHSA record
- Affected version ranges and fix versions taken verbatim from the advisory files
- smallvec: all 5 advisories are historical (2018–2021); current 1.x (≥1.6.1) is clean
- time: RUSTSEC-2020-0071 has no CVE or CVSS assigned; RUSTSEC-2026-0009 has CVE-2026-25727 / GHSA-r6v5-fh4h-64xc
- Npgsql: `Microsoft.Data.SqlClient` also has 2 advisories (GHSA-8g2p-5pqh-5jmc / CVE-2022-41064 and GHSA-98g6-xh36-x2p7 / CVE-2024-0056) — screened but deferred to a future pass
