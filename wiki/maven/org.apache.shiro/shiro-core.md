# Apache Shiro / shiro-core (Maven)

**Registry:** Maven Central
**Weekly Downloads:** unknown (Maven Central stats API unavailable in this environment)
**Repository:** https://github.com/apache/shiro
**Security Contact:** security@apache.org
**Disclosure Policy:** https://shiro.apache.org/security-reports.html
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|---------|
| *No public proactive source-code audits on record.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|---------|
| CVE-2016-4437 / GHSA-p836-389h-j692 | **Critical CVSS 9.8** | Missing or default AES cipher key for the "remember me" cookie enables remote attackers to forge deserialization payloads — executing arbitrary code or bypassing access restrictions entirely. The built-in default key (if left unchanged) is publicly known, making all default-configured deployments directly exploitable. | 1.2.5 | [GHSA-p836-389h-j692](https://github.com/advisories/GHSA-p836-389h-j692) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-4437) |
| CVE-2020-1957 / GHSA-26gr-cvq3-qxgf | **Critical CVSS 9.8** | Authentication bypass when Shiro is deployed with Spring dynamic controllers — URL normalization differences between Shiro's path-matching and the Spring DispatcherServlet allow specially crafted requests to circumvent authentication for protected endpoints. | 1.5.2 | [GHSA-26gr-cvq3-qxgf](https://github.com/advisories/GHSA-26gr-cvq3-qxgf) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2020-1957) |
| CVE-2020-11989 / GHSA-72w9-fcj5-3fcg | **Critical CVSS 9.8** | Second Spring dynamic controller authentication bypass variant — a different crafted request path exploits URL parsing differences to reach protected routes without authentication, requiring a separate fix from CVE-2020-1957. | 1.5.3 | [GHSA-72w9-fcj5-3fcg](https://github.com/advisories/GHSA-72w9-fcj5-3fcg) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2020-11989) |
| CVE-2021-41303 / GHSA-f6jp-j6w3-w9hm | **Critical CVSS 9.8** | Authentication bypass via specially crafted HTTP request when integrated with Spring Boot — path-matching inconsistency between Shiro and the Spring DispatcherServlet allows unauthenticated access to protected routes. | 1.8.0 | [GHSA-f6jp-j6w3-w9hm](https://github.com/advisories/GHSA-f6jp-j6w3-w9hm) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-41303) |
| CVE-2022-32532 / GHSA-4cf5-xmhp-3xj7 | **Critical CVSS 9.8** | `RegexRequestMatcher` authorization bypass when regex contains `.` — on some servlet containers, newline characters (`%0a`) in the URL path are not filtered before regex matching, causing `.` to match `\n` and bypass authorization rules protecting those paths. | 1.9.1 | [GHSA-4cf5-xmhp-3xj7](https://github.com/advisories/GHSA-4cf5-xmhp-3xj7) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-32532) |
| CVE-2022-40664 / GHSA-45x9-q6vj-cqgq | **Critical CVSS 9.8** | Authentication bypass via `RequestDispatcher` — when an application uses `forward()` or `include()` for internal request dispatch, Shiro's authentication filter can be bypassed because the forwarded request is treated as already-authenticated, allowing unauthenticated access to protected resources. | 1.10.0 | [GHSA-45x9-q6vj-cqgq](https://github.com/advisories/GHSA-45x9-q6vj-cqgq) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-40664) |
| CVE-2020-13933 / GHSA-2vgm-wxr3-6w2j | **High CVSS 9.1** | Authentication bypass via specially crafted HTTP request — exploits path normalization differences in Shiro's URL-pattern matcher to access protected resources without credentials. | 1.6.0 | [GHSA-2vgm-wxr3-6w2j](https://github.com/advisories/GHSA-2vgm-wxr3-6w2j) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2020-13933) |
| CVE-2019-12422 / GHSA-r679-m633-g7wc | **High** | "Remember me" cookie is susceptible to padding oracle attack — attackers forge valid cookies to impersonate other users or decrypt cookie contents, bypassing authentication without knowing the AES key. | 1.4.2 | [GHSA-r679-m633-g7wc](https://github.com/advisories/GHSA-r679-m633-g7wc) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2019-12422) |
| CVE-2026-49268 / GHSA-x96m-rh44-vgv8 | **High** | LDAP Distinguished Name injection in `DefaultLdapRealm` — user-supplied username values are concatenated directly into LDAP DN templates without RFC 2253 character escaping, enabling attacker-controlled DN structure manipulation that may bypass authentication or assume other users' identities. | 2.2.1 / 3.0.0-alpha-2 | [GHSA-x96m-rh44-vgv8](https://github.com/advisories/GHSA-x96m-rh44-vgv8) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-49268) |
| CVE-2023-46749 / GHSA-jc7h-c423-mpjc | **Moderate** | Path traversal authentication bypass — semicolons in URL paths exploit normalization differences to reach protected endpoints without authentication when combined with certain path-rewriting configurations. The default `blockSemicolon` setting mitigates this; disabling it is the triggering condition. | 1.13.0 / 2.0.0-alpha4 | [GHSA-jc7h-c423-mpjc](https://github.com/advisories/GHSA-jc7h-c423-mpjc) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-46749) |
| CVE-2026-43827 / GHSA-fcvm-3cpj-f9qx | **Moderate** | Session fixation in default configuration — existing session is not invalidated on successful login, nor is a new session ID generated, enabling session hijacking if an attacker can pre-seed a session ID (e.g., via network position or a prior vulnerability). | 2.2.0 / 3.0.0-alpha-2 | [GHSA-fcvm-3cpj-f9qx](https://github.com/advisories/GHSA-fcvm-3cpj-f9qx) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-43827) |
| CVE-2026-23901 / GHSA-c4qc-4q9p-m9q9 | **Low** | Username enumeration via timing side-channel — distinct code paths for non-existent vs. existing users produce measurable response time differences, enabling brute-force username enumeration over a network. | 2.1.0 | [GHSA-c4qc-4q9p-m9q9](https://github.com/advisories/GHSA-c4qc-4q9p-m9q9) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-23901) |

## Security Posture Notes

- **All 12 GHSA advisories** for `org.apache.shiro:shiro-core` (2016–2026) are individually mapped on this page. This represents complete coverage of the public advisory record for this package.
- **Dominant root cause — URL path normalization mismatch with Spring (6 of 12 advisories):** CVE-2020-1957, CVE-2020-11989, CVE-2020-13933, CVE-2021-41303, CVE-2022-40664, and CVE-2023-46749 all stem from the same fundamental architecture issue: Shiro's path-matching logic and the underlying servlet container / Spring dispatcher normalize and interpret URL paths differently. An attacker crafts a URL that passes Shiro's authentication check but is routed to a protected endpoint by the application framework. This class of vulnerability required six iterative fixes across 2020–2023 (versions 1.5.2 → 1.13.0) and has not yet had a systematic root-cause resolution; applications must apply each fix and stay current.
- **"Remember me" cookie security (CVE-2016-4437, CVE-2019-12422):** The AES-encrypted "remember me" cookie has been attacked twice — first via a missing/default cipher key enabling deserialization RCE, then via a padding oracle enabling cookie forgery. Key mitigations: configure a strong, randomly generated AES-128/256 key; disable "remember me" if not operationally required; use GCM mode rather than CBC.
- **RegexRequestMatcher bypass (CVE-2022-32532):** The `.` metacharacter in Java regex matches any character, including `\n`. On servlet containers that pass unfiltered path data to Shiro, a URL containing `%0a` (URL-encoded newline) can bypass a regex-based authorization rule. Organizations using `RegexRequestMatcher` with `.` in patterns should audit their rule set and upgrade to 1.9.1+.
- **Current maintained versions:** Apache Shiro 2.x is the primary maintained line (current stable 2.2.1); 1.x is in maintenance mode for critical security fixes only. The 3.0.0-alpha series is in development. Applications on 1.x should plan migration to 2.x.
- **Security contact:** Embargoed reports to security@apache.org; public advisories published at https://shiro.apache.org/security-reports.html.

## Dependencies of Note

- **Java Servlet API / servlet container** — most auth bypass advisories involve mismatches with the container's path normalization (Tomcat, Jetty, Undertow behave differently for `%0a`, semicolons, and double-encoding). Exploitability for CVE-2022-32532 and CVE-2022-40664 is container-dependent.
- **Spring Framework / Spring Boot** — when Spring's `DispatcherServlet` routes requests, Shiro's filters may see a different URL than Spring's controllers; this mismatch is the root cause for 4+ Critical auth bypass advisories.
- **Apache Commons BeanUtils** — used in Shiro's property binding; keep BeanUtils current to avoid unrelated deserialization boundary issues.

## Open Questions

- What is the current weekly download count for shiro-core across Maven Central? (Stats API blocked in this environment.)
- Have all known Spring integration auth bypass patterns (2020–2023) been covered by a systematic path-normalization audit for current Spring Boot 3.x + Jakarta EE integration?
- What is the migration path from shiro-core 1.x to 2.x for applications currently on the maintenance line? Is a published migration guide available?

## Related Pages

- [[maven/org.springframework.security/spring-security-core]] — recommended Spring authentication framework with more Spring-native path matching
- [[maven/org.springframework/spring-web]] — Spring web whose URL routing interacts with Shiro's path matching
- [[maven/index]]

---
*Last updated: 2026-07-31 | Sources: 12 GHSA advisories (GHSA-p836-389h-j692, GHSA-26gr-cvq3-qxgf, GHSA-72w9-fcj5-3fcg, GHSA-f6jp-j6w3-w9hm, GHSA-4cf5-xmhp-3xj7, GHSA-45x9-q6vj-cqgq, GHSA-2vgm-wxr3-6w2j, GHSA-r679-m633-g7wc, GHSA-x96m-rh44-vgv8, GHSA-jc7h-c423-mpjc, GHSA-fcvm-3cpj-f9qx, GHSA-c4qc-4q9p-m9q9)*
