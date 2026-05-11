# org.springframework.security:spring-security-config (Maven)

**Registry:** Maven Central  
**Weekly Downloads:** unknown  
**Repository:** https://github.com/spring-projects/spring-security  
**Security Contact / Advisories:** Spring Security advisories via https://spring.io/security  
**Disclosure Policy:** https://spring.io/security  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-11 | OpenClaw recurring review | advisory mapping (public records only) | public-source curation (OSV.dev package query and vulnerability records, GitHub Advisory Database aliases, Spring security advisory links surfaced from OSV, public CVE/NVD records, Maven Central metadata; local proxy synthesis used only as a drafting aid) | Added initial Maven package page mapping 5 public `spring-security-config` advisories across WebFlux `**` matcher bypass, multi-servlet authorization-rule ambiguity, servlet-path matching omissions in Java/XML configuration, and world-writable `spring-security.xsd` packaging metadata. | https://osv.dev/list?ecosystem=Maven&q=org.springframework.security%3Aspring-security-config |

## Known Vulnerabilities

The table below is a package-level public advisory map from OSV.dev for `org.springframework.security:spring-security-config`, cross-checked against GitHub Advisory Database aliases and Spring advisory / commit references where OSV provided them. Reachability is application- and configuration-dependent.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-34034 / GHSA-3h6f-g5f3-gc4w | Critical | Using `**` as a pattern in Spring Security configuration for WebFlux could create a mismatch between Spring Security and Spring WebFlux pattern matching, creating a potential security bypass. | 5.6.12, 5.7.10, 5.8.5, 6.0.5, 6.1.2 | https://osv.dev/vulnerability/GHSA-3h6f-g5f3-gc4w |
| CVE-2023-34035 / GHSA-4vpr-xfrp-cj64 | High | Applications using `requestMatchers(String)` with multiple servlets, including Spring MVC's `DispatcherServlet`, could misconfigure authorization rules so they did not apply to the intended servlet endpoints. | 5.8.5, 6.0.5, 6.1.2 | https://osv.dev/vulnerability/GHSA-4vpr-xfrp-cj64 ; https://github.com/advisories/GHSA-4vpr-xfrp-cj64 |
| CVE-2023-34042 / GHSA-9gp8-6cg8-7h34 | Moderate | The `spring-security.xsd` file inside the `spring-security-config` JAR was world-writable when extracted, an incorrect-permission issue that public records classify as a potential local privilege-escalation risk if combined with filesystem access. | 5.7.11, 5.8.7, 6.0.7, 6.1.4 | https://osv.dev/vulnerability/GHSA-9gp8-6cg8-7h34 ; https://github.com/advisories/GHSA-9gp8-6cg8-7h34 |
| CVE-2026-22753 / GHSA-4wrg-8wpc-h923 | High | When an application used `securityMatchers(String)` and a `PathPatternRequestMatcher.Builder` bean to prepend a servlet path, matching requests to that filter chain could fail and intended security controls could be inactive. | 7.0.5 | https://osv.dev/vulnerability/GHSA-4wrg-8wpc-h923 ; https://spring.io/security/cve-2026-22753 |
| CVE-2026-22754 / GHSA-4vrc-j85c-598c | High | XML authorization rules using `<sec:intercept-url servlet-path="/servlet-path" pattern="/endpoint/**"/>` did not correctly include the servlet path when computing path matches, which could leave related authorization rules unexercised. | 7.0.5 | https://osv.dev/vulnerability/GHSA-4vrc-j85c-598c ; https://spring.io/security/cve-2026-22754 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.springframework.security%3Aspring-security-config*

## Security Posture Notes

- The public advisory pattern is tightly focused on **configuration-to-runtime authorization mismatches**: string request matchers, WebFlux `**` matching, multi-servlet applications, servlet-path prepending, and XML namespace authorization rules.
- `CVE-2023-34035`, `CVE-2026-22753`, and `CVE-2026-22754` all highlight servlet-path / matcher context as a recurring risk. Applications with more than one servlet, explicit servlet paths, or mixed Spring MVC and non-MVC endpoints deserve careful configuration review.
- `CVE-2023-34034` is WebFlux-specific in the public OSV text and should not be flattened into a universal servlet-stack finding, even though it is package-scoped to `spring-security-config`.
- `CVE-2023-34042` is qualitatively different from the request-matching advisories: it concerns file permissions on `spring-security.xsd` when the JAR contents are extracted, not remote request authorization by itself.
- Maven Central metadata saved in this pass listed `7.1.0-RC1` as the latest/release artifact for `spring-security-config`; production consumers should still choose supported stable Spring Security maintenance lines and the relevant fixed version for their line.

## Dependencies of Note

- `spring-security-config` is usually paired with `spring-security-web` and `spring-security-core`; request-matcher behavior can also depend on Spring MVC, WebFlux, servlet container path handling, and the exact Java/XML configuration style used by the application.
- This page tracks package-scoped public advisories only; it does not imply every application using the artifact exposes every listed behavior.

## Open Questions

- Should the KB add a Spring Security matcher-pattern note that summarizes safe migration from ambiguous `requestMatchers(String)` / `securityMatchers(String)` usage to explicit MVC, ant, regex, or path-pattern matchers where appropriate?
- Which Spring Boot versions inherited the affected `spring-security-config` ranges for `CVE-2023-34035`, `CVE-2026-22753`, and `CVE-2026-22754`?
- Should `spring-security-webflux` or WebFlux-specific Spring Security surfaces receive separate coverage, or are package-scoped `spring-security-config` / `spring-security-web` pages enough for now?

## Related Pages

- [[maven/org.springframework.security/spring-security-web]]
- [[maven/org.springframework/spring-webmvc]]
- [[maven/org.springframework/spring-web]]
- [[maven/index]]

---
*Last updated: 2026-05-11 | Sources: 5 (OSV.dev package query and individual vulnerability records, GitHub Advisory Database public aliases, Spring security advisory links surfaced by OSV, public CVE/NVD records, Maven Central metadata, plus a successful local proxy drafting pass used only as a synthesis aid)*
