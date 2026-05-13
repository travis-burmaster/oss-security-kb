# org.apache.httpcomponents:httpclient (Maven)

**Registry:** Maven Central  
**Latest Version:** 4.5.14 (Maven Central search API during 2026-05-13 review)  
**Repository:** https://github.com/apache/httpcomponents-client  
**Security Contact:** Apache Security Team / HttpComponents project channels  
**Disclosure Policy:** https://hc.apache.org/security.html  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-13 | OpenClaw recurring review | package-level public advisory mapping for Maven `org.apache.httpcomponents:httpclient` | public-source curation from OSV.dev package and vulnerability records, GitHub Advisory Database aliases surfaced by OSV, public CVE records, Apache HttpComponents release / security pages, Maven Central metadata, upstream issue / commit references surfaced by public records, and local proxy-assisted drafting | Added initial Maven page mapping 6 public package-scoped advisories across TLS hostname-verification failures, proxy credential leakage, SSL-handshake timeout DoS, and malformed-URI target-host confusion through the 4.5.13 / 5.0.3 fix boundary. | https://osv.dev/list?ecosystem=Maven&q=org.apache.httpcomponents%3Ahttpclient |

## Known Vulnerabilities

This table is a package-level public advisory map for the legacy Maven coordinate `org.apache.httpcomponents:httpclient` (HttpClient 4.x). The 2020 malformed-authority advisory also had a 5.x fixed version, but the package coordinate on this page remains the 4.x artifact.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2011-1498 / GHSA-gw85-4gmf-m7rh | MODERATE | When used with an authenticating proxy server, affected HttpClient 4.x versions could send the `Proxy-Authorization` header to the origin server, exposing proxy credentials to remote web servers. | 4.1.1 | https://osv.dev/vulnerability/GHSA-gw85-4gmf-m7rh ; https://www.cve.org/CVERecord?id=CVE-2011-1498 |
| CVE-2012-6153 / GHSA-2x83-r56g-cv47 | HIGH | Hostname verification could incorrectly match certificate distinguished-name fields, allowing server spoofing / man-in-the-middle risk; public records describe this as an incomplete fix boundary from the earlier Commons HttpClient lineage. | 4.2.3 | https://osv.dev/vulnerability/GHSA-2x83-r56g-cv47 ; https://www.cve.org/CVERecord?id=CVE-2012-6153 |
| CVE-2013-4366 / GHSA-pqwh-44jj-p5rm | CRITICAL | HttpClient 4.3.0 did not ensure the `X509HostnameVerifier` was non-null, effectively disabling hostname verification by default in the affected builder path. | 4.3.1 | https://osv.dev/vulnerability/GHSA-pqwh-44jj-p5rm ; https://www.cve.org/CVERecord?id=CVE-2013-4366 |
| CVE-2014-3577 / GHSA-cfh5-3ghh-wfjx | MODERATE | Hostname verification could be bypassed by crafted certificate distinguished-name content containing a `CN=` substring in a non-CN field. | 4.3.5 | https://osv.dev/vulnerability/GHSA-cfh5-3ghh-wfjx ; https://www.cve.org/CVERecord?id=CVE-2014-3577 |
| CVE-2015-5262 / GHSA-fmj5-wv96-r2ch | MODERATE | `SSLConnectionSocketFactory` ignored `http.socket.timeout` during SSL handshakes, allowing remote HTTPS endpoints to hang callers and cause denial of service. | 4.3.6 | https://osv.dev/vulnerability/GHSA-fmj5-wv96-r2ch ; https://www.cve.org/CVERecord?id=CVE-2015-5262 |
| CVE-2020-13956 / GHSA-7r82-7xv7-xcpj | MODERATE | Malformed authority components in `java.net.URI` values could make HttpClient pick the wrong request target host, creating host-confusion / request-routing risk. | 4.5.13, 5.0.3 | https://osv.dev/vulnerability/GHSA-7r82-7xv7-xcpj ; https://www.cve.org/CVERecord?id=CVE-2020-13956 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.apache.httpcomponents%3Ahttpclient*

## Security Posture Notes

- `org.apache.httpcomponents:httpclient` is a high-blast-radius Java HTTP client because it is widely embedded directly and transitively by JVM applications, build tooling, clients, plugins, and server-side integrations.
- The public advisory history is compact but security-critical: four of the six records are transport or authority-boundary issues involving TLS hostname verification, proxy credential forwarding, or request target-host selection.
- Consumers should inventory transitive copies of the 4.x coordinate separately from the newer `org.apache.httpcomponents.client5:httpclient5` line. Maven Central reported `4.5.14` as the latest 4.x artifact during this review, while public advisory fixed versions include `4.5.13` and `5.0.3` for the 2020 host-confusion issue.
- Hostname-verification advisories in this page are historical but operationally important because many downstream projects shade, relocate, or pin HTTP clients for long periods.
- This review did not perform active vulnerability hunting, exploit validation, or live target testing. It only normalized already-public advisory, CVE, maintainer, release, and package metadata.

## Dependencies of Note

- Applications may receive this artifact transitively through older SDKs, integration frameworks, search / data clients, Maven plugins, Jenkins plugins, or vendor libraries.
- Remediation should check both direct Maven dependencies and shaded / bundled copies. The 2020 malformed-authority issue is especially relevant where applications build request URIs from semi-trusted input.
- Proxy-credential exposure risk is configuration-dependent and mainly applies to authenticating-proxy deployments on affected versions.

## Open Questions

- Which high-usage Java SDKs still pin the legacy 4.x coordinate instead of `httpclient5`?
- Should future KB maintenance add a separate page for `org.apache.httpcomponents.client5:httpclient5` to avoid mixing the 4.x and 5.x coordinates?
- Are there public downstream advisories or postmortems showing real-world reachability for the malformed-authority host-confusion issue in common frameworks?

## Related Pages

- [[maven/index]]
- [[maven/io.netty/netty-codec-http]]
- [[maven/org.apache.tomcat.embed/tomcat-embed-core]]
- [[python/requests]]
- [[python/urllib3]]
- [[npm/undici]]

---
*Last updated: 2026-05-13 | Sources: OSV package query and individual vulnerability records for `org.apache.httpcomponents:httpclient`; GitHub Advisory Database aliases surfaced by OSV; public CVE records; Apache HttpComponents release / security pages; Maven Central metadata; upstream issue / commit references surfaced by public records; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid.*
