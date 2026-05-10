# org.apache.tomcat.embed:tomcat-embed-core (Maven)

**Registry:** Maven Central  
**Weekly Downloads:** unknown  
**Repository:** https://github.com/apache/tomcat  
**Security Contact:** Apache Security Team / Tomcat security process  
**Disclosure Policy:** https://tomcat.apache.org/security.html  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-10 | OpenClaw recurring review | advisory mapping (public records only) | public-source curation from OSV.dev package query, GitHub Advisory Database aliases surfaced by OSV, public CVE/NVD links surfaced by OSV, Apache Tomcat security pages, Maven Central metadata, and local proxy-assisted drafting | Added initial Maven package page for 64 package-scoped public OSV records, with representative classes across HTTP parsing/request validation, HTTP/2 and multipart DoS, security-constraint and CLIENT_CERT authentication bypasses, open redirects, logging/information exposure, and path/resource boundaries. | https://osv.dev/list?ecosystem=Maven&q=org.apache.tomcat.embed%3Atomcat-embed-core |

## Known Vulnerabilities

The table below is a representative package-level advisory map for `org.apache.tomcat.embed:tomcat-embed-core`. The saved OSV package query for this pass returned 64 public records; this page highlights the recurring classes and recent/high-signal records rather than reproducing every historical Tomcat CVE inline.

| CVE / Issue | Description | Fixed in | Source |
|-------------|-------------|----------|--------|
| CVE-2020-1938 / GHSA-c9hw-wf7x-jp9j | Improper privilege-management issue in Tomcat's AJP connector lineage. | 7.0.100, 8.5.51, 9.0.31 | https://osv.dev/vulnerability/GHSA-c9hw-wf7x-jp9j |
| CVE-2020-1935 / GHSA-qxf4-chvg-4r8r | Potential HTTP request-smuggling issue in Apache Tomcat. | 7.0.100, 8.5.51, 9.0.31 | https://osv.dev/vulnerability/GHSA-qxf4-chvg-4r8r |
| CVE-2021-25329 / GHSA-jgwr-3qm3-26f3 | Potential remote-code-execution issue in Apache Tomcat. | 7.0.108, 8.5.61, 9.0.41, 10.0.2 | https://osv.dev/vulnerability/GHSA-jgwr-3qm3-26f3 |
| CVE-2023-24998 / GHSA-hfrx-6qgj-fp6c | Apache Commons FileUpload denial-of-service issue relevant to Tomcat multipart handling. | 8.5.88, 9.0.71, 10.1.5, 11.0.0-M5 | https://osv.dev/vulnerability/GHSA-hfrx-6qgj-fp6c |
| CVE-2023-28709 / GHSA-cx6h-86xw-9x34 | Incomplete fix follow-up for CVE-2023-24998. | 9.0.74, 10.1.8, 11.0.0-M5 | https://osv.dev/vulnerability/GHSA-cx6h-86xw-9x34 |
| CVE-2023-44487 / GHSA-qppj-fm5r-hxr3 | HTTP/2 stream-cancellation / rapid-reset denial-of-service class. | 8.5.94, 9.0.81, 10.1.14, 11.0.0-M12 | https://osv.dev/vulnerability/GHSA-qppj-fm5r-hxr3 |
| CVE-2023-46589 / GHSA-fccv-jmmp-qg76 | Improper input-validation issue in Apache Tomcat. | 8.5.96, 9.0.83, 10.1.16, 11.0.0-M11 | https://osv.dev/vulnerability/GHSA-fccv-jmmp-qg76 |
| CVE-2024-34750 / GHSA-wm9w-rjj3-j356 | Denial-of-service issue in Apache Tomcat. | 9.0.90, 10.1.25, 11.0.0-M21 | https://osv.dev/vulnerability/GHSA-wm9w-rjj3-j356 |
| CVE-2025-48988 / GHSA-h3gc-qfqq-6h8f | Multipart-upload denial-of-service issue. | 9.0.106, 10.1.42, 11.0.8 | https://osv.dev/vulnerability/GHSA-h3gc-qfqq-6h8f |
| CVE-2025-49125 / GHSA-wc4r-xq3c-5cf3 | Security-constraint bypass for pre/post-resources. | 9.0.106, 10.1.42, 11.0.8 | https://osv.dev/vulnerability/GHSA-wc4r-xq3c-5cf3 |
| CVE-2025-52520 / GHSA-wr62-c79q-cv37 | Catalina denial-of-service issue through bypassing configured size limits. | 9.0.107, 10.1.43, 11.0.9 | https://osv.dev/vulnerability/GHSA-wr62-c79q-cv37 |
| CVE-2025-53506 / GHSA-25xr-qj8w-c4vf | Coyote denial-of-service issue via excessive HTTP/2 streams. | 9.0.107, 10.1.43, 11.0.9 | https://osv.dev/vulnerability/GHSA-25xr-qj8w-c4vf |
| CVE-2025-66614 / GHSA-fpj8-gq4v-p354 | Client-certificate verification bypass. | 9.0.113, 10.1.50, 11.0.15 | https://osv.dev/vulnerability/GHSA-fpj8-gq4v-p354 |
| CVE-2026-24733 / GHSA-qq5r-98hh-rxc9 | Security-constraint bypass with HTTP/0.9 handling. | 9.0.113, 10.1.50, 11.0.15 | https://osv.dev/vulnerability/GHSA-qq5r-98hh-rxc9 |
| CVE-2026-29145 / GHSA-95jq-rwvf-vjx4 | CLIENT_CERT authentication did not fail as expected in affected configurations. | 9.0.116, 10.1.53, 11.0.20 | https://osv.dev/vulnerability/GHSA-95jq-rwvf-vjx4 |
| CVE-2026-34483 / GHSA-rv64-5gf8-9qq8 | Improper output encoding / escaping in `JsonAccessLogValve`. | 9.0.116, 10.1.54, 11.0.21 | https://osv.dev/vulnerability/GHSA-rv64-5gf8-9qq8 |
| CVE-2026-34500 / GHSA-24j9-x2wg-9qv6 | Later CLIENT_CERT authentication failure case in affected Tomcat lines. | 9.0.117, 10.1.54, 11.0.21 | https://osv.dev/vulnerability/GHSA-24j9-x2wg-9qv6 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.apache.tomcat.embed%3Atomcat-embed-core*

## Security Posture Notes

- `tomcat-embed-core` has a broad public advisory surface because it packages Tomcat's embedded servlet container core: HTTP parsing, Coyote connectors, Catalina resource handling, servlet security constraints, multipart handling, access logging, and authentication integrations can all become package-scoped issues.
- The 2025-2026 public record cluster is especially dense. Recurrent themes in the saved OSV data include denial of service through HTTP/2, multipart upload, or size-limit boundary behavior; security-constraint bypasses; CLIENT_CERT authentication failures; open redirect cases; and logging / information-disclosure issues.
- Exposure is deployment- and connector-dependent. Some records require specific connectors or features such as HTTP/2, AJP, CGI, rewrite rules, pre/post-resources, multipart upload handling, JSON access logging, or CLIENT_CERT authentication. This page should not be read as saying every embedded Tomcat application is equally affected by every row.
- Maven Central metadata saved in this pass listed `11.0.22` as the latest / release version. Many production applications remain on the 9.0.x or 10.1.x lines, so remediation should follow the fixed version for the supported line actually in use rather than treating the latest major as a drop-in upgrade.
- The public advisory trail shows several incomplete-fix / follow-up patterns, including the multipart DoS follow-up after `CVE-2023-24998` and repeated CLIENT_CERT authentication records. When reviewing deployed stacks, verify the exact Tomcat line and patch level rather than relying only on a broad major-version label.

## Dependencies of Note

- `tomcat-embed-core` is commonly pulled in by Spring Boot and other Java web frameworks. Application exposure depends on the complete dependency tree, chosen embedded-container version, and feature configuration.
- Commons FileUpload-related records may also matter for applications using Tomcat multipart handling or adjacent upload libraries. See [[maven/commons-fileupload/commons-fileupload]] for the standalone Commons FileUpload coordinate.

## Open Questions

- Should the KB split Tomcat pages by major line (`9.0.x`, `10.1.x`, `11.0.x`) or keep one coordinate-level page with fixed-version columns?
- Which high-usage frameworks or starters pin affected `tomcat-embed-core` versions after public fixes, and are their upgrade notes clear?
- Should a future pass normalize all 64 OSV records into a generated appendix rather than keeping this page focused on representative classes?

## Related Pages

- [[maven/index]]
- [[maven/org.springframework/spring-core]]
- [[maven/commons-fileupload/commons-fileupload]]
- [[maven/org.apache.logging.log4j/log4j-core]]

---
*Last updated: 2026-05-10 | Sources: 6 (OSV package query and individual vulnerability records, GitHub Advisory Database public aliases surfaced by OSV, public CVE/NVD links surfaced by OSV, Apache Tomcat security pages, Maven Central metadata, local proxy synthesis used as drafting aid only)*
