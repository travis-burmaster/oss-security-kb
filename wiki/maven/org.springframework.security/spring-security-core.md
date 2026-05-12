# org.springframework.security:spring-security-core (Maven)

**Registry:** Maven Central  
**Weekly Downloads:** unknown  
**Repository:** https://github.com/spring-projects/spring-security  
**Security Contact / Advisories:** Spring Security advisories via https://spring.io/security  
**Disclosure Policy:** https://spring.io/security  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-11 | OpenClaw recurring review | advisory mapping (public records only) | public-source curation (OSV.dev package query and vulnerability records, GitHub Advisory Database aliases, Spring security advisory links surfaced from OSV, public CVE/NVD records, Maven Central metadata; local proxy synthesis used only as a drafting aid) | Added initial Maven package page mapping 31 public `spring-security-core` advisories across authorization and authentication bypasses, method-security annotation boundaries, cryptographic / token-generation weaknesses, deserialization, LDAP / SAML / CAS / OAuth-related integration boundaries, logout / security-context behavior, and DoS / enumeration issues. | https://osv.dev/list?ecosystem=Maven&q=org.springframework.security%3Aspring-security-core |

## Known Vulnerabilities

The table below is a package-level public advisory map from OSV.dev for `org.springframework.security:spring-security-core`, cross-checked against GitHub Advisory Database aliases and Spring advisory / commit references where OSV provided them. Reachability is application- and configuration-dependent.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2018-15801 / GHSA-27xw-p8v6-9jjr | High | Spring Security vulnerable to Authorization Bypass | 5.1.2 | https://osv.dev/vulnerability/GHSA-27xw-p8v6-9jjr ; https://github.com/advisories/GHSA-27xw-p8v6-9jjr |
| CVE-2020-5408 / GHSA-2ppp-9496-p23q | Moderate | Insufficient Entropy in Spring Security | 4.2.16, 5.0.16, 5.1.10, 5.2.4, 5.3.2 | https://osv.dev/vulnerability/GHSA-2ppp-9496-p23q ; https://github.com/advisories/GHSA-2ppp-9496-p23q |
| CVE-2010-3700 / GHSA-3295-h9qx-r82x | Moderate | Authentication Bypass Using an Alternate Path or Channel in SpringSource Spring Security and Acegi Security | 2.0.6, 3.0.4 | https://osv.dev/vulnerability/GHSA-3295-h9qx-r82x ; https://github.com/advisories/GHSA-3295-h9qx-r82x |
| CVE-2012-5055 / GHSA-3533-rvpc-6x56 | Moderate | Exposure of Sensitive Information to an Unauthorized Actor in Spring Security | 2.0.8, 3.0.8, 3.1.3 | https://osv.dev/vulnerability/GHSA-3533-rvpc-6x56 ; https://github.com/advisories/GHSA-3533-rvpc-6x56 |
| CVE-2011-2731 / GHSA-4644-hg35-55m9 | Moderate | Concurrent Execution using Shared Resource with Improper Synchronization in Spring Security | 2.0.7, 3.0.6 | https://osv.dev/vulnerability/GHSA-4644-hg35-55m9 ; https://github.com/advisories/GHSA-4644-hg35-55m9 |
| CVE-2020-5407 / GHSA-48rw-j489-928m | High | Signature wrapping vulnerability in Spring Security | 5.2.4, 5.3.2 | https://osv.dev/vulnerability/GHSA-48rw-j489-928m ; https://github.com/advisories/GHSA-48rw-j489-928m |
| CVE-2011-2732 / GHSA-5xm9-rf63-wj7h | Moderate | Improper Control of Generation of Code in Spring Security | 2.0.7, 3.0.6 | https://osv.dev/vulnerability/GHSA-5xm9-rf63-wj7h ; https://github.com/advisories/GHSA-5xm9-rf63-wj7h |
| CVE-2016-5007 / GHSA-8crv-49fr-2h6j | High | Spring Security and Spring Framework may not recognize certain paths that should be protected | 4.1.1, 4.3.1 | https://osv.dev/vulnerability/GHSA-8crv-49fr-2h6j ; https://github.com/advisories/GHSA-8crv-49fr-2h6j |
| CVE-2025-41248 / GHSA-8v5q-rhf3-jphm | High | Spring Security annotation detection mechanism has authorization bypass | 6.4.10, 6.5.4 | https://osv.dev/vulnerability/GHSA-8v5q-rhf3-jphm ; https://github.com/advisories/GHSA-8v5q-rhf3-jphm |
| CVE-2025-41232 / GHSA-9pp5-9c7g-4r83 | Critical | Spring Security authorization bypass for method security annotations on private methods | 6.4.6 | https://osv.dev/vulnerability/GHSA-9pp5-9c7g-4r83 ; https://github.com/advisories/GHSA-9pp5-9c7g-4r83 |
| CVE-2024-22257 / GHSA-f3jh-qvm4-mg39 | High | Erroneous authentication pass in Spring Security | 5.7.12, 5.8.11, 6.1.8, 6.2.3 | https://osv.dev/vulnerability/GHSA-f3jh-qvm4-mg39 ; https://github.com/advisories/GHSA-f3jh-qvm4-mg39 |
| CVE-2011-2894 / GHSA-f866-m9mv-2xr3 | Moderate | Spring Framework and Spring Security vulnerable to Deserialization of Untrusted Data | 2.0.7, 3.0.6 | https://osv.dev/vulnerability/GHSA-f866-m9mv-2xr3 ; https://github.com/advisories/GHSA-f866-m9mv-2xr3 |
| CVE-2014-0097 / GHSA-gv9v-c375-hvmg | High | Improper Authentication in Spring Security | 3.1.5.RELEASE, 3.2.2.RELEASE | https://osv.dev/vulnerability/GHSA-gv9v-c375-hvmg ; https://github.com/advisories/GHSA-gv9v-c375-hvmg |
| CVE-2022-22978 / GHSA-hh32-7344-cg2f | Critical | Authorization bypass in Spring Security | 5.4.11, 5.5.7, 5.6.4 | https://osv.dev/vulnerability/GHSA-hh32-7344-cg2f ; https://github.com/advisories/GHSA-hh32-7344-cg2f |
| CVE-2025-22223 / GHSA-hh3m-g4qj-4835 | Moderate | Spring Security Vulnerable to Authorization Bypass via Security Annotations | 6.4.4 | https://osv.dev/vulnerability/GHSA-hh3m-g4qj-4835 ; https://github.com/advisories/GHSA-hh3m-g4qj-4835 |
| CVE-2024-38810 / GHSA-hmqf-wpq9-jq83 | Moderate | Spring Security Missing Authorization vulnerability | 6.3.2 | https://osv.dev/vulnerability/GHSA-hmqf-wpq9-jq83 ; https://github.com/advisories/GHSA-hmqf-wpq9-jq83 |
| CVE-2022-31692 / GHSA-mmmh-wcxm-2wr4 | Critical | Spring Security authorization rules can be bypassed via forward or include dispatcher types | 5.6.9, 5.7.5 | https://osv.dev/vulnerability/GHSA-mmmh-wcxm-2wr4 ; https://github.com/advisories/GHSA-mmmh-wcxm-2wr4 |
| CVE-2024-38827 / GHSA-q3v6-hm2v-pw99 | Moderate | Spring Framework has Authorization Bypass for Case Sensitive Comparisons | 5.7.14, 5.8.16, 6.0.14, 6.1.12, 6.2.8, 6.3.5 | https://osv.dev/vulnerability/GHSA-q3v6-hm2v-pw99 ; https://github.com/advisories/GHSA-q3v6-hm2v-pw99 |
| CVE-2019-3795 / GHSA-v2r2-7qm7-jj6v | Moderate | Spring Security uses insufficiently random values | 4.2.12, 5.0.12, 5.1.5 | https://osv.dev/vulnerability/GHSA-v2r2-7qm7-jj6v ; https://github.com/advisories/GHSA-v2r2-7qm7-jj6v |
| CVE-2019-11272 / GHSA-v33x-prhc-gph5 | High | Insufficiently Protected Credentials and Improper Authentication in Spring Security | 4.2.13, 4.2.13.RELEASE | https://osv.dev/vulnerability/GHSA-v33x-prhc-gph5 ; https://github.com/advisories/GHSA-v33x-prhc-gph5 |
| CVE-2016-9879 / GHSA-v35c-49j6-q8hq | High | Security Constraint Bypass in Spring Security | 3.2.10.RELEASE, 4.1.4.RELEASE, 4.2.1.RELEASE | https://osv.dev/vulnerability/GHSA-v35c-49j6-q8hq ; https://github.com/advisories/GHSA-v35c-49j6-q8hq |
| CVE-2018-1199 / GHSA-v596-fwhq-8x48 | Moderate | Improper Input Validation in org.springframework.security:spring-security-core, org.springframework.security:spring-security-core , and org.springframework:spring-core | 4.1.5, 4.2.4, 4.3.14, 5.0.1, 5.0.3 | https://osv.dev/vulnerability/GHSA-v596-fwhq-8x48 ; https://github.com/advisories/GHSA-v596-fwhq-8x48 |
| CVE-2017-4995 / GHSA-vhrg-v3cv-p247 | High | Deserialization of Untrusted Data in Spring Security | 4.2.3.RELEASE, 5.0.0.M2 | https://osv.dev/vulnerability/GHSA-vhrg-v3cv-p247 ; https://github.com/advisories/GHSA-vhrg-v3cv-p247 |
| CVE-2025-22234 / GHSA-vqxh-445g-37fc | Moderate | Spring Security has a broken timing attack mitigation implemented in DaoAuthenticationProvide | 6.3.9, 6.4.5 | https://osv.dev/vulnerability/GHSA-vqxh-445g-37fc ; https://github.com/advisories/GHSA-vqxh-445g-37fc |
| CVE-2026-22746 / GHSA-vxf7-qj7q-83fh | Low | Spring Security Vulnerable to User Attribute Enumeration when Using DaoAuthenticationProvider | 6.5.10, 7.0.5 | https://osv.dev/vulnerability/GHSA-vxf7-qj7q-83fh ; https://github.com/advisories/GHSA-vxf7-qj7q-83fh |
| CVE-2024-22234 / GHSA-w3w6-26f2-p474 | High | Broken Access Control in Spring Security With Direct Use of isFullyAuthenticated | 6.1.7, 6.2.2 | https://osv.dev/vulnerability/GHSA-w3w6-26f2-p474 ; https://github.com/advisories/GHSA-w3w6-26f2-p474 |
| CVE-2021-22119 / GHSA-w9jg-gvgr-354m | High | Resource Exhaustion in Spring Security | 5.2.11, 5.3.10, 5.4.7, 5.5.1 | https://osv.dev/vulnerability/GHSA-w9jg-gvgr-354m ; https://github.com/advisories/GHSA-w9jg-gvgr-354m |
| CVE-2014-3527 / GHSA-wmv4-5w76-vp9g | Critical | Authorization Bypass in Spring Security | 3.1.7, 3.2.5 | https://osv.dev/vulnerability/GHSA-wmv4-5w76-vp9g ; https://github.com/advisories/GHSA-wmv4-5w76-vp9g |
| CVE-2022-22976 / GHSA-wx54-3278-m5g4 | Moderate | Integer overflow in BCrypt class in Spring Security | 5.5.7, 5.6.4 | https://osv.dev/vulnerability/GHSA-wx54-3278-m5g4 ; https://github.com/advisories/GHSA-wx54-3278-m5g4 |
| CVE-2026-22751 / GHSA-x2wq-9x2f-fhj7 | Moderate | Spring Security Core has a TOCTOU race condition when One-Time Token login with JdbcOneTimeTokenService is configured | 6.5.10, 7.0.5 | https://osv.dev/vulnerability/GHSA-x2wq-9x2f-fhj7 ; https://github.com/advisories/GHSA-x2wq-9x2f-fhj7 |
| CVE-2023-20862 / GHSA-x873-6rgc-94jc | Moderate | Spring Security logout not clearing security context | 5.7.8, 5.8.3, 6.0.3 | https://osv.dev/vulnerability/GHSA-x873-6rgc-94jc ; https://github.com/advisories/GHSA-x873-6rgc-94jc |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.springframework.security%3Aspring-security-core*

## Security Posture Notes

- The public advisory history is concentrated around **authorization and authentication boundaries**: request matching, path normalization, dispatcher-type handling, method-security annotation detection, private methods, generic super types, and erroneous authentication decisions.
- Several records are highly configuration-dependent. Examples include `RegexRequestMatcher` patterns, method-security modes, SAML / OAuth / CAS integrations, LDAP authorities population, X.509 or one-time-token flows, and applications that directly use helper methods such as `isFullyAuthenticated`.
- The cryptographic / token-generation records are older but still useful for legacy inventory review: public advisories cover insufficient randomness, broken timing-attack mitigation, BCrypt integer overflow behavior, and SAML signature-wrapping boundaries.
- Newer advisories in this package family continue to land across maintained `6.x` / `7.x` lines, so downstream review should pin to a supported Spring Security maintenance line and apply the fixed release for that line rather than relying only on a package-level "latest" value.
- Maven Central metadata saved in this pass listed `7.1.0-RC1` as the latest/release artifact for `spring-security-core`; production consumers should prefer supported stable Spring Security maintenance releases and the relevant public advisory fixed version.

## Dependencies of Note

- `spring-security-core` is the shared foundation for adjacent Spring Security modules such as `spring-security-web`, `spring-security-config`, OAuth / SAML support, and framework integrations. Application reachability depends on enabled authentication mechanisms, security DSL configuration, and whether method security is in use.
- This page tracks package-scoped public advisories only; it does not imply every application using the artifact exposes every listed behavior.

## Open Questions

- Should the KB add cross-page Spring Security guidance that groups `spring-security-core`, `spring-security-web`, and `spring-security-config` advisories by request-matcher, method-security, and authentication-integration themes?
- Which Spring Boot starter trains still pin affected `spring-security-core` ranges after the listed fixed releases?
- Should `spring-security-oauth2-*` and `spring-security-saml2-*` receive separate package-level pages for integration-specific advisories surfaced through the Spring Security advisory set?

## Related Pages

- [[maven/org.springframework.security/spring-security-web]]
- [[maven/org.springframework.security/spring-security-config]]
- [[maven/org.springframework/spring-core]]
- [[maven/index]]

---
*Last updated: 2026-05-11 | Sources: 31 (OSV.dev package query and individual vulnerability records, GitHub Advisory Database public aliases, Spring security advisory links surfaced by OSV, public CVE/NVD records, Maven Central metadata, plus a successful local proxy drafting pass used only as a synthesis aid)*
