# log4net (.NET / NuGet)

**Registry:** NuGet
**Weekly Downloads:** unknown (418M total NuGet downloads across all versions as of 2026-08-13; ~907K downloads for current stable 3.3.2)
**Repository:** https://github.com/apache/logging-log4net
**Security Contact:** security@apache.org
**Disclosure Policy:** https://logging.apache.org/log4net/security.html
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|---------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|---------|
| CVE-2006-0743 / GHSA-f9fr-w54q-772h | Moderate (CWE-134) | Format string vulnerability in `LocalSyslogAppender` — log4net 1.2.9 passes attacker-influenced log messages to `syslog()` via a format string parameter; remote attackers may trigger denial of service or (in theory) memory corruption | 1.2.10 | [GHSA-f9fr-w54q-772h](https://github.com/advisories/GHSA-f9fr-w54q-772h) |
| CVE-2018-1285 / GHSA-2cwj-8chv-9pp9 | Critical (CVSS 9.8 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H; CWE-611) | XML External Entity (XXE) injection — log4net does not disable XML external entity processing when parsing configuration files; an attacker who can supply or modify a log4net configuration file can read arbitrary files from the server filesystem or trigger server-side request forgery | 2.0.10 | [GHSA-2cwj-8chv-9pp9](https://github.com/advisories/GHSA-2cwj-8chv-9pp9) |
| CVE-2026-40021 / GHSA-4f7c-pmjv-c25w | Moderate (CVSS 5.3 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N) | `XmlLayout` and `XmlLayoutSchemaLog4J` do not sanitize characters forbidden by the XML 1.0 specification (e.g., certain control characters) in MDC property keys/values and log event identity fields; log events containing forbidden characters are silently discarded by XML parsers, enabling an attacker who controls log message content to suppress audit records or cause log integrity failures | 3.3.0 | [GHSA-4f7c-pmjv-c25w](https://github.com/advisories/GHSA-4f7c-pmjv-c25w) |

### Notes on downstream / unreviewed advisories

Two unreviewed GHSA records reference log4net in a downstream product context but are NOT direct log4net library vulnerabilities:
- **CVE-2021-44028 / GHSA-6vh7-mxw3-7f49**: XXE in Quest KACE Desktop Authority < 11.2 via attacker-controlled log4net config; root cause is the same as CVE-2018-1285 in an earlier bundled log4net version.
- **CVE-2023-45253 / GHSA-64fx-j998-rqp7**: Privilege escalation in Huddly HuddlyCameraService < 8.0.7 exploiting log4net's `RollingFileAppender.DeleteFile` method (CWE-269, CVSS 9.1 local); this is an application-level privilege escalation in a specific product, not a log4net library vulnerability.

## Security Posture Notes

Apache log4net is the dominant .NET/NuGet logging framework ported from the Java log4j project. It is maintained by the Apache Software Foundation under the Apache Logging Services project. Total NuGet downloads exceed 418 million across all versions.

Key posture observations:
- **CVE-2018-1285 (XXE, Critical)** is the most significant advisory. Any application using log4net where the log4net configuration file can be supplied or influenced by an attacker is at risk. The fix (≥ 2.0.10) disables external entity resolution during configuration parsing. Deployments on log4net < 2.0.10 remain fully exposed; the 2.x line has 17 releases (2.0.0–2.0.17) before the fix.
- **CVE-2026-40021 (log suppression, Moderate)** is an audit-integrity concern rather than a direct RCE or data-exfiltration risk: an attacker who can inject XML-1.0-forbidden characters into log messages can make those events disappear from XML-format log outputs. Applications that rely on log4net XML layouts for audit trails in security-relevant contexts should upgrade to ≥ 3.3.0.
- log4net is NOT log4j. The infamous Log4Shell (CVE-2021-44228) is a Java log4j 2.x vulnerability; it does not apply to log4net. Confirming this is a frequent operational question.
- The Apache logging-log4net security page acknowledges the XXE advisory (CVE-2018-1285) and references the 2.0.10 fix.
- Current stable: **3.3.2** (released 2026-06-25). All mapped advisories are fixed in earlier releases.
- Version 3.x (released 2024+) represents a major rewrite with .NET 8+ targets; the older 2.x line remains in widespread use.

## Dependencies of Note

log4net has minimal external dependencies (mostly BCL). The XXE risk (CVE-2018-1285) stems from `System.Xml` behavior; the fix does not replace the XML stack but disables external entity resolution.

## Open Questions

- No third-party security audit of log4net is on public record — a future pass should check the Apache security archive.
- A future pass should verify whether any advisories exist in the 3.x line beyond CVE-2026-40021.
- Total weekly NuGet downloads not available from the registration API; future pass should try the NuGet stats API at `https://www.nuget.org/stats/packages/log4net` for a current figure.

## Related Pages

- [[dotnet/System.Security.Cryptography.Xml]] — XML processing / XXE risk context in .NET
- [[dotnet/index]]

---
*Last updated: 2026-08-13 | Sources: 5 (3 github-reviewed + 2 unreviewed downstream GHSA records; NuGet registration API)*
