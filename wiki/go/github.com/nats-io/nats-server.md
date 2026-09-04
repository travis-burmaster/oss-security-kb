# nats-server (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (server binary distributed via direct download / Docker / Helm, not imported as a Go library)
**Repository:** https://github.com/nats-io/nats-server
**Security Contact:** security@nats.io (listed in SECURITY.md)
**Disclosure Policy:** https://github.com/nats-io/nats-server/security/policy (coordinated disclosure; 90-day embargo)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-09-04 | oss-security-kb pass | advisory-database | public-advisories | 14 advisories mapped (2019–2026) | github/advisory-database |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-13126 | High CVSS 7.5 AV:N | Integer overflow in NATS Server < 2.2.0 allows remote crash via crafted request (CWE-190) | ≥ 2.2.0 | [GHSA-jp4j-47f9-2vc3](https://github.com/advisories/GHSA-jp4j-47f9-2vc3) |
| CVE-2020-26521 | High CVSS 7.5 AV:N | Malicious NATS account creates User JWT with abnormal state → nil dereference crash in nats-io/jwt; affects nats-server deployments trusting third-party accounts | nats-server ≥ 2.1.9 | [GHSA-h2fg-54x9-5qhq](https://github.com/advisories/GHSA-h2fg-54x9-5qhq) |
| CVE-2020-28466 | High CVSS 7.5 AV:N | Export/import cycle between accounts → CPU/memory exhaustion and crash; requires at least two accounts; fixed with cycle detection in 2.2.0 | ≥ 2.2.0 | [GHSA-gwj5-3vfq-q992](https://github.com/advisories/GHSA-gwj5-3vfq-q992) |
| CVE-2021-3127 | Critical AV:N | Import Token bindings mishandled in nats-io/jwt/v2: malicious account can import any exported Subject from another account — cross-account data access without authorization | nats-server ≥ 2.2.0; jwt/v2 ≥ 2.0.1 | [GHSA-62mh-w5cv-p88c](https://github.com/advisories/GHSA-62mh-w5cv-p88c) |
| CVE-2022-28357 | Critical CVSS 9.8 AV:N/AC:L/PR:N | Directory traversal via "unintended path to a management action from a management account" (CWE-22); no authentication required in affected configurations; enables unauthorized file system access | ≥ 2.7.4 | [GHSA-vpjc-4jcv-jc29](https://github.com/advisories/GHSA-vpjc-4jcv-jc29) |
| CVE-2023-47090 | Moderate | Implicit `$G` user in an `authorization {}` config block can sometimes be used for unauthenticated access even when per-user accounts were intended; affects 2.2.0–2.9.22 and 2.10.0–2.10.1 | 2.9.23 / 2.10.2 | [GHSA-fr2g-9hjm-wr23](https://github.com/advisories/GHSA-fr2g-9hjm-wr23) |
| CVE-2025-30215 | Critical AV:N/PR:L | JetStream admin APIs lack per-account authorization: any JetStream user can call account-purge, server-remove, stream-move, and stream-cancel-move against assets in _other_ accounts, enabling "total destruction of JetStream configuration and data" across account boundaries | 2.10.27 / 2.11.1 | [GHSA-fhg8-qxh5-7q3w](https://github.com/advisories/GHSA-fhg8-qxh5-7q3w) |
| CVE-2026-27571 | Moderate AV:N/AC:H/PR:N/A:H | WebSocket handler does not bound memory during decompression of compressed messages → compression bomb triggers OOM crash; no authentication required; affects WebSocket-enabled deployments | 2.11.12 / 2.12.3 | [GHSA-qrvq-68c2-7grw](https://github.com/advisories/GHSA-qrvq-68c2-7grw) |
| CVE-2026-29785 | High AV:N/PR:N | Malicious remote NATS server triggers a server panic via compression negotiation on the leafnode port — pre-authentication; affects hub/spoke deployments with compression enabled; workaround: `compression: off` on leafnode | 2.11.14 / 2.12.5 | [GHSA-52jh-2xxh-pwh6](https://github.com/advisories/GHSA-52jh-2xxh-pwh6) |
| CVE-2026-33215 | Moderate AV:N/AC:H/PR:N | MQTT Client ID malfeasance allows session and message hijacking via the MQTT client interface (CWE-287); no workaround | 2.11.15 / 2.12.6 | [GHSA-fcjp-h8cc-6879](https://github.com/advisories/GHSA-fcjp-h8cc-6879) |
| CVE-2026-33217 | High AV:N/PR:L | ACLs not applied in the `$MQTT.>` subject namespace; any authenticated MQTT client can access messages in the `$MQTT.>` namespace belonging to other clients, bypassing ACL restrictions | 2.11.15 / 2.12.6 | [GHSA-jxxm-27vp-c3m5](https://github.com/advisories/GHSA-jxxm-27vp-c3m5) |
| CVE-2026-33218 | High AV:N/AC:L/PR:N | Unauthenticated client connecting to leafnode port crashes server via crafted malformed message before authentication completes; workaround: restrict leafnode port via firewall or disable if unused | 2.11.15 / 2.12.6 | [GHSA-vprv-35vv-q339](https://github.com/advisories/GHSA-vprv-35vv-q339) |
| CVE-2026-33246 | Moderate AV:N/PR:L | Leafnode connections can spoof the `Nats-Request-Info` header; leafnodes are not fully trusted unless the system account is also bridged, enabling identity spoofing for request routing metadata | 2.11.15 / 2.12.6 | [GHSA-55h8-8g96-x4hj](https://github.com/advisories/GHSA-55h8-8g96-x4hj) |
| CVE-2026-33248 | Moderate AV:N/AC:H/PR:L | Incorrect Subject DN matching in mTLS `verify_and_map` authentication: certain RDN construction patterns bypass client certificate verification; requires a valid certificate from a trusted CA with an unusual DN | 2.11.15 / 2.12.6 | [GHSA-3f24-pcvm-5jqc](https://github.com/advisories/GHSA-3f24-pcvm-5jqc) |

*14 advisories mapped (2019–2026). Total GHSA search results for nats-server: 33 — remaining records not reviewed in this pass may cover the nats-io/jwt and nats-io/nats.go companion packages or older withdrawn duplicates.*

## Security Posture Notes

NATS Server is a high-performance, cloud-native messaging system and CNCF project (~15,000+ GitHub stars). It is widely deployed as infrastructure for microservices, IoT, and edge messaging, with over 40 client implementations. The server is maintained by Synadia Communications.

**Disclosure process:** NATS maintains a documented security policy at https://github.com/nats-io/nats-server/security/policy with a security@nats.io contact and coordinated 90-day embargo process. The project has a consistent track record of releasing advisories alongside patches.

**Advisory patterns (2019–2026):**
- **Account/authorization boundary failures** are the dominant category: CVE-2021-3127 (cross-account token import), CVE-2022-28357 (management account path traversal), CVE-2023-47090 (implicit $G user bypass), and CVE-2025-30215 (JetStream cross-account admin API) all reflect the complexity of NATS's multi-tenant account model. CVE-2025-30215 is particularly severe — it allowed complete destruction of another account's JetStream configuration.
- **Pre-authentication DoS on protocol ports:** CVE-2026-29785 (leafnode compression), CVE-2026-33218 (leafnode malformed message), and CVE-2026-27571 (WebSocket compression bomb) are all unauthenticated and require only network access to the relevant port.
- **MQTT interface:** CVE-2026-33215 (session hijack) and CVE-2026-33217 (ACL namespace bypass) both affect the MQTT protocol bridge added in NATS 2.2.0; operators not using MQTT can disable the bridge.
- **mTLS auth:** CVE-2026-33248 affects the `verify_and_map` mode; operators using standard TLS client auth (without the `map` functionality) are unaffected.

**2026 March cluster (6 CVEs, fixed 2.11.15 / 2.12.6):** Six advisories were released simultaneously — CVE-2026-29785 (fixed one release earlier, 2.11.14 / 2.12.5), CVE-2026-33215/33217/33218/33246/33248. Operators should verify they are running ≥ 2.11.15 or ≥ 2.12.6.

**Dependency risk:** nats-server bundles nats-io/jwt and nats-io/nkeys; the nats-io/jwt library itself had Critical (CVE-2021-3127) and High (CVE-2020-26521) advisories that affect nats-server when third-party accounts are trusted.

**Latest stable:** v2.14.6 (2026-08-27). Current unaffected by all mapped advisories.

## Dependencies of Note

- **github.com/nats-io/jwt/v2** — embedded NATS JWT library; CVE-2021-3127 (Critical import token binding bypass) and CVE-2020-26521 (High nil-deref via crafted JWT) affect this dependency and propagate to nats-server
- **github.com/nats-io/nkeys** — Ed25519 key pair handling for NATS; no public advisory on record as of this pass
- Standard Go TLS / net/http stack; inherits golang.org/x/crypto and net/http vulnerabilities

## Open Questions

- 19 of 33 GHSA records in github/advisory-database not individually reviewed; future pass should enumerate them to confirm scope (whether they are for nats-io/nats.go client, nats-io/jwt, nats-io/nats-server v1.x, or additional server advisories)
- GHSA-fr2g-9hjm-wr23 (CVE-2023-47090 primary) only encountered via its withdrawn duplicate; the primary should be reviewed directly to confirm affected version range
- nats-io/nkeys not searched in advisory databases in this pass

## Related Pages

- [[go/github.com/golang-jwt/jwt]]
- [[go/index]]

---
*Last updated: 2026-09-04 | Sources: 14 GHSA advisories (github/advisory-database via raw.githubusercontent.com); pkg.go.dev*
