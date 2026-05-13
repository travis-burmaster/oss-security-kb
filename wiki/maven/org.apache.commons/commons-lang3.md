# org.apache.commons:commons-lang3 (Maven)

**Registry:** Maven Central  
**Latest Version:** 3.20.0 (Maven Central search API during 2026-05-13 review)  
**Repository:** https://github.com/apache/commons-lang  
**Security Contact:** Apache Security Team / Commons project channels  
**Disclosure Policy:** https://commons.apache.org/security.html  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-13 | OpenClaw recurring review | package-level public advisory mapping for Maven `org.apache.commons:commons-lang3` | public-source curation from OSV.dev package and vulnerability records, GitHub Advisory Database, public CVE records, Apache Commons security / disclosure pages, Apache public mailing-list advisory, Maven Central metadata, upstream fix commit references, and local proxy-assisted drafting | Added initial advisory-mapped Maven page for Commons Lang 3.x, covering the public `ClassUtils.getClass(...)` uncontrolled-recursion / `StackOverflowError` denial-of-service issue fixed in 3.18.0, with legacy 2.x coordinate context. | https://osv.dev/list?ecosystem=Maven&q=org.apache.commons%3Acommons-lang3 |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-48924 / GHSA-j288-q9x7-2f5v | Moderate | `ClassUtils.getClass(...)` can recurse uncontrollably on very long inputs and throw `StackOverflowError`. Because Java `Error` conditions are often not caught by applications and libraries, public records describe this as an application-stop / denial-of-service risk. | 3.18.0 for `org.apache.commons:commons-lang3`; the legacy `commons-lang:commons-lang` 2.0–2.6 line is also listed as affected. | https://github.com/advisories/GHSA-j288-q9x7-2f5v ; https://www.cve.org/CVERecord?id=CVE-2025-48924 ; https://lists.apache.org/thread/bgv0lpswokgol11tloxnjfzdl7yrc1g1 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.apache.commons%3Acommons-lang3*

## Security Posture Notes

- Commons Lang is a foundational Java utility dependency with broad direct and transitive reach. Its public package-advisory footprint is small, but even narrow utility-method flaws can matter when exposed to attacker-controlled input through reflection, expression, template, or plugin systems.
- The current public advisory set for the `org.apache.commons:commons-lang3` coordinate centers on one uncontrolled-recursion / denial-of-service issue fixed in `3.18.0`.
- Public OSV / GHSA data also names the older `commons-lang:commons-lang` 2.x coordinate as affected from 2.0 through 2.6. That is a separate legacy artifact line and should not be confused with the 3.x Maven coordinate tracked by this page.
- Maven Central reported `3.20.0` as the latest `commons-lang3` version during this review, newer than the published 3.18.0 fix point.
- This review did not perform active vulnerability hunting, exploit validation, or live target testing. It only normalized already-public advisory, CVE, Apache, Maven Central, and upstream repository evidence.

## Dependencies of Note

- Commons Lang is frequently pulled transitively by JVM frameworks, build tooling, enterprise SDKs, and older application stacks. Inventory should check shaded / bundled copies as well as direct Maven dependencies.
- Reachability depends on whether untrusted or very long strings can flow into `ClassUtils.getClass(...)` or wrappers around it.

## Open Questions

- Which common Java frameworks or plugin systems expose user-controlled class-name resolution paths that could make `ClassUtils.getClass(...)` reachable?
- Should the KB add a separate legacy page for `commons-lang:commons-lang` 2.x to avoid mixing the retired 2.x coordinate with the maintained 3.x coordinate?
- Are there public downstream advisories documenting shaded or pinned Commons Lang copies that remained below 3.18.0 after the upstream fix?

## Related Pages

- [[maven/commons-io/commons-io]]
- [[maven/org.apache.commons/commons-compress]]
- [[maven/index]]

---
*Last updated: 2026-05-13 | Sources: OSV package query and individual vulnerability record for `org.apache.commons:commons-lang3`; GitHub Advisory Database entry for GHSA-j288-q9x7-2f5v; public CVE record for CVE-2025-48924; Apache Commons security / disclosure pages; Apache public mailing-list advisory; Maven Central metadata; upstream fix commit reference surfaced by OSV; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid.*
