# Microsoft.Data.SqlClient (.NET)

**Registry:** NuGet
**Weekly Downloads:** unknown (widely used as the primary ADO.NET data provider for Microsoft SQL Server; consumed by Entity Framework Core, Dapper, and most enterprise .NET data-access stacks; as of 2026-07-10)
**Repository:** https://github.com/dotnet/SqlClient
**Security Contact:** https://msrc.microsoft.com/report
**Disclosure Policy:** Microsoft Security Response Center (MSRC); https://www.microsoft.com/en-us/msrc/security-policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No third-party audits on record. Microsoft maintains an internal SDL process; security issues are reported via MSRC and disclosed through GitHub Security Advisories.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-41064 / GHSA-8g2p-5pqh-5jmc | Moderate (CVSS:3.1 7.1 AV:A/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N) | Information disclosure via async query timeout race — under high-load conditions, a timeout during an asynchronously executed SQL query can cause incorrect data from a different in-flight query to be returned to the caller; requires an adjacent network attacker or a shared SQL Server connection pool | Microsoft.Data.SqlClient ≥ 1.1.4 or ≥ 2.1.2; System.Data.SqlClient ≥ 4.8.5 | [GHSA-8g2p-5pqh-5jmc](https://github.com/advisories/GHSA-8g2p-5pqh-5jmc) |
| CVE-2024-0056 / GHSA-98g6-xh36-x2p7 | High (CVSS:3.1 7.7 AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:N) | SQL Data Provider security feature bypass — a network-exploitable TLS/security-feature bypass vulnerability in Microsoft.Data.SqlClient and System.Data.SqlClient; allows a remote attacker to bypass SQL Server connection security features without prior authentication; exact mechanism is not fully disclosed in the public GHSA record | Microsoft.Data.SqlClient ≥ 2.1.7 / 3.1.5 / 4.0.5 / 5.1.3; System.Data.SqlClient ≥ 4.8.6 | [GHSA-98g6-xh36-x2p7](https://github.com/advisories/GHSA-98g6-xh36-x2p7) |

## Security Posture Notes

`Microsoft.Data.SqlClient` is the modern, actively maintained ADO.NET driver for Microsoft SQL Server. It supersedes the older `System.Data.SqlClient` (shipped in-box with .NET Framework) and is the recommended driver for all new development targeting SQL Server from .NET 5 onward. Entity Framework Core (EF Core) uses it as the default SQL Server provider.

**CVE-2024-0056 (High CVSS 7.7)** is the most significant advisory: a network-reachable security feature bypass affecting all major release lines (1.x, 2.x, 3.x, 4.x, 5.x). The MSRC advisory classifies it as a TLS-related bypass but does not publicly disclose the precise exploitation mechanism. The broad version range and network attack vector (AV:N) make this a high-priority update for any application connecting to SQL Server from external or semi-trusted network contexts. Fixed in: 2.1.7 / 3.1.5 / 4.0.5 / 5.1.3.

**CVE-2022-41064 (Moderate CVSS 7.1)** involves cross-query data leakage under timeout races in the async query path. While an adjacent-network context (AV:A) limits direct external exploitability, this is meaningful in shared connection-pool environments (cloud database gateways, multi-tenant SQL Server instances) where data from one tenant's query timing out could be read by another request.

**Transitive dependency risk**: Applications using Entity Framework Core (via `Microsoft.EntityFrameworkCore.SqlServer`), Dapper, or other ORM packages that take a transitive dependency on `Microsoft.Data.SqlClient` should verify they are pulling a fixed version. The GHSA record for CVE-2024-0056 includes guidance for resolving both direct and transitive dependencies.

**Version line support**: Microsoft.Data.SqlClient follows a .NET support lifecycle. The `2.1.x` long-term support line and `5.x` current line receive active security patches. Older 1.x, 3.x, and 4.x lines are end-of-life or in maintenance-only mode; consumers should upgrade to a supported branch.

## Dependencies of Note

- `Microsoft.EntityFrameworkCore.SqlServer` — EF Core's SQL Server provider takes a direct dependency on `Microsoft.Data.SqlClient`; EF Core applications are transitively exposed to these CVEs.
- `System.Data.SqlClient` — the legacy in-box driver (part of .NET Framework, still a NuGet package for .NET Core) shares the CVE-2022-41064 and CVE-2024-0056 vulnerability history and has its own fixed versions; see the GHSA records for corresponding `System.Data.SqlClient` fixed versions.

## Open Questions

- Are there additional advisories in the 6.x release line (latest as of 2026) not covered by this mapping? Check the GitHub Security Advisories tab at https://github.com/dotnet/SqlClient/security/advisories.
- What is the exact TLS mechanism bypassed in CVE-2024-0056? The MSRC public advisory is intentionally vague; a follow-up deep-dive could clarify whether it affects Encrypt=Mandatory or certificate validation.
- What are the total NuGet download counts for Microsoft.Data.SqlClient? The NuGet stats API did not return download totals in this pass; revisit with direct NuGet gallery query.

## Related Pages

- [[dotnet/Npgsql]]
- [[dotnet/System.Text.Json]]
- [[dotnet/index]]

---
*Last updated: 2026-07-10 | Sources: 3 (github/advisory-database GHSA records × 2, MSRC advisory context, NuGet package metadata)*
