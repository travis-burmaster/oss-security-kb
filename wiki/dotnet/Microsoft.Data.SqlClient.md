# Microsoft.Data.SqlClient (NuGet)

**Registry:** NuGet
**Weekly Downloads:** unknown (NuGet registration API does not expose per-package download totals; Microsoft.Data.SqlClient is the primary .NET SQL Server driver, a transitive dependency of Entity Framework Core SQL Server)
**Repository:** https://github.com/dotnet/SqlClient
**Security Contact:** Microsoft Security Response Center (https://msrc.microsoft.com/report); GitHub security advisories (https://github.com/dotnet/SqlClient/security)
**Disclosure Policy:** https://github.com/dotnet/SqlClient/security/policy (MSRC coordinated disclosure)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No public proactive audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-41064 / GHSA-8g2p-5pqh-5jmc | **Moderate** (CVSS:3.1 AV:A/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N) | .NET Information Disclosure: under high-load conditions, a timeout in an asynchronously executed SQL query can cause the result of a *different* query to be returned to the calling thread — a race condition in the async connection-pool path shared between `Microsoft.Data.SqlClient` and `System.Data.SqlClient`. In multi-tenant applications this can expose cross-tenant query results. Affects Microsoft.Data.SqlClient ≤ 1.1.3 and 2.0.0–2.1.1; System.Data.SqlClient ≤ 4.8.4. | Microsoft.Data.SqlClient ≥ 1.1.4, ≥ 2.1.2; System.Data.SqlClient ≥ 4.8.5 | [GHSA-8g2p-5pqh-5jmc](https://github.com/advisories/GHSA-8g2p-5pqh-5jmc) |
| CVE-2024-0056 / GHSA-98g6-xh36-x2p7 | **High** (CVSS:3.1 AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:N; CWE-319) | SQL Data Provider Security Feature Bypass: a network-positioned attacker can bypass the TLS/encryption layer protecting SQL Server communication (CWE-319: Cleartext Transmission of Sensitive Information), enabling man-in-the-middle access to query data and authentication credentials. The scope-changed, high-confidentiality/integrity vector reflects the ability to read or tamper with all SQL traffic. Affects Microsoft.Data.SqlClient across all maintained lines < 2.1.7, 3.0.0–3.1.4, 4.0.0–4.0.4, 5.0.0–5.1.2; System.Data.SqlClient ≤ 4.8.5. | Microsoft.Data.SqlClient ≥ 2.1.7, ≥ 3.1.5, ≥ 4.0.5, ≥ 5.1.3; System.Data.SqlClient ≥ 4.8.6 | [GHSA-98g6-xh36-x2p7](https://github.com/advisories/GHSA-98g6-xh36-x2p7) |

## Security Posture Notes

- **Microsoft.Data.SqlClient** is the successor to the legacy `System.Data.SqlClient` and the required .NET data provider for Microsoft SQL Server across all modern .NET targets (Core, 5/6/7/8/9). It is a transitive dependency in `Microsoft.EntityFrameworkCore.SqlServer`, which makes its advisory history directly relevant to a broad fraction of .NET web applications, Azure workloads, and enterprise data tiers.
- **CVE-2024-0056 (TLS bypass, High):** The most significant advisory on record. The CVSS scope-changed C:H/I:H vector indicates a network attacker can recover SQL credentials and read/tamper with query data without any application-level interaction — only a network position is required. The fix was coordinated via MSRC and released simultaneously across all maintained major version lines (2.x through 5.x). Any deployment on an unpatched minor version within those ranges should be treated as an active risk.
- **CVE-2022-41064 (info disclosure, Moderate):** The race-condition path under high concurrency produces unexpected cross-query data leakage rather than a classic remote-attack vector. The AV:A/AC:H scope reflects that the attacker must either induce high load or observe the race; however, in high-throughput multi-tenant deployments (shared connection pools), cross-tenant query result exposure is a serious integrity and confidentiality concern.
- **Current stable: 7.0.2** (latest non-preview as of 2026-07-14); preview 7.1.0-preview2 also available. Both are well past the vulnerable boundaries for all published advisories.
- **Note on `System.Data.SqlClient`:** The legacy package is also affected by both advisories above. Projects still using System.Data.SqlClient should migrate to Microsoft.Data.SqlClient ≥ 5.x.
- Security reports go to the Microsoft Security Response Center (MSRC) at https://msrc.microsoft.com/report. GitHub security advisories at https://github.com/dotnet/SqlClient/security are also monitored.

## Dependencies of Note

- **`Microsoft.EntityFrameworkCore.SqlServer`** — the dominant ORM layer for .NET SQL Server carries a transitive dependency on this package. Applications using EF Core may receive security fixes through EF Core version bumps.
- **`System.Data.SqlClient`** — the legacy predecessor package; both packages are affected by both published advisories. Migration to `Microsoft.Data.SqlClient` is the recommended upgrade path.

## Open Questions

- Are there additional advisories in the MSRC archive or the GitHub advisory database for the 1.x line not surfaced in this pass?
- Does the TLS bypass (CVE-2024-0056) affect all `Encrypt` configuration modes equally (`Mandatory`, `true`, `Strict`) or only specific settings?
- What is the actual NuGet total download count? (The NuGet registration API does not expose this value; alternative stats endpoints may surface it in a future pass.)

## Related Pages

- [[dotnet/Newtonsoft.Json]]
- [[dotnet/System.Text.Json]]
- [[dotnet/Npgsql]]
- [[dotnet/index]]

---
*Last updated: 2026-07-14 | Sources: 2 (GHSA-8g2p-5pqh-5jmc / CVE-2022-41064, GHSA-98g6-xh36-x2p7 / CVE-2024-0056)*
