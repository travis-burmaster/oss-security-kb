# Azure.Identity (.NET / NuGet)

**Registry:** NuGet
**Weekly Downloads:** ~23.8M/week est. (1.9 billion total NuGet downloads across all versions as of 2026-08-14; ~3.4 million downloads/day reported on nuget.org)
**Repository:** https://github.com/Azure/azure-sdk-for-net (monorepo, `sdk/identity/Azure.Identity/`)
**Security Contact:** https://msrc.microsoft.com/report (Microsoft Security Response Center); security@microsoft.com
**Disclosure Policy:** https://github.com/Azure/azure-sdk-for-net/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-08-14 | OSS Security KB | GHSA database lookup for NuGet Azure.Identity package | automated | 3 public advisory rows mapped (GHSA-5mfx through GHSA-m5vv) | [github/advisory-database](https://github.com/github/advisory-database) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-36414 / GHSA-5mfx-4wcx-rv27 | Critical (CVSS 9.9 AV:N/AC:L/PR:L/UI:N) | Azure Identity SDK remote code execution: an authenticated (low-privilege) attacker can exploit the library to execute arbitrary code remotely. Full scope of the RCE vector was not detailed in the public advisory beyond the CWE classification; the fix was delivered in version 1.10.2 (October 2023). The high CVSS reflects network-accessible attack surface requiring only low privileges. | 1.10.2 | [GHSA-5mfx-4wcx-rv27](https://github.com/advisories/GHSA-5mfx-4wcx-rv27) |
| CVE-2024-29992 / GHSA-wvxc-855f-jvrv | Moderate (CVSS 7.1 AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N; CWE-522) | Azure Identity Library information disclosure: a local low-privilege attacker can access credentials or token data handled by the library (CWE-522 — insufficiently protected credentials). The vulnerability requires local access and yields high confidentiality impact. Mitigated by upgrading to 1.11.0 (released April 9, 2024). | 1.11.0 | [GHSA-wvxc-855f-jvrv](https://github.com/advisories/GHSA-wvxc-855f-jvrv) |
| CVE-2024-35255 / GHSA-m5vv-6r4h-3vj9 | Medium (CVSS 6.2 AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N) | Azure Identity Libraries elevation of privilege / information disclosure: a local low-privilege attacker can escalate privileges or access sensitive token/credential information handled by the Azure Identity library. This advisory affects `Azure.Identity` (NuGet) as well as the cross-ecosystem `azure-identity` (PyPI), `@azure/identity` (npm), `com.azure:azure-identity` (Maven), and `azure-sdk-for-go`. The NuGet package is fixed in 1.11.4 (released June 2024). | 1.11.4 | [GHSA-m5vv-6r4h-3vj9](https://github.com/advisories/GHSA-m5vv-6r4h-3vj9) |

*OSV live record: https://osv.dev/list?ecosystem=NuGet&q=Azure.Identity*

## Security Posture Notes

`Azure.Identity` is the official Microsoft NuGet package providing Microsoft Entra ID (formerly Azure Active Directory) token-based authentication for .NET applications. It supplies `TokenCredential` implementations — `DefaultAzureCredential`, `ManagedIdentityCredential`, `ClientSecretCredential`, `WorkloadIdentityCredential`, and others — used by the entire Azure SDK for .NET ecosystem. With 1.9 billion total downloads and 1,900+ dependent packages, it is one of the highest-impact authentication libraries in the .NET ecosystem.

**Current stable version:** 1.21.0 (released April 11, 2026). All three mapped advisories are fixed in versions released before 1.21.0. Any application running `Azure.Identity` < 1.11.4 is exposed to at least one unfixed advisory (the cross-ecosystem EoP / info-disclosure in CVE-2024-35255).

**CVE-2023-36414 (Critical CVSS 9.9, RCE):** This is the most severe advisory. A CVSS 9.9 critical RCE with only PR:L (low privileges required) and network access (AV:N) represents a significant attack surface in credential-handling flows. Projects that deployed `Azure.Identity` < 1.10.2 in any internet-exposed context should treat this as a high-priority upgrade, especially in scenarios where the library is invoked in response to unauthenticated or minimally authenticated network requests.

**CVE-2024-29992 and CVE-2024-35255 (local credential disclosure / EoP):** Both advisories share a local attack vector (AV:L, PR:L) and high confidentiality impact (C:H), making them relevant in multi-tenant environments, shared cloud compute infrastructure, container deployments where process isolation is imperfect, or any scenario where a lower-privilege process can observe memory or credential caches of a higher-privilege process using Azure.Identity.

**Cross-ecosystem scope (CVE-2024-35255):** GHSA-m5vv-6r4h-3vj9 affects Azure Identity libraries across multiple language ecosystems (PyPI, npm, Maven, Go, and NuGet). Organizations using Azure Identity across multiple language stacks must coordinate upgrades across all affected SDKs. The NuGet package requires upgrade to ≥ 1.11.4; other ecosystems have separate fix versions.

**SECURITY.md:** Microsoft maintains a SECURITY.md in the azure-sdk-for-net monorepo pointing to the MSRC reporting portal. Third-party security researchers should report via https://msrc.microsoft.com/report rather than opening public GitHub issues for potential vulnerabilities.

## Dependencies of Note

`Azure.Identity` transitively depends on `Microsoft.Identity.Client` (MSAL.NET). CVE-2024-35255 also lists `Microsoft.Identity.Client` versions 4.49.1–4.60.3 and 4.61.0–4.61.2 as affected (fixed ≥ 4.60.4 / ≥ 4.61.3). Projects that take a direct dependency on `Microsoft.Identity.Client` independently of `Azure.Identity` must also upgrade MSAL to the patched version.

- [[dotnet/Microsoft.IdentityModel.JsonWebTokens]] — Microsoft JWT library in the same identity stack; JWE compression bomb advisory (CVE-2024-21319)
- [[dotnet/Microsoft.AspNetCore.Authentication.Negotiate]] — ASP.NET Core Windows/Kerberos/NTLM handler; 2026 LDAP EoP cluster

## Open Questions

- Verify whether `DefaultAzureCredential` (the most commonly used credential type) is the primary affected code path for CVE-2023-36414, or whether the RCE is triggered via a specific credential implementation (e.g. `VisualStudioCredential`, extension-based credential).
- Confirm which specific token-caching / credential-persistence mechanism triggers the CWE-522 information disclosure in CVE-2024-29992 and CVE-2024-35255 (e.g. token cache stored in process memory vs. disk vs. keychain).
- Assess whether newer v1.12.x–v1.21.x releases contain any additional GHSA advisories not yet captured in the public advisory database; cross-reference with the Azure SDK for .NET release notes and CHANGELOG.

## Related Pages

- [[dotnet/Microsoft.IdentityModel.JsonWebTokens]]
- [[dotnet/Microsoft.AspNetCore.Authentication.Negotiate]]
- [[dotnet/index]]

---
*Last updated: 2026-08-14 | Sources: 4 (github/advisory-database: 3 GHSA records; nuget.org package page; Azure/azure-sdk-for-net SECURITY.md)*
