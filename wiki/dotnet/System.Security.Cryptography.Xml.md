# System.Security.Cryptography.Xml (NuGet)

**Registry:** NuGet
**Repository:** https://github.com/dotnet/runtime (library ships as part of .NET; package is published on NuGet)
**Disclosure Policy / Security:** https://github.com/dotnet/runtime/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-06 | OpenClaw recurring review | package advisory refresh | public-source curation (OSV.dev package query, GitHub Advisory Database / public GitHub security advisories, dotnet/announcements, public CVE / MSRC / NVD references, local Claude-compatible proxy used only as a drafting aid) | Reconciled the page against the full OSV package result and expanded it from 1 to 5 public package-scoped advisories, adding the 2018 XML-processing DoS pair, the 2022 information-disclosure advisory, and the second April 2026 EncryptedXml DoS advisory. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| 2026-05-01 | [@travis-burmaster](https://github.com/travis-burmaster) | package advisory review | public-source curation (GitHub Advisory Database / OSV.dev / public CVE record / maintainer announcement) | 1 published advisory mapped (DoS via resource consumption in EncryptedXml) | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-rr3c-f55v-qhv5 / CVE-2018-0764 | High (CVSS 7.5) | Denial of service when .NET / .NET Core improperly process XML documents. OSV and NVD describe this as distinct from CVE-2018-0765 even though both share the XML-processing DoS theme and NuGet fix boundary. | 4.4.2 | [OSV](https://osv.dev/vulnerability/GHSA-rr3c-f55v-qhv5) · [GitHub Advisory Database](https://github.com/advisories/GHSA-rr3c-f55v-qhv5) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2018-0764) |
| GHSA-35hc-x2cw-2j4v / CVE-2018-0765 | High (CVSS 7.5) | Denial of service when .NET / .NET Core improperly process XML documents. Public records track it as a separate 2018 XML-processing DoS issue with the same NuGet fixed version as CVE-2018-0764. | 4.4.2 | [OSV](https://osv.dev/vulnerability/GHSA-35hc-x2cw-2j4v) · [GitHub Advisory Database](https://github.com/advisories/GHSA-35hc-x2cw-2j4v) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2018-0765) |
| GHSA-vh55-786g-wjwj / CVE-2022-34716 | High (CVSS 7.5) | Information disclosure in .NET Core 3.1 / .NET 6.0 that could lead to unauthorized access of privileged information. OSV also carries BIT aliases for dotnet, dotnet-sdk, and powershell records; this row is package-scoped to `System.Security.Cryptography.Xml`. | 4.7.1 for the package line below 5.0.0; 6.0.1 for the 5.x/6.x package line | [OSV](https://osv.dev/vulnerability/GHSA-vh55-786g-wjwj) · [GitHub Advisory](https://github.com/dotnet/aspnetcore/security/advisories/GHSA-vh55-786g-wjwj) · [dotnet/announcements#232](https://github.com/dotnet/announcements/issues/232) · [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-34716) |
| GHSA-w3x6-4m5h-cxqf / CVE-2026-26171 | High (CVSS 7.5) | Denial of service via uncontrolled resource consumption in `EncryptedXml` (System.Security.Cryptography.Xml). The public advisory lists CWE-400 and CWE-611. | 8.0.3 / 9.0.15 / 10.0.6 | [OSV](https://osv.dev/vulnerability/GHSA-w3x6-4m5h-cxqf) · [GitHub Advisory](https://github.com/dotnet/runtime/security/advisories/GHSA-w3x6-4m5h-cxqf) · [dotnet/announcements#389](https://github.com/dotnet/announcements/issues/389) · [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26171) |
| GHSA-37gx-xxp4-5rgx / CVE-2026-33116 | High (CVSS 7.5) | Denial of service in `EncryptedXml` where an attacker can cause an infinite loop. The public advisory lists CWE-835, CWE-400, and CWE-20. | 8.0.3 / 9.0.15 / 10.0.6 | [OSV](https://osv.dev/vulnerability/GHSA-37gx-xxp4-5rgx) · [GitHub Advisory](https://github.com/dotnet/runtime/security/advisories/GHSA-37gx-xxp4-5rgx) · [dotnet/announcements#392](https://github.com/dotnet/announcements/issues/392) · [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33116) |

## Security Posture Notes

- Exposure for the 2026 advisories depends on whether untrusted XML input can reach the affected `EncryptedXml` code paths in a deployed application.
- CVE-2026-26171 and CVE-2026-33116 affect the same currently maintained package branches in the OSV record (`8.x`, `9.x`, and `10.x`) and share the same fixed versions: **8.0.3**, **9.0.15**, and **10.0.6**.
- The older 2018 XML-processing DoS records both show a NuGet fixed version of **4.4.2**. The 2022 information-disclosure record has separate package fix boundaries (**4.7.1** and **6.0.1**) and many runtime-package aliases; this page records only the `System.Security.Cryptography.Xml` package-scoped impact.
- Microsoft guidance in the public advisories is to update the affected package version and redeploy; the 2026 advisories also recommend updating the runtime and/or SDK while noting that package update is the vulnerability remediation path for affected package consumers.

## Related Pages

- [[dotnet/index]]

---
*Last updated: 2026-05-06 | Sources: OSV.dev package query (5 records), GitHub Advisory Database / public GitHub security advisories, dotnet/announcements, MSRC / NVD public CVE records*
