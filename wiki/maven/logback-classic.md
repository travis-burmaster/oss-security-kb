# ch.qos.logback:logback-classic (Maven)

**Registry:** Maven Central
**Weekly Downloads:** unknown (Maven Central download stats unavailable via API)
**Repository:** https://github.com/qos-ch/logback
**Security Contact:** https://jira.qos.ch/
**Disclosure Policy:** https://github.com/qos-ch/logback/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-09-22 | oss-security-kb nightly | api-surface / advisory-review | automated | 4 advisories mapped | [GHSA database](https://github.com/github/advisory-database) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2017-5929 / GHSA-vmfg-rjjm-rjrj | Critical CVSS 9.8 AV:N/AC:L/PR:N/UI:N | Unsafe Java deserialization in SocketServer and ServerSocketReceiver — attacker sends malicious serialized objects via network socket enabling arbitrary code execution; CWE-502 | 1.2.0 | [GHSA-vmfg-rjjm-rjrj](https://github.com/advisories/GHSA-vmfg-rjjm-rjrj) |
| CVE-2021-42550 / GHSA-668q-qrv7-99fm | Moderate CVSS 6.6 AV:N/AC:H/PR:H | JNDI/LDAP lookup in logback configuration enables arbitrary class loading when attacker has write access to logback XML config; disclosed during the Log4Shell era; CWE-502 | 1.2.9 | [GHSA-668q-qrv7-99fm](https://github.com/advisories/GHSA-668q-qrv7-99fm) |
| CVE-2023-6378 / GHSA-vmq6-5m68-f53m | High AV:L/AC:L/PR:N/UI:N/S:C/C:N/I:N/A:H | Serialization DoS in receiver component — attacker sends poisoned data to receiver causing Denial-of-Service; only exploitable when logback receiver is deployed; CWE-502 | 1.2.13 / 1.3.12 / 1.4.12 | [GHSA-vmq6-5m68-f53m](https://github.com/advisories/GHSA-vmq6-5m68-f53m) |
| CVE-2026-19880 / GHSA-9mh8-hq67-v26g | Moderate CWE-22 path traversal | MDC-based discriminator value flows unsanitized into a nested FileAppender path — attacker controlling the MDC value (e.g., via HTTP request header) can create and append log files outside intended directory; unreviewed advisory | 1.6.3 | [GHSA-9mh8-hq67-v26g](https://github.com/advisories/GHSA-9mh8-hq67-v26g) |

## Security Posture Notes

Logback is the de facto default logging backend for the JVM ecosystem: Spring Boot auto-configures it as the default `slf4j` implementation since Spring Boot 1.x. Logstash, Kafka Connect, Dropwizard, and hundreds of enterprise frameworks depend on it transitively. The `ch.qos.logback:logback-classic` artifact provides FileAppender, ConsoleAppender, RollingFileAppender, SMTPAppender, DBAppender, SiftingAppender, and the full XML/Groovy configuration infrastructure.

Security pattern: three of the four advisories (CVE-2017-5929, CVE-2021-42550, CVE-2023-6378) involve deserialization or JNDI subsystems that are either disabled by default or require elevated attacker privileges:
- SocketServer / ServerSocketReceiver (CVE-2017-5929) listen on a TCP port and are uncommon in production; not enabled by default.
- CVE-2021-42550 requires attacker write access to the logback XML configuration file — a significantly higher privilege bar than Log4Shell, despite being disclosed simultaneously.
- CVE-2023-6378 requires the receiver component to be deployed and listening.

The 2026 MDC path-traversal (CVE-2026-19880) is the most universally applicable risk: any deployment where an HTTP header or user-controlled value flows into an MDC key consumed by a SiftingAppender discriminator is affected. The logback manual documents per-user log routing via SiftingAppender as a standard pattern.

Current recommended minimum: **1.5.x** (active maintenance) or 1.4.x ≥ 1.4.12. All 1.2.x versions are EOL. Latest stable as of this pass: **1.5.18** (2026); 1.6.3 resolves the MDC path traversal.

## Dependencies of Note

- `ch.qos.logback:logback-core` — co-released with logback-classic; most advisories affect both artifacts.
- `org.slf4j:slf4j-api` — logging facade; logback-classic is the reference implementation. No direct advisories.
- `org.codehaus.janino:janino` — expression compiler used in Janino conditional filters; older janino versions carry class-loading and expression-evaluation risk in constrained contexts.

## Open Questions

- GHSA-9mh8-hq67-v26g (CVE-2026-19880) is not yet GitHub-reviewed; confirm fix details in the 1.6.3 changelog once reviewed.
- Pre-1.2.0 history: GHSA-vmfg-rjjm-rjrj covers the major deserialization class; verify whether any additional pre-1.2.0 records exist in older CVE feeds.
- The 1.5.x branch introduced the Fluent API — check whether any new attack surface was introduced.

## Related Pages

- [[maven/org.apache.logging.log4j/log4j-core]] — sibling logging framework with Log4Shell/JNDI coverage
- [[maven/index]]

---
*Last updated: 2026-09-22 | Sources: 4 (GHSA-vmfg-rjjm-rjrj, GHSA-668q-qrv7-99fm, GHSA-vmq6-5m68-f53m, GHSA-9mh8-hq67-v26g)*
