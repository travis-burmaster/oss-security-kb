# Newtonsoft.Json (dotnet)

**Registry:** NuGet
**Weekly Downloads:** unknown (as of 2026-04-11)
**Repository:** https://github.com/JamesNK/Newtonsoft.Json
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-11 | OpenClaw recurring review | package advisory history | manual | 1 publicly disclosed package vulnerability curated from OSV, GHSA, CVE, upstream issue discussion, and 13.0.1 release notes | https://osv.dev/list?ecosystem=NuGet&q=Newtonsoft.Json |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-21907 / GHSA-5crp-9r3c-p9vr | High | Highly nested JSON could trigger excessive CPU / memory use during deserialization and stack overflow during serialization, leading to denial of service unless callers constrained depth. | 13.0.1 | https://github.com/advisories/GHSA-5crp-9r3c-p9vr |

*Full CVE history: https://osv.dev/list?ecosystem=NuGet&q=Newtonsoft.Json*

## Security Posture Notes

- `Newtonsoft.Json` remains one of the most deployed JSON libraries in the .NET ecosystem, with NuGet reporting more than 7.9 billion total downloads, so even a narrow parser-behavior flaw has unusually large downstream reach.
- The publicly curated package-level advisory history is currently sparse rather than noisy: the clearest evidence-backed package vulnerability surfaced in this review is the nested-input denial-of-service issue fixed in 13.0.1.
- Upstream 13.0.1 release notes align with the advisory and show two relevant hardening changes: default `MaxDepth` for `JsonReader` and `JsonSerializer` moved to 64, and `JsonSelectSettings` gained a configurable regex timeout.
- Exploitability is highly input- and configuration-dependent. The advisory itself notes that applications could mitigate earlier versions by setting `JsonSerializerSettings.MaxDepth`, which suggests many real-world risks sit at the boundary between package defaults and application hardening.

## Dependencies of Note

- `System.Text.Json` remains the most important future comparison page so the KB can distinguish legacy versus modern .NET JSON parser and serializer assumptions.
- Application code that enables polymorphic deserialization, custom converters, or permissive type-handling settings remains security-relevant even when the package itself has only a small number of tracked advisories.

## Open Questions

- Are there additional public maintainer statements or release notes that cleanly separate package-level parser bugs from application-level unsafe-deserialization guidance?
- Should this page eventually split parser/resource-exhaustion issues from serializer and type-handling risks so future site rendering stays easy to scan?
- Is there enough public evidence to add a sourced hardening section around `MaxDepth`, regex usage in JSONPath-like queries, and safe deserialization defaults?

## Related Pages

- [[dotnet/index]]

---
*Last updated: 2026-04-11 | Sources: 6 (OSV package query, GitHub Advisory Database, upstream issue #2457, upstream PR/commit history, 13.0.1 release notes, NuGet package metadata)*
