# org.springframework:spring-web (Maven)

**Registry:** Maven (Maven Central)  
**Weekly Downloads:** unknown  
**Repository:** https://github.com/spring-projects/spring-framework  
**Security Contact:** Spring / Broadcom advisory process  
**Disclosure Policy:** https://spring.io/security  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-11 | OpenClaw recurring review | advisory mapping (public records only) | public-source curation (OSV.dev package query and vulnerability records, GitHub Advisory Database aliases, public CVE/NVD records, Spring security advisories and issue / commit references surfaced from OSV, Maven Central metadata; local proxy synthesis used only as a drafting aid) | Added initial Maven package page mapping 12 public package-scoped advisories across URL parsing / host validation, RFD, conditional-request DoS, DataBinder behavior, unsafe deserialization, XML input DoS, Cross-Site Tracing, CSRF, privilege-management, and XSS / response-generation boundaries. | https://osv.dev/list?ecosystem=Maven&q=org.springframework%3Aspring-web |

## Known Vulnerabilities

The table below is a package-level public advisory map from OSV.dev for `org.springframework:spring-web`, cross-checked against Spring advisory / issue / commit references where OSV provided them. Reachability is application- and configuration-dependent; this page does not claim that every Spring Web consumer exposes every listed boundary.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2013-6429 / GHSA-g6hf-f9cq-q7w7 | unknown | Cross-site request forgery issue in Spring Framework affecting older Spring Web / MVC request handling. | 3.2.5.RELEASE | https://osv.dev/vulnerability/GHSA-g6hf-f9cq-q7w7 |
| CVE-2013-6430 / GHSA-xjrf-8x4f-43h4 | MODERATE | Improper neutralization of input during web page generation, creating an XSS / response-generation boundary issue in affected Spring Framework versions. | 3.2.2.RELEASE | https://osv.dev/vulnerability/GHSA-xjrf-8x4f-43h4 |
| CVE-2015-3192 / GHSA-6v7w-535j-rq5m | HIGH | XML input handling could consume excessive resources and cause denial of service in affected Spring Framework versions. | 3.2.14, 4.1.7, 5.0.0.RC3 | https://osv.dev/vulnerability/GHSA-6v7w-535j-rq5m |
| CVE-2016-1000027 / GHSA-4wrc-f8pq-fpqp | CRITICAL | Unsafe Java deserialization methods in Spring Framework remained a dangerous boundary when exposed to untrusted serialized data. | 6.0.0 | https://osv.dev/vulnerability/GHSA-4wrc-f8pq-fpqp |
| CVE-2018-11039 / GHSA-9gcm-f4x3-8jpw | HIGH | Cross-Site Tracing risk around HTTP `TRACE` handling could expose sensitive header information under affected configurations. | 4.3.18, 5.0.7 | https://osv.dev/vulnerability/GHSA-9gcm-f4x3-8jpw |
| CVE-2021-22118 / GHSA-gfwj-fwqj-fp3v | HIGH | Improper privilege-management issue in Spring Framework affecting request / security boundary behavior in vulnerable deployments. | 5.2.15, 5.3.7 | https://osv.dev/vulnerability/GHSA-gfwj-fwqj-fp3v |
| CVE-2024-22243 / GHSA-ccgv-vj62-xf9h | HIGH | `UriComponentsBuilder` URL parsing / host validation flaw could enable open redirect or SSRF when applications trust parsed host data from attacker-controlled URLs. | 5.3.32, 6.0.17, 6.1.4 | https://osv.dev/vulnerability/GHSA-ccgv-vj62-xf9h ; https://spring.io/security/cve-2024-22243 |
| CVE-2024-22259 / GHSA-hgjh-9rj2-g67j | HIGH | Follow-on URL parsing / host validation vulnerability in Spring Framework, again relevant to applications making security decisions from parsed URL components. | 5.3.33, 6.0.18, 6.1.5 | https://osv.dev/vulnerability/GHSA-hgjh-9rj2-g67j ; https://spring.io/security/cve-2024-22259 |
| CVE-2024-22262 / GHSA-2wrp-6fg6-hmc5 | HIGH | Additional URL parsing / host validation issue in Spring Framework that could affect open-redirect or SSRF defenses built on vulnerable parsing behavior. | 5.3.34, 6.0.19, 6.1.6 | https://osv.dev/vulnerability/GHSA-2wrp-6fg6-hmc5 ; https://spring.io/security/cve-2024-22262 |
| CVE-2024-38809 / GHSA-2rmj-mq67-h97g | LOW | Conditional HTTP request handling could be abused for denial of service against affected Spring Framework versions. | 5.3.38, 6.0.23, 6.1.12 | https://osv.dev/vulnerability/GHSA-2rmj-mq67-h97g ; https://spring.io/security/cve-2024-38809 |
| CVE-2024-38820 / GHSA-4gc7-5j7h-4qph | LOW | DataBinder case-sensitive match exception could affect binding / authorization assumptions where applications rely on case-sensitive property matching. | 6.1.14 | https://osv.dev/vulnerability/GHSA-4gc7-5j7h-4qph ; https://spring.io/security/cve-2024-38820 |
| CVE-2025-41234 / GHSA-6r3c-xf4w-jxjm | HIGH | Reflected file download vulnerability when request-controlled input is reflected into `Content-Disposition`-relevant responses in affected Spring Framework versions. | 6.1.21, 6.2.8 | https://osv.dev/vulnerability/GHSA-6r3c-xf4w-jxjm ; https://spring.io/security/cve-2025-41234 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.springframework%3Aspring-web*

## Security Posture Notes

- The strongest recent cluster is the 2024 `UriComponentsBuilder` URL parsing / host-validation sequence (`CVE-2024-22243`, `CVE-2024-22259`, and `CVE-2024-22262`). These records matter most where applications parse attacker-controlled URLs and then make allowlist, redirect, or outbound-request decisions from the parsed host.
- Several records are framework-boundary issues rather than universal package RCE: RFD, Cross-Site Tracing, CSRF, conditional-request DoS, XML-input DoS, and DataBinder behavior depend on enabled endpoints, request flows, and application-specific use of Spring Web APIs.
- `CVE-2016-1000027` is retained because public advisory databases still mark `spring-web` as affected and because unsafe deserialization remains high impact if legacy remoting / serialization paths receive untrusted data. The remediation boundary is a major-version migration rather than a small patch in old lines.
- Maven Central metadata saved in this pass listed `7.0.7` as the latest release. Consumers should choose a supported Spring Framework maintenance line compatible with their application and apply that line's fixed release, rather than treating the newest major as a drop-in upgrade.
- This page is intentionally separate from `spring-webmvc`: `spring-web` owns foundational web utilities and HTTP abstractions, while MVC / WebFlux pages may carry additional static-resource, view-template, router, and application-model advisories.

## Dependencies of Note

- This page tracks direct `org.springframework:spring-web` package-scoped records. Spring applications commonly include adjacent artifacts such as `spring-webmvc`, `spring-webflux`, `spring-core`, Spring Security, and Spring Boot starters.
- Some public records involve interactions with Spring Security or application-level URL allowlists. Those are included only where OSV / GHSA marks `org.springframework:spring-web` as affected.

## Open Questions

- Should `org.springframework:spring-webflux` receive a separate page to keep WebFlux-specific multipart, static-resource, and functional-router records distinct from the shared `spring-web` utility surface?
- Which Spring Framework lines should the KB present as supported remediation baselines for long-lived enterprise applications that cannot immediately move to 7.x?
- Are downstream Spring Boot starter pages useful, or would they duplicate artifact-level pages without improving remediation guidance?

## Related Pages

- [[maven/index]]
- [[maven/org.springframework/spring-core]]
- [[maven/org.springframework/spring-webmvc]]

---
*Last updated: 2026-05-11 | Sources: 5 (OSV package query and individual vulnerability records, GitHub Advisory Database public aliases surfaced by OSV, public CVE/NVD records, Spring advisory / issue / commit references surfaced by OSV, Maven Central metadata)*
