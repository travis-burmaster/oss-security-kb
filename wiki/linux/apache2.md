# Apache HTTP Server (linux)

**Registry:** distro
**Weekly Downloads:** N/A — pre-installed or available via package manager on all major Linux distributions; one of the two most widely deployed HTTP servers globally
**Repository:** https://github.com/apache/httpd
**Security Contact:** security@apache.org
**Disclosure Policy:** https://httpd.apache.org/security_report.html
**Current Status:** advisory-mapped

## Audit History

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|---------|
| CVE-2017-3167 | Critical CVSS 9.8 | `ap_get_basic_auth_pw()` misuse: third-party modules calling this function outside the authentication phase may bypass authentication requirements entirely | 2.2.33 / 2.4.26 | [GHSA-9mgw-4qp5-wrrj](https://github.com/advisories/GHSA-9mgw-4qp5-wrrj) |
| CVE-2019-0211 | High CVSS 7.8 | Local privilege escalation via MPM scoreboard shared memory: child processes/threads (running with reduced privileges) can corrupt the scoreboard to execute arbitrary code as the parent process (root); affects MPM event, worker, and prefork | 2.4.39 | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2019-0211) |
| CVE-2021-40438 | Critical CVSS 9.0 | mod_proxy SSRF: a crafted uri-path causes mod_proxy to forward requests to an attacker-controlled origin server; CISA Known Exploited Vulnerabilities catalog | 2.4.49 | [GHSA-rwxq-58vm-3v2j](https://github.com/advisories/GHSA-rwxq-58vm-3v2j) |
| CVE-2021-41773 | High CVSS 7.5 | Path normalisation flaw (2.4.49 only): maps URLs outside the document root; with CGI enabled enables unauthenticated RCE; actively exploited in the wild before patch; incomplete fix — see CVE-2021-42013 | 2.4.50 (incomplete) | [GHSA-29h7-gr57-5f8r](https://github.com/advisories/GHSA-29h7-gr57-5f8r) |
| CVE-2021-42013 | Critical CVSS 9.8 | Incomplete fix for CVE-2021-41773: alternate URL encoding restores path traversal in 2.4.50; CGI-enabled configurations allow unauthenticated RCE; CISA KEV listed | 2.4.51 | [GHSA-m24x-wx9p-jqmh](https://github.com/advisories/GHSA-m24x-wx9p-jqmh) |
| CVE-2022-22720 | Critical CVSS 9.8 | HTTP/1.1 request smuggling: server fails to close inbound connection when errors are encountered discarding the request body; enables smuggling to backend applications | 2.4.53 | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-22720) |
| CVE-2022-36760 | Critical CVSS 9.8 | mod_proxy_ajp HTTP Request Smuggling: an attacker can smuggle requests through to an AJP-connected backend; requires mod_proxy_ajp to be active | 2.4.55 | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-36760) |
| CVE-2023-25690 | Critical CVSS 9.8 | mod_proxy HTTP Request Smuggling via certain RewriteRule or ProxyPassMatch patterns that improperly process user-supplied request-target values; can bypass access controls and poison caches | 2.4.56 | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-25690) |
| CVE-2024-38474 | Critical CVSS 9.8 | mod_rewrite substitution encoding flaw: unsafe RewriteRule capture-group substitution allows scripts not directly URL-reachable to be executed, and may disclose CGI script source code | 2.4.60 | [GHSA-x6g9-g4wf-qrf7](https://github.com/advisories/GHSA-x6g9-g4wf-qrf7) |
| CVE-2024-38475 | Critical CVSS 9.1 | mod_rewrite improper output escaping: URLs mapped to filesystem locations intended for serving but not directly reachable via URL; may enable code execution or source disclosure | 2.4.60 | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-38475) |
| CVE-2024-38476 | Critical CVSS 9.8 | mod_proxy info disclosure / SSRF via malicious backend response headers: a controlled backend can embed instructions causing mod_proxy to disclose information, perform SSRF, or execute local scripts | 2.4.60 | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-38476) |

## Security Posture Notes

Apache HTTP Server is one of the two most widely deployed HTTP servers globally and is present in virtually all Linux distributions. The project operates a mature coordinated disclosure process via security@apache.org with a full version history of security advisories at httpd.apache.org/security/. The 2.4.x line is the only maintained series; 2.2.x is EOL.

A recurring vulnerability pattern exists in mod_proxy (CVE-2021-40438, CVE-2022-36760, CVE-2023-25690, CVE-2024-38476) and mod_rewrite (CVE-2024-38474, CVE-2024-38475), making these modules high-risk attack surfaces in any proxy-forward configuration. The CVE-2021-41773 / CVE-2021-42013 pair was one of the most widely exploited web server vulnerabilities in recent years, driving CISA emergency directives; the fact that the first fix was incomplete and the 2.4.50 "fix" was almost immediately bypassed illustrates the difficulty of path-normalisation correctness.

Total public advisories for 2.4.x: 50+ across the series. This pass maps 11 representative entries with CVSS ≥ 7.0.

## Dependencies of Note

- **OpenSSL / mod_ssl**: TLS exposure is tied to the installed OpenSSL version; see [[linux/openssl]].
- **mod_proxy_ajp + Tomcat**: mod_proxy_ajp enables request-smuggling attacks against AJP-connected Tomcat backends when enabled; see [[maven/org.apache.tomcat.embed/tomcat-embed-core]].
- **CGI scripts**: CGI-enabled directories dramatically increase impact of path traversal and mod_rewrite bugs (CVE-2021-41773, CVE-2021-42013, CVE-2024-38474).

## Open Questions

- Map remaining 39+ high/critical CVEs from the 2.4.x advisory archive; notable gaps include CVE-2022-22721 (2.4.53 batch buffer overflow), CVE-2017-7679 (mod_mime buffer overread), and CVE-2017-9788 (mod_auth_digest memory problems).
- Assess distro-specific patch lag for Debian stable, RHEL 9, and Ubuntu LTS relative to upstream 2.4.60.
- Confirm whether CVE-2021-40438 SSRF remains exploitable via configuration workarounds in versions where 2.4.49 is not available for upgrade.

## Related Pages

- [[linux/nginx]]
- [[linux/openssl]]
- [[maven/org.apache.tomcat.embed/tomcat-embed-core]]
- [[linux/index]]

---
*Last updated: 2026-08-08 | Sources: 11*
