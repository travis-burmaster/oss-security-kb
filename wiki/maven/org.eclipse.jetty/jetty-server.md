# org.eclipse.jetty:jetty-server (Maven)

**Registry:** Maven Central  
**Weekly Downloads:** unknown (as of 2026-05-12)  
**Repository:** https://github.com/jetty/jetty.project  
**Security Contact:** security@jetty.org  
**Disclosure Policy:** https://github.com/jetty/jetty.project/security/policy  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-12 | OpenClaw recurring review | public advisory mapping for the Jetty server artifact | public-source curation (OSV.dev package query and individual vulnerability records, GitHub Advisory Database records surfaced through OSV, public CVE records, upstream Jetty `SECURITY.md`, Maven Central metadata, local Claude-compatible proxy draft assist) | Added initial Maven page mapping 26 public `jetty-server` advisories across HTTP request-smuggling / parser-boundary bugs, resource-exhaustion DoS, information disclosure, response/error-page XSS, session/logout behavior, cookie parsing, and gzip/TLS handling through the 12.0.32 / 12.1.6 fix train. | https://osv.dev/list?ecosystem=Maven&q=org.eclipse.jetty%3Ajetty-server |
| *No public proactive source-code audit on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

This table is a package-level public advisory map from OSV.dev / GitHub Advisory Database for `org.eclipse.jetty:jetty-server`, cross-checked against public CVE references where available.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2006-6969 / GHSA-jg2x-r643-w2ch | MODERATE | Jetty Uses Predictable Session Identifiers | 4.2.27, 5.1.12, 6.0.2, 6.1.0pre3 | https://osv.dev/vulnerability/GHSA-jg2x-r643-w2ch ; https://github.com/advisories/GHSA-jg2x-r643-w2ch ; https://www.cve.org/CVERecord?id=CVE-2006-6969 |
| CVE-2011-4461 / GHSA-qxp4-27vx-xmm3 | MODERATE | Improper Input Validation in Jetty | 8.1.0.RC4 | https://osv.dev/vulnerability/GHSA-qxp4-27vx-xmm3 ; https://github.com/advisories/GHSA-qxp4-27vx-xmm3 ; https://www.cve.org/CVERecord?id=CVE-2011-4461 |
| CVE-2015-2080 / GHSA-ghgj-3xqr-6jfm | HIGH | Jetty vulnerable to exposure of sensitive information to unauthenticated remote users | 9.2.9.v20150224 | https://osv.dev/vulnerability/GHSA-ghgj-3xqr-6jfm ; https://github.com/advisories/GHSA-ghgj-3xqr-6jfm ; https://www.cve.org/CVERecord?id=CVE-2015-2080 |
| CVE-2016-4800 / GHSA-872g-2h8h-362q | CRITICAL | Jetty contains an alias issue that could allow unauthenticated remote code execution due to specially crafted request | 9.3.9 | https://osv.dev/vulnerability/GHSA-872g-2h8h-362q ; https://github.com/advisories/GHSA-872g-2h8h-362q ; https://www.cve.org/CVERecord?id=CVE-2016-4800 |
| CVE-2017-7656 / GHSA-84q7-p226-4x5w | HIGH | Jetty vulnerable to cache poisoning due to inconsistent HTTP request handling (HTTP Request Smuggling) | 9.3.24.v20180605, 9.4.11.v20180605 | https://osv.dev/vulnerability/GHSA-84q7-p226-4x5w ; https://github.com/advisories/GHSA-84q7-p226-4x5w ; https://www.cve.org/CVERecord?id=CVE-2017-7656 |
| CVE-2017-7657 / GHSA-vgg8-72f2-qm23 | CRITICAL | Critical severity vulnerability that affects org.eclipse.jetty:jetty-server | 9.2.25.v20180606, 9.3.24.v20180605 | https://osv.dev/vulnerability/GHSA-vgg8-72f2-qm23 ; https://github.com/advisories/GHSA-vgg8-72f2-qm23 ; https://www.cve.org/CVERecord?id=CVE-2017-7657 |
| CVE-2017-7658 / GHSA-6x9x-8qw9-9pp6 | CRITICAL | Jetty vulnerable to authorization bypass due to inconsistent HTTP request handling (HTTP Request Smuggling) | 9.2.25.v20180606, 9.3.24.v20180605, 9.4.11.v20180605 | https://osv.dev/vulnerability/GHSA-6x9x-8qw9-9pp6 ; https://github.com/advisories/GHSA-6x9x-8qw9-9pp6 ; https://www.cve.org/CVERecord?id=CVE-2017-7658 |
| CVE-2017-9735 / GHSA-wfcc-pff6-rgc5 | HIGH | Jetty vulnerable to exposure of sensitive information due to observable discrepancy | 9.2.22.v20170606, 9.3.20.v20170531, 9.4.6.v20170531 | https://osv.dev/vulnerability/GHSA-wfcc-pff6-rgc5 ; https://github.com/advisories/GHSA-wfcc-pff6-rgc5 ; https://www.cve.org/CVERecord?id=CVE-2017-9735 |
| CVE-2018-12536 / GHSA-9rgv-h7x4-qw8g | MODERATE | Eclipse Jetty Server generates error message containing sensitive information | 9.3.24.v20180605, 9.4.11.v20180605 | https://osv.dev/vulnerability/GHSA-9rgv-h7x4-qw8g ; https://github.com/advisories/GHSA-9rgv-h7x4-qw8g ; https://www.cve.org/CVERecord?id=CVE-2018-12536 |
| CVE-2018-12538 / GHSA-mwcx-532g-8pq3 | HIGH | Access and integrity issue within Eclipse Jetty | 9.4.11.v20180605 | https://osv.dev/vulnerability/GHSA-mwcx-532g-8pq3 ; https://github.com/advisories/GHSA-mwcx-532g-8pq3 ; https://www.cve.org/CVERecord?id=CVE-2018-12538 |
| CVE-2018-12545 / GHSA-h2f4-v4c4-6wx4 | HIGH | Uncontrolled Resource Consumption in org.eclipse.jetty:jetty-server | 9.3.25.v20180904, 9.4.12.v20180830 | https://osv.dev/vulnerability/GHSA-h2f4-v4c4-6wx4 ; https://github.com/advisories/GHSA-h2f4-v4c4-6wx4 ; https://www.cve.org/CVERecord?id=CVE-2018-12545 |
| CVE-2019-10241 / GHSA-7vx9-xjhr-rw6h | MODERATE | Cross-site Scripting in Eclipse Jetty | 9.2.27.v20190403, 9.3.26.v20190403, 9.4.16.v20190411 | https://osv.dev/vulnerability/GHSA-7vx9-xjhr-rw6h ; https://github.com/advisories/GHSA-7vx9-xjhr-rw6h ; https://www.cve.org/CVERecord?id=CVE-2019-10241 |
| CVE-2019-10246 / GHSA-r28m-g6j9-r2h5 | MODERATE | Information Exposure vulnerability in Eclipse Jetty | 9.2.28.v20190418, 9.3.27.v20190418, 9.4.17.v20190418 | https://osv.dev/vulnerability/GHSA-r28m-g6j9-r2h5 ; https://github.com/advisories/GHSA-r28m-g6j9-r2h5 ; https://www.cve.org/CVERecord?id=CVE-2019-10246 |
| CVE-2019-10247 / GHSA-xc67-hjx6-cgg6 | MODERATE | Installation information leak in Eclipse Jetty | 9.2.28.v20190418, 9.3.27.v20190418, 9.4.17.v20190418 | https://osv.dev/vulnerability/GHSA-xc67-hjx6-cgg6 ; https://github.com/advisories/GHSA-xc67-hjx6-cgg6 ; https://www.cve.org/CVERecord?id=CVE-2019-10247 |
| CVE-2019-17632 / GHSA-5h9j-q6j2-253f | MODERATE | Unescaped exception messages in error responses in Jetty | 9.4.24.v20191120 | https://osv.dev/vulnerability/GHSA-5h9j-q6j2-253f ; https://github.com/advisories/GHSA-5h9j-q6j2-253f ; https://www.cve.org/CVERecord?id=CVE-2019-17632 |
| CVE-2019-17638 / GHSA-x3rh-m7vp-35f2 | CRITICAL | Operation on a Resource after Expiration or Release in Jetty Server | 9.4.30.v20200611 | https://osv.dev/vulnerability/GHSA-x3rh-m7vp-35f2 ; https://github.com/advisories/GHSA-x3rh-m7vp-35f2 ; https://www.cve.org/CVERecord?id=CVE-2019-17638 |
| CVE-2020-27218 / GHSA-86wm-rrjm-8wh8 | MODERATE | Buffer not correctly recycled in Gzip Request inflation | 9.4.35.v20201120 | https://osv.dev/vulnerability/GHSA-86wm-rrjm-8wh8 ; https://github.com/advisories/GHSA-86wm-rrjm-8wh8 ; https://www.cve.org/CVERecord?id=CVE-2020-27218 |
| CVE-2020-27223 / GHSA-m394-8rww-3jr7 | MODERATE | DOS vulnerability for Quoted Quality CSV headers | 10.0.1, 11.0.1, 9.4.37 | https://osv.dev/vulnerability/GHSA-m394-8rww-3jr7 ; https://github.com/advisories/GHSA-m394-8rww-3jr7 ; https://www.cve.org/CVERecord?id=CVE-2020-27223 |
| CVE-2021-28165 / GHSA-26vr-8j45-3r4w | HIGH | Jetty vulnerable to incorrect handling of invalid large TLS frame, exhausting CPU resources | 10.0.2, 11.0.2, 9.4.39 | https://osv.dev/vulnerability/GHSA-26vr-8j45-3r4w ; https://github.com/advisories/GHSA-26vr-8j45-3r4w ; https://www.cve.org/CVERecord?id=CVE-2021-28165 |
| CVE-2021-34428 / GHSA-m6cp-vxjx-65j6 | LOW | SessionListener can prevent a session from being invalidated breaking logout | 10.0.3, 11.0.3, 9.4.41 | https://osv.dev/vulnerability/GHSA-m6cp-vxjx-65j6 ; https://github.com/advisories/GHSA-m6cp-vxjx-65j6 ; https://www.cve.org/CVERecord?id=CVE-2021-34428 |
| CVE-2022-2191 / GHSA-8mpp-f3f7-xc28 | HIGH | Jetty SslConnection does not release pooled ByteBuffers in case of errors | 10.0.10, 11.0.10 | https://osv.dev/vulnerability/GHSA-8mpp-f3f7-xc28 ; https://github.com/advisories/GHSA-8mpp-f3f7-xc28 ; https://www.cve.org/CVERecord?id=CVE-2022-2191 |
| CVE-2023-26048 / GHSA-qw69-rqj8-6qw8 | MODERATE | OutOfMemoryError for large multipart without filename in Eclipse Jetty | 10.0.14, 11.0.14, 9.4.51.v20230217 | https://osv.dev/vulnerability/GHSA-qw69-rqj8-6qw8 ; https://github.com/advisories/GHSA-qw69-rqj8-6qw8 ; https://www.cve.org/CVERecord?id=CVE-2023-26048 |
| CVE-2023-26049 / GHSA-p26g-97m4-6q7c | LOW | Eclipse Jetty's cookie parsing of quoted values can exfiltrate values from other cookies | 10.0.14, 11.0.14, 12.0.0.beta0, 9.4.51.v20230217 | https://osv.dev/vulnerability/GHSA-p26g-97m4-6q7c ; https://github.com/advisories/GHSA-p26g-97m4-6q7c ; https://www.cve.org/CVERecord?id=CVE-2023-26049 |
| CVE-2024-13009 / GHSA-q4rv-gq96-w7c5 | HIGH | **UNSUPPORTED WHEN ASSIGNED** GzipHandler causes part of request body to be seen as request body of a separate request | 9.4.57.v20241219 | https://osv.dev/vulnerability/GHSA-q4rv-gq96-w7c5 ; https://github.com/advisories/GHSA-q4rv-gq96-w7c5 ; https://www.cve.org/CVERecord?id=CVE-2024-13009 |
| CVE-2024-8184 / GHSA-g8m5-722r-8whq | MODERATE | Eclipse Jetty's ThreadLimitHandler.getRemote() vulnerable to remote DoS attacks | 10.0.24, 11.0.24, 12.0.9, 9.4.56 | https://osv.dev/vulnerability/GHSA-g8m5-722r-8whq ; https://github.com/advisories/GHSA-g8m5-722r-8whq ; https://www.cve.org/CVERecord?id=CVE-2024-8184 |
| CVE-2026-1605 / GHSA-xxh7-fcf3-rj7f | HIGH | The Eclipse Jetty Server Artifact has a Gzip request memory leak  | 12.0.32, 12.1.6 | https://osv.dev/vulnerability/GHSA-xxh7-fcf3-rj7f ; https://github.com/advisories/GHSA-xxh7-fcf3-rj7f ; https://www.cve.org/CVERecord?id=CVE-2026-1605 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.eclipse.jetty%3Ajetty-server*

## Security Posture Notes

- `jetty-server` is a high-value Java HTTP server surface: request parsing, connection handling, gzip/TLS handling, multipart processing, session behavior, cookie parsing, and error responses all appear in the public advisory history.
- Request-smuggling / inconsistent-request-handling appears as a recurring theme in the Jetty server records, especially the 2017 advisory cluster and the later `CVE-2024-13009` GzipHandler request-body boundary issue.
- Resource-exhaustion DoS is the densest theme in this pass: public records cover TLS frame CPU exhaustion, SslConnection buffer release, multipart memory exhaustion, ThreadLimitHandler remote-address handling, header parsing, gzip request handling, and the 2026 gzip request memory leak.
- Several older records are information-disclosure or response-generation bugs, including installation / system-path exposure and unescaped exception messages in error responses. Treat default error pages and deployment metadata as sensitive in exposed Jetty deployments.
- Jetty has a mature public disclosure posture: upstream directs security reports to `security@jetty.org`, uses private GitHub security advisories during handling, coordinates CVE assignment through Eclipse, and states that active Jetty versions are supported for security issues.
- Maven Central metadata showed `12.1.9` as the latest / release version during this review, while OSV records in scope list recent fixed versions through `12.0.32` and `12.1.6`.

## Dependencies of Note

- Jetty deployments commonly involve adjacent Jetty modules (`jetty-http`, `jetty-io`, `jetty-util`, servlet / HTTP2 modules) and reverse proxies. Future reviews should map co-affected Jetty artifacts rather than assuming every server vulnerability is isolated to this artifact.
- Pages for `io.netty:netty-codec-http`, `org.springframework:spring-webflux`, `org.springframework:spring-webmvc`, and `org.apache.tomcat.embed:tomcat-embed-core` are useful comparison points for HTTP parser, request-boundary, and embedded-server risk.

## Open Questions

- Which Jetty major lines should the KB highlight as practical remediation baselines for teams still on 9.4.x, 10.x, 11.x, or 12.x?
- Should future passes split Jetty HTTP/2, servlet, utility, and server-core advisories into separate artifact pages to avoid over- or under-attributing transitive exposure?
- Are there public downstream postmortems or maintainer release notes that clarify real-world reachability for the newer gzip and ThreadLimitHandler DoS records?

## Related Pages

- [[maven/io.netty/netty-codec-http]]
- [[maven/org.apache.tomcat.embed/tomcat-embed-core]]
- [[maven/org.springframework/spring-webflux]]
- [[maven/org.springframework/spring-webmvc]]
- [[maven/index]]

---
*Last updated: 2026-05-12 | Sources: 30 (OSV package query and individual vulnerability records for `org.eclipse.jetty:jetty-server`; GitHub Advisory Database records surfaced through OSV; public CVE records; upstream Jetty `SECURITY.md`; Maven Central metadata; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid)*
