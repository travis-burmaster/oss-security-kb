# System.Security.Cryptography.Xml (NuGet)

**Registry:** NuGet
**Repository:** https://github.com/dotnet/runtime (library ships as part of .NET; package is published on NuGet)
**Disclosure Policy / Security:** https://github.com/dotnet/runtime/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-01 | [@travis-burmaster](https://github.com/travis-burmaster) | package advisory review | public-source curation (GitHub Advisory Database / OSV.dev / public CVE record / maintainer announcement) | 1 published advisory mapped (DoS via resource consumption in EncryptedXml) | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-w3x6-4m5h-cxqf / CVE-2026-26171 | High (CVSS 7.5) | Denial of service via uncontrolled resource consumption in `EncryptedXml` (System.Security.Cryptography.Xml). Advisory lists CWE-400 (Uncontrolled Resource Consumption) and CWE-611 (Improper Restriction of XML External Entity Reference). | 8.0.3 / 9.0.15 / 10.0.6 | [OSV](https://osv.dev/vulnerability/GHSA-w3x6-4m5h-cxqf) · [dotnet/announcements#389](https://github.com/dotnet/announcements/issues/389) · [CVE record](https://www.cve.org/CVERecord?id=CVE-2026-26171) |

## Security Posture Notes

- Exposure depends on whether untrusted XML input can reach the affected `EncryptedXml` code paths in a deployed application.
- Patching guidance per the public advisory: update to a fixed package version and redeploy. The advisory additionally recommends updating the runtime and/or SDK, but states it is not necessary to patch the vulnerability.

## Related Pages

- [[dotnet/index]]

---
*Last updated: 2026-05-01 | Sources: OSV.dev + dotnet/announcements + CVE.org*
