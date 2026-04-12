# Newtonsoft.Json (.NET / NuGet)

**Registry:** NuGet
**Weekly Downloads:** unknown (as of 2026-04-11)
**Repository:** https://github.com/JamesNK/Newtonsoft.Json
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-11 | OpenClaw recurring review | api-surface | manual | 1 publicly disclosed package vulnerability curated from OSV, GHSA, CVE, and upstream issue / fix history | https://osv.dev/list?ecosystem=NuGet&q=Newtonsoft.Json |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-21907 / GHSA-5crp-9r3c-p9vr | High | Deeply nested JSON could trigger high CPU / memory consumption during deserialization and `StackOverflowException` during serialization or `JObject.ToString()`, producing denial-of-service risk in applications that accept attacker-controlled JSON or object graphs. | 13.0.1 | https://github.com/advisories/GHSA-5crp-9r3c-p9vr |

*Full CVE history: https://osv.dev/list?ecosystem=NuGet&q=Newtonsoft.Json*

## Security Posture Notes

- The public package-specific advisory history gathered in this review is narrow but concrete: one GHSA / CVE-backed denial-of-service issue tied to extreme nesting depth rather than a broad stream of package-level parser bugs.
- Advisory and upstream fix references agree that versions before 13.0.1 could spend significant CPU / RAM while deserializing highly nested input and could hit `StackOverflowException` on serialization-related paths for deeply nested structures.
- Upstream fixed the issue in PR #2462 / commit `7e77bbe1beccceac4fc7b174b53abfefac278b66`, changing default `MaxDepth` handling in `JsonReader` and `JsonSerializer`, and the 13.0.1 release is the practical upgrade anchor for downstream users.
- `Newtonsoft.Json` remains security-relevant less because of a long package-level CVE list and more because it often sits on deserialization trust boundaries in older .NET applications, SDKs, and compatibility layers.
- Many dangerous `TypeNameHandling` discussions around Json.NET are application-configuration problems rather than clean package vulnerabilities; they should only be added here when backed by package-specific public advisories or clearly scoped upstream guidance.

## Dependencies of Note

- `System.Text.Json` is still the most important comparison page to add later so the KB can distinguish legacy Json.NET operational assumptions from newer built-in .NET JSON behavior.
- Downstream frameworks that expose custom converters, polymorphic deserialization, or global serializer settings are adjacent risk surfaces even when the package advisory itself is DoS-focused.

## Open Questions

- Are there public maintainer-authored hardening notes or release notes beyond the GHSA / issue / PR trail that would support a small evidence-backed hardening section for `MaxDepth` and safe serializer defaults?
- Which Json.NET misuse patterns deserve future cross-links on this page without blurring the line between package vulnerabilities and insecure application configuration?
- Should a future companion page cover `System.Text.Json` so the KB can make safer migration / default-behavior comparisons without overloading this package page?

## Related Pages

- [[dotnet/index]]

---
*Last updated: 2026-04-11 | Sources: 7 (OSV package query, GHSA advisory page, CVE record, upstream issue #2457, upstream PR #2462, upstream fix commit, 13.0.1 release page)*
