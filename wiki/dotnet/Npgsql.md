# Npgsql (.NET / NuGet)

**Registry:** NuGet
**Weekly Downloads:** unknown (as of 2026-06-28); 871.2M total all-version downloads
**Repository:** https://github.com/npgsql/npgsql
**Security Contact:** GitHub Security Advisories — https://github.com/npgsql/npgsql/security
**Disclosure Policy:** https://github.com/npgsql/npgsql/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-x9vc-6hfv-hg8c / CVE-2024-32655 | High (CVSS 9.1) | Integer overflow in `WriteBind()`: `int` variables store the message length and sum of parameter lengths; overflow causes Npgsql to write an incorrectly small message-length field in the PostgreSQL wire-protocol `Bind` message, allowing the server to misread message boundaries and enabling injection of arbitrary wire-protocol messages and SQL statements | 4.0.14, 4.1.13, 5.0.18, 6.0.11, 7.0.7, 8.0.3 | [GHSA-x9vc-6hfv-hg8c](https://github.com/advisories/GHSA-x9vc-6hfv-hg8c) |

## Security Posture Notes

Npgsql is the open-source .NET data provider for PostgreSQL maintained by the Npgsql Development Team (GitHub: `npgsql/npgsql`). It is the de facto standard PostgreSQL client library for .NET and the default backend provider for Npgsql.EntityFrameworkCore.PostgreSQL (used by ASP.NET Core applications targeting PostgreSQL). With 871M+ total NuGet downloads, it has very high ecosystem exposure.

**CVE-2024-32655 context:** The vulnerability originates in the `WriteBind()` method that serialises query parameters for the PostgreSQL wire protocol. When the total parameter length overflows a 32-bit signed integer, the computed length field wraps to a negative or truncated value, causing the server to misinterpret subsequent bytes as a new protocol message boundary. An attacker who controls query parameters (or their cumulative size) can exploit this to inject arbitrary PostgreSQL protocol messages — effectively wire-protocol-level SQL injection that bypasses parameterised query protections. The CVSS 9.1 score reflects network-accessible exploitation under typical connection-pool conditions. All maintained release branches (4.0 through 8.0) were affected; fixes were released simultaneously in May 2024.

Current latest stable: 10.0.3 (released 2026-05-27). No known open advisories for 8.0.3+ / 9.x / 10.x.

## Dependencies of Note

None flagged at the Npgsql package level — transitive security exposure is primarily through the connected PostgreSQL server version and its CVE history.

## Open Questions

- Were 9.x and 10.x also affected by the CVE-2024-32655 integer-overflow path, or was the length type widened to `long` in those release branches?
- Has Npgsql undergone any third-party protocol-fuzzing or security audit examining wire-protocol message construction?

## Related Pages

- [[dotnet/index]]

---
*Last updated: 2026-06-28 | Sources: 1*
