# Microsoft.IdentityModel.JsonWebTokens (.NET / NuGet)

**Registry:** NuGet
**Weekly Downloads:** unknown (as of 2026-06-15)
**Repository:** https://github.com/AzureAD/azure-activedirectory-identitymodel-extensions-for-dotnet
**Security Contact:** secure@microsoft.com
**Disclosure Policy:** https://aka.ms/opensource/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-21319 / GHSA-59j7-ghrg-fj52 | Medium (CVSS 6.8, scope change S:C) | **JWE compression bomb DoS**: An attacker who can craft a malicious JSON Web Encryption (JWE) token with a high compression ratio can cause the server to allocate excessive memory during decompression, triggering an out-of-memory condition. Unauthenticated path in ASP.NET Core project templates; attacker must have the public encryption key registered with the IdP (e.g., Entra ID) to generate a valid encrypted token. Also affects `System.IdentityModel.Tokens.Jwt`. Duplicate advisory GHSA-8g9c-28fc-mcx2 has been withdrawn in favor of this record. | >= 7.1.2 (7.x line) / >= 6.34.0 (6.x line) / >= 5.7.0 (5.x line) | [GHSA-59j7-ghrg-fj52](https://github.com/advisories/GHSA-59j7-ghrg-fj52) |

*OSV link: https://osv.dev/list?ecosystem=NuGet&q=Microsoft.IdentityModel.JsonWebTokens*

## Security Posture Notes

`Microsoft.IdentityModel.JsonWebTokens` is the current-generation Microsoft JWT library for .NET, part of the `Microsoft.IdentityModel.*` package family used across ASP.NET Core authentication middleware, Azure AD / Entra ID integrations, and `Microsoft.AspNetCore.Authentication.JwtBearer`. Its predecessor, `System.IdentityModel.Tokens.Jwt`, carries the same CVE-2024-21319 advisory.

CVE-2024-21319 is a **compression bomb** (zip bomb variant) attack surface in the JWE (JSON Web Encryption) decompression path. The attack requires that the adversary hold the public encryption key registered with the identity provider — limiting exploitability to adversaries with legitimate access to the IdP registration, which is why the CVSS score is Medium despite the scope change (`S:C`). Microsoft's announcement at https://github.com/dotnet/announcements/issues/290 notes that only projects using JWT-based authentication via the listed ASP.NET Core project templates are affected.

The repository has an active security policy at https://aka.ms/opensource/security and reports through MSRC; public announcements are filed in the dotnet/announcements repository.

At the time of this pass, only one package-scoped GHSA was confirmed for `Microsoft.IdentityModel.JsonWebTokens` in the reviewed sources. The osv.dev API was not accessible during this pass.

## Dependencies of Note

- `System.IdentityModel.Tokens.Jwt` carries the same CVE-2024-21319 record and should be updated in tandem.
- `Microsoft.AspNetCore.Authentication.JwtBearer` and `Microsoft.AspNetCore.Authentication.OpenIdConnect` are the consuming packages most commonly pulled into ASP.NET Core projects; both should be updated to their patched equivalents when remediating CVE-2024-21319.

## Open Questions

- Query osv.dev when API access is available to confirm no additional NuGet package-scoped records exist for this package beyond CVE-2024-21319.
- Check whether newer `Microsoft.IdentityModel.*` versions (8.x and beyond) carry new advisory records.
- Verify NuGet weekly download count to quantify blast radius.

## Related Pages

- [[dotnet/Newtonsoft.Json]]
- [[dotnet/System.Text.Json]]
- [[dotnet/index]]

---
*Last updated: 2026-06-15 | Sources: 1 GHSA record (github/advisory-database via GitHub code search)*
