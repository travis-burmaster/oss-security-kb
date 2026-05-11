# org.springframework.security:spring-security-web (Maven)

**Registry:** Maven Central  
**Weekly Downloads:** unknown  
**Repository:** https://github.com/spring-projects/spring-security  
**Security Contact / Advisories:** Spring Security advisories via https://spring.io/security  
**Disclosure Policy:** https://spring.io/security  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-11 | OpenClaw recurring review | advisory mapping (public records only) | public-source curation (OSV.dev package query and vulnerability records, GitHub Advisory Database aliases, Spring security advisory links surfaced from OSV, public CVE/NVD records, Maven Central metadata; local proxy synthesis used only as a drafting aid) | Added initial Maven package page mapping 5 public `spring-security-web` advisories across request matching / authorization bypass, WebFlux static-resource authorization, HTTP response-header emission, `SecurityContext` privilege extension, and X.509 client-certificate identity extraction. | https://osv.dev/list?ecosystem=Maven&q=org.springframework.security%3Aspring-security-web |

## Known Vulnerabilities

The table below is a package-level public advisory map from OSV.dev for `org.springframework.security:spring-security-web`, cross-checked against GitHub Advisory Database aliases and Spring advisory / commit references where OSV provided them. Reachability is application- and configuration-dependent.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-22112 / GHSA-gq28-h5vg-8prx | High | Spring Security could fail to save the `SecurityContext` if it changed more than once in a single request. OSV notes an attacker could leverage this only when application code first triggers the state change, potentially extending elevated privileges beyond the intended request scope. | 5.2.9, 5.3.8, 5.4.4 | https://osv.dev/vulnerability/GHSA-gq28-h5vg-8prx ; https://tanzu.vmware.com/security/cve-2021-22112 |
| CVE-2022-22978 / GHSA-hh32-7344-cg2f | Critical | `RegexRequestMatcher` could be misconfigured and bypassed on some servlet containers, especially when applications used `.` in request-matching regular expressions. | 5.4.11, 5.5.7, 5.6.4 | https://osv.dev/vulnerability/GHSA-hh32-7344-cg2f ; https://github.com/advisories/GHSA-hh32-7344-cg2f |
| CVE-2024-38821 / GHSA-c4q5-6c82-3qpw | Critical | Spring WebFlux applications with non-`permitAll` Spring Security authorization rules on Spring static-resource support could have those static-resource authorization rules bypassed under the conditions described in the public advisory. | 5.7.13, 5.8.15, 6.0.13, 6.1.11, 6.2.7, 6.3.4 | https://osv.dev/vulnerability/GHSA-c4q5-6c82-3qpw ; https://spring.io/security/cve-2024-38821 |
| CVE-2026-22732 / GHSA-mf92-479x-3373 | Critical | Servlet applications specifying HTTP response headers through Spring Security could fail to have those headers written for affected version ranges. | 6.5.9, 7.0.4 | https://osv.dev/vulnerability/GHSA-mf92-479x-3373 ; https://spring.io/security/cve-2026-22732 |
| CVE-2026-22747 / GHSA-2jrg-rf5x-568g | Moderate | `SubjectX500PrincipalExtractor` did not correctly handle certain malformed X.509 certificate `CN` values, which could lead to reading the wrong username and impersonating another user. | 7.0.5 | https://osv.dev/vulnerability/GHSA-2jrg-rf5x-568g ; https://spring.io/security/cve-2026-22747 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.springframework.security%3Aspring-security-web*

## Security Posture Notes

- The public advisory pattern is concentrated around **authorization boundary and request-processing behavior**: request matcher bypasses, WebFlux static-resource authorization, `SecurityContext` persistence, response-header emission, and X.509 identity extraction.
- Several records are explicitly configuration-dependent. For example, `CVE-2024-38821` requires a WebFlux application using Spring static-resource support with authorization rules on those resources, and `CVE-2022-22978` centers on applications that use `RegexRequestMatcher` patterns susceptible to bypass.
- `CVE-2026-22732` is notable because it affects defensive HTTP headers rather than direct endpoint access. Downstream review should check whether applications depend on Spring Security to emit HSTS, frame, MIME-sniffing, or related browser-protection headers.
- `CVE-2026-22747` is specific to X.509 client-certificate authentication and malformed certificate common-name parsing. It should be prioritized for deployments that authenticate users or services from client certificates.
- Maven Central metadata saved in this pass listed `7.1.0-RC1` as the latest/release artifact for `spring-security-web`; production consumers should still choose supported stable Spring Security maintenance lines and the relevant fixed version for their line.

## Dependencies of Note

- `spring-security-web` is normally used with adjacent Spring Security modules such as `spring-security-config`, `spring-security-core`, and framework artifacts such as Spring MVC or WebFlux. Reachability often depends on the complete application stack and security DSL configuration.
- This page tracks package-scoped public advisories only; it does not imply every application using the artifact exposes every listed behavior.

## Open Questions

- Should the KB add a separate page for `org.springframework.security:spring-security-core`, which has a larger historical advisory set involving authentication, OAuth / SAML, cryptography, and method-security boundaries?
- Which Spring Boot starter versions still pin affected `spring-security-web` ranges after the fixed releases listed above?
- Would a cross-page note for Spring request-matcher pitfalls help connect `spring-security-web`, `spring-security-config`, `spring-webmvc`, and `spring-webflux` advisory patterns?

## Related Pages

- [[maven/org.springframework.security/spring-security-config]]
- [[maven/org.springframework/spring-webmvc]]
- [[maven/org.springframework/spring-web]]
- [[maven/index]]

---
*Last updated: 2026-05-11 | Sources: 5 (OSV.dev package query and individual vulnerability records, GitHub Advisory Database public aliases, Spring security advisory links surfaced by OSV, public CVE/NVD records, Maven Central metadata, plus a successful local proxy drafting pass used only as a synthesis aid)*
