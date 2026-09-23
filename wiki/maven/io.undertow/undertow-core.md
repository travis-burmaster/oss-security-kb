# undertow-core (Maven / Java)

**Registry:** Maven Central (`io.undertow:undertow-core`)
**Weekly Downloads:** unknown (Maven Central does not publish granular download statistics)
**Repository:** https://github.com/undertow-io/undertow
**Security Contact:** Red Hat Product Security — secalert@redhat.com / https://access.redhat.com/security/
**Disclosure Policy:** https://access.redhat.com/security/team/contact/
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-h6p6-fc4w-cqhx / CVE-2014-7816 | Moderate | Windows path traversal via `..` sequences in resource URIs. CWE-22. | 1.0.17 / 1.1.0.CR5 / 1.2.0.Beta3 | [GHSA](https://github.com/advisories/GHSA-h6p6-fc4w-cqhx) |
| GHSA-3f57-w2rp-72fc / CVE-2016-7046 | Moderate (CVSS 7.5) | Long URL forwarded via proxy triggers `BufferOverflowException` → DoS. CWE-248. | 1.3.25.Final / 1.4.3.Final | [GHSA](https://github.com/advisories/GHSA-3f57-w2rp-72fc) |
| GHSA-3x7h-5hfr-hvjm / CVE-2017-2670 | High (CVSS 7.5) | WebSocket infinite loop on non-clean TCP close — unauthenticated pre-auth DoS. CWE-835. | 1.3.28 | [GHSA](https://github.com/advisories/GHSA-3x7h-5hfr-hvjm) |
| GHSA-5gg7-5wv8-4gcj / CVE-2017-12165 | High (CVSS 7.5) | HTTP request smuggling via unusual whitespace in transfer-encoding headers. CWE-444. | 1.3.31 / 1.4.17 / 2.0.0.Beta1 | [GHSA](https://github.com/advisories/GHSA-5gg7-5wv8-4gcj) |
| GHSA-cccf-7xw3-p2vr / CVE-2020-10719 | Moderate (CVSS 5.8) | HTTP request smuggling via chunked encoding with large chunk sizes. CWE-444. | 2.1.1.Final | [GHSA](https://github.com/advisories/GHSA-cccf-7xw3-p2vr) |
| GHSA-fj7c-vg2v-ccrm / CVE-2021-3690 | High (CVSS 7.5) | WebSocket PONG buffer accumulation → heap memory exhaustion DoS. | 2.0.40 / 2.2.10 | [GHSA](https://github.com/advisories/GHSA-fj7c-vg2v-ccrm) |
| GHSA-339q-62wm-c39w / CVE-2021-3859 | High (CVSS 7.5) | HTTP/2 invocation timeout handling causes server-side DoS. | 2.2.15.Final | [GHSA](https://github.com/advisories/GHSA-339q-62wm-c39w) |
| GHSA-m4mm-pg93-fv78 / CVE-2023-1108 | High (CVSS 7.5) | SSL/TLS handshake infinite loop in `SslConduit` — pre-auth network DoS. CWE-835. | 2.2.24.Final / 2.3.5.Final | [GHSA](https://github.com/advisories/GHSA-m4mm-pg93-fv78) |
| GHSA-3jrv-jgp8-45v3 / CVE-2023-4639 | High | Cookie parsing flaw allows `HttpOnly` cookie exfiltration or cookie value spoofing. | 2.2.31.Final / 2.3.12.Final | [GHSA](https://github.com/advisories/GHSA-3jrv-jgp8-45v3) |
| GHSA-ch7q-gpff-h9hp / CVE-2024-3653 | Moderate (CVSS 5.3) | Learning-push handler retains HTTP/2 headers in memory when `maxAge=-1` (default) — memory leak leading to DoS. CWE-401. | 2.2.34.Final / 2.3.15.Final | [GHSA](https://github.com/advisories/GHSA-ch7q-gpff-h9hp) |

*Note: GHSA-22c5-cpvr-cfvq / CVE-2024-4109 was found but is WITHDRAWN from the advisory database and is not included above. ~40 total advisories exist across the full history; this page maps 10 representative records spanning 2014–2024.*

## Security Posture Notes

`undertow-core` is the HTTP server engine powering WildFly (JBoss EAP) and is an optional embedded server in Spring Boot (via the `spring-boot-starter-undertow` artifact, replacing the default Tomcat). It is written in Java by Red Hat and maintained under the `undertow-io` GitHub organization.

**Recurring DoS pattern.** Four advisories (CVE-2017-2670, CVE-2021-3690, CVE-2021-3859, CVE-2023-1108) share the pattern of a network-reachable infinite loop or resource accumulation triggered without authentication — a sustained weakness in event-loop and conduit handling across WebSocket, HTTP/2, and TLS layers. All are pre-auth, All-CVSS-AV:N, and all were rated High (CVSS 7.5). The 2023 SSL handshake loop (CVE-2023-1108) and the 2017 WebSocket loop (CVE-2017-2670) share the same root class (CWE-835).

**HTTP request smuggling.** Two advisories (CVE-2017-12165, CVE-2020-10719) reflect weaknesses in HTTP/1.1 parsing boundary enforcement — whitespace in transfer-encoding headers and oversized chunk values respectively. Both are CWE-444 and enabled proxy-assisted request smuggling against back-end Undertow instances.

**Cookie boundary flaw.** CVE-2023-4639 affects cookie parsing and enables `HttpOnly` exfiltration or value spoofing. Red Hat assigned the fixed versions 2.2.31.Final and 2.3.12.Final.

**Security stewardship.** Red Hat Product Security (secalert@redhat.com) is the primary disclosure contact, consistent with upstream Red Hat / JBoss governance. Advisories are coordinated through Red Hat's Bugzilla and published to GHSA. Release cadence is tied to WildFly and Spring Boot Undertow support lifecycles.

**End-of-life risk.** The 1.x line is EOL. The `2.2.x` line tracks WildFly 26.x (Red Hat JBoss EAP 7.x). The `2.3.x` line tracks WildFly 27+. Users on `2.2.x` < 2.2.34.Final or `2.3.x` < 2.3.15.Final are exposed to CVE-2024-3653 (memory leak). Earlier 2.x minors are exposed to the full set above.

## Dependencies of Note

- `undertow-core` depends on XNIO (non-blocking I/O framework), which is also maintained by Red Hat. No GHSA package-level advisories for XNIO found in this pass.
- `undertow-servlet` and `undertow-websockets-jsr` are companion artifacts with additional exposure surface; not mapped in this pass.

## Open Questions

- Six additional 2024 GHSA advisories for `io.undertow:undertow-core` were found but not yet fully mapped in this pass: GHSA-v76w-3ph8-vm66, GHSA-w6qf-42m7-vh68, GHSA-9442-gm4v-r222, GHSA-9623-mqmm-5rcf, GHSA-xpp6-8r3j-ww43, GHSA-97cq-f4jm-mv8h. A follow-up pass should map these and determine if they extend the DoS or smuggling pattern.
- Monitor for advisories filed against `undertow-servlet` and `undertow-websockets-jsr` companion artifacts.
- Evaluate whether the SSL infinite-loop pattern (CVE-2023-1108) has been addressed at the XNIO layer as well.

## Related Pages

- [[maven/org.eclipse.jetty/jetty-server]]
- [[maven/org.apache.tomcat.embed/tomcat-embed-core]]
- [[maven/io.netty/netty-codec-http]]
- [[maven/index]]

---
*Last updated: 2026-09-23 | Sources: 11*
