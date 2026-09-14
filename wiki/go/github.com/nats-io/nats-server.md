# NATS Server (Go)

**Registry:** pkg.go.dev — Go module `github.com/nats-io/nats-server/v2` (server binary; not imported as a library)
**Weekly Downloads:** N/A — deployed as a server binary, not imported by external Go modules; 20,699 GitHub stars, 1,949 forks (as of 2026-09-14)
**Repository:** https://github.com/nats-io/nats-server
**Security Contact:** https://github.com/nats-io/nats-server/security/policy
**Disclosure Policy:** https://github.com/nats-io/nats-server/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-09-14 | wiki maintainer | Public GHSA/CVE advisory mapping only — advisory-db search + raw advisory fetch | advisory-mapping | 24 active advisories confirmed (2019–2026); 2 withdrawn duplicates excluded | [GitHub Advisory Database](https://github.com/advisories?query=nats-io%2Fnats-server) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-13126 / GHSA-jp4j-47f9-2vc3 | High CVSS 7.5 AV:N/AC:L/PR:N | Integer overflow / wraparound — crafted requests trigger remote server crash; CWE-190 | 2.2.0 | [GHSA-jp4j-47f9-2vc3](https://github.com/advisories/GHSA-jp4j-47f9-2vc3) |
| CVE-2020-26521 / GHSA-h2fg-54x9-5qhq | High CVSS 7.5 AV:N/AC:L/PR:N | JWT nil pointer dereference — malicious User JWT causes server panic / DoS; also affects nats-io/jwt < 1.1.0; CWE-476 | nats-io/jwt 1.1.0, nats-server 2.1.9 | [GHSA-h2fg-54x9-5qhq](https://github.com/advisories/GHSA-h2fg-54x9-5qhq) |
| CVE-2020-26892 / GHSA-2c64-vj8g-vwrq | High | JWT credential expiry silently bypassed — time-based JWT expiration of user / account credentials not enforced; authenticated clients retain access after credential expiry | 2.1.9 | [GHSA-2c64-vj8g-vwrq](https://github.com/advisories/GHSA-2c64-vj8g-vwrq) |
| CVE-2020-28466 / GHSA-gwj5-3vfq-q992 | High CVSS 7.5 AV:N/AC:L/PR:N/A:H | Import loops in account imports — cyclic account export / import chains cause CPU and memory exhaustion DoS; no authentication required | 2.2.0 | [GHSA-gwj5-3vfq-q992](https://github.com/advisories/GHSA-gwj5-3vfq-q992) |
| CVE-2021-3127 / GHSA-62mh-w5cv-p88c | Critical | JWT import token permission validation bypass — server warns rather than rejects on permission mismatch; import tokens from one account usable in another account to access unauthorized subjects; affects nats-io/jwt ≤ 1.2.2 and nats-server 2.0.0–2.1.9; CWE-863 | nats-io/jwt/v2 2.0.1, nats-server 2.2.0 | [GHSA-62mh-w5cv-p88c](https://github.com/advisories/GHSA-62mh-w5cv-p88c) |
| CVE-2022-24450 / GHSA-g6w6-r76c-28j7 | High CVSS 8.1 AV:N/AC:L/PR:L | Authenticated clients can specify arbitrary target accounts in CONNECT message — allows gaining System account privileges or impersonating any account; affects 2.0.0–2.7.1 | 2.7.2 | [GHSA-g6w6-r76c-28j7](https://github.com/advisories/GHSA-g6w6-r76c-28j7) |
| CVE-2022-28357 / GHSA-vpjc-4jcv-jc29 | Critical CVSS 9.8 AV:N/AC:L/PR:N/UI:N | Directory traversal via unintended path from management account → unauthorized management actions; unauthenticated network access; CWE-22 | 2.7.4 | [GHSA-vpjc-4jcv-jc29](https://github.com/advisories/GHSA-vpjc-4jcv-jc29) |
| CVE-2022-29946 / GHSA-2h2x-8hh2-mfq8 | High CVSS 7.1 | Negative user permissions not enforced for queue subscriptions on wildcards — denied subjects accessible via queue group subscription path; CWE-863 | 2.8.2 | [GHSA-2h2x-8hh2-mfq8](https://github.com/advisories/GHSA-2h2x-8hh2-mfq8) |
| CVE-2023-47090 / GHSA-fr2g-9hjm-wr23 | High | Auth bypass via implicit no-auth user — when `accounts` block contains only the system account (`$G`), server incorrectly creates an implicit no-auth user; unauthenticated clients can connect in this specific configuration | 2.9.23, 2.10.2 | [GHSA-fr2g-9hjm-wr23](https://github.com/advisories/GHSA-fr2g-9hjm-wr23) |
| CVE-2025-30215 / GHSA-fhg8-qxh5-7q3w | Critical CVSS 9.1 AV:N/AC:L/PR:L | JetStream admin API cross-account privilege escalation — admin API endpoints allow unauthorized cross-account administrative actions (account purge, server removal, stream move) without required authorization; affects 2.2.0–2.10.26 | 2.10.27, 2.11.1 | [GHSA-fhg8-qxh5-7q3w](https://github.com/advisories/GHSA-fhg8-qxh5-7q3w) |
| CVE-2026-27571 / GHSA-qrvq-68c2-7grw | Moderate CVSS 5.9 AV:N/AC:H/PR:N | WebSocket compression bomb DoS — pre-authentication attacker sends minimal bytes triggering unbounded server memory expansion via Deflate decompression; CWE-409, CWE-770; requires WebSocket enabled | 2.11.12, 2.12.3 | [GHSA-qrvq-68c2-7grw](https://github.com/advisories/GHSA-qrvq-68c2-7grw) |
| CVE-2026-27889 / GHSA-pq2q-rcw4-3hr6 | High CVSS 9.1 AV:N/AC:L/PR:N/UI:N | WebSocket pre-auth server crash — 15-byte crafted frame exploits missing 64→32-bit cast bounds check; server panic drops all connected clients; no authentication required | 2.11.14, 2.12.5 | [GHSA-pq2q-rcw4-3hr6](https://github.com/advisories/GHSA-pq2q-rcw4-3hr6) |
| CVE-2026-29785 / GHSA-52jh-2xxh-pwh6 | High CVSS 7.5 AV:N/AC:L/PR:N | Leafnode compression panic — malicious compression header on leafnode port causes nil pointer dereference before authentication; CWE-476 | 2.11.14, 2.12.5 | [GHSA-52jh-2xxh-pwh6](https://github.com/advisories/GHSA-52jh-2xxh-pwh6) |
| CVE-2026-33215 / GHSA-fcjp-h8cc-6879 | Moderate AV:N/AC:H/PR:N/C:H/A:L | MQTT session / message hijacking — malicious MQTT Client ID reuse enables unauthorized interception of another client's messages; CWE-287 | 2.11.15, 2.12.6 | [GHSA-fcjp-h8cc-6879](https://github.com/advisories/GHSA-fcjp-h8cc-6879) |
| CVE-2026-33216 / GHSA-v722-jcv5-w7mc | High AV:N/AC:L/PR:N/S:C/C:H | MQTT plaintext password disclosure via monitoring endpoint — MQTT client passwords misidentified as JWT tokens and exposed in plaintext; monitoring port access sufficient; CWE-256 | 2.11.15, 2.12.6 | [GHSA-v722-jcv5-w7mc](https://github.com/advisories/GHSA-v722-jcv5-w7mc) |
| CVE-2026-33217 / GHSA-jxxm-27vp-c3m5 | High CVSS 7.2 | MQTT ACL bypass — ACLs not applied in `$MQTT.>` internal subject namespace; authenticated MQTT clients can access subjects outside their permission scope; CWE-863 | 2.11.15, 2.12.6 | [GHSA-jxxm-27vp-c3m5](https://github.com/advisories/GHSA-jxxm-27vp-c3m5) |
| CVE-2026-33218 / GHSA-vprv-35vv-q339 | High CVSS 7.5 AV:N/AC:L/PR:N | Leafnode pre-auth panic via malformed message — improper input validation on leafnode port causes server crash before authentication; CWE-20 | 2.11.15, 2.12.6 | [GHSA-vprv-35vv-q339](https://github.com/advisories/GHSA-vprv-35vv-q339) |
| CVE-2026-33219 / GHSA-8r68-gvr4-jh7j | Moderate CVSS 5.3 AV:N/AC:L/PR:N | WebSocket bandwidth-amplification DoS — server buffers large uncompressed WebSocket frames without authentication; memory consumption proportional to attacker bandwidth | 2.11.15, 2.12.6 | [GHSA-8r68-gvr4-jh7j](https://github.com/advisories/GHSA-8r68-gvr4-jh7j) |
| CVE-2026-33222 / GHSA-9983-vrx2-fg9c | Moderate AV:N/AC:L/PR:H/I:H | JetStream restore authorization bypass — authenticated operators can restore streams to unauthorized stream names via crafted restore requests; CWE-285 | 2.11.15, 2.12.6 | [GHSA-9983-vrx2-fg9c](https://github.com/advisories/GHSA-9983-vrx2-fg9c) |
| CVE-2026-33223 / GHSA-pwx7-fx9r-hr4h | Moderate CVSS 5.4 AV:N/AC:L/PR:L/S:C | Incomplete `Nats-Request-Info` header stripping — attacker-injected identity header reaches downstream services, enabling caller impersonation; CWE-290 | 2.11.15, 2.12.6 | [GHSA-pwx7-fx9r-hr4h](https://github.com/advisories/GHSA-pwx7-fx9r-hr4h) |
| CVE-2026-33246 / GHSA-55h8-8g96-x4hj | Moderate CVSS 5.1 AV:N/AC:L/PR:L/S:C/C:L/I:L | Leafnode identity spoofing — leafnode connections can inject / spoof `Nats-Request-Info` headers, enabling account / user impersonation to hub-connected services | 2.11.15, 2.12.6 | [GHSA-55h8-8g96-x4hj](https://github.com/advisories/GHSA-55h8-8g96-x4hj) |
| CVE-2026-33247 / GHSA-x6g4-f6q3-fqvv | High AV:N/AC:H/PR:N/C:H/I:H | Credentials exposed via monitoring `/debug/vars` endpoint — server credentials passed as argv visible through monitoring port to any network-accessible observer; CWE-215 | 2.11.15, 2.12.6 | [GHSA-x6g4-f6q3-fqvv](https://github.com/advisories/GHSA-x6g4-f6q3-fqvv) |
| CVE-2026-33248 / GHSA-3f24-pcvm-5jqc | Moderate CVSS 5.4 AV:N/AC:H/PR:L/C:L/I:L | mTLS Subject DN matching bypass in `verify_and_map` — incorrect DN comparison allows certificate-authenticated clients to gain unauthorized account access | 2.11.15, 2.12.6 | [GHSA-3f24-pcvm-5jqc](https://github.com/advisories/GHSA-3f24-pcvm-5jqc) |
| CVE-2026-33249 / GHSA-8m2x-3m6q-6w8j | Moderate AV:N/AC:L/PR:L/I:L | Message tracing redirect — authenticated clients can redirect server-generated trace messages to subjects outside their publish permissions via trace headers; CWE-863 | 2.11.15, 2.12.6 | [GHSA-8m2x-3m6q-6w8j](https://github.com/advisories/GHSA-8m2x-3m6q-6w8j) |

*Total: 24 active GHSA-reviewed advisories confirmed (2 withdrawn duplicates excluded: GHSA-9r5x-fjv3-q6h4 withdrawn duplicate of GHSA-62mh-w5cv-p88c; GHSA-4frv-5fj6-4p25 withdrawn duplicate of GHSA-fr2g-9hjm-wr23). Additional advisories may exist for the separate `github.com/nats-io/nats-streaming-server` and `github.com/nats-io/jwt` / `github.com/nats-io/jwt/v2` packages (not mapped here). Full OSV query not available; see primary source links.*

## Security Posture Notes

NATS Server (`nats-io/nats-server`) is a high-performance cloud-native messaging system. It underpins the NATS.io ecosystem — a CNCF project widely deployed in microservices, IoT, edge computing, and financial infrastructure. The server is written in Go and distributed as a single statically linked binary.

**Maintainer and disclosure:** Actively maintained by Synadia Communications. Security policy and private reporting at https://github.com/nats-io/nats-server/security/policy. Synadia has consistently issued coordinated batch disclosures with same-day patches; the March 2026 batch (14 advisories fixed in 2.11.15/2.12.6) is the largest single-release security cluster to date.

**Recurring vulnerability classes:**
- **Pre-authentication DoS** (CVE-2026-27889, CVE-2026-29785, CVE-2026-33218, CVE-2026-33219, CVE-2026-27571): Multiple vectors exist for crashing or resource-exhausting the server before any authentication. Deployments exposing leafnode, WebSocket, or cluster ports to untrusted networks are highest-risk.
- **Authorization / permission bypass** (CVE-2021-3127, CVE-2022-24450, CVE-2022-29946, CVE-2023-47090, CVE-2026-33217, CVE-2026-33222): Account isolation and permission enforcement have had recurring gaps across JWT, queue groups, MQTT ACLs, and JetStream management APIs.
- **Credential / identity exposure** (CVE-2020-26892, CVE-2026-33216, CVE-2026-33247): Credentials have been exposed via monitoring endpoints and through inadequate expiry enforcement.
- **Identity spoofing** (CVE-2026-33223, CVE-2026-33246, CVE-2026-33215): `Nats-Request-Info` header stripping has been incomplete in multiple release windows; MQTT session semantics have allowed Client ID-based impersonation.

**Current stable:** v2.14.6 (as of 2026-09-14). The minimum safe version as of the March 2026 batch is **v2.11.15** or **v2.12.6**; any deployment on earlier 2.x versions should upgrade urgently.

**Deployment exposure surface:** Unlike most library packages, nats-server exposes a network surface on NATS (4222), Cluster (6222), Monitor HTTP (8222), Leafnode (7422), and WebSocket (optional) ports. Each subsystem has had independent CVEs. Network segmentation of these ports is a mandatory compensating control.

## Dependencies of Note

- `github.com/nats-io/jwt` / `github.com/nats-io/jwt/v2`: JWT parsing library used for NKey-based authentication; several server advisories (CVE-2020-26521, CVE-2020-26892, CVE-2021-3127) are rooted in jwt library bugs that manifest in the server. Separate advisory tracking recommended.
- `github.com/nats-io/nats-streaming-server` (deprecated): Streaming server built on nats-server; CVE-2022-24450 and CVE-2022-29946 also affect streaming server; streaming server is deprecated and should be migrated to JetStream.

## Open Questions

- Whether v2.14.x introduces new vulnerabilities or backport gaps — the March 2026 batch only covers ≤ v2.12.6; v2.13 and v2.14 line patch status should be confirmed against the NATS security page.
- NATS operator mode (decentralized JWT auth) has distinct trust boundaries from credential-based auth — a focused mapping of operator-mode-specific advisories against the JWT library would add value.
- The `nats-server` binary is widely used as a sidecar in Kubernetes via NATS Operator and Helm chart — Kubernetes deployment configurations (service port exposure, network policies) deserve a separate dependency cross-reference.

## Related Pages

- [[kubernetes/helm]] — Helm package manager (NATS Helm chart packaging is downstream)
- [[go/github.com/redis/go-redis]] — peer Go server-side client advisory reference
- [[go/index]]

---
*Last updated: 2026-09-14 | Sources: 25 (24 GHSA advisory JSON files + GitHub API metadata)*
