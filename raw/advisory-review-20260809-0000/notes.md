# Advisory Review — 2026-08-09

## Pass summary
- Date: 2026-08-09
- Ecosystems targeted: Rust/crates.io, .NET/NuGet
- Pages added: rust/prost, dotnet/Microsoft.AspNetCore.Authentication.Negotiate
- Total advisories mapped: 3 (1 RUSTSEC + 1 GHSA for prost; 2 GHSA for Negotiate)

## Candidates considered

### Initial Rust candidates
1. **rust/zip** — No RUSTSEC advisories in advisory-db (path:crates/zip returned 0 results). Rejected (no confirmed advisories to map).
2. **rust/prost** — RUSTSEC-2020-0002 / CVE-2020-35858 confirmed. Selected. 524M+ total downloads, ~122M/week.

### Initial .NET candidates
1. **StackExchange.Redis** — 0 GHSA results in github/advisory-database. Rejected (no confirmed advisories).
2. **Microsoft.AspNetCore.Authentication.Negotiate** — 2 GHSA results (both July 2026, High severity). Selected. 56.3M total downloads.

## URLs consulted

### rust/prost
- https://crates.io/api/v1/crates/prost — download stats, max_version 0.14.4
- rustsec/advisory-db search: `repo:rustsec/advisory-db path:crates/prost` → RUSTSEC-2020-0002.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/prost/RUSTSEC-2020-0002.md — advisory text
- github/advisory-database search: `prost CVE-2020-35858 repo:github/advisory-database` → GHSA-gv73-9mwv-fwgq.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/08/GHSA-gv73-9mwv-fwgq/GHSA-gv73-9mwv-fwgq.json — GHSA detail
- https://github.com/tokio-rs/prost — repository (referenced, not fetched)

### dotnet/Microsoft.AspNetCore.Authentication.Negotiate
- github/advisory-database search: `Authentication.Negotiate repo:github/advisory-database path:advisories` → 2 results (total_count: 2)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/07/GHSA-8prm-248r-h957/GHSA-8prm-248r-h957.json — CVE-2026-47300 detail
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/07/GHSA-2p3q-h3hg-jcqq/GHSA-2p3q-h3hg-jcqq.json — CVE-2026-47303 detail
- https://api.nuget.org/v3-flatcontainer/microsoft.aspnetcore.authentication.negotiate/index.json — latest version 10.0.10
- https://www.nuget.org/packages/Microsoft.AspNetCore.Authentication.Negotiate — total download count 56.3M
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-47300 (referenced in GHSA)
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-47303 (referenced in GHSA)

## Environment notes
- OSV.dev (api.osv.dev) blocked — HTTP 403 as expected; all advisories sourced from rustsec/advisory-db and github/advisory-database
- azuresearch-usnc.nuget.org blocked — used api.nuget.org and nuget.org instead for package stats
- git push blocked (HTTP 403) — using mcp__github__ tools for all remote writes
- gh CLI not installed — not used
