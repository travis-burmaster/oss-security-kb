# XStream / com.thoughtworks.xstream:xstream (Maven)

**Registry:** Maven Central
**Weekly Downloads:** unknown (Maven Central stats API unavailable in this environment)
**Repository:** https://github.com/x-stream/xstream
**Security Contact:** https://x-stream.github.io/security.html
**Disclosure Policy:** https://x-stream.github.io/security.html
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No public proactive source-code audits on record.*

## Known Vulnerabilities

XStream has an exceptionally dense public advisory record, driven by its default blacklist-based deserialization security model. Advisories are grouped below by fix-train. 31 individual CVE advisories are mapped on this page spanning 2020–2022. The March 2021 batch (11 CVEs, fixed 1.4.16) and August 2021 batch (14 CVEs, fixed 1.4.18) are the two largest disclosure clusters; the August 2021 release also replaced the blacklist model with an opt-in whitelist.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-26217 / GHSA-mw36-7c6c-q4q2 | High | Remote code execution — attacker injects `ProcessBuilder` / `EventHandler` / `ImageIO$ContainsFilter` types into a manipulated stream, causing the JVM to execute arbitrary OS shell commands; discovered by Chen L, Zhihong Tian, Hui Lu (Guangzhou University). | 1.4.14 | [GHSA-mw36-7c6c-q4q2](https://github.com/advisories/GHSA-mw36-7c6c-q4q2) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2020-26217) |
| CVE-2020-26258 / GHSA-4cch-wxpw-8p28 | Moderate | Server-Side Request Forgery — unmarshalling of a manipulated input stream issues requests to arbitrary intranet or localhost URLs; fixed alongside CVE-2020-26259 in 1.4.15. | 1.4.15 | [GHSA-4cch-wxpw-8p28](https://github.com/advisories/GHSA-4cch-wxpw-8p28) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2020-26258) |
| CVE-2020-26259 / GHSA-jfvx-7wrx-43fh | Moderate (CVSS 7.7) | Arbitrary file deletion — manipulated unmarshalling input triggers deletion of attacker-specified files on the host; requires JAX-WS on the classpath. | 1.4.15 | [GHSA-jfvx-7wrx-43fh](https://github.com/advisories/GHSA-jfvx-7wrx-43fh) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2020-26259) |
| CVE-2021-21341 / GHSA-2p3x-qw9c-25hh | High (CVSS 7.5) | Denial of service via CPU exhaustion — crafted input stream causes 100% CPU consumption on the target; the DoS variant of the March 2021 batch (all 11 CVEs fixed 1.4.16). | 1.4.16 | [GHSA-2p3x-qw9c-25hh](https://github.com/advisories/GHSA-2p3x-qw9c-25hh) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-21341) |
| CVE-2021-21342 / GHSA-hvv8-336g-rx3m | Moderate | Server-Side Request Forgery — unmarshalling accesses arbitrary intranet/localhost data streams via File class manipulation; discovered by 钟潦贵 (Liaogui Zhong). | 1.4.16 | [GHSA-hvv8-336g-rx3m](https://github.com/advisories/GHSA-hvv8-336g-rx3m) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-21342) |
| CVE-2021-21343 / GHSA-74cv-f58x-f9wf | Moderate | Arbitrary file deletion on the local host via manipulated unmarshalling stream. | 1.4.16 | [GHSA-74cv-f58x-f9wf](https://github.com/advisories/GHSA-74cv-f58x-f9wf) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-21343) |
| CVE-2021-21344 / GHSA-59jw-jqf4-3wq3 | Moderate | Arbitrary code execution — crafted input stream causes XStream to load and execute code from a remote host. | 1.4.16 | [GHSA-59jw-jqf4-3wq3](https://github.com/advisories/GHSA-59jw-jqf4-3wq3) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-21344) |
| CVE-2021-21345 / GHSA-hwpc-8xqv-jvj4 | Moderate | Remote command execution via privileged process stream manipulation — exploitable when the attacker has sufficient process rights. | 1.4.16 | [GHSA-hwpc-8xqv-jvj4](https://github.com/advisories/GHSA-hwpc-8xqv-jvj4) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-21345) |
| CVE-2021-21346 / GHSA-4hrm-m67v-5cxr | Moderate | Arbitrary code execution via manipulated input stream. | 1.4.16 | [GHSA-4hrm-m67v-5cxr](https://github.com/advisories/GHSA-4hrm-m67v-5cxr) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-21346) |
| CVE-2021-21347 / GHSA-qpfq-ph7r-qv6f | Moderate | Arbitrary code execution — loads and executes code from a remote host via manipulated stream. | 1.4.16 | [GHSA-qpfq-ph7r-qv6f](https://github.com/advisories/GHSA-qpfq-ph7r-qv6f) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-21347) |
| CVE-2021-21348 / GHSA-56p8-3fh9-4cvq | Moderate | ReDoS — a crafted input stream triggers a regular expression with catastrophic backtracking, occupying a thread at maximum CPU indefinitely. | 1.4.16 | [GHSA-56p8-3fh9-4cvq](https://github.com/advisories/GHSA-56p8-3fh9-4cvq) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-21348) |
| CVE-2021-21349 / GHSA-f6hm-88x3-mfjv | Moderate | Server-Side Request Forgery — unmarshalling of a manipulated input stream causes XStream to issue HTTP requests to internal/localhost services. | 1.4.16 | [GHSA-f6hm-88x3-mfjv](https://github.com/advisories/GHSA-f6hm-88x3-mfjv) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-21349) |
| CVE-2021-21350 / GHSA-43gc-mjxg-gvrq | Moderate | Arbitrary code execution via Swing UI types injected into the manipulated stream. | 1.4.16 | [GHSA-43gc-mjxg-gvrq](https://github.com/advisories/GHSA-43gc-mjxg-gvrq) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-21350) |
| CVE-2021-21351 / GHSA-hrcp-8f3q-4w2c | Moderate | Arbitrary code execution requiring admin privileges — loads and executes code from a remote host; the highest-privilege variant of the March 2021 ACE cluster. | 1.4.16 | [GHSA-hrcp-8f3q-4w2c](https://github.com/advisories/GHSA-hrcp-8f3q-4w2c) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-21351) |
| CVE-2021-29505 / GHSA-7chv-rrw6-w6fc | High (CVSS 7.5) | Remote command execution via server-side deserialization — attacker with sufficient process privileges executes OS commands by manipulating the input stream; independently discovered and disclosed after the March 2021 batch; fixed in the 1.4.17 maintenance release. | 1.4.17 | [GHSA-7chv-rrw6-w6fc](https://github.com/advisories/GHSA-7chv-rrw6-w6fc) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-29505) |
| CVE-2021-39139 / GHSA-64xx-cq4q-mf44 | High (CVSS 9.1) | Arbitrary code execution — exploitable on JDK ≤ 1.7u21 or when external Xalan is on the classpath; crafted stream triggers gadget chain execution. Part of the August 2021 batch (14 CVEs, all fixed 1.4.18). | 1.4.18 | [GHSA-64xx-cq4q-mf44](https://github.com/advisories/GHSA-64xx-cq4q-mf44) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-39139) |
| CVE-2021-39140 / GHSA-6wf9-jmg9-vxcc | Moderate (CVSS 6.5) | Denial of service — attacker with low-privilege access forces 100% CPU usage via manipulated input stream; the only DoS in the August 2021 batch. | 1.4.18 | [GHSA-6wf9-jmg9-vxcc](https://github.com/advisories/GHSA-6wf9-jmg9-vxcc) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-39140) |
| CVE-2021-39141 / GHSA-g5w6-mrj7-75h2 | High (CVSS 9.1) | Arbitrary code execution via gadget chain triggered by manipulated stream; reported by Tencent TSRC. | 1.4.18 | [GHSA-g5w6-mrj7-75h2](https://github.com/advisories/GHSA-g5w6-mrj7-75h2) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-39141) |
| CVE-2021-39144 / GHSA-j9h8-phrw-h4fh | High (CVSS 9.1, E:H) | Remote command execution — attacker with sufficient deserialization access can execute OS-level commands via the stream; exploit maturity flag E:H indicates public exploits existed at disclosure. | 1.4.18 | [GHSA-j9h8-phrw-h4fh](https://github.com/advisories/GHSA-j9h8-phrw-h4fh) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-39144) |
| CVE-2021-39145 / GHSA-8jrj-525p-826v | High (CVSS 9.1) | Arbitrary code execution via gadget chain; independently reported by Alibaba Cloud Security and DBAPPSecurity. | 1.4.18 | [GHSA-8jrj-525p-826v](https://github.com/advisories/GHSA-8jrj-525p-826v) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-39145) |
| CVE-2021-39146 / GHSA-p8pq-r894-fm8f | High (CVSS 9.1) | Arbitrary code execution via gadget chain; reported by Tencent Security Response Center. | 1.4.18 | [GHSA-p8pq-r894-fm8f](https://github.com/advisories/GHSA-p8pq-r894-fm8f) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-39146) |
| CVE-2021-39147 / GHSA-h7v4-7xg3-hxcc | High (CVSS 9.1) | Arbitrary code execution via gadget chain; reported by wh1t3p1g, Tencent TSRC. | 1.4.18 | [GHSA-h7v4-7xg3-hxcc](https://github.com/advisories/GHSA-h7v4-7xg3-hxcc) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-39147) |
| CVE-2021-39148 / GHSA-qrx8-8545-4wg2 | High (CVSS 9.1) | Arbitrary code execution via gadget chain; reported by wh1t3p1g, Tencent TSRC. | 1.4.18 | [GHSA-qrx8-8545-4wg2](https://github.com/advisories/GHSA-qrx8-8545-4wg2) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-39148) |
| CVE-2021-39149 / GHSA-3ccq-5vw3-2p6x | High (CVSS 9.1) | Arbitrary code execution via gadget chain; reported by Lai Han, NSFOCUS. | 1.4.18 | [GHSA-3ccq-5vw3-2p6x](https://github.com/advisories/GHSA-3ccq-5vw3-2p6x) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-39149) |
| CVE-2021-39150 / GHSA-cxfm-5m4g-x7xp | High (CVSS 9.1) | SSRF — attacker reaches intranet/localhost resources via unmarshalling on Java 8–14 targets. | 1.4.18 | [GHSA-cxfm-5m4g-x7xp](https://github.com/advisories/GHSA-cxfm-5m4g-x7xp) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-39150) |
| CVE-2021-39151 / GHSA-hph2-m3g5-xxv4 | High (CVSS 9.1) | Arbitrary code execution via gadget chain; reported by Smi1e, DBAPPSecurity WEBIN Lab. | 1.4.18 | [GHSA-hph2-m3g5-xxv4](https://github.com/advisories/GHSA-hph2-m3g5-xxv4) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-39151) |
| CVE-2021-39152 / GHSA-xw4p-crpj-vjx2 | High (CVSS 9.0) | SSRF — second SSRF vector in the August 2021 batch; Java 8–14 targets. | 1.4.18 | [GHSA-xw4p-crpj-vjx2](https://github.com/advisories/GHSA-xw4p-crpj-vjx2) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-39152) |
| CVE-2021-39153 / GHSA-2q8x-2p7f-574v | High (CVSS 9.1) | Arbitrary code execution; requires Java 8–14 or JavaFX on the classpath. | 1.4.18 | [GHSA-2q8x-2p7f-574v](https://github.com/advisories/GHSA-2q8x-2p7f-574v) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-39153) |
| CVE-2021-39154 / GHSA-6w62-hx7r-mw68 | High (CVSS 9.1) | Arbitrary code execution via gadget chain; reported by ka1n4t. | 1.4.18 | [GHSA-6w62-hx7r-mw68](https://github.com/advisories/GHSA-6w62-hx7r-mw68) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-39154) |
| CVE-2021-43859 / GHSA-rmr5-cpv2-vgjf | High (CVSS 7.5) | Denial of service via CPU exhaustion — injection of highly recursive collections or maps causes hash-code calculation to run indefinitely, consuming 100% CPU on the target host; no auth required with AC:L. | 1.4.19 | [GHSA-rmr5-cpv2-vgjf](https://github.com/advisories/GHSA-rmr5-cpv2-vgjf) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-43859) |
| CVE-2022-40151 / GHSA-f8cc-g7j8-xxpm | High (CVSS 7.5) | Denial of service via stack overflow — injecting deeply nested objects during unmarshalling causes a `StackOverflowError`; exploitable without authentication when AC:L. | 1.4.20 | [GHSA-f8cc-g7j8-xxpm](https://github.com/advisories/GHSA-f8cc-g7j8-xxpm) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-40151) |

*OSV link: https://osv.dev/list?ecosystem=Maven&q=com.thoughtworks.xstream*

## Security Posture Notes

XStream is a Java library for serializing and deserializing Java objects to/from XML (and optionally JSON). It is embedded across a large swath of the Java ecosystem — Jenkins, Sonatype Nexus, various enterprise middleware, and many frameworks — making its security history unusually consequential.

**Root cause: Blacklist-based deserialization model (pre-1.4.18).** Before 1.4.18, XStream guarded against unsafe deserialization using a blacklist of known-dangerous Java types (converters). This model is fundamentally flawed: security researchers routinely found new gadget chains that bypassed the blacklist, each triggering a new batch of CVEs. The March 2021 batch (11 CVEs) and August 2021 batch (14 CVEs) are the culmination of this arms race, collectively covering RCE, SSRF, file deletion, and DoS vectors across multiple JDK and classpath configurations.

**1.4.18 whitelist model (August 2021).** XStream 1.4.18 replaced the blacklist with an allowlist (Security Framework). By default, no types are allowed to be deserialized; applications must explicitly configure which types are permitted. This is the correct architectural fix for the blacklist problem. Applications upgrading from 1.4.16 to 1.4.18 must configure the allowlist or deserialization will be blocked entirely — this is a breaking change that requires application-level migration effort.

**March 2021 batch (fixed 1.4.16).** Eleven CVEs (CVE-2021-21341 through CVE-2021-21351) were disclosed simultaneously on 2021-03-22, covering arbitrary code execution (5 variants), arbitrary file deletion (2 variants), SSRF (1), DoS via infinite loop (1), and DoS via regex catastrophic backtracking (1). All 11 are individually mapped in the table above.

**August 2021 batch (fixed 1.4.18).** Fourteen CVEs (CVE-2021-39139 through CVE-2021-39154, with gaps at -39142 and -39143) were disclosed simultaneously on 2021-08-25. Thirteen of the fourteen involve ACE or RCE via gadget chains (CVSS 9.0–9.1); one (CVE-2021-39140) is a DoS. CVE-2021-39144 has an exploit-maturity flag of E:H indicating active public exploits at the time of disclosure. Reporters include researchers from Tencent TSRC, Alibaba Cloud Security, DBAPPSecurity, NSFOCUS, and independent researchers. All 14 are individually mapped above.

**CVE-2021-43859 and CVE-2022-40151 (1.4.19, 1.4.20 patches).** Even after the whitelist model was introduced, DoS vulnerabilities requiring only a crafted input stream (not a class-loading gadget) continued to be found: recursive-collection CPU exhaustion (1.4.19) and deeply nested object stack overflow (1.4.20). These affect any application that accepts XML input from untrusted sources and calls `fromXML()`.

**Recommendation:** Upgrade to 1.4.20 or later and configure the XStream Security Framework allowlist. Consider replacing XStream with a purpose-built format like Jackson, Gson, or Protocol Buffers if untrusted XML deserialization is not a core requirement — XStream's design coupling XML structure to Java type instantiation makes safe use from untrusted input inherently difficult.

**Current status:** The project is maintained but has sparse commit history in recent years. The latest release at time of this pass is 1.4.20+ (check https://x-stream.github.io/download.html for the current version).

## Dependencies of Note

- **Java standard library / JDK version:** Exploitability of several RCE advisories (CVE-2021-39139, CVE-2021-39150, CVE-2021-39152, CVE-2021-39153) depends on JDK version (≤ 1.7u21 or Java 8–14) or the presence of optional classpath entries (Xalan, JavaFX). Modern JDK 17+ with module encapsulation limits some gadget chain paths.
- **jenkins-core** — Jenkins has historically embedded XStream and carries its own XStream-related CVE history; see [[maven/org.apache.logging.log4j/log4j-core]] for a parallel transitive-dep risk example.
- **No additional runtime Maven dependencies** — XStream itself has minimal compile-time dependencies (xmlpull, kxml2 for the XML pull-parsing backend), none with known active advisories.

## Open Questions

- Confirm the current latest release version and whether any 2023+ advisories have been published (the GitHub Advisory Database search returned 88 total results, including advisories for downstream consumers of XStream such as Jenkins and Sonatype Nexus; precise count of xstream-package-level advisories post-2022 was not confirmed in this pass).
- Obtain weekly download count from Maven Central once the stats API is accessible.
- Assess whether CVE-2022-41966 (stack-overflow DoS via `XmlReaderWrapper`, reported December 2022, CVSS 7.5) is present in the advisory database as a distinct record from CVE-2022-40151.

## Related Pages

- [[maven/com.fasterxml.jackson.core/jackson-databind]]
- [[maven/org.yaml/snakeyaml]]
- [[maven/org.apache.struts/struts2-core]]
- [[maven/index]]

---
*Last updated: 2026-08-01 | Sources: GitHub Advisory Database (github/advisory-database) — 31 xstream-package advisories fetched via mcp__github__search_code and WebFetch on raw.githubusercontent.com*
