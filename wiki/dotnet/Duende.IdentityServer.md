# Duende.IdentityServer / IdentityServer4 (.NET / NuGet)

**Registry:** NuGet
**Weekly Downloads:** Duende.IdentityServer ~26.3M total (active, current 8.0.4); IdentityServer4 ~67.8M total (EOL, 4.1.2) (as of 2026-08-03)
**Repository:** https://github.com/DuendeSoftware/IdentityServer (Duende, active); https://github.com/IdentityServer/IdentityServer4 (archived, EOL)
**Security Contact:** security@duendesoftware.com
**Disclosure Policy:** https://github.com/DuendeSoftware/IdentityServer/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-08-03 | oss-security-kb | advisory-mapping | automated | 3 github-reviewed GHSA advisories mapped | [github/advisory-database](https://github.com/github/advisory-database) |

*No independent audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-39694 / GHSA-ff4q-64jc-gx98 | Moderate | Open redirect — IdentityServer incorrectly treats attacker-crafted URLs as local/trusted during redirect validation, enabling phishing via crafted login flows. CWE-601; CVSS v3.1 AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:N/A:N. Affects Duende.IdentityServer 6.0–7.0 and IdentityServer4 ≤ 4.1.2 (EOL, no patch) | Duende.IdentityServer 7.0.6 / 6.3.10 / 6.2.5 / 6.1.8 / 6.0.5; IdentityServer4: **no fix — EOL** | [GHSA-ff4q-64jc-gx98](https://github.com/advisories/GHSA-ff4q-64jc-gx98) |
| (no CVE) / GHSA-55p7-v223-x366 | Moderate | Open redirect — companion record to CVE-2024-39694 specifically tracking IdentityServer4's end-of-life status. Root cause identical (CWE-601; same CVSS vector); filed to make clear that IdentityServer4 will receive no patch. Affects all IdentityServer4 versions ≤ 4.1.2 | No fix — IdentityServer4 end-of-life since December 2022; migrate to Duende.IdentityServer | [GHSA-55p7-v223-x366](https://github.com/advisories/GHSA-55p7-v223-x366) |
| CVE-2024-49755 / GHSA-v9xq-2mvm-x8xc | Low | Insufficient validation of the `cnf` claim in DPoP access tokens in the Local API authentication handler — allows a leaked DPoP access token to be accepted without possession of the corresponding private key, defeating the proof-of-possession binding. CWE-287; CVSS v3.1 AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N. Affects Duende.IdentityServer 7.0.0–7.0.7 only (versions ≤ 6.3 do not support DPoP in Local APIs and are unaffected) | Duende.IdentityServer 7.0.8 | [GHSA-v9xq-2mvm-x8xc](https://github.com/advisories/GHSA-v9xq-2mvm-x8xc) |

## Security Posture Notes

**IdentityServer4** (last release 4.1.2, March 2021) reached end of support in December 2022 when its maintainers transitioned development to the commercially licensed **Duende IdentityServer**. The IdentityServer4 repository is archived and receives no security fixes. All production installations of IdentityServer4 remain permanently exposed to CVE-2024-39694 and any future vulnerabilities discovered in the codebase. Organizations running IdentityServer4 should treat migration to Duende.IdentityServer (or an alternative OIDC framework) as a security-required action, not an optional upgrade.

**Duende.IdentityServer** (current stable 8.0.4, July 2026) is commercially licensed: free for development, testing, and low-revenue production use; tiered paid license for commercial production deployments. It maintains an active security disclosure program and has patched all three public advisories promptly across all supported major versions. The open redirect (CVE-2024-39694) was fixed simultaneously in five version branches; the DPoP claim validation flaw (CVE-2024-49755) was fixed in 7.0.8.

Both packages implement the full OAuth 2.0 Authorization Server and OpenID Connect Provider specification for ASP.NET Core. Their security perimeter extends broadly — token issuance, client credential validation, consent flows, session management, PKCE, and DPoP proof-of-possession all represent trust boundaries that warrant careful configuration review independent of any named CVE.

**Download context:** IdentityServer4's 67.8M total NuGet downloads reflect its dominance as the de facto .NET OIDC server during 2016–2022. Duende.IdentityServer's 26.3M total reflect rapid adoption post-fork. Combined, they underpin a large share of .NET OAuth/OIDC infrastructure in production today.

## Dependencies of Note

- `Microsoft.AspNetCore.*` — ASP.NET Core host; web security boundary
- `Microsoft.IdentityModel.Tokens` / `Microsoft.IdentityModel.JsonWebTokens` — JWT handling; see [[dotnet/Microsoft.IdentityModel.JsonWebTokens]] for the CVE-2024-21319 JWE compression bomb DoS

## Open Questions

- Search for pre-2024 IdentityServer4 advisories not captured in the github-reviewed GHSA set (3 found are the only github-reviewed records; unreviewed NVD imports may exist for older CVEs)
- Evaluate DPoP usage prevalence in Duende deployments to calibrate GHSA-v9xq-2mvm-x8xc risk surface
- Track Duende.IdentityServer 8.x advisory coverage on next pass

## Related Pages

- [[dotnet/Microsoft.IdentityModel.JsonWebTokens]]
- [[dotnet/index]]

---
*Last updated: 2026-08-03 | Sources: github/advisory-database (GHSA-ff4q-64jc-gx98, GHSA-55p7-v223-x366, GHSA-v9xq-2mvm-x8xc); api.nuget.org download stats*
