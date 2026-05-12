# org.springframework:spring-webflux (Maven)

**Registry:** Maven Central  
**Weekly Downloads:** unknown (as of 2026-05-12)  
**Repository:** https://github.com/spring-projects/spring-framework  
**Security Contact:** Spring / Broadcom security advisory process  
**Disclosure Policy:** https://spring.io/security  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-12 | OpenClaw recurring review | public advisory mapping for Spring WebFlux artifact | public-source curation (OSV.dev package query and vulnerability records, GitHub Advisory Database records surfaced through OSV, public CVE/NVD records, Spring security advisories, upstream `SECURITY.md`, Maven Central metadata, local Claude-compatible proxy draft assist) | Added initial Maven page mapping 10 public `spring-webflux` advisories across Spring4Shell data-binding RCE, functional static-resource path traversal, CORS preflight CSRF, reflected file download, script-template path limitation, SSE stream integrity, multipart temporary-file DoS, static-resource DoS, and cache poisoning through the 6.2.18 / 7.0.7 fix train. | https://osv.dev/list?ecosystem=Maven&q=org.springframework%3Aspring-webflux |
| *No public proactive source-code audit on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

This table is a package-level public advisory map from OSV.dev / GitHub Advisory Database for `org.springframework:spring-webflux`, cross-checked against Spring advisory pages and public CVE references where available.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-5397 / GHSA-7pm4-g2qj-j85x | MODERATE | Spring MVC / WebFlux endpoints could be exposed to CSRF through CORS preflight behavior; the public advisory highlights client-certificate authentication as a notable edge case. | 5.2.3 | https://osv.dev/vulnerability/GHSA-7pm4-g2qj-j85x ; https://spring.io/security/cve-2020-5397 |
| CVE-2020-5398 / GHSA-8wx2-9q48-vm9r | HIGH | Applications that place user-controlled input into `Content-Disposition` filenames could be vulnerable to reflected file download (RFD) behavior in Spring MVC / WebFlux responses. | 5.0.16.RELEASE, 5.1.13.RELEASE, 5.2.3.RELEASE | https://osv.dev/vulnerability/GHSA-8wx2-9q48-vm9r ; https://spring.io/security/cve-2020-5398 |
| CVE-2022-22965 / GHSA-36p3-wjmg-h94x | CRITICAL | “Spring4Shell” data-binding RCE affecting Spring MVC or WebFlux applications on JDK 9+ under specific deployment conditions; the public advisory calls out Tomcat WAR deployments and notes the default Spring Boot executable JAR path was not vulnerable to the known exploit. | 5.2.20.RELEASE, 5.3.18 | https://osv.dev/vulnerability/GHSA-36p3-wjmg-h94x ; https://spring.io/security/cve-2022-22965 |
| CVE-2024-38816 / GHSA-cx7f-g6mp-7hqm | HIGH | Functional web frameworks (`WebMvc.fn` / `WebFlux.fn`) serving static resources from explicit `FileSystemResource` locations were vulnerable to path traversal. | 6.1.13 | https://osv.dev/vulnerability/GHSA-cx7f-g6mp-7hqm ; https://spring.io/security/cve-2024-38816 |
| CVE-2024-38819 / GHSA-g5vr-rgqm-vf78 | HIGH | Follow-on path traversal issue in applications serving static resources through functional web frameworks; public references link it to the same static-resource / filesystem boundary. | 6.1.14 | https://osv.dev/vulnerability/GHSA-g5vr-rgqm-vf78 ; https://spring.io/security/cve-2024-38819 |
| CVE-2026-22735 / GHSA-6hcq-hmm3-jj3c | LOW | Spring MVC and WebFlux applications using Server-Sent Events (SSE) could experience stream corruption, affecting response integrity under the conditions described by the Spring advisory. | 6.2.17, 7.0.6 | https://osv.dev/vulnerability/GHSA-6hcq-hmm3-jj3c ; https://spring.io/security/cve-2026-22735 |
| CVE-2026-22737 / GHSA-4773-3jfm-qmx3 | MODERATE | Java scripting-engine-backed template views, such as JRuby or Jython script templates, in Spring MVC / WebFlux could disclose files outside configured script template locations. | 6.2.17, 7.0.6 | https://osv.dev/vulnerability/GHSA-4773-3jfm-qmx3 ; https://spring.io/security/cve-2026-22737 |
| CVE-2026-22740 / GHSA-5843-p793-ghmm | LOW | WebFlux server applications processing multipart requests could leave temporary files undeleted for larger parts under some circumstances, allowing disk-space exhaustion. | 6.2.18, 7.0.7 | https://osv.dev/vulnerability/GHSA-5843-p793-ghmm ; https://spring.io/security/cve-2026-22740 |
| CVE-2026-22741 / GHSA-wg35-8jpf-2xv3 | LOW | Static resource-chain caching with encoded resource resolution could be cache-poisoned when the resource cache was empty at attack time. | 6.2.18, 7.0.7 | https://osv.dev/vulnerability/GHSA-wg35-8jpf-2xv3 ; https://spring.io/security/cve-2026-22741 |
| CVE-2026-22745 / GHSA-6p4f-wcwh-5vvm | MODERATE | Spring MVC / WebFlux applications serving static resources from the file system on Windows could spend excessive time resolving malicious resource requests, causing denial of service. | 6.2.18, 7.0.7 | https://osv.dev/vulnerability/GHSA-6p4f-wcwh-5vvm ; https://spring.io/security/cve-2026-22745 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.springframework%3Aspring-webflux*

## Security Posture Notes

- `spring-webflux` carries a compact but important public advisory set because it sits on reactive HTTP request handling, functional routing, static-resource serving, multipart parsing, response construction, and streaming response behavior.
- The highest-impact record is `CVE-2022-22965` / Spring4Shell. The public advisory is explicit that exposure depended on application and deployment shape, so inventory should check runtime/deployment conditions rather than treating every dependency occurrence as equally reachable.
- Static-resource and filesystem-boundary issues recur across the WebFlux-relevant set: `CVE-2024-38816`, `CVE-2024-38819`, `CVE-2026-22737`, `CVE-2026-22741`, and `CVE-2026-22745` all depend on specific routing, template, cache, OS, or resource-handler configuration.
- The 2026 records show active maintenance on lower-severity but operationally relevant boundaries: SSE stream integrity, multipart temporary-file cleanup, static-resource cache poisoning, and Windows file-resolution denial of service.
- Spring publishes dedicated security advisories and the upstream repository uses GitHub security features. The upstream `SECURITY.md` points reporters to https://spring.io/security and the component advisory pages include affected-version and fixed-version guidance.

## Dependencies of Note

- WebFlux exposure often depends on adjacent components and configuration: Reactor Netty or another reactive runtime, functional route definitions, static-resource handling, script-template engines, multipart handling, CORS/client-certificate behavior, and Spring Security policy.
- Pages for `org.springframework:spring-core`, `org.springframework:spring-web`, `org.springframework:spring-webmvc`, and Spring Security artifacts should be read alongside this page because Spring advisories frequently span multiple modules.

## Open Questions

- Which supported Spring Framework maintenance lines should the KB highlight as enterprise remediation baselines for teams that cannot immediately move to 7.x?
- Are there public downstream incident reports that clarify real-world reachability for the newer WebFlux-specific multipart temporary-file, static-resource cache, and Windows path-resolution issues?
- Should future passes add a separate normalization note for Reactor Netty / Netty HTTP parser advisories commonly present in WebFlux deployments?

## Related Pages

- [[maven/org.springframework/spring-core]]
- [[maven/org.springframework/spring-web]]
- [[maven/org.springframework/spring-webmvc]]
- [[maven/org.springframework.security/spring-security-web]]
- [[maven/index]]

---
*Last updated: 2026-05-12 | Sources: 38 (OSV package query and individual vulnerability records for `org.springframework:spring-webflux`; GitHub Advisory Database records surfaced through OSV; public CVE/NVD records; Spring security advisories including CVE-2022-22965, CVE-2026-22737, CVE-2026-22740, CVE-2026-22741, and CVE-2026-22745; upstream SECURITY.md; Maven Central metadata; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid)*
