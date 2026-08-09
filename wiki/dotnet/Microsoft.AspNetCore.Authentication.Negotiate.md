# Microsoft.AspNetCore.Authentication.Negotiate (.NET / NuGet)

**Registry:** NuGet
**Weekly Downloads:** unknown (total: ~56.3 million as of 2026-08-09)
**Repository:** https://github.com/dotnet/aspnetcore
**Security Contact:** https://github.com/dotnet/aspnetcore/security (GitHub private vulnerability reporting)
**Disclosure Policy:** https://msrc.microsoft.com/report (Microsoft Security Response Center)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-08-09 | oss-security-kb | advisory-db sweep | automated (GHSA search) | 2 confirmed advisories | [GHSA-8prm-248r-h957](https://github.com/advisories/GHSA-8prm-248r-h957), [GHSA-2p3q-h3hg-jcqq](https://github.com/advisories/GHSA-2p3q-h3hg-jcqq) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-47300 / GHSA-8prm-248r-h957 | **High** CVSS 8.8 AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H | Elevation of privilege in the ASP.NET Core Negotiate authentication handler via improper validation. Affects applications using Negotiate authentication with LDAP for role retrieval. An authenticated low-privilege attacker can escalate privileges (CWE-303: Incorrect Implementation of Authentication Algorithm). Affects .NET 8.0.0–8.0.28, .NET 9.0.0–9.0.17, .NET 10.0.0–10.0.9. | .NET 8 → 8.0.29 / .NET 9 → 9.0.18 / .NET 10 → 10.0.10 | [GHSA-8prm-248r-h957](https://github.com/advisories/GHSA-8prm-248r-h957) / [CVE-2026-47300](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-47300) |
| CVE-2026-47303 / GHSA-2p3q-h3hg-jcqq | **High** CVSS 8.8 AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H | Elevation of privilege in the ASP.NET Core Negotiate authentication handler via improper parsing. Enables authentication bypass by assumed-immutable data manipulation and LDAP injection. An authenticated low-privilege attacker can escalate privileges or bypass authorization checks. Affects .NET 8.0.0–8.0.28, .NET 9.0.0–9.0.17, .NET 10.0.0–10.0.9. | .NET 8 → 8.0.29 / .NET 9 → 9.0.18 / .NET 10 → 10.0.10 | [GHSA-2p3q-h3hg-jcqq](https://github.com/advisories/GHSA-2p3q-h3hg-jcqq) / [CVE-2026-47303](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-47303) |

## Security Posture Notes

`Microsoft.AspNetCore.Authentication.Negotiate` provides Windows Authentication support (Negotiate/Kerberos/NTLM) for ASP.NET Core applications. It is a first-party Microsoft package shipped as part of the ASP.NET Core runtime bundle. The current stable release is 10.0.10 (~56.3M total NuGet downloads as of 2026-08-09).

Both confirmed advisories (CVE-2026-47300 and CVE-2026-47303) were published on 2026-07-21 as part of a July 2026 .NET security patch release. Both are High severity (CVSS 8.8) elevation-of-privilege vulnerabilities that share the same affected version ranges and fixed versions. They are distinct issues:

- **CVE-2026-47300** targets the validation path of the authentication handler, likely in how the Negotiate challenge/response is checked before LDAP group membership lookups are made.
- **CVE-2026-47303** targets the parsing path and additionally introduces LDAP injection risk, allowing an attacker to manipulate LDAP queries issued during role retrieval.

Both require only low privilege (PR:L) — an already-authenticated domain user — and no user interaction, making them practical attack vectors in corporate / intranet deployments where Negotiate auth with LDAP is a common pattern.

**Scope**: These vulnerabilities only affect applications that:
1. Use `Microsoft.AspNetCore.Authentication.Negotiate` explicitly (not the IIS-managed Windows Authentication).
2. Configure Negotiate authentication *and* LDAP-based role retrieval. Applications using Negotiate without LDAP (token-only auth) may not be affected.

Disclosure follows standard Microsoft Patch Tuesday / coordinated disclosure via MSRC; both advisories were simultaneously disclosed across .NET 8, 9, and 10.

## Dependencies of Note

- **System.DirectoryServices.Protocols** — used for LDAP queries during role retrieval; LDAP injection in CVE-2026-47303 flows through this dependency.

## Open Questions

- Confirm whether the LDAP injection in CVE-2026-47303 is exploitable on non-LDAP (pure Kerberos token, no group lookup) configurations.
- Review whether on-premises Kerberos-only deployments (no LDAP role retrieval) are affected by either CVE.
- Check for backport availability on .NET 6 (EOL May 2024) — no patch expected, migration required.

## Related Pages

- [[dotnet/Microsoft.IdentityModel.JsonWebTokens]]
- [[dotnet/Duende.IdentityServer]]
- [[dotnet/index]]

---
*Last updated: 2026-08-09 | Sources: 2 (GitHub Advisory Database / MSRC)*
