# org.apache.kafka:kafka-clients (Maven)

**Registry:** Maven Central  
**Latest Version:** 4.2.0 (Maven Central search API during 2026-05-12 review)  
**Repository:** https://github.com/apache/kafka  
**Security Contact:** Apache Security Team / Kafka vulnerability process  
**Disclosure Policy:** https://kafka.apache.org/community/cve-list/  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-12 | OpenClaw recurring review | package-level public advisory mapping for Maven `org.apache.kafka:kafka-clients` | public-source curation from OSV.dev package and vulnerability records, GitHub Advisory Database aliases surfaced by OSV, public CVE/NVD links, Apache Kafka public CVE list, Maven Central metadata, upstream issue / PR / commit references surfaced by the public records, and local proxy-assisted drafting | Added initial Maven page mapping 7 public package-scoped advisories across OAUTHBEARER / JWT validation, producer buffer-pool data integrity, arbitrary file / URL access through OAuth bearer endpoint configuration, ConfigProvider filesystem read, sensitive DEBUG logging, timing / session-boundary behavior, and authenticated-client impersonation. | https://osv.dev/list?ecosystem=Maven&q=org.apache.kafka%3Akafka-clients |

## Known Vulnerabilities

This table is a package-level public advisory map for `org.apache.kafka:kafka-clients`, cross-checked against Apache Kafka's public CVE list where the maintainer page covered the same CVE. Exposure is strongly configuration-dependent; this page does not claim every Kafka client deployment is affected by every row.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2017-12610 / GHSA-xm78-4m3g-7wm7 | MODERATE | Authenticated Kafka clients could impersonate other users in affected PLAINTEXT / SASL_SSL boundary conditions. | 0.10.2.2, 0.11.0.2 | https://osv.dev/vulnerability/GHSA-xm78-4m3g-7wm7 ; https://www.cve.org/CVERecord?id=CVE-2017-12610 |
| CVE-2021-38153 / GHSA-3j6g-hxx5-3q26 | MODERATE | Timing / observable-discrepancy issue affecting Kafka Connect and clients. | 2.6.3, 2.7.2, 2.8.1 | https://osv.dev/vulnerability/GHSA-3j6g-hxx5-3q26 ; https://kafka.apache.org/community/cve-list/#CVE-2021-38153 |
| CVE-2024-31141 / GHSA-2x2g-32r7-p4x8 | MODERATE | Automatic `ConfigProvider` loading could allow privilege escalation to filesystem read access in affected client configurations. | 3.7.1 | https://osv.dev/vulnerability/GHSA-2x2g-32r7-p4x8 ; https://kafka.apache.org/community/cve-list/#CVE-2024-31141 |
| CVE-2025-27817 / GHSA-vgq5-3255-v292 | MODERATE | OAuth bearer token / JWKS endpoint URL configuration could enable arbitrary file read or SSRF when untrusted parties can influence Kafka client configuration. | 3.9.1, 4.0.0 | https://osv.dev/vulnerability/GHSA-vgq5-3255-v292 ; https://kafka.apache.org/community/cve-list/#CVE-2025-27817 |
| CVE-2026-35554 / GHSA-5qcv-4rpc-jp93 | HIGH | Producer buffer-pool race condition could corrupt batches and silently deliver messages to unintended topics, affecting confidentiality and integrity. | 3.9.2, 4.0.2, 4.1.2, 4.2.0 | https://osv.dev/vulnerability/GHSA-5qcv-4rpc-jp93 ; https://kafka.apache.org/community/cve-list/#CVE-2026-35554 |
| CVE-2026-33558 / GHSA-wf66-mphr-4c4r | MODERATE | `NetworkClient` DEBUG logging could expose sensitive request / response information when DEBUG level is enabled. | 3.9.2, 4.0.1, 4.1.0 | https://osv.dev/vulnerability/GHSA-wf66-mphr-4c4r ; https://kafka.apache.org/community/cve-list/#CVE-2026-33558 |
| CVE-2026-33557 / GHSA-28jg-cgg7-j4wc | CRITICAL | Kafka's default OAUTHBEARER validator in affected 4.1.x brokers accepted JWTs without validating signature, issuer, or audience when OAUTHBEARER was configured. | 4.1.2, 4.2.0 | https://osv.dev/vulnerability/GHSA-28jg-cgg7-j4wc ; https://kafka.apache.org/community/cve-list/#CVE-2026-33557 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.apache.kafka%3Akafka-clients*

## Security Posture Notes

- `kafka-clients` is a high-blast-radius Java dependency because it is the standard producer / consumer / admin client library used across JVM data pipelines, stream-processing services, and Kafka-integrated platforms.
- The public package-scoped record is compact but high-signal. Recent 2025-2026 advisories include OAuth bearer endpoint configuration abuse, sensitive client log exposure, OAUTHBEARER JWT validation, and producer buffer-pool data corruption / misrouting.
- Several advisories are configuration-dependent. Important conditions include OAUTHBEARER usage, whether untrusted parties can influence client configuration, DEBUG logging for `NetworkClient`, PLAINTEXT or SASL boundary choices, and exact producer timeout / in-flight request behavior.
- Apache's public CVE list gives line-specific guidance. During this review, Maven Central listed `4.2.0` as the latest version, while fixed versions in public advisories also include maintained 3.9.x, 4.0.x, and 4.1.x patch lines.
- The 2026 producer race advisory is especially operationally important because the maintainer description frames it as silent data corruption / misrouting rather than a simple crash. Consumers should verify the exact `kafka-clients` version that applications ship, including transitive dependencies from stream-processing frameworks or connectors.
- This review did not perform active vulnerability hunting, exploit validation, or live target testing. It only normalized already-public advisory, CVE, maintainer, and release metadata.

## Dependencies of Note

- `kafka-clients` is commonly embedded transitively by Kafka Connect plugins, stream-processing frameworks, application frameworks, and vendor clients. Remediation should inventory both direct and transitive copies.
- OAuth bearer configuration is a recurring boundary in the recent record. Applications that expose Kafka client or connector configuration to tenants or operators need tighter allow-listing and patch verification than applications with static, fully trusted configs.

## Open Questions

- Should future passes split Kafka broker, Connect, and `kafka-clients`-only exposure into separate pages, or keep this Maven coordinate as the client-library anchor with links to broader Kafka CVEs?
- Which high-usage frameworks pin affected `kafka-clients` versions after the 3.9.2 / 4.0.2 / 4.1.2 / 4.2.0 fix train?
- Are there public postmortems or downstream advisories showing real-world reachability for the producer message-misrouting race in common application patterns?

## Related Pages

- [[maven/index]]
- [[maven/io.netty/netty-codec-http]]
- [[maven/org.apache.tomcat.embed/tomcat-embed-core]]
- [[go/google.golang.org/grpc]]

---
*Last updated: 2026-05-12 | Sources: OSV package query and individual vulnerability records for `org.apache.kafka:kafka-clients`; GitHub Advisory Database aliases surfaced by OSV; public CVE/NVD records; Apache Kafka public CVE list; Maven Central metadata; upstream issue / PR / commit references surfaced by public records; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid.*
