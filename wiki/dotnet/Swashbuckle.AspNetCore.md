# Swashbuckle.AspNetCore (.NET / NuGet)

**Registry:** NuGet — https://www.nuget.org/packages/Swashbuckle.AspNetCore
**Weekly Downloads:** ~1.2–1.3 billion total NuGet downloads (as of 2026-08-27)
**Repository:** https://github.com/domaindrivendev/Swashbuckle.AspNetCore
**Security Contact:** https://github.com/domaindrivendev/Swashbuckle.AspNetCore/security (GitHub Security Advisories)
**Disclosure Policy:** GitHub private vulnerability reporting
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2021-12-09 | swagger-api / GitHub | api-surface (swagger-ui ?url parameter) | manual | 1 filed | [GHSA-qrmm-w75w-3wpx](https://github.com/advisories/GHSA-qrmm-w75w-3wpx) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-qrmm-w75w-3wpx (no CVE assigned) | **Moderate** (CWE-918 SSRF) | SwaggerUI SSRF via `?url` query parameter: the hosted SwaggerUI endpoint accepts an arbitrary remote OpenAPI definition URL, enabling phishing attacks where a trusted domain's SwaggerUI loads a malicious API definition and tricks users into submitting credentials to the attacker via the "Try it out" feature. Not exploitable for unauthenticated server-side request forgery in typical deployment. Versions < 3.38.0 (swagger-ui) can be chained with CVE-2020-26870 for reflected XSS. Affects `Swashbuckle.AspNetCore.SwaggerUI` package. | Swashbuckle.AspNetCore 6.3.0 / Swashbuckle.AspNetCore.SwaggerUI 6.3.0 | [GHSA-qrmm-w75w-3wpx](https://github.com/advisories/GHSA-qrmm-w75w-3wpx) |

## Security Posture Notes

Swashbuckle.AspNetCore is the de facto standard library for generating and serving Swagger/OpenAPI documentation in ASP.NET Core applications, with ~1.2–1.3 billion total NuGet downloads. It bundles a specific version of the upstream `swagger-ui` JavaScript frontend, which means Swashbuckle releases are gated on swagger-ui releases for client-side security fixes.

**Key security configuration considerations:**
- The `?url` redirect issue (GHSA-qrmm-w75w-3wpx) is mitigated by disabling the URL override via `c.SupportedSubmitMethods()` configuration or by restricting the SwaggerUI endpoint to development environments only (the recommended practice for production deployments).
- SwaggerUI endpoints should **not** be exposed in production without authentication — a publicly reachable SwaggerUI with "Try it out" enabled exposes the full API surface to unauthenticated users.
- The package version of the bundled swagger-ui changes with each Swashbuckle release; verify the bundled swagger-ui version matches patched upstream when evaluating exposure.

**Latest stable:** 10.2.3 (released 2026-06-22). The project is actively maintained by Domaindrivendev (Richard Morris) with community contributions.

**Ecosystem note:** This advisory also affects the upstream `swagger-ui` (npm), `swagger-ui-dist` (npm), and `swagger-ui-react` (npm) packages at the same root cause.

## Dependencies of Note

- Bundles a specific version of **swagger-ui** (npm) at build time — track swagger-ui CVEs (e.g., CVE-2020-26870 DOMPurify XSS) when evaluating the bundled version.
- `Swashbuckle.AspNetCore.SwaggerGen` generates OpenAPI JSON from ASP.NET Core controller reflection; untrusted controller/model naming is a potential input boundary worth reviewing separately.

## Open Questions

- What version of swagger-ui is bundled in the current Swashbuckle.AspNetCore 10.2.3 release? Verify against latest swagger-ui CVE history.
- Has the upstream `?url` parameter been removed or whitelisted in swagger-ui 5.x (current stable), removing the SSRF vector by default?
- Are there any additional GHSA advisories filed under the `domaindrivendev/Swashbuckle.AspNetCore` GitHub repository not yet reviewed in github/advisory-database?

## Related Pages

- [[dotnet/index]]
- [[dotnet/Newtonsoft.Json]] — commonly bundled alongside for JSON serialization
- [[dotnet/System.Text.Json]] — alternative serializer in ASP.NET Core 6+

---
*Last updated: 2026-08-27 | Sources: GHSA-qrmm-w75w-3wpx (github/advisory-database); NuGet registry metadata*
