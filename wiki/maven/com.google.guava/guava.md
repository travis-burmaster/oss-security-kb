# com.google.guava:guava (Maven)

**Registry:** Maven Central  
**Latest Version:** 33.6.0-jre (Maven repository metadata during 2026-05-15 review)  
**Repository:** https://github.com/google/guava  
**Security Contact:** no repository-level SECURITY.md confirmed in this pass  
**Disclosure Policy:** no repository-level SECURITY.md confirmed in this pass; public records are tracked through GitHub Advisory Database / CVE channels  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-15 | OpenClaw recurring review | package-level public advisory mapping for Maven `com.google.guava:guava` | public-source curation from OSV.dev package and vulnerability records, GitHub Advisory Database aliases surfaced through OSV, public CVE / NVD records, upstream GitHub issues / commits / release references surfaced by the public records, GitHub repository metadata, Maven repository metadata, and local proxy-assisted drafting | Added initial advisory-mapped Maven page for Guava covering three public package-scoped records: deserialization-driven allocation DoS fixed in the 24.1.1 line, and two local temporary-file / temporary-directory exposure records addressed in the 32.0.x line. | https://osv.dev/list?ecosystem=Maven&q=com.google.guava%3Aguava |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2018-10237 / GHSA-mvr2-9pj6-7w5j | Moderate | Guava 11.0 through the pre-24.1.1 line could allocate memory eagerly during deserialization of crafted data in `AtomicDoubleArray` Java serialization and `CompoundOrdering` GWT serialization paths. Public records frame this as a denial-of-service risk for servers that deserialize attacker-provided data. | 24.1.1 line (`24.1.1-android` in OSV range; corresponding fixed Guava release family) | https://github.com/advisories/GHSA-mvr2-9pj6-7w5j ; https://nvd.nist.gov/vuln/detail/CVE-2018-10237 |
| CVE-2020-8908 / GHSA-5mg8-w23w-74h3 | Low | `com.google.common.io.Files.createTempDir()` created directories using default Unix-like temporary-directory permissions, which could expose files to other local users on the same machine. The public advisory recommends avoiding the method or explicitly tightening permissions after creation. | 32.0.0-android according to OSV / GHSA affected range; fixed release family is the 32.0.x line | https://github.com/advisories/GHSA-5mg8-w23w-74h3 ; https://nvd.nist.gov/vuln/detail/CVE-2020-8908 ; https://github.com/google/guava/issues/4011 |
| CVE-2023-2976 / GHSA-7g45-4rm6-3mm3 | Moderate | `FileBackedOutputStream` could create files under Java's default temporary directory on Unix systems and Android Ice Cream Sandwich in a way that allowed other local users or apps with access to that directory to read created files. The advisory notes that 32.0.0 contains the security fix but recommends 32.0.1 because 32.0.0 broke some Windows functionality. | 32.0.0-android per OSV / GHSA; 32.0.1 recommended in advisory text for functional safety | https://github.com/advisories/GHSA-7g45-4rm6-3mm3 ; https://nvd.nist.gov/vuln/detail/CVE-2023-2976 ; https://github.com/google/guava/issues/6532 ; https://github.com/google/guava/releases/tag/v32.0.0 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=com.google.guava%3Aguava*

## Security Posture Notes

- Guava is a foundational Java utility library with unusually broad transitive reach across JVM applications, build tooling, enterprise SDKs, and server frameworks. Even compact package-level advisory history can matter because vulnerable helpers are often reached through downstream abstractions.
- The currently mapped public package-scoped Guava records split into two main classes: deserialization / eager-allocation denial of service in older 11.x–24.x lines, and local temporary-file or temporary-directory exposure in APIs that create files under shared system temp locations.
- The temporary-directory issues are local-access and deployment-context-sensitive. They should not be described as remote data exfiltration unless a downstream application exposes a stronger attacker path.
- Public records for CVE-2020-8908 and CVE-2023-2976 overlap in theme but track different Guava APIs (`Files.createTempDir()` and `FileBackedOutputStream`). Keep them as separate public identifiers while noting their shared temp-file boundary.
- Maven repository metadata showed `33.6.0-jre` as latest during this review, newer than all public fixed-version boundaries mapped here.
- No repository-level `SECURITY.md` was confirmed in this pass, and the repository security-advisory API returned no repository-owned advisory objects; the mapped advisories are public GitHub Advisory Database / CVE / OSV records.
- This review did not perform active vulnerability hunting, exploit validation, or live target testing. It only normalized already-public advisory, CVE, OSV/GHSA, upstream issue / release, repository, and Maven metadata evidence.

## Dependencies of Note

- Guava is frequently pulled transitively and may be shaded or repackaged. Inventory should check direct Maven coordinates, shaded copies, Android variants, and older forked coordinates referenced by OSV records.
- Deserialization exposure depends on whether attacker-controlled serialized data can reach affected Guava types. Temporary-file exposure depends on local multi-user or shared-application environments and whether sensitive data is written to the Guava-created files or directories.

## Open Questions

- Which high-usage Java frameworks still pin Guava below the 32.0.x line or shade older Guava code into fat JARs?
- Are there public downstream advisories where Guava's temp-file APIs became remotely reachable through application-specific upload, export, or cache flows?
- Should the KB add separate compatibility notes for Android and `-jre` / `-android` variants when OSV fixed ranges name only one classifier-style release suffix?

## Related Pages

- [[maven/commons-io/commons-io]]
- [[maven/com.fasterxml.jackson.core/jackson-databind]]
- [[maven/index]]

---
*Last updated: 2026-05-15 | Sources: OSV package query and individual vulnerability records for `com.google.guava:guava`; GitHub Advisory Database entries for GHSA-mvr2-9pj6-7w5j, GHSA-5mg8-w23w-74h3, and GHSA-7g45-4rm6-3mm3; public CVE / NVD records for CVE-2018-10237, CVE-2020-8908, and CVE-2023-2976; upstream GitHub issues / commits / release references surfaced by OSV; GitHub repository metadata and repository security-policy checks; Maven repository metadata; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid.*
