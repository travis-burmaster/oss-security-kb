# org.springframework:spring-webmvc (Maven)

**Registry:** Maven Central  
**Weekly Downloads:** unknown (as of 2026-05-11)  
**Repository:** https://github.com/spring-projects/spring-framework  
**Security Contact:** Spring / Broadcom security advisory process  
**Disclosure Policy:** https://spring.io/security  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-11 | OpenClaw recurring review | public advisory mapping for Spring MVC artifact | public-source curation (OSV.dev package query and vulnerability records, GitHub Advisory Database records, public CVE/NVD records, Spring security advisories, upstream issues / commits surfaced from OSV, Maven Central metadata, local proxy draft assist) | Added initial Maven page mapping 18 public `spring-webmvc` advisories across data-binding RCE, path / static-resource boundaries, XXE, CSRF / request matching, RFD / XSS, cache poisoning, SSE stream integrity, and denial-of-service classes through 2026. | https://osv.dev/list?ecosystem=Maven&q=org.springframework%3Aspring-webmvc |
| *No public proactive source-code audit on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

This table is a package-level public advisory map from OSV.dev / GitHub Advisory Database for `org.springframework:spring-webmvc`, cross-checked against Spring advisory pages and public CVE references where available.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2014-0054 / GHSA-8cmm-qj8g-fcp6 | Unspecified in GHSA/OSV | `Jaxb2RootElementHttpMessageConverter` in Spring MVC did not fully disable external entity resolution, leaving an XXE issue that could read files, trigger DoS, or support CSRF-style effects; public notes describe it as an incomplete fix for earlier XML converter CVEs. | 3.2.8, 4.0.2 | https://osv.dev/vulnerability/GHSA-8cmm-qj8g-fcp6 ; https://nvd.nist.gov/vuln/detail/CVE-2014-0054 |
| CVE-2014-0225 / GHSA-f93f-g33r-8pcp | HIGH | XML processing in affected Spring Framework lines did not disable DTD URI-reference resolution by default when processing user-provided XML, enabling XXE. | 3.2.8, 4.0.5 | https://osv.dev/vulnerability/GHSA-f93f-g33r-8pcp ; https://nvd.nist.gov/vuln/detail/CVE-2014-0225 |
| CVE-2014-1904 / GHSA-ff7p-jqjm-v66h | Unspecified in GHSA/OSV | Spring MVC form tag rendering could reflect the requested URI into the default action, enabling XSS in affected 3.0.x/3.2.x and 4.0.x lines. | 3.2.8.RELEASE, 4.0.2.RELEASE | https://osv.dev/vulnerability/GHSA-ff7p-jqjm-v66h ; https://nvd.nist.gov/vuln/detail/CVE-2014-1904 |
| CVE-2014-3625 / GHSA-hhm4-hwq6-3c6w | Unspecified in GHSA/OSV | Static resource handling in Spring Framework could allow directory traversal / file disclosure through crafted resource requests. | 3.2.12, 4.0.8, 4.1.2 | https://osv.dev/vulnerability/GHSA-hhm4-hwq6-3c6w ; https://nvd.nist.gov/vuln/detail/CVE-2014-3625 |
| CVE-2016-9878 / GHSA-2m8h-fgr8-2q9w | HIGH | Paths supplied to Spring Framework `ResourceServlet` were not properly sanitized, allowing directory traversal in affected 3.2.x, 4.2.x, and 4.3.x lines. | 3.2.18, 4.2.9, 4.3.5 | https://osv.dev/vulnerability/GHSA-2m8h-fgr8-2q9w ; https://nvd.nist.gov/vuln/detail/CVE-2016-9878 |
| CVE-2020-5397 / GHSA-7pm4-g2qj-j85x | MODERATE | Spring MVC / WebFlux endpoints could be exposed to CSRF through CORS preflight behavior, especially in the client-certificate edge case documented in the public advisory. | 5.2.3 | https://osv.dev/vulnerability/GHSA-7pm4-g2qj-j85x ; https://nvd.nist.gov/vuln/detail/CVE-2020-5397 |
| CVE-2020-5398 / GHSA-8wx2-9q48-vm9r | HIGH | Applications that placed user-controlled input into `Content-Disposition` filenames could be vulnerable to reflected file download (RFD) behavior in Spring MVC / WebFlux. | 5.0.16.RELEASE, 5.1.13.RELEASE, 5.2.3.RELEASE | https://osv.dev/vulnerability/GHSA-8wx2-9q48-vm9r ; https://nvd.nist.gov/vuln/detail/CVE-2020-5398 |
| CVE-2022-22965 / GHSA-36p3-wjmg-h94x | CRITICAL | “Spring4Shell” data-binding RCE in Spring MVC / WebFlux applications on JDK 9+ under specific deployment conditions, notably Tomcat WAR deployments; the public advisory notes Spring Boot executable JAR deployments were not vulnerable to the known exploit path. | 5.2.20.RELEASE, 5.3.18 | https://osv.dev/vulnerability/GHSA-36p3-wjmg-h94x ; https://github.com/advisories/GHSA-36p3-wjmg-h94x ; https://spring.io/security/cve-2022-22965 |
| CVE-2023-20860 / GHSA-7phw-cxx7-q9vq | HIGH | Pattern mismatch between Spring Security `mvcRequestMatcher` using `**` and Spring MVC matching could create a security bypass in affected 5.3.x and 6.0.x versions. | 5.3.26, 6.0.7 | https://osv.dev/vulnerability/GHSA-7phw-cxx7-q9vq ; https://spring.io/security/cve-2023-20860 |
| CVE-2023-34053 / GHSA-v94h-hvhg-mf9h | HIGH | Crafted HTTP requests could cause denial of service when Spring MVC / WebFlux applications used Micrometer observation instrumentation (`micrometer-core` plus an `ObservationRegistry`, commonly via Spring Boot Actuator). | 6.0.14 | https://osv.dev/vulnerability/GHSA-v94h-hvhg-mf9h ; https://spring.io/security/cve-2023-34053 |
| CVE-2024-38816 / GHSA-cx7f-g6mp-7hqm | HIGH | Functional web frameworks (`WebMvc.fn` / `WebFlux.fn`) serving static resources from explicit `FileSystemResource` locations were vulnerable to path traversal. | 6.1.13 | https://osv.dev/vulnerability/GHSA-cx7f-g6mp-7hqm ; https://spring.io/security/cve-2024-38816 |
| CVE-2024-38819 / GHSA-g5vr-rgqm-vf78 | HIGH | Follow-on path traversal issue in applications serving static resources through functional web frameworks; public references link it to the same static-resource / filesystem boundary. | 6.1.14 | https://osv.dev/vulnerability/GHSA-g5vr-rgqm-vf78 ; https://nvd.nist.gov/vuln/detail/CVE-2024-38819 |
| CVE-2024-38828 / GHSA-w3c8-7r8f-9jp8 | MODERATE | Spring MVC controller methods with `@RequestBody byte[]` parameters were vulnerable to denial of service from crafted request bodies. | 5.3.42 | https://osv.dev/vulnerability/GHSA-w3c8-7r8f-9jp8 ; https://spring.io/security/cve-2024-38828 |
| CVE-2025-41242 / GHSA-r936-gwx5-v52f | HIGH | Spring MVC applications could be vulnerable to path traversal when deployed as WARs or with embedded Servlet containers that do not reject suspicious path sequences, while also serving static resources. | 6.2.10 | https://osv.dev/vulnerability/GHSA-r936-gwx5-v52f ; http://spring.io/security/cve-2025-41242 |
| CVE-2026-22735 / GHSA-6hcq-hmm3-jj3c | LOW | Spring MVC and WebFlux applications using Server-Sent Events (SSE) could experience stream corruption, affecting response integrity under the conditions described by the Spring advisory. | 6.2.17, 7.0.6 | https://osv.dev/vulnerability/GHSA-6hcq-hmm3-jj3c ; https://spring.io/security/cve-2026-22735 |
| CVE-2026-22737 / GHSA-4773-3jfm-qmx3 | HIGH | Java scripting-engine-backed template views (for example JRuby or Jython) in Spring MVC / WebFlux could disclose files outside configured script template locations. | 6.2.17, 7.0.6 | https://osv.dev/vulnerability/GHSA-4773-3jfm-qmx3 ; https://spring.io/security/cve-2026-22737 |
| CVE-2026-22741 / GHSA-wg35-8jpf-2xv3 | LOW | Static resource-chain caching with encoded resource resolution could be cache-poisoned when the resource cache was empty at attack time. | 6.2.18, 7.0.7 | https://osv.dev/vulnerability/GHSA-wg35-8jpf-2xv3 ; https://github.com/advisories/GHSA-wg35-8jpf-2xv3 ; https://spring.io/security/cve-2026-22741 |
| CVE-2026-22745 / GHSA-6p4f-wcwh-5vvm | MODERATE | Spring MVC / WebFlux applications serving static resources from the file system on Windows could spend excessive time resolving malicious resource requests, causing a denial of service. | 6.2.18, 7.0.7 | https://osv.dev/vulnerability/GHSA-6p4f-wcwh-5vvm ; https://github.com/advisories/GHSA-6p4f-wcwh-5vvm ; https://spring.io/security/cve-2026-22745 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.springframework%3Aspring-webmvc*

## Security Posture Notes

- `spring-webmvc` has a dense, long-running public advisory history because it sits directly on request routing, data binding, message conversion, static-resource serving, and browser-facing response behavior.
- The most severe public record in this package map is `CVE-2022-22965` / Spring4Shell, but exposure was not universal: the published exploit path required Spring MVC or WebFlux on JDK 9+ and deployment conditions such as Tomcat WAR packaging. Inventory should check deployment shape, not only dependency version.
- Static-resource and path-boundary issues recur across the record set (`CVE-2014-3625`, `CVE-2016-9878`, `CVE-2024-38816`, `CVE-2024-38819`, `CVE-2025-41242`, `CVE-2026-22737`, `CVE-2026-22745`, and `CVE-2026-22741`). Several newer advisories are highly configuration-dependent, involving functional routing, script template views, Windows filesystem behavior, cache settings, or Servlet-container path canonicalization.
- XML converter hardening was historically fragile: `CVE-2014-0054` is documented as an incomplete-fix follow-up to earlier XXE issues, and `CVE-2014-0225` separately tracks DTD URI-reference handling.
- Spring publishes dedicated security advisories and the upstream repository uses GitHub security features. The upstream `SECURITY.md` points reporters to https://spring.io/security and the component advisory pages include affected-version and fixed-version guidance.
- Maven Central metadata saved in this pass listed `7.0.7` as the latest / release version for `spring-webmvc` with last update timestamp `20260417070527`. Consumers should still remediate within supported Spring Framework lines rather than treating a new major version as a simple drop-in upgrade.

## Dependencies of Note

- `spring-webmvc` risk often depends on adjacent runtime components: Servlet container behavior, Spring Security matchers, Micrometer / Actuator instrumentation, XML converters, scripting engines, and static-resource configuration.
- Pages for `org.springframework:spring-core` and future `org.springframework:spring-web` / Spring Security artifacts should be read alongside this page because many public advisories span multiple Spring Framework modules.

## Open Questions

- Should the KB add a separate `org.springframework:spring-web` page to normalize the WebFlux / HTTP client-server advisories that overlap but are not identical to `spring-webmvc`?
- Which supported Spring Framework maintenance lines should be highlighted as remediation baselines for enterprises unable to move to 7.x?
- Are there public downstream incident reports that clarify real-world reachability for the newer static-resource cache, Windows path-resolution, and Servlet-container-canonicalization issues?

## Related Pages

- [[maven/org.springframework/spring-core]]
- [[maven/org.apache.tomcat.embed/tomcat-embed-core]]
- [[maven/index]]

---
*Last updated: 2026-05-11 | Sources: 68 (OSV package query and individual vulnerability records for `org.springframework:spring-webmvc`; GitHub Advisory Database records; public CVE/NVD records; Spring security advisories including CVE-2022-22965, CVE-2026-22737, CVE-2026-22741, and CVE-2026-22745; upstream issues / commits surfaced from OSV; Maven Central metadata; upstream SECURITY.md; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid)*
