# org.springframework:spring-core (Maven)

**Registry:** Maven (Maven Central)  
**Weekly Downloads:** unknown  
**Repository:** https://github.com/spring-projects/spring-framework  
**Security Contact:** Spring / Broadcom advisory process  
**Disclosure Policy:** https://spring.io/security  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-09 | OpenClaw recurring review | advisory mapping (public records only) | public-source curation (OSV.dev package query and vulnerability records, GitHub Advisory Database aliases, public CVE/NVD records, Spring advisory / release links surfaced from OSV, Maven Central metadata; local proxy synthesis attempted but rate-limited and not used) | Added initial Maven package page mapping 18 public advisories across path/resource handling, authorization boundaries, logging, JSONP/cross-domain behavior, deserialization, and denial-of-service issues. | https://osv.dev/list?ecosystem=Maven&q=org.springframework%3Aspring-core |

## Known Vulnerabilities

The table below is a package-level public advisory map from OSV.dev for `org.springframework:spring-core`, cross-checked against Spring advisory / release links where OSV provided them.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2009-1190 / GHSA-wjjr-h4wh-w6vv | MODERATE | Inefficient regular-expression handling in Spring MVC/controller routing could cause excessive CPU consumption on crafted requests. | 3.0.0.RELEASE | https://osv.dev/vulnerability/GHSA-wjjr-h4wh-w6vv |
| CVE-2011-2730 / GHSA-wv88-pf73-x22p | HIGH | Expression-language handling could allow attacker-controlled directives to be evaluated in affected Spring Framework versions. | 2.5.6.SEC03, 2.5.7.SR023, 3.0.6 | https://osv.dev/vulnerability/GHSA-wv88-pf73-x22p |
| CVE-2011-2894 / GHSA-f866-m9mv-2xr3 | MODERATE | Deserialization of untrusted data affected Spring Framework / Spring Security remoting surfaces in older lines. | 2.0.7, 3.0.6 | https://osv.dev/vulnerability/GHSA-f866-m9mv-2xr3 |
| CVE-2014-3578 / GHSA-rhcg-rwhx-qj3j | MODERATE | Directory traversal / path-restriction bypass in Spring Framework resource handling. | 3.2.9, 4.0.5 | https://osv.dev/vulnerability/GHSA-rhcg-rwhx-qj3j |
| CVE-2015-0201 / GHSA-45vg-2v73-vm62 | MODERATE | Java SockJS client generated predictable session IDs, enabling cross-session message confusion in affected 4.1.x versions. | 4.1.5 | https://osv.dev/vulnerability/GHSA-45vg-2v73-vm62 |
| CVE-2015-5211 / GHSA-pgf9-h69p-pcgf | HIGH | Static resource handling could expose files or directories through crafted resource paths. | 3.2.15, 4.1.8, 4.2.2 | https://osv.dev/vulnerability/GHSA-pgf9-h69p-pcgf |
| CVE-2016-5007 / GHSA-8crv-49fr-2h6j | HIGH | Path matching ambiguity between Spring Framework and Spring Security could leave protected paths unrecognized. | 4.1.1, 4.3.1 | https://osv.dev/vulnerability/GHSA-8crv-49fr-2h6j |
| CVE-2018-11040 / GHSA-f26x-pr96-vw86 | MODERATE | Optional JSONP support in REST / Jackson view integrations could enable unintended cross-domain data exposure when configured. | 4.3.18.RELEASE, 5.0.7.RELEASE | https://osv.dev/vulnerability/GHSA-f26x-pr96-vw86 |
| CVE-2018-1199 / GHSA-v596-fwhq-8x48 | MODERATE | URL path-parameter handling ambiguity could allow security-constraint bypasses for secured Spring MVC static-resource URLs. | 4.1.5, 4.2.4, 4.3.14, 5.0.1, 5.0.3 | https://osv.dev/vulnerability/GHSA-v596-fwhq-8x48 |
| CVE-2018-1257 / GHSA-rcpf-vj53-7h2m | MODERATE | Crafted STOMP messages to Spring's simple in-memory WebSocket broker could trigger regex-based denial of service. | 4.3.17, 5.0.6 | https://osv.dev/vulnerability/GHSA-rcpf-vj53-7h2m |
| CVE-2018-1258 / GHSA-cxrj-66c5-9fmh | HIGH | Authorization bypass when Spring Framework method-security annotation resolution interacts with Spring Security. | 5.0.6.RELEASE | https://osv.dev/vulnerability/GHSA-cxrj-66c5-9fmh |
| CVE-2018-1271 / GHSA-g8hw-794c-4j9g | MODERATE | Directory traversal in Spring Framework static resource handling. | 4.3.15, 5.0.5 | https://osv.dev/vulnerability/GHSA-g8hw-794c-4j9g |
| CVE-2018-1272 / GHSA-4487-x383-qpph | HIGH | Multipart request construction could let attacker-controlled input insert extra parts into an outbound request, potentially causing downstream privilege confusion. | 4.3.15, 5.0.5 | https://osv.dev/vulnerability/GHSA-4487-x383-qpph |
| CVE-2018-15756 / GHSA-ffvq-7w96-97p7 | HIGH | DoS in Spring Framework from crafted range requests / resource handling in affected versions. | 4.3.20.RELEASE, 5.0.10.RELEASE, 5.1.1.RELEASE | https://osv.dev/vulnerability/GHSA-ffvq-7w96-97p7 |
| CVE-2021-22060 / GHSA-6gf2-pvqw-37ph | MODERATE | Log entry injection in Spring Framework that could let authenticated users forge or manipulate log output. | 5.2.19, 5.3.14 | https://osv.dev/vulnerability/GHSA-6gf2-pvqw-37ph |
| CVE-2021-22096 / GHSA-rfmp-97jj-h8m6 | MODERATE | Log injection through insufficient output neutralization in Spring Framework logging paths. | 5.2.18, 5.3.11 | https://osv.dev/vulnerability/GHSA-rfmp-97jj-h8m6 |
| CVE-2024-22233 / GHSA-r4q3-7g4q-x89m | HIGH | Server-side web DoS in Spring Framework fixed in the 6.0.x and 6.1.x lines. | 6.0.16, 6.1.3 | https://osv.dev/vulnerability/GHSA-r4q3-7g4q-x89m ; https://spring.io/security/cve-2024-22233 |
| CVE-2025-41249 / GHSA-jmp9-x22r-554x | HIGH | Annotation detection can fail on methods in generic type hierarchies, which may affect authorization decisions with Spring Security method security. | 6.2.11 | https://osv.dev/vulnerability/GHSA-jmp9-x22r-554x ; https://spring.io/security/cve-2025-41249 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.springframework%3Aspring-core*

## Security Posture Notes

- The public advisory pattern is broad rather than concentrated in one parser: Spring Core issues span static-resource/path normalization, framework/security path matching, annotation/method-security resolution, logging output neutralization, optional JSONP behavior, remoting/deserialization, and web denial-of-service cases.
- Exposure is highly configuration-dependent. Several records require Spring Security method security, Spring MVC static resource handling, SockJS / WebSocket messaging, JSONP/Jackson view support, or vulnerable remoting/resource-serving usage rather than affecting every Spring Core consumer equally.
- The most recent record in this pass is `CVE-2025-41249` / `GHSA-jmp9-x22r-554x`, fixed in `6.2.11`, where annotation detection on generic type hierarchies may affect authorization decisions when Spring Security method security relies on such annotations.
- Maven Central metadata saved in this pass listed `7.0.7` as the latest release. Consumers should still choose a supported Spring Framework line compatible with their application and use the fixed version for that line rather than treating the latest major as a drop-in upgrade.
- Older 2.x, 3.x, and 4.x records remain important for long-lived enterprise applications because many advisories are framework-boundary issues that may be reachable through application-specific MVC, resource, messaging, or security configurations.

## Dependencies of Note

- This page tracks direct `org.springframework:spring-core` package-scoped records. Spring applications commonly include many adjacent artifacts (`spring-web`, `spring-webmvc`, `spring-security-*`, Boot starters), so a full application review should check the complete Spring dependency set.
- Some public records involve interaction with Spring Security. Those are included here only where OSV / GHSA marks `org.springframework:spring-core` as affected.

## Open Questions

- Should the KB add separate pages for `org.springframework:spring-web`, `spring-webmvc`, and Spring Security artifacts to avoid overloading the Spring Core page with adjacent framework advisories?
- Which currently supported Spring Framework maintenance lines should be treated as the remediation baseline for downstream users who cannot jump to the latest 7.x release?
- Are there high-impact downstream products whose public advisories clarify reachability for the path/resource-handling and method-security records?

## Related Pages

- [[maven/index]]
- [[maven/org.apache.logging.log4j/log4j-core]]
- [[maven/com.fasterxml.jackson.core/jackson-databind]]

---
*Last updated: 2026-05-09 | Sources: 5 (OSV package query and individual vulnerability records, GitHub Advisory Database public aliases surfaced by OSV, public CVE/NVD records, Spring advisory / release links surfaced by OSV, Maven Central metadata)*
