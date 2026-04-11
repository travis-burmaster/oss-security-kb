# Newtonsoft.Json (dotnet)

**Registry:** NuGet
**Weekly Downloads:** unknown (as of 2026-04-11)
**Repository:** https://github.com/JamesNK/Newtonsoft.Json
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** baseline stub

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| Review pending | — | This page has not yet been populated with package-specific advisory history. Use OSV, NuGet package history, and upstream issue history as starting points. | — | https://osv.dev/list?ecosystem=NuGet&q=Newtonsoft.Json |

*Full CVE history: https://osv.dev/list?ecosystem=NuGet&q=Newtonsoft.Json*

## Security Posture Notes

- `Newtonsoft.Json` remains one of the most installed JSON libraries in the .NET ecosystem, especially in legacy applications, SDKs, and compatibility layers that predate `System.Text.Json` adoption.
- Its security relevance centers on parser behavior, deserialization boundaries, polymorphic type handling, metadata features, and how downstream applications expose JSON-controlled object graphs.
- NuGet search currently reports more than 7.9 billion total downloads, which is a strong ecosystem-importance signal even though a clean weekly-download metric is not readily exposed in the same shape as npm or PyPI.

## Dependencies of Note

- `System.Text.Json` is the most important comparison page to add later so the KB can distinguish old versus modern .NET JSON parser and serializer assumptions.
- Downstream frameworks that enable custom converters or type-name handling should eventually be linked here because exploitability often depends on integration patterns rather than the package alone.

## Open Questions

- Have any public targeted reviews covered dangerous deserialization patterns, `TypeNameHandling`, or custom converter misuse in modern `Newtonsoft.Json` deployments?
- Which historical vulnerabilities should be tracked on the package page itself versus on application-level insecure configuration guidance?
- Should this page eventually split parser bugs, deserialization hazards, and safe-default guidance into separate sections for better site rendering?

## Related Pages

- [[dotnet/index]]

---
*Last updated: 2026-04-11 | Sources: 3 (NuGet package search metadata, upstream repository, OSV package query)*
