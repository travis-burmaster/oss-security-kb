# org.apache.httpcomponents.client5:httpclient5 (Maven)

**Registry:** Maven Central  
**Latest Version:** 5.6.1 (Maven Central search API during 2026-05-14 review)  
**Repository:** https://github.com/apache/httpcomponents-client  
**Security Contact:** Apache Security Team / HttpComponents project channels  
**Disclosure Policy:** https://hc.apache.org/security.html  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-14 | OpenClaw recurring review | package-level public advisory mapping for Maven `org.apache.httpcomponents.client5:httpclient5` | public-source curation from OSV.dev package and vulnerability records, GitHub Advisory Database aliases surfaced through OSV, public CVE / NVD records, Apache mailing-list and oss-security advisories, upstream PR / commit references, Maven Central metadata, Apache HttpComponents security material, and local proxy-assisted drafting | Added initial HttpClient 5.x coordinate page covering two public advisories: disabled domain / hostname checks in the 5.4 line fixed in 5.4.3 and SCRAM-SHA-256 mutual-authentication verification in the 5.6 line fixed in 5.6.1. | https://osv.dev/list?ecosystem=Maven&q=org.apache.httpcomponents.client5%3Ahttpclient5 |

## Known Vulnerabilities

This page tracks the Maven coordinate `org.apache.httpcomponents.client5:httpclient5` (Apache HttpClient 5.x). The older `org.apache.httpcomponents:httpclient` 4.x coordinate is tracked separately.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-27820 / GHSA-73m2-qfq3-56cx | HIGH | Public advisory records describe a regression in which Apache HttpClient could disable domain / hostname checks for affected 5.4-line releases, undermining TLS endpoint identity verification. OSV lists the affected range as `5.4-alpha1` through versions before `5.4.3`. | 5.4.3 | https://osv.dev/vulnerability/GHSA-73m2-qfq3-56cx ; https://nvd.nist.gov/vuln/detail/CVE-2025-27820 ; https://lists.apache.org/thread/55xhs40ncqv97qvoocok44995xp5kqn8 ; https://github.com/apache/httpcomponents-client/pull/574 ; https://github.com/apache/httpcomponents-client/pull/621 |
| CVE-2026-40542 / GHSA-v468-qcjx-r72w | MODERATE | Public Apache / GHSA records state that HttpClient accepted SCRAM-SHA-256 authentication without proper mutual-authentication verification in the affected 5.6 line. OSV lists the affected range as `5.6-alpha1` through versions before `5.6.1`. | 5.6.1 | https://osv.dev/vulnerability/GHSA-v468-qcjx-r72w ; https://nvd.nist.gov/vuln/detail/CVE-2026-40542 ; https://lists.apache.org/thread/tfmgv86xr0z1y096vs3z0y315t1v3o97 ; http://www.openwall.com/lists/oss-security/2026/04/22/5 ; https://github.com/apache/httpcomponents-client/commit/726eac2323d370435d8afca1e0540aa099927f18 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.apache.httpcomponents.client5%3Ahttpclient5*

## Security Posture Notes

- `httpclient5` is a high-blast-radius Java HTTP client used directly and transitively by JVM applications, SDKs, build tooling, integrations, and server-side services.
- The public advisory footprint for the 5.x coordinate is currently compact but security-sensitive: both records involve trust-boundary behavior in TLS endpoint identity or authentication negotiation.
- Published affected ranges are narrow and line-specific. `CVE-2025-27820` is tied to the 5.4 line before `5.4.3`; `CVE-2026-40542` is tied to the 5.6 line before `5.6.1`. This page does not extend those ranges beyond OSV / Apache / public advisory data.
- Consumers should inventory 4.x and 5.x HttpClient coordinates separately. The 4.x coordinate has distinct historical TLS, proxy, and URI host-confusion advisories and is tracked at [[maven/org.apache.httpcomponents/httpclient]].
- This review did not perform active vulnerability hunting, exploit validation, or live target testing. It only normalized already-public advisory, CVE, maintainer, release, and package metadata.

## Dependencies of Note

- Remediation should check direct Maven dependencies, dependency-management overrides, shaded JARs, and embedded vendor copies.
- TLS hostname-verification and authentication-negotiation issues are especially relevant for applications that connect to semi-trusted hosts, use corporate proxies, or rely on mutual authentication semantics.

## Open Questions

- Which high-usage Java SDKs have already adopted the 5.x coordinate and are exposed to the narrow 5.4 / 5.6 affected windows?
- Should future KB maintenance add a shared Java HTTP-client comparison note covering Apache HttpClient 4.x, HttpClient 5.x, Jetty client/server, Netty codecs, and JDK HTTP Client parser / TLS boundaries?

## Related Pages

- [[maven/org.apache.httpcomponents/httpclient]]
- [[maven/io.netty/netty-codec-http]]
- [[maven/org.eclipse.jetty/jetty-server]]
- [[maven/org.apache.tomcat.embed/tomcat-embed-core]]
- [[maven/index]]

---
*Last updated: 2026-05-14 | Sources: OSV package query and individual vulnerability records for `org.apache.httpcomponents.client5:httpclient5`; GitHub Advisory Database aliases surfaced through OSV; public CVE / NVD records for CVE-2025-27820 and CVE-2026-40542; Apache mailing-list advisory threads; oss-security posting for CVE-2026-40542; upstream PR / commit references; Maven Central metadata; Apache HttpComponents security material; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid.*
