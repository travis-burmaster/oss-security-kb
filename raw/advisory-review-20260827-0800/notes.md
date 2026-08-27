# Advisory Review — 2026-08-27 08:00 UTC

## Targets

1. `linux/rsync` — rsync file-synchronization tool
2. `dotnet/Swashbuckle.AspNetCore` — ASP.NET Core Swagger/OpenAPI library

## Sources Consulted

### rsync

| URL | Accessed | Purpose |
|-----|----------|---------|
| https://github.com/advisories/GHSA-85h7-m8c3-v9wc | 2026-08-27 | CVE-2024-12084 unreviewed advisory (Critical CVSS 9.8 heap overflow) |
| https://github.com/advisories/GHSA-xh5q-pch5-g3xq | 2026-08-27 | CVE-2024-12085 unreviewed advisory (High CVSS 7.5 info leak) |
| mcp__github__search_code repo:github/advisory-database rsync | 2026-08-27 | Discovery: found 23 total results; filtered to 6 rsync-native CVEs |
| GHSA-82c6-8mfc-c23h | 2026-08-27 | CVE-2024-12086 Moderate — server enumerates client files |
| GHSA-9x68-7qq6-v523 | 2026-08-27 | CVE-2024-12087 Moderate — path traversal via --inc-recursive |
| GHSA-ffph-g3pc-8r3g | 2026-08-27 | CVE-2024-12088 Moderate — --safe-links bypass |
| GHSA-gp7r-m4cc-qhwq | 2026-08-27 | CVE-2024-12747 Moderate — symlink race condition |
| https://github.com/RsyncProject/rsync | 2026-08-27 | Repository and security contact verification |

All 6 CVEs disclosed 2025-01-14 by Google Open Source Security Team. Fixed version: rsync 3.4.0.
openwall.com/lists/oss-security/2025/01/14/3 blocked by egress proxy; GHSA unreviewed records used as primary sources.

### Swashbuckle.AspNetCore

| URL | Accessed | Purpose |
|-----|----------|---------|
| https://github.com/advisories/GHSA-qrmm-w75w-3wpx | 2026-08-27 | SSRF via ?url advisory (primary source) |
| mcp__github__search_code repo:github/advisory-database Swashbuckle | 2026-08-27 | Discovery: 1 result found (GHSA-qrmm-w75w-3wpx) |
| https://api.nuget.org/v3/registration5-gz-semver2/swashbuckle.aspnetcore/index.json | 2026-08-27 | NuGet registry metadata — downloads and version |
| https://www.nuget.org/packages/Swashbuckle.AspNetCore | 2026-08-27 | Package metadata: ~1.3B downloads, latest 10.2.3 |
| https://github.com/domaindrivendev/Swashbuckle.AspNetCore | 2026-08-27 | Repository and security contact verification |

Only 1 GHSA advisory found for Swashbuckle.AspNetCore itself; swagger-ui upstream npm package has additional XSS history tracked separately (CVE-2020-26870). Search for CVE-2024-45046 in advisory database returned 0 results; not included without verified source.
