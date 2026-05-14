# org.apache.zookeeper:zookeeper (maven)

**Registry:** Maven Central
**Group:** org.apache.zookeeper
**Artifact:** zookeeper
**Current Version:** 3.9.5 (Maven metadata last updated 2026-03-05)
**Project:** https://zookeeper.apache.org/
**Repository:** https://github.com/apache/zookeeper
**Security Contact:** https://zookeeper.apache.org/security.html
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-13 | OpenClaw recurring review | public advisory review | OSV / GHSA / CVE / Apache advisory mailing-list posts / release notes / Maven Central metadata | 9 public package-scoped advisories across quorum authorization, AdminServer authentication / permission checks, persistent watcher disclosure, TLS hostname verification, logging exposure, and command DoS | https://osv.dev/list?ecosystem=Maven&q=org.apache.zookeeper%3Azookeeper |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-24308 / GHSA-crhr-qqj8-rpxc | High | `ZKConfig` could log sensitive client configuration values at INFO level in 3.8.5 and 3.9.4. | 3.8.6 / 3.9.5 | https://osv.dev/vulnerability/GHSA-crhr-qqj8-rpxc |
| CVE-2026-24281 / GHSA-7xrh-hqfc-g7qr | High | `ZKTrustManager` hostname verification fell back to reverse-DNS PTR lookup when IP SAN validation failed, enabling hostname-verification bypass if an attacker could present a trusted certificate for the PTR name. | 3.8.6 / 3.9.5 | https://osv.dev/vulnerability/GHSA-7xrh-hqfc-g7qr |
| CVE-2025-58457 / GHSA-2hmj-97jw-28jh | Moderate | AdminServer snapshot / restore commands lacked the intended root-path authorization check, allowing an authenticated but insufficiently privileged client to invoke sensitive operations. | 3.9.4 | https://osv.dev/vulnerability/GHSA-2hmj-97jw-28jh |
| CVE-2024-51504 / GHSA-g93m-8x6h-g5gv | High | AdminServer IP-based authentication could be bypassed because default client-IP detection trusted spoofable HTTP headers such as `X-Forwarded-For`. | 3.9.3 | https://osv.dev/vulnerability/GHSA-g93m-8x6h-g5gv |
| CVE-2024-23944 / GHSA-r978-9m6m-6gm6 | Moderate | Persistent watcher handling missed ACL checks when a watch event triggered, exposing full znode paths below a parent the watcher owner could access. | 3.8.4 / 3.9.2; OSV also lists 3.7.2 as last affected | https://osv.dev/vulnerability/GHSA-r978-9m6m-6gm6 |
| CVE-2023-44981 / GHSA-7286-pgfv-vxvh | Critical | With SASL quorum peer authentication enabled, omitting the optional instance portion of a SASL authentication ID could skip authorization checks and let an arbitrary endpoint join the quorum. | 3.7.2 / 3.8.3 / 3.9.1 | https://osv.dev/vulnerability/GHSA-7286-pgfv-vxvh |
| CVE-2019-0201 / GHSA-2hw2-62cp-p9p7 | Moderate | `getACL()` returned ACL identifier information without a permission check, exposing digest-authentication hash material as plaintext strings. | 3.4.14 / 3.5.5 | https://osv.dev/vulnerability/GHSA-2hw2-62cp-p9p7 |
| CVE-2018-8012 / GHSA-ccqf-c5hq-77mp | High | Older quorum join behavior lacked authentication / authorization, allowing an arbitrary endpoint to join and propagate counterfeit changes. | 3.4.10 / 3.5.4-beta | https://osv.dev/vulnerability/GHSA-ccqf-c5hq-77mp |
| CVE-2017-5637 / GHSA-7cwj-j333-x7f7 | High | CPU-intensive four-letter-word commands (`wchp` / `wchc`) could be abused to consume server CPU and degrade legitimate client service. | 3.4.10 / 3.5.3 | https://osv.dev/vulnerability/GHSA-7cwj-j333-x7f7 |

## Security Posture Notes

- ZooKeeper is a coordination service with a high-integrity cluster boundary: quorum membership, ACL checks, AdminServer exposure, and TLS identity verification are more important than raw package import risk.
- Recent advisories cluster around operational control surfaces: AdminServer authentication / authorization, configuration logging, and TLS hostname verification. Treat AdminServer exposure and proxy/header handling as part of the effective package risk boundary.
- Several older advisories are configuration-sensitive: SASL quorum peer authentication, Digest authentication, four-letter-word commands, and AdminServer options change the reachable attack surface.
- The `CVE-2026-*` identifiers were present in the public OSV / GHSA / Apache evidence at review time; no private or unpublished claims were added.

## Dependencies of Note

- TLS certificate trust configuration, reverse-DNS behavior, quorum peer settings, AdminServer settings, and ACL layout materially affect exploitability.
- ZooKeeper ACLs are not recursive; AdminServer snapshot / restore guidance in the public advisory specifically calls out root ACL handling and command-disable mitigations.

## Open Questions

- Should a future pass split client library risk from server / quorum operational risk for deployments that only consume ZooKeeper as an embedded dependency?
- Which downstream platforms bundle ZooKeeper with backported fixes that should be normalized separately from upstream Maven coordinates?

## Related Pages

- [[maven/index]]

---
*Last updated: 2026-05-13 | Sources: 7 (OSV package query + OSV vulnerability records; GitHub Advisory Database records; public CVE/NVD records; Apache ZooKeeper security/advisory mailing-list references; upstream release notes and commits surfaced through OSV; Maven Central metadata; local proxy synthesis used only as drafting aid)*
