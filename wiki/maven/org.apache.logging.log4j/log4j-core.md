# org.apache.logging.log4j:log4j-core (Maven / Java)

**Registry:** Maven Central
**Coordinates:** `org.apache.logging.log4j:log4j-core`
**Current upstream release metadata:** Maven metadata listed `2.25.4` as the latest 2.x release and `3.0.0-beta3` as the latest/beta line in this pass.
**Repository:** https://github.com/apache/logging-log4j2
**Security Contact:** security@logging.apache.org
**Disclosure Policy:** https://logging.apache.org/security.html
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-06 | OpenClaw recurring review | package advisory history / Maven gap fill | public-source curation using OSV.dev package query, GitHub Advisory Database identifiers, public CVE/NVD aliases, Apache Logging security page, Apache Log4j release notes, and Maven Central metadata | Added a dedicated Maven page for `log4j-core`, mapping 11 public OSV/GHSA records across Log4Shell/JNDI, socket-server deserialization, SMTP / socket TLS hostname verification, recursive lookup DoS, JDBC appender JNDI configuration risk, RFC5424 log injection, XML log-event loss, and Log4j 1.x compatibility/EOL boundary history. | https://osv.dev/list?ecosystem=Maven&q=org.apache.logging.log4j%3Alog4j-core |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2017-5645 / GHSA-fxph-q3j8-mv87 | CVSS 3.0 | Log4j 2.x before 2.8.2 could deserialize untrusted serialized log events when the TCP or UDP socket server received crafted binary payloads. | 2.8.2 | https://github.com/advisories/GHSA-fxph-q3j8-mv87 |
| CVE-2020-9488 / GHSA-vwqq-5vrc-xw9h | CVSS 3.1 | The SMTP appender could validate certificates without verifying hostname matches, weakening TLS server authentication. | 2.13.2; 2.12.3; 2.3.2 | https://github.com/advisories/GHSA-vwqq-5vrc-xw9h |
| CVE-2021-44228 / GHSA-jfh8-c2jp-5v3q | CVSS 3.1 | Log4Shell: attacker-controlled log messages / parameters could trigger JNDI lookups and remote code injection in vulnerable Log4j Core versions. OSV/GHSA records show the initial 2.15.0 fix path plus later maintained-line fixes. | 2.15.0; 2.12.2; 2.3.1 | https://github.com/advisories/GHSA-jfh8-c2jp-5v3q |
| CVE-2021-45046 / GHSA-7rjr-3q55-vv33 | CVSS 3.1 | Incomplete Log4Shell fix: certain non-default pattern-layout / Thread Context Map configurations could still allow malicious JNDI lookup patterns. | 2.16.0; 2.12.2 | https://github.com/advisories/GHSA-7rjr-3q55-vv33 |
| CVE-2021-45105 / GHSA-p6xc-xr62-6r2g | CVSS 3.1 | Self-referential lookups in attacker-controlled Thread Context Map data could cause uncontrolled recursion and denial of service. | 2.17.0; 2.12.3; 2.3.1 | https://github.com/advisories/GHSA-p6xc-xr62-6r2g |
| CVE-2021-44832 / GHSA-8489-44mv-ggj8 | CVSS 3.1 | JDBC Appender JNDI data-source names could enable code execution when an attacker had permission to modify Log4j configuration; default configurations were not affected. | 2.17.1; 2.12.4; 2.3.2 | https://github.com/advisories/GHSA-8489-44mv-ggj8 |
| CVE-2023-26464 / GHSA-vp98-w2p3-mv35 | CVSS 3.1 | OSV includes an Apache Log4j 1.x EOL denial-of-service record on this package boundary for versions before the Log4j 2 line. This row is retained with EOL context rather than treated as a modern Log4j Core 2.x regression. | 2.0 boundary / migrate to maintained Log4j 2.x | https://github.com/advisories/GHSA-vp98-w2p3-mv35 |
| CVE-2025-68161 / GHSA-vc5p-v9hr-52mj | CVSS 4.0 | Socket Appender TLS hostname verification was not performed in affected 2.x releases, enabling man-in-the-middle risk when TLS sockets were configured in exposed network paths. | 2.25.3 | https://github.com/advisories/GHSA-vc5p-v9hr-52mj |
| CVE-2026-34477 / GHSA-6hg6-v5c8-fphq | CVSS 4.0 | Follow-on hostname-verification issue: the `verifyHostName` attribute in `<Ssl>` configuration was silently ignored even after the system-property path had been fixed. | 2.25.4 | https://github.com/advisories/GHSA-6hg6-v5c8-fphq |
| CVE-2026-34478 / GHSA-445c-vh5m-36rj | CVSS 4.0 | `Rfc5424Layout` could permit log injection because renamed configuration attributes caused newline escaping / TLS framing settings to be silently ignored in direct layout configurations. | 2.25.4 | https://github.com/advisories/GHSA-445c-vh5m-36rj |
| CVE-2026-34480 / GHSA-3pxv-7cmr-fjr4 | CVSS 4.0 | `XmlLayout` could emit XML 1.0 forbidden characters from log messages or MDC data, causing malformed XML or dropped log events in downstream processors. | 2.25.4 | https://github.com/advisories/GHSA-3pxv-7cmr-fjr4 |

*Full advisory history: https://osv.dev/list?ecosystem=Maven&q=org.apache.logging.log4j%3Alog4j-core*

## Security Posture Notes

- `log4j-core` is a high-impact Java logging implementation. Its public security history is dominated by trust-boundary mistakes in **JNDI lookups**, **serialized log-event receivers**, **network appenders**, and **structured log layouts**.
- The 2021 Log4Shell sequence should be read as a fix train rather than a single row: CVE-2021-44228 was followed by CVE-2021-45046, CVE-2021-45105, and CVE-2021-44832, each narrowing or changing the exploitable conditions.
- Version context matters. OSV/GHSA records show maintained-line fixes for legacy branches (`2.3.x`, `2.12.x`) as well as the mainline 2.x releases; consumers should not flatten all fixed-version strings into one universal upgrade floor without checking their Java/runtime constraints.
- Apache Logging's public security page is unusually explicit about threat model assumptions: configuration files, environment variables, and log format strings are treated as trusted deployer inputs, while log messages and Thread Context keys/values are not trusted.
- Recent 2025-2026 advisories are mostly about **log integrity and transport configuration** rather than classic RCE: TLS hostname verification gaps, RFC5424 log-injection behavior, and XML log-event loss in downstream processing.
- Apache Logging states that Log4j 1 reached end of life in 2015. The Log4j 1.x/EOL record is retained for migration context, but this page should avoid implying that unsupported 1.x defects are maintained in the same way as Log4j Core 2.x issues.

## Dependencies of Note

- `log4j-api` should generally be kept version-aligned with `log4j-core`; GHSA records repeatedly note that `log4j-api` is not directly affected by the listed `log4j-core` vulnerabilities but version skew can create compatibility problems.
- Network appenders (SMTP, Socket, JDBC/JNDI, syslog/RFC5424) and layout choices (`XmlLayout`, `Rfc5424Layout`, Pattern Layout with context lookups) are the recurring security-sensitive surfaces.
- Third-party repackages and bridges such as `org.ops4j.pax.logging:pax-logging-log4j2` have separate fix versions in some GHSA records and should not be silently conflated with the upstream Maven coordinate.

## Open Questions

- Should the KB add separate pages for `log4j-api`, `log4j-1.2-api`, or `log4j-layout-template-json` to avoid overloading this `log4j-core` page with adjacent artifact history?
- Which downstream Java frameworks still pin maintained-line fix branches such as `2.12.x` or `2.3.x`, and should those compatibility branches be captured in a future ecosystem note?
- Would a dedicated timeline for the December 2021 Log4Shell fix train make the page clearer without duplicating public incident writeups?

## Related Pages

- [[maven/index]]
- [[linux/openssl]]
- [[npm/openssl]]

---
*Last updated: 2026-05-06 | Sources: 6 (OSV.dev package query for `org.apache.logging.log4j:log4j-core`, GitHub Advisory Database / public GHSA pages, public CVE/NVD aliases, Apache Logging security page, Apache Log4j release notes, Maven Central metadata, plus a successful local proxy drafting pass used only as a synthesis aid)*
