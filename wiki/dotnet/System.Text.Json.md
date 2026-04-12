# System.Text.Json (.NET / NuGet)

**Registry:** NuGet
**Weekly Downloads:** unknown (as of 2026-04-12)
**Repository:** https://github.com/dotnet/runtime
**Security Contact:** secure@microsoft.com
**Disclosure Policy:** https://github.com/dotnet/runtime/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-12 | OpenClaw recurring review | package advisory history | manual | 2 publicly disclosed package vulnerabilities curated from OSV, GHSA, CVE, Microsoft advisory text, and upstream announcement threads | https://osv.dev/list?ecosystem=NuGet&q=System.Text.Json |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-30105 / GHSA-hh2w-p6rv-4g7w | High | `JsonSerializer.DeserializeAsyncEnumerable` against untrusted input could trigger denial-of-service conditions via uncontrolled resource consumption. | 8.0.4 | https://github.com/advisories/GHSA-hh2w-p6rv-4g7w |
| CVE-2024-43485 / GHSA-8g4q-xg66-9fp4 | High | Deserializing attacker-controlled input into models that use `[JsonExtensionData]` could trigger an algorithmic-complexity denial of service. | 8.0.5, 6.0.10 | https://github.com/advisories/GHSA-8g4q-xg66-9fp4 |

*Full CVE history: https://osv.dev/list?ecosystem=NuGet&q=System.Text.Json*

## Security Posture Notes

- The clean public package-level advisory record gathered in this pass is short but meaningful: both currently published `System.Text.Json` package advisories are denial-of-service bugs in deserialization paths rather than code-execution findings.
- The 2024 advisory set highlights two specific high-risk features to treat carefully at trust boundaries: streaming deserialization via `DeserializeAsyncEnumerable` and extension-data capture via `[JsonExtensionData]`.
- Microsoft's advisory text makes remediation unusually concrete because the fixes are tied to runtime / SDK servicing releases as well as NuGet package versions; self-contained deployments need rebuild and redeploy, not just host patching.
- Public evidence in this pass did **not** justify broad claims that `System.Text.Json` has the same configuration-driven risk profile as older Json.NET `TypeNameHandling` discussions. Keeping the page focused on published package advisories avoids mixing package defects with application misuse.
- OSV package metadata is useful here, but the GHSA advisory tables are the more precise source for affected-version wording, especially because the July 2024 advisory text centers on .NET 8 servicing while package metadata can look broader at a glance.

## Dependencies of Note

- `Microsoft.NETCore.App` and related SDK/runtime servicing releases matter because many downstream users consume these fixes through platform updates rather than direct package pinning.
- `Newtonsoft.Json` is the most useful comparison page because teams often evaluate serializer migration or mixed deployments across both stacks.

## Open Questions

- Are there public maintainer posts, design notes, or release-note callouts that would support a small hardening section on safe use of `DeserializeAsyncEnumerable` with untrusted streams?
- Should this page eventually distinguish package-consumption guidance for direct NuGet users versus applications inheriting fixes through .NET runtime servicing?
- Are there other public `System.Text.Json` security fixes that landed only in bundled runtime release notes and were not published as package-scoped GHSA / OSV records?

## Related Pages

- [[dotnet/Newtonsoft.Json]]
- [[dotnet/index]]

---
*Last updated: 2026-04-12 | Sources: 6 (OSV package query, two GHSA advisory pages, two CVE records, Microsoft announcement thread for CVE-2024-43485)*
