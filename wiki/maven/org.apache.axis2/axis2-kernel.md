# org.apache.axis2:axis2-kernel — Apache Axis2/Java (maven)

**Registry:** Maven Central
**Group:** org.apache.axis2
**Artifact:** axis2-kernel (core engine; older GHSA records map to the `org.apache.axis2:axis2` aggregate artifact and `axis2-transport-http`)
**Current Version:** 2.0.2 (Maven metadata last updated 2026-10-28)
**Weekly Downloads:** unknown (as of 2026-11-22)
**Project:** https://axis.apache.org/axis2/java/core/
**Repository:** https://github.com/apache/axis-axis2-java-core
**Security Contact:** https://www.apache.org/security/ (Apache Security Team)
**Disclosure Policy:** https://www.apache.org/security/
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-11-22 | LLM advisory-review pass | public advisory mapping for Axis2/Java | GitHub Advisory Database records (reviewed and unreviewed), upstream 2.0.2 release notes, CISA KEV catalog 2026.11.20, Maven Central metadata | 14 public advisories mapped (8 from 2026); none on CISA KEV | [raw/advisory-review-20261122-0500/notes.md](../../../raw/advisory-review-20261122-0500/notes.md) |

## Known Vulnerabilities

### 2026

The seven 2.0.2 records were published 2026-11-09 (GHSA, unreviewed) with Apache announcements on the Apache mailing lists (oss-security copies dated 2026-11-06 for most). None of the 2026 GHSA records carries a Maven package mapping yet.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-123753 / GHSA-p73m-5r4v-xhg8 | Critical (GHSA) | SSRF: an unauthenticated caller could supply a non-anonymous WS-Addressing `wsa:ReplyTo` / `wsa:FaultTo`, and Axis2 would connect to that address to deliver the response or fault. 2.0.2 refuses decoupled responses unless `allowNonAnonymousResponseEndpoints` is enabled. Through 2.0.1. | 2.0.2 | [GHSA](https://github.com/advisories/GHSA-p73m-5r4v-xhg8) · [Apache announcement](https://lists.apache.org/thread.html/rddzl5jfmlr09yr9qj33by7kzprwwvnc) · [release notes](https://raw.githubusercontent.com/apache/axis-axis2-java-core/master/src/site/markdown/release-notes/2.0.2.md) |
| CVE-2026-120761 / GHSA-qr3h-4xv7-vc63 | Critical (GHSA) | XXE: when a client built an `AxisService` from a WSDL URL, wsdl4j import resolution parsed imported documents with DOCTYPE and external entities enabled, allowing local file read or JVM-issued network requests by whoever controls the WSDL. Through 2.0.1. | 2.0.2 | [GHSA](https://github.com/advisories/GHSA-qr3h-4xv7-vc63) · [Apache announcement](https://lists.apache.org/thread.html/7jw9v3qz0cdpon7fc6vsvkqp0jdt5kt0) |
| CVE-2026-123770 / GHSA-6qx5-4pcm-5fgh | High (GHSA) | Unbounded multipart/form-data and form-urlencoded request bodies bypassed the servlet container's post-size limit, and multipart temp files were not deleted; unauthenticated memory or disk exhaustion. Through 2.0.1. | 2.0.2 | [GHSA](https://github.com/advisories/GHSA-6qx5-4pcm-5fgh) · [Apache announcement](https://lists.apache.org/thread.html/78poyrrggq8tjoos5tgw508m7oylqjlg) |
| CVE-2026-120367 / GHSA-78w3-p65q-wwh7 | High (GHSA) | JSON message builders (Gson, Moshi, HTTP/2) buffered the whole request body with no size limit; unauthenticated memory exhaustion. 2.0.2 adds `jsonMaxRequestSize`. Through 2.0.1. | 2.0.2 | [GHSA](https://github.com/advisories/GHSA-78w3-p65q-wwh7) · [Apache announcement](https://lists.apache.org/thread.html/kf6goprhhtvfzb6lwnbvnors7xnq0w0r) |
| CVE-2026-120832 / GHSA-p3g5-3wm8-wh38 | Moderate (GHSA) | SSRF: building a service description from a WSDL fetched absolute `wsdl:import`, `xsd:import` and `xsd:include` locations with no scheme or host restriction; AAR and WAR deployment resolvers did the same. Through 2.0.1. | 2.0.2 | [GHSA](https://github.com/advisories/GHSA-p3g5-3wm8-wh38) · [Apache announcement](https://lists.apache.org/thread.html/bdf689rhvgg6rtlgqvvq8728f8pkj6zb) |
| CVE-2026-123779 / GHSA-f58r-c62m-574f | Moderate (GHSA) | `exposeServiceMetadata` was enforced only on `?wsdl`, `?wsdl2` and `?xsd`; other routes (packaged .wsdl/.xsd files, OpenAPI, Swagger UI, MCP catalog, services listing, WS-MEX, ping) still disclosed metadata to anonymous callers. Through 2.0.1. | 2.0.2 | [GHSA](https://github.com/advisories/GHSA-f58r-c62m-574f) · [Apache announcement](https://lists.apache.org/thread.html/qqn6c4fb8tj0ldmb97c75zzxdjrh5dl3) |
| CVE-2026-123766 / GHSA-84h8-j9vj-p626 | Moderate (GHSA) | XSS in the OpenAPI module's Swagger UI page: a Host-header-derived value was written into the page without encoding. Affects 2.0.1. | 2.0.2 | [GHSA](https://github.com/advisories/GHSA-84h8-j9vj-p626) · [Apache announcement](https://lists.apache.org/thread.html/gzxdd4gobm1kb0jdonmn4n8xhjkwlrbg) |
| CVE-2026-66713 / GHSA-fhh8-qfj4-g948 | Critical (GHSA) | Deserialization of untrusted data in the Tribes-based clustering component on Apache Tomcat (only when clustering is enabled; off by default). Unauthenticated RCE via the cluster channel. Through 2.0.0; 2.0.1 removes clustering. | 2.0.1 | [GHSA](https://github.com/advisories/GHSA-fhh8-qfj4-g948) · [Apache announcement](https://lists.apache.org/thread/fgggbv3sjjqw7p6q0j88gspt9b2rb728) |

### Earlier advisories

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2012-5785 / GHSA-wwq7-pxwc-p4rc | Moderate (GHSA) | No TLS hostname verification against certificate CN / subjectAltName (`axis2`, `axis2-transport-http`). | 1.8.0 | [GHSA](https://github.com/advisories/GHSA-wwq7-pxwc-p4rc) |
| CVE-2012-4418 / GHSA-88r4-38gc-97p4 | Moderate (GHSA) | Message forgery and authentication bypass via XML Signature wrapping. | 1.7.9 | [GHSA](https://github.com/advisories/GHSA-88r4-38gc-97p4) |
| CVE-2012-5351 / GHSA-66rx-gqx3-p98m | Moderate (GHSA) | SAML signature-exclusion attack: forged messages with an assertion lacking a Signature element. | 1.6.4 | [GHSA](https://github.com/advisories/GHSA-66rx-gqx3-p98m) |
| CVE-2010-2103 / GHSA-23x8-j7hm-5xwf | Moderate (GHSA) | XSS in the admin console `engagingglobally` page via the `modules` parameter (GHSA maps `org.apache.axis2.wso2:axis2`). | 1.6.0 | [GHSA](https://github.com/advisories/GHSA-23x8-j7hm-5xwf) |
| CVE-2010-1632 / GHSA-23vv-v25h-qwqw | High (GHSA) | DTDs in SOAP messages not rejected: file read, SSRF and DoS via crafted entity declarations (GHSA maps `org.apache.axis2.wso2:axis2`). | 1.5.2 | [GHSA](https://github.com/advisories/GHSA-23vv-v25h-qwqw) |
| CVE-2010-0219 / GHSA-9x38-862g-jg8w | High (GHSA, unreviewed) | Default `admin` / `axis2` admin-console credentials allow uploading a crafted web service for code execution, as shipped in several vendor products. | No version stated in the record; 2.0.2 ships the admin console with empty credentials, which disables it | [GHSA](https://github.com/advisories/GHSA-9x38-862g-jg8w) · [2.0.2 release notes](https://raw.githubusercontent.com/apache/axis-axis2-java-core/master/src/site/markdown/release-notes/2.0.2.md) |

Live record: https://osv.dev/list?ecosystem=Maven&q=org.apache.axis2

## Security Posture Notes

- Axis2/Java is maintained; 2.0.2 is the current release and fixes every 2026 issue above. The 2.0.2 release notes list new secure defaults: decoupled WS-Addressing responses refused, SOAP-body-namespace dispatch off, an admin console that is disabled until credentials are set, and new request-size ceilings (`multipartMaxRequestSize`, `soapMaxRequestSize`, `jsonMaxRequestSize` and others). Deployments that opt back in to the old behavior reopen the matching risk.
- Apache recommends Axis2/Java as the migration target for end-of-life Axis 1.x (see [[maven/axis/axis]], CVE-2026-90436 on CISA KEV).
- None of the eight 2026 GHSA records has a Maven package mapping, so GHSA-driven dependency scanners may not flag 2.0.1 and older.

## Dependencies of Note

- wsdl4j import resolution was the XXE path for CVE-2026-120761.

## Open Questions

- Which vendor products embedding Axis2/Java (for example, products with exposed `/axis2/services` endpoints) have shipped 2.0.2?
- Will GitHub review the 2026 records and add `org.apache.axis2` package mappings?

## Related Pages

- [[maven/axis/axis]]
- [[maven/index]]

---
*Last updated: 2026-11-22 | Sources: 17 (14 GitHub Advisory Database records, upstream 2.0.2 release notes, CISA KEV catalog 2026.11.20, Maven Central metadata)*
