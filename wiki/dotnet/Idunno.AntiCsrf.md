# Idunno.AntiCsrf (.NET)

**Registry:** none (not published on NuGet; distributed as `Idunno.AntiCsrf.dll` from the retired CodePlex project, archived at https://codeplexarchive.org/project/AntiCSRF)
**Weekly Downloads:** unknown (no NuGet package; `api.nuget.org` returned no registration for `idunno.anticsrf` on 2026-11-25)
**Repository:** unknown (CodePlex archive only: https://codeplexarchive.org/project/AntiCSRF)
**Security Contact:** none listed (defunct project with no active maintainer, per MNDT-2026-0048)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-11-04 | Google Cloud FLARE OTF and Mandiant Incident Response | `Idunno.AntiCsrf.dll` 0.9.1.0 (`AntiCsrfModule`, `CsrfSettings`) found during an incident response | Root-cause analysis of decompiled module during incident response | 1 (CVE-2026-131914) | [MNDT-2026-0048](https://github.com/mandiant/Vulnerability-Disclosures/blob/master/2026/MNDT-2026-0048.md) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-131914 / GHSA-pj2m-2r8v-h9cp | Critical (CVSS 4.0 9.3 per Mandiant; GHSA label Critical, CVSS 3.1 vector AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H); **CISA KEV** (added 2026-11-24, due 2026-11-27, forensic triage required) | Unauthenticated RCE through insecure deserialization (CWE-502). `AntiCsrfModule.PreRequestHandlerExecute` checks only that the CSRF cookie and form field are non-empty, then passes the form field to a parameterless `ObjectStateFormatter.Deserialize()` with no MAC, signature or binder. One `POST` to any ASP.NET WebForms page that does not opt out of the check (`ISuppressCsrfCheck` / `[SuppressCsrfCheck]`) runs an `ObjectStateFormatter` gadget chain in `w3wp.exe`. The page does not need a `<form runat="server">`. Mandiant reports active exploitation. Affects all versions through 0.9.1 Beta. | No fix. The project is defunct (last release 0.9.1 Beta, December 2008); Mandiant advises removing the module and DLL | [MNDT-2026-0048](https://github.com/mandiant/Vulnerability-Disclosures/blob/master/2026/MNDT-2026-0048.md), [GHSA-pj2m-2r8v-h9cp](https://github.com/advisories/GHSA-pj2m-2r8v-h9cp), [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-131914) |

## Security Posture Notes

Idunno.AntiCsrf is a 2008-era `IHttpModule` that adds double-submit-cookie CSRF protection to ASP.NET WebForms applications. It was published on CodePlex, never on NuGet, so dependency scanners that read `packages.config` or `*.csproj` package references will not find it. It shows up only as a `bin/Idunno.AntiCsrf.dll` file and as `Idunno.AntiCsrf.AntiCsrfModule` entries under `<httpModules>` / `<modules>` in `Web.config`.

The defaults are cookie `__CSRFCOOKIE` and form field `__CSRFTOKEN`. Mandiant notes a setter bug: if `<csrfSettings>` is missing from `Web.config`, the form field name becomes `RaiseException`. Defenders searching logs should look for both names.

Mandiant's remediation guidance (MNDT-2026-0048):
1. Remove the module entries, the `csrfSettings` config section, any `ISuppressCsrfCheck` / `[SuppressCsrfCheck]` references, and `Idunno.AntiCsrf.dll` from `bin/`.
2. Replace it with a supported mechanism: `System.Web.Helpers.AntiForgery`, `Page.ViewStateUserKey` with MAC-verified ViewState, or ASP.NET Core `IAntiforgery`.
3. Review IIS logs for unusual `POST` requests to `.aspx` pages that return HTTP 302 or 500 with large request sizes. Where exploitation is found, rotate `<machineKey>` keys and other secrets in `Web.config` and `applicationHost.config`, and check webroots for unauthorized files.

MNDT-2026-0048 publishes MD5, SHA-1 and SHA-256 hashes for the official 0.9.1.0 build and two rebuilds from source. Locally recompiled copies will hash differently, so search by file and type name as well.

The same bug class hit Sitecore's `Sitecore.Security.AntiCSRF` module (CVE-2019-9874, unauthenticated deserialization through `__CSRFTOKEN`; CISA KEV 2025-03-26). That is a different product and is not mapped here.

## Dependencies of Note

- Depends only on the .NET Framework `System.Web` pipeline. The vulnerable sink is `System.Web.UI.ObjectStateFormatter` used without a `machineKey`-backed MAC.

## Open Questions

- The CVE record and KEV entry name only 0.9.1 Beta. Are there forks or vendor-bundled copies of the module in commercial ASP.NET products that need their own advisories?
- GHSA-pj2m-2r8v-h9cp is unreviewed and has no package mapping. Recheck whether GitHub reviews it or maps it to a NuGet identifier.

## Related Pages

- [[dotnet/Newtonsoft.Json]]
- [[dotnet/YamlDotNet]]
- [[dotnet/index]]

---
*Last updated: 2026-11-25 | Sources: 3 (MNDT-2026-0048, GHSA-pj2m-2r8v-h9cp, cisagov/kev-data 2026.11.24)*
