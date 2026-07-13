# Apache Commons Text (Maven)

**Registry:** Maven Central
**Stable Version:** unknown (see https://github.com/apache/commons-text/releases; 1.10.0 is minimum safe version)
**Repository:** https://github.com/apache/commons-text
**Security Contact:** security@apache.org
**Disclosure Policy:** https://www.apache.org/security/
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No public proactive audits on record.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-42889 / GHSA-599f-7c49-w659 | **Critical CVSS 9.8** | **Text4Shell:** `StringSubstitutor` / `StringLookup` variable interpolation enables RCE and SSRF via default-enabled `script:`, `dns:`, and `url:` lookup handlers when processing untrusted configuration strings. The `script:` interpolator executes arbitrary code in the JVM via the Java `ScriptEngine` API. Attackers who control any string processed by `StringSubstitutor.replace()` or equivalent can trigger remote code execution with no authentication requirement. Affects versions 1.5 through 1.9; mitigation in 1.10.0 disables the problematic lookups by default. | 1.10.0 | [GHSA-599f-7c49-w659](https://github.com/advisories/GHSA-599f-7c49-w659) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-42889) |

## Security Posture Notes

- **Apache Software Foundation security policy** governs disclosure: embargoed reports to security@apache.org, typically released publicly ≥ 14 days after fix availability.
- **Text4Shell (CVE-2022-42889) context:** Attracted significant attention in October 2022 as a structural parallel to Log4Shell: both involve powerful string interpolation with network-callable lookups enabled by default. However, Text4Shell requires the application to actively pass untrusted data to a `StringSubstitutor` or `StringLookup` API, narrowing the exploitable attack surface compared to Log4Shell's implicit logging path. The Apache team assessed real-world exploitability as lower than Log4Shell for most deployments, but applications that process user-supplied configuration templates, email templates, or any dynamic string expansion through commons-text are directly at risk.
- **1.10.0 mitigation:** Disables `ScriptStringLookup`, `DnsStringLookup`, and `UrlStringLookup` by default. Upgrading requires no source changes in most cases; the API surface is preserved.
- **One advisory confirmed:** Only GHSA-599f-7c49-w659 / CVE-2022-42889 was found in the GitHub Advisory Database for `org.apache.commons:commons-text` during this pass. No additional published advisories exist for versions after 1.10.0 in this source.
- Downstream exposure: commons-text is used in template processing, SQL-building helpers, and string diffing tools. Spring Boot and various Apache projects include it as a transitive dependency.

## Dependencies of Note

- `org.apache.commons:commons-lang3` — commons-text extends commons-lang3 utilities; no known cross-package security boundary at this level.
- **Transitive risk:** Any application feeding user-controlled strings to `StringSubstitutor`, the deprecated `StrSubstitutor`, or any `StringLookup`-based API on versions 1.5–1.9 is vulnerable to Text4Shell.

## Open Questions

- What is the current latest stable version? (Maven Central stats API blocked in this environment; see project releases for current version.)
- Are there any additional advisories for versions after 1.10.0?
- Has Apache published a post-incident threat-model document for the Text4Shell interpolation design?

## Related Pages

- [[maven/org.apache.logging.log4j/log4j-core]] — Log4Shell (CVE-2021-44228) structural parallel via JNDI interpolation
- [[maven/org.apache.commons/commons-lang3]]
- [[maven/index]]

---
*Last updated: 2026-07-13 | Sources: 1 (GHSA-599f-7c49-w659 / NVD CVE-2022-42889)*
