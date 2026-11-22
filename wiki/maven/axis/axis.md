# axis:axis / org.apache.axis:axis — Apache Axis 1.x (maven)

**Registry:** Maven Central
**Group / Artifact:** `axis:axis` (versions 1.2-alpha-1 through 1.4) and `org.apache.axis:axis` (1.4 only)
**Current Version:** 1.4 (last release; Maven metadata for `org.apache.axis:axis` last updated 2006-04-23)
**Weekly Downloads:** unknown (as of 2026-11-22)
**Project:** https://axis.apache.org/axis/
**Repository:** https://github.com/apache/axis-axis1-java
**Security Contact:** https://www.apache.org/security/ (Apache Security Team)
**Disclosure Policy:** https://www.apache.org/security/
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-11-22 | LLM advisory-review pass | public advisory mapping for Axis 1.x | GitHub Advisory Database records (reviewed and unreviewed), CISA KEV catalog 2026.11.20, Maven Central metadata | 8 public advisories mapped, 1 on CISA KEV | [raw/advisory-review-20261122-0500/notes.md](../../../raw/advisory-review-20261122-0500/notes.md) |

## Known Vulnerabilities

Axis 1.x is end-of-life. The Apache Axis project states it does not expect to ship another 1.x release; for the 2023 and 2026 issues it publishes patches in the GitHub repository for anyone building from source. "No release" below means no fixed Axis 1.x release exists on Maven Central.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-90436 / GHSA-988f-c54m-f8jj | Critical (GHSA, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H); **CISA KEV, added 2026-11-18** | Unsafe reflection when parsing an inbound SOAP fault. A `<detail><exceptionName>` element makes Axis load the named class (running its static initializer) and, with a String `<data>` element, instantiate it before checking that it is an `AxisFault`. This happens while the engine resolves the target service, before per-service handler chains, so service-level authentication does not protect against it. Remote code execution with a suitable class on the classpath. All Axis 1.x through 1.4. The GHSA record is unreviewed and carries no Maven package mapping, so dependency scanners keyed on GHSA package data may not flag it. | No release; upstream patch commit 41f3b4e | [GHSA](https://github.com/advisories/GHSA-988f-c54m-f8jj) · [Apache announcement](https://lists.apache.org/thread/8slf0j9gz35z56t0glt5h0ncwlbn4bdz) · [patch](https://github.com/apache/axis-axis1-java/commit/41f3b4e8d04e310ca81f86b92630ab2c11d608bd) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-90436) |
| CVE-2023-51441 / GHSA-hr2c-p8rh-238h | High (GHSA) | Improper input validation lets users with access to the admin service perform SSRF. Affects through 1.3 per the record. | No release; upstream patch commit 685c309 | [GHSA](https://github.com/advisories/GHSA-hr2c-p8rh-238h) · [Apache announcement](https://lists.apache.org/thread/8nrm5thop8f82pglx4o0jg8wmvy6d9yd) |
| CVE-2023-40743 / GHSA-rmqp-9w4c-gc7w | Critical (GHSA) | `ServiceFactory.getService` permits dangerous lookup mechanisms such as LDAP; passing untrusted input can lead to DoS, SSRF or RCE. | No release; upstream patch commit 7e66753 | [GHSA](https://github.com/advisories/GHSA-rmqp-9w4c-gc7w) · [Apache announcement](https://lists.apache.org/thread/gs0qgk2mgss7zfhzdd6ftfjvm4kp7v82) |
| CVE-2019-0227 / GHSA-h9gj-rqrw-x4fq | High (GHSA) | SSRF in the Axis 1.4 distribution (expired-domain issue described by Rhino Security Labs). | No release (last affected 1.4) | [GHSA](https://github.com/advisories/GHSA-h9gj-rqrw-x4fq) |
| CVE-2018-8032 / GHSA-96jq-75wh-2658 | Moderate (GHSA) | Cross-site scripting in the default servlet/services. | No release (last affected 1.4) | [GHSA](https://github.com/advisories/GHSA-96jq-75wh-2658) |
| CVE-2014-3596 / GHSA-r53v-vm87-f72c | Moderate (GHSA) | `getCN` does not correctly verify the server hostname against the certificate, enabling TLS man-in-the-middle; incomplete fix for CVE-2012-5784. | No release (last affected 1.4) | [GHSA](https://github.com/advisories/GHSA-r53v-vm87-f72c) |
| CVE-2012-5784 / GHSA-55w9-c3g2-4rrh | Moderate (GHSA) | No TLS hostname verification against certificate CN / subjectAltName, enabling man-in-the-middle. | No release (last affected 1.4) | [GHSA](https://github.com/advisories/GHSA-55w9-c3g2-4rrh) |
| CVE-2007-2353 / GHSA-2c4w-2px5-9x3x | Moderate (GHSA) | Requesting a non-existent WSDL file reveals the installation path in the exception message (Axis 1.0). | 1.2 | [GHSA](https://github.com/advisories/GHSA-2c4w-2px5-9x3x) |

Live record: https://osv.dev/list?ecosystem=Maven&q=axis

## Security Posture Notes

- Axis 1.x has had no release since 1.4 (April 2006) and is end-of-life. Every issue above except CVE-2007-2353 is unfixed in any published artifact. The project's guidance is to migrate to a different SOAP engine such as Apache Axis2/Java, or build Axis 1.x from source with the upstream patches applied.
- CVE-2026-90436 is the first Axis 1.x entry on CISA KEV. CISA's federal due date was 2026-11-21 and the catalog flags it for forensic triage. CISA notes it "could affect an open-source component, third-party library, protocol, or proprietary implementation", so products that embed Axis 1.x are in scope even when they do not list Axis as a dependency.
- Two Maven coordinates exist. Reviewed GHSA records list both `axis:axis` and `org.apache.axis:axis`; scanners that match only one coordinate will miss the other.

## Dependencies of Note

- Exploitation of CVE-2026-90436 depends on a usable class on the application classpath; the larger the classpath (application servers, bundled frameworks), the higher the practical risk.

## Open Questions

- Which vendor products embedding Axis 1.x have issued their own advisories for CVE-2026-90436?
- Will GitHub review GHSA-988f-c54m-f8jj and add Maven package mappings?

## Related Pages

- [[maven/org.apache.axis2/axis2-kernel]]
- [[maven/commons-collections/commons-collections]]
- [[maven/index]]

---
*Last updated: 2026-11-22 | Sources: 10 (8 GitHub Advisory Database records, CISA KEV catalog 2026.11.20, Maven Central metadata)*
