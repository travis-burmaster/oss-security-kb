# CoreDNS (Kubernetes)

**Registry:** pkg.go.dev
**Weekly Downloads:** deployed in all Kubernetes clusters since v1.13 (2018); ~12.3k GitHub stars; CNCF graduated
**Repository:** https://github.com/coredns/coredns
**Security Contact:** security@coredns.io
**Disclosure Policy:** https://github.com/coredns/coredns/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-26017 / GHSA-c9v3-4pv7-87pr | High (CVSS 7.7) | ACL bypass via TOCTOU — `acl` plugin evaluates before `rewrite`, allowing access-control bypass via rewrite rules that expose restricted internal services (CWE-367) | 1.14.2 | [GHSA-c9v3-4pv7-87pr](https://github.com/advisories/GHSA-c9v3-4pv7-87pr) |
| CVE-2026-33190 / GHSA-qhmp-q7xh-99rh | High (CVSS 7.5/8.7) | TSIG authentication bypass on DoT/DoH/DoH3/DoQ/gRPC — `tsig` plugin trusts transport-layer `TsigStatus()` return value rather than performing its own HMAC verification; DoT/DoH/etc. transports always return nil, accepting any request as authenticated (CWE-287, CWE-303) | 1.14.3 | [GHSA-qhmp-q7xh-99rh](https://github.com/advisories/GHSA-qhmp-q7xh-99rh) |
| CVE-2026-35579 / GHSA-vp29-5652-4fw9 | High (CVSS 7.5/6.3) | TSIG authentication bypass on gRPC/QUIC — checks key name existence but skips `dns.TsigVerify()`; DoH/DoH3 hardcode `TsigStatus()` to nil, accepting any TSIG record regardless of key name or MAC validity (CWE-287) | 1.14.3 | [GHSA-vp29-5652-4fw9](https://github.com/advisories/GHSA-vp29-5652-4fw9) |
| CVE-2026-33489 / GHSA-h8mm-c463-wjq3 | High (CVSS 7.5/6.3) | `transfer` plugin subzone ACL bypass — `longestMatch()` uses lexicographic string comparison instead of longest DNS label match, allowing a permissive parent-zone rule to override a restrictive subzone rule and enable unauthorized AXFR/IXFR (CWE-862, CWE-863) | 1.14.3 | [GHSA-h8mm-c463-wjq3](https://github.com/advisories/GHSA-h8mm-c463-wjq3) |
| CVE-2026-32936 / GHSA-63cw-r7xf-jmwr | High (CVSS 7.5/8.7) | DoH GET CPU/memory amplification DoS — expensive URL parsing, base64 decoding, and DNS message unpacking performed on oversized `dns=` query parameters before input validation rejects them (CWE-400) | 1.14.3 | [GHSA-63cw-r7xf-jmwr](https://github.com/advisories/GHSA-63cw-r7xf-jmwr) |
| CVE-2026-32934 / GHSA-2wpx-qpw2-g5h5 | High (CVSS 7.5/8.7) | DoQ worker pool DoS regression — goroutine spawned per accepted QUIC stream even with `worker_pool_size` configured; workers block indefinitely in `io.ReadFull()` with no per-stream read deadline; attacker sends 1 byte/stream to stall all workers and exhaust memory (regression of CVE-2025-47950 fix; CWE-770) | 1.14.3 | [GHSA-2wpx-qpw2-g5h5](https://github.com/advisories/GHSA-2wpx-qpw2-g5h5) |
| CVE-2026-26018 / GHSA-h75p-j8xm-m278 | High (CVSS 7.5) | Loop plugin crash-on-demand DoS — self-test qname seeded with `time.Now().UnixNano()` (predictable PRNG; CWE-337); attacker with log-read access observes qname and sends 3 matching HINFO queries to crash the server via `log.Fatalf()` / `os.Exit(1)` | 1.14.2 | [GHSA-h75p-j8xm-m278](https://github.com/advisories/GHSA-h75p-j8xm-m278) |
| CVE-2025-47950 / GHSA-cvx7-x8pj-x2gw | High (CVSS 7.5) | DoQ memory exhaustion — DoQ server spawns a new goroutine per incoming QUIC stream with no limit on concurrent streams or goroutines, enabling remote OOM crash (CWE-770); introduced `max_streams` and `worker_pool_size` options in fix | 1.12.2 | [GHSA-cvx7-x8pj-x2gw](https://github.com/advisories/GHSA-cvx7-x8pj-x2gw) |
| CVE-2023-28452 / GHSA-hfmw-7g3m-gj6q | High (CVSS 5.9/8.2) | TuDoor attack DoS — attacker can forge a DNS response targeting the resolver's source port without guessing TXID, causing the resolver to discard valid responses and enter a non-responsive state (CWE-290) | 1.11.0 | [GHSA-hfmw-7g3m-gj6q](https://github.com/advisories/GHSA-hfmw-7g3m-gj6q) |
| CVE-2025-68151 / GHSA-527x-5wrf-22m2 | Moderate | gRPC/HTTPS/HTTP3 missing connection and stream limits DoS; gRPC additionally lacks DNS-spec message-size validation (accepts ~4 MB rather than the 64 KB DNS spec limit) (CWE-770) | 1.14.0 | [GHSA-527x-5wrf-22m2](https://github.com/advisories/GHSA-527x-5wrf-22m2) |
| CVE-2024-0874 / GHSA-m9w6-wp3h-vq8g | Moderate (CVSS 5.3) | Cache plugin returns invalid cache entries due to incorrectly implemented caching (CWE-524); integrity impact on DNS resolution | 1.11.2 | [GHSA-m9w6-wp3h-vq8g](https://github.com/advisories/GHSA-m9w6-wp3h-vq8g) |
| CVE-2022-2837 / GHSA-h828-v5pv-33qx | Moderate (CVSS 6.1) | Namespace-based external TLD redirect — users who create namespaces/projects matching an external TLD can redirect traffic for that TLD to pods they control (CWE-601, CWE-923); no CoreDNS code fix, mitigate via Kubernetes RBAC restricting namespace creation | none (last affected 1.9.3) | [GHSA-h828-v5pv-33qx](https://github.com/advisories/GHSA-h828-v5pv-33qx) |
| CVE-2022-2835 / GHSA-ch7v-37xg-75ph | Moderate (CVSS 4.4) | Namespace-based internal FQDN redirect — malicious users can reroute internal `<service>.<namespace>.svc` calls to pods they control (CWE-923); no CoreDNS code fix, mitigate via Kubernetes RBAC restricting namespace creation | none (last affected 1.9.3) | [GHSA-ch7v-37xg-75ph](https://github.com/advisories/GHSA-ch7v-37xg-75ph) |
| CVE-2023-30464 / GHSA-h92q-fgpp-qhrq | Moderate (CVSS 3.7) | Cache poisoning via birthday attack — attacker can inject forged DNS responses exploiting TXID/source-port prediction probability (CWE-290); no fix version recorded | none recorded | [GHSA-h92q-fgpp-qhrq](https://github.com/advisories/GHSA-h92q-fgpp-qhrq) |
| CVE-2019-19794 / GHSA-gv9j-4w24-q7vx | Moderate | Predictable TXID via `math/rand` — CoreDNS used the go DNS library before 1.1.25 which seeded TXID from `math/rand`, enabling DNS response forgery | 1.6.6 | [GHSA-gv9j-4w24-q7vx](https://github.com/advisories/GHSA-gv9j-4w24-q7vx) |

## Security Posture Notes

CoreDNS is the default DNS server for Kubernetes clusters since v1.13 (December 2018) and a CNCF graduated project (~12.3k GitHub stars). It is deployed in virtually every production Kubernetes cluster, making it a high-value target for denial-of-service attacks and DNS manipulation.

The April 2026 advisory cluster (5 advisories, all fixed in 1.14.3) is the most significant in CoreDNS history and appears to reflect a coordinated security audit: two independent TSIG authentication bypass paths (CVE-2026-33190, CVE-2026-35579), one ACL bypass in the `transfer` plugin (CVE-2026-33489), one DoH GET amplification DoS (CVE-2026-32936), and a DoQ goroutine exhaustion regression (CVE-2026-32934 — a regression of the 1.12.2 fix for CVE-2025-47950). Clusters not yet on 1.14.3 remain exposed to all five.

The March 2026 cluster (CVE-2026-26017, CVE-2026-26018) highlights two architectural risks: plugin evaluation ordering between `acl` and `rewrite` is a TOCTOU flaw in the security model, and the loop plugin's crash-on-demand primitive for anyone with log read access is a denial-of-service risk in multi-tenant environments.

CVE-2022-2835 and CVE-2022-2837 (namespace-based traffic redirect, no code fix) are design-level trust-boundary limitations: when untrusted tenants can create namespaces whose names match external domains, CoreDNS cannot distinguish legitimate internal service traffic from attacker-controlled pods. These require Kubernetes-level RBAC mitigations, not a CoreDNS patch.

## Dependencies of Note

- `github.com/miekg/dns` — foundational Go DNS library; CoreDNS is the primary consumer; the historical predictable-TXID issue (GHSA-44r7-7p62-q3fr) in miekg/dns < 1.1.25 is the upstream root cause of CVE-2019-19794 in CoreDNS. See [[go/github.com/miekg/dns]].

## Open Questions

- What is the CoreDNS version distribution across Kubernetes clusters in the wild? Many clusters may still run 1.11.x or earlier (exposed to the 2026 cluster) as Kubernetes upgrades do not always update embedded components simultaneously.
- Are the two namespace-based redirect advisories (CVE-2022-2835, CVE-2022-2837) tracked and mitigated by the Kubernetes SIG Security team at the admission-control level?
- Does the cache poisoning birthday-attack advisory (CVE-2023-30464) have a known workaround or planned fix in a future release?
- GHSA-93mf-426m-g6x9 (September 2025, unreviewed in this pass) — review in a future pass.

## Related Pages

- [[kubernetes/kube-apiserver]]
- [[kubernetes/index]]
- [[go/github.com/miekg/dns]]

---
*Last updated: 2026-08-24 | Sources: 15*
