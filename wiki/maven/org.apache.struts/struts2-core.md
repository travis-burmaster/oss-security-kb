# Apache Struts 2 / struts2-core (Maven)

**Registry:** Maven Central
**Weekly Downloads:** unknown (Maven Central stats API unavailable in this environment)
**Repository:** https://github.com/apache/struts
**Security Contact:** security@apache.org
**Disclosure Policy:** https://struts.apache.org/security/
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|---------|
| *No public proactive source-code audits on record.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|---------|
| CVE-2017-5638 / GHSA-j77q-2qqg-6989 | **Critical CVSS 9.8+** (E:H) | **S2-045 (Equifax breach vector):** Incorrect exception handling in the Jakarta Multipart parser evaluates a malformed `Content-Type` header containing a `#cmd=` expression as an OGNL expression — unauthenticated RCE via a single HTTP request with no interaction required. Actively exploited in March 2017 and used in the Equifax breach affecting ~148 million individuals. | 2.3.32 / 2.5.10.1 | [GHSA-j77q-2qqg-6989](https://github.com/advisories/GHSA-j77q-2qqg-6989) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2017-5638) |
| CVE-2017-12611 / GHSA-8fx9-5hx8-crhm | **Critical CVSS 9.8** | **S2-053:** Freemarker template tags allow an unintentional expression syntax (non-string-literal) to trigger OGNL evaluation on user-controlled data → unauthenticated RCE without requiring authentication or user interaction. | 2.3.34 / 2.5.11 | [GHSA-8fx9-5hx8-crhm](https://github.com/advisories/GHSA-8fx9-5hx8-crhm) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2017-12611) |
| CVE-2021-31805 / GHSA-v8j6-6c2r-r27c | **Critical CVSS 9.8** | **S2-062:** Incomplete fix for CVE-2020-17530 (S2-061). Certain tag attributes remain susceptible to forced double OGNL evaluation via `%{...}` sequences when developer code passes user input through those attributes — RCE if the attacker controls the evaluated string. | 2.5.30 | [GHSA-v8j6-6c2r-r27c](https://github.com/advisories/GHSA-v8j6-6c2r-r27c) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-31805) |
| CVE-2023-50164 / GHSA-2j39-qcjm-428w | **Critical CVSS 9.8** | **S2-066:** Flawed file upload parameter handling allows path traversal — attackers manipulate upload parameters to write files outside the intended upload directory, enabling RCE via a malicious uploaded file. | 2.5.33 / 6.3.0.2 | [GHSA-2j39-qcjm-428w](https://github.com/advisories/GHSA-2j39-qcjm-428w) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-50164) |
| CVE-2024-53677 / GHSA-43mq-6xmg-29vm | **Critical CVSS 9.8** | **S2-067:** File upload logic in the legacy `FileuploadInterceptor` is flawed — attackers manipulate upload parameters for directory traversal enabling arbitrary file write and RCE under certain conditions. Full remediation requires migrating to the new file upload mechanism introduced in 6.4.0; a version upgrade alone is insufficient. | 6.4.0 (+ interceptor migration) | [GHSA-43mq-6xmg-29vm](https://github.com/advisories/GHSA-43mq-6xmg-29vm) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-53677) |
| CVE-2016-4436 / GHSA-xm92-v2mq-842q | **Critical CVSS 9.8** | **S2-035:** Improper action name cleanup allows unauthenticated remote attackers to bypass security restrictions and execute arbitrary code via crafted network requests. | 2.3.29 / 2.5.1 | [GHSA-xm92-v2mq-842q](https://github.com/advisories/GHSA-xm92-v2mq-842q) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-4436) |
| CVE-2016-4461 / GHSA-864w-r5qj-h6fj | **High CVSS 8.8** | **S2-029:** Forced double OGNL evaluation via `%{}` sequences on authenticated requests — incomplete fix for CVE-2016-0785. Requires attacker to control a form field value processed by a vulnerable tag attribute. | 2.3.29 | [GHSA-864w-r5qj-h6fj](https://github.com/advisories/GHSA-864w-r5qj-h6fj) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-4461) |
| CVE-2013-1965 / GHSA-whmq-v94q-34p9 | **High** | **S2-012:** OGNL code injection via crafted redirect parameter names — remote attackers execute arbitrary OGNL expressions by submitting specially crafted parameters to redirect-using actions. | 2.3.14.3 | [GHSA-whmq-v94q-34p9](https://github.com/advisories/GHSA-whmq-v94q-34p9) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2013-1965) |
| CVE-2023-41835 / GHSA-729q-fcgp-r5xh | **High** | Uploaded files persist in `struts.multipart.saveDir` even when the request is denied due to exceeding `maxStringLength` — enabling disk exhaustion DoS against systems without out-of-band cleanup. | 2.5.32 / 6.1.2.2 / 6.3.0.1 | [GHSA-729q-fcgp-r5xh](https://github.com/advisories/GHSA-729q-fcgp-r5xh) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-41835) |
| CVE-2025-64775 / GHSA-xx7v-hqxh-cjr9 | **High** | **S2-068:** File leak in multipart request processing — uploaded files are not cleaned up on certain error paths, causing disk exhaustion DoS. Affects Struts 2.0–2.3.37, 2.5.0–2.5.33, 6.0.0–6.7.0, 7.0.0–7.0.3. | 6.8.0 / 7.1.1 | [GHSA-xx7v-hqxh-cjr9](https://github.com/advisories/GHSA-xx7v-hqxh-cjr9) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-64775) |
| CVE-2025-66675 / GHSA-rg58-xhh7-mqjw | **High CVSS 7.5** | **S2-068 (second advisory):** Additional file leak variant in multipart request handling — related but distinct from CVE-2025-64775, affecting versions through 6.7.4 and 7.0.3; same fix versions. | 6.8.0 / 7.1.1 | [GHSA-rg58-xhh7-mqjw](https://github.com/advisories/GHSA-rg58-xhh7-mqjw) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-66675) |
| CVE-2019-0233 / GHSA-ccp5-gg58-pxfm | **High CVSS 7.5** | Access permission override during file upload operations triggers a Denial of Service condition. | 2.5.22 | [GHSA-ccp5-gg58-pxfm](https://github.com/advisories/GHSA-ccp5-gg58-pxfm) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2019-0233) |
| CVE-2016-8738 / GHSA-86vq-8qhc-5rqw | **High CVSS 7.5** | **S2-044:** URLValidator DoS — specially crafted URL causes denial of service by overwhelming the server during URL validation when the built-in `URLValidator` is configured for form fields accepting URLs. | 2.5.12 | [GHSA-86vq-8qhc-5rqw](https://github.com/advisories/GHSA-86vq-8qhc-5rqw) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-8738) |
| CVE-2015-5209 / GHSA-4qgj-9mvg-3929 | **High** | Attackers manipulate Struts internals or affect container settings through the special `top` object in the ValueStack, accessed via insufficiently restricted request parameters. | 2.3.24.1 | [GHSA-4qgj-9mvg-3929](https://github.com/advisories/GHSA-4qgj-9mvg-3929) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2015-5209) |
| CVE-2015-1831 / GHSA-q2cg-xf9p-h457 | **High** | Inadequate default exclusion patterns allow remote attackers to bypass parameter exclusion controls and compromise internal application state via specially crafted parameter names. | 2.3.20.1 | [GHSA-q2cg-xf9p-h457](https://github.com/advisories/GHSA-q2cg-xf9p-h457) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2015-1831) |
| CVE-2023-34149 / GHSA-8f6x-v685-g2xc | **Moderate** | **S2-063:** Non-file multipart form fields are loaded into memory as strings without enforcing size limits — OOM DoS when `struts.multipart.maxSize` is configured to match or exceed available memory. | 2.5.31 / 6.1.2.1 | [GHSA-8f6x-v685-g2xc](https://github.com/advisories/GHSA-8f6x-v685-g2xc) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-34149) |

## Security Posture Notes

- **60 total GHSA advisories** exist in the GitHub Advisory Database for `org.apache.struts:struts2-core` (2008–2025). This page individually maps 16 of the most security-significant records. Notable advisories not individually fetched in this pass include: CVE-2018-11776 / S2-057 (Critical: namespace-based RCE when `alwaysSelectFullNamespace` is enabled — CVSS 9.8, widely exploited 2018), CVE-2019-0230 / S2-059 (Critical: forced OGNL evaluation via Freemarker tag attributes), and CVE-2020-17530 / S2-061 (Critical: forced OGNL evaluation — the flaw CVE-2021-31805 is an incomplete fix of).
- **Recurring root causes:** (1) OGNL/expression language injection — Struts 2 evaluates OGNL expressions from HTTP parameters and tag attributes; forced double evaluation of user-controlled strings is a persistent multi-year pattern. (2) File upload handling — two sequential path traversal RCE advisories (S2-066/S2-067) plus multiple disk exhaustion DoS advisories share the same `FileuploadInterceptor` ancestry. (3) Multipart parser boundary failures — CVE-2017-5638, S2-063, and S2-068 all root in multipart parsing error paths.
- **S2-045 / CVE-2017-5638 breach context:** Exploited in the Equifax data breach (May–July 2017), exposing PII for ~148 million individuals. A public PoC was released within 24 hours of the advisory. Struts 2 installations not using the Jakarta Multipart parser were unaffected. This breach established enterprise patching urgency for Struts as a high-priority security maintenance task.
- **S2-066/067 file upload RCE chain (2023–2024):** Two sequential vulnerabilities in `FileuploadInterceptor`. Full mitigation for S2-067 / CVE-2024-53677 requires migrating to the new file upload mechanism introduced in 6.4.0; a version upgrade alone is insufficient for complete remediation.
- **Active maintenance:** Apache Struts maintains two supported lines: 6.x (current stable 6.8.0) and 7.x (current stable 7.1.1). The 2.x and 5.x lines are EOL. The Apache Struts Security Bulletin at https://struts.apache.org/security/ is the canonical source for current-version status and all advisories.
- **Security contact:** Embargoed reports to security@apache.org; Apache Software Foundation security policy governs the embargo and release schedule.

## Dependencies of Note

- **OGNL expression library** — foundational to Struts 2's MVC design; a significant fraction of historical RCEs are reachable because OGNL evaluates framework-internal expressions using the same engine as developer expressions. Forced double evaluation of user-supplied values is the common exploit path.
- **Jakarta/Apache FileUpload (commons-fileupload)** — the legacy multipart parser (see [[maven/commons-fileupload/commons-fileupload]]); S2-045 exploited a Struts wrapper around this library's error handling.
- **Freemarker** — template engine used in some Struts 2 view configurations; S2-053 exploited improper expression handling in Freemarker tags.

## Open Questions

- Have the remaining 44 GHSA advisories (beyond the 16 mapped here) been triaged for severity and uniqueness, particularly the 2018 namespace RCE (S2-057/CVE-2018-11776) and the 2019–2020 forced-OGNL cluster?
- What is the current download volume for struts2-core 6.x vs. legacy 2.x lines in active enterprise deployments? (Maven Central stats API blocked in this environment.)
- Does the Apache Struts Security Team have a published threat model for the OGNL evaluation engine and the current expression-safety boundary in 6.x/7.x?

## Related Pages

- [[maven/commons-fileupload/commons-fileupload]] — multipart parser foundational dependency
- [[maven/org.apache.commons/commons-text]] — Text4Shell: parallel forced-evaluation vulnerability pattern (JNDI/script interpolation)
- [[maven/org.apache.logging.log4j/log4j-core]] — Log4Shell: analogous ecosystem-level RCE via expression injection
- [[maven/index]]

---
*Last updated: 2026-07-31 | Sources: 16 GHSA advisories (GHSA-j77q-2qqg-6989, GHSA-8fx9-5hx8-crhm, GHSA-v8j6-6c2r-r27c, GHSA-2j39-qcjm-428w, GHSA-43mq-6xmg-29vm, GHSA-xm92-v2mq-842q, GHSA-864w-r5qj-h6fj, GHSA-whmq-v94q-34p9, GHSA-729q-fcgp-r5xh, GHSA-xx7v-hqxh-cjr9, GHSA-rg58-xhh7-mqjw, GHSA-ccp5-gg58-pxfm, GHSA-86vq-8qhc-5rqw, GHSA-4qgj-9mvg-3929, GHSA-q2cg-xf9p-h457, GHSA-8f6x-v685-g2xc)*
