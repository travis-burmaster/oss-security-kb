# etcd (Go / go.etcd.io/etcd/v3)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (critical Kubernetes infrastructure; consumed indirectly via the Kubernetes ecosystem)
**Repository:** https://github.com/etcd-io/etcd
**Security Contact:** security@etcd.io
**Disclosure Policy:** https://github.com/etcd-io/etcd/blob/main/security/security-release-process.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2020 | Trail of Bits (CNCF-commissioned) | full-source | manual | Multiple findings; full report public | [etcd Security Audit 2020 (PDF)](https://github.com/etcd-io/etcd/blob/master/security/SECURITY_AUDIT.pdf) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-5gjm-fj42-x983 / CVE-2018-1098 | High (CVSS 9.8) | CSRF in etcd ≤ 3.3.1 allows unauthenticated attacker to create in-order keys via POST from a malicious page | 3.4.0 | [GHSA-5gjm-fj42-x983](https://github.com/advisories/GHSA-5gjm-fj42-x983) |
| GHSA-h6xx-pmxh-3wgp / CVE-2018-16886 | High (CVSS 9.8) | RBAC + client-cert-auth bypass: TLS CN matching an RBAC username allows any trusted-cert holder to authenticate as that user via gRPC-gateway | 3.2.26, 3.3.11 | [GHSA-h6xx-pmxh-3wgp](https://github.com/advisories/GHSA-h6xx-pmxh-3wgp) |
| GHSA-p4g4-wgrh-qrg2 / CVE-2020-15106 | Low (CVSS 3.1) | Forged WAL entry with oversized frame length causes Raft participant panic (DoS) — no size validation in WAL decode | 3.3.23, 3.4.10 | [GHSA-p4g4-wgrh-qrg2](https://github.com/advisories/GHSA-p4g4-wgrh-qrg2) |
| GHSA-m332-53r6-2w93 / CVE-2020-15112 | Low (CVSS 3.1) | WAL `ReadAll` panics on entry with index exceeding total entry count — attacker-controlled WAL triggers Raft DoS | 3.3.23, 3.4.10 | [GHSA-m332-53r6-2w93](https://github.com/advisories/GHSA-m332-53r6-2w93) |
| GHSA-2xhq-gv6c-p224 / CVE-2020-15114 | High (CVSS 7.1) | Gateway self-referential endpoint loop exhausts file descriptors — authenticated user can trigger DoS | 3.3.23, 3.4.10 | [GHSA-2xhq-gv6c-p224](https://github.com/advisories/GHSA-2xhq-gv6c-p224) |
| GHSA-wr2v-9rpq-c35q / CVE-2020-15136 | Moderate (CVSS 7.5) | Gateway TLS validation applies only to DNS SRV-discovered endpoints; manually specified `--endpoints` flags bypass TLS authentication | 3.3.23, 3.4.10 | [GHSA-wr2v-9rpq-c35q](https://github.com/advisories/GHSA-wr2v-9rpq-c35q) |
| GHSA-4993-m7g5-r9hh / CVE-2020-15115 | Moderate (CVSS 7.5) | No minimum password length enforced on user create/update — enables brute-force of short credentials | 3.3.23, 3.4.10 | [GHSA-4993-m7g5-r9hh](https://github.com/advisories/GHSA-4993-m7g5-r9hh) |
| GHSA-528j-9r78-wffx | Low | User credentials (login + password) written in plaintext to WAL log on each authentication — WAL file exposure leaks credentials | 3.3.23, 3.4.10 | [GHSA-528j-9r78-wffx](https://github.com/advisories/GHSA-528j-9r78-wffx) |
| GHSA-9gp7-6833-wv89 | Low | Negative cluster-node size value during service discovery causes out-of-bounds panic with no recovery | 3.3.23, 3.4.10 | [GHSA-9gp7-6833-wv89](https://github.com/advisories/GHSA-9gp7-6833-wv89) |
| GHSA-h8g9-6gvh-5mrc | Low | Gateway TOCTOU: endpoints authenticated once at startup; subsequent auth-setting changes to those endpoints are not revalidated | 3.3.23, 3.4.10 | [GHSA-h8g9-6gvh-5mrc](https://github.com/advisories/GHSA-h8g9-6gvh-5mrc) |
| GHSA-5x4g-q5rc-36jp | Low | `--cipher-suites` flag permits insecure TLS ciphers when explicitly configured; secure by default only when the flag is omitted | 3.3.23, 3.4.10 | [GHSA-5x4g-q5rc-36jp](https://github.com/advisories/GHSA-5x4g-q5rc-36jp) |
| GHSA-vjg6-93fv-qv64 | Low | CN-based (certificate) authentication failures logged with insufficient detail — audit log gaps for denied access | 3.3.23, 3.4.10 | [GHSA-vjg6-93fv-qv64](https://github.com/advisories/GHSA-vjg6-93fv-qv64) |
| GHSA-pm3m-32r3-7mfh | Low | Negative auto-compaction retention value causes continuous compaction loop — excessive CPU consumption and log output | 3.3.23, 3.4.10 | [GHSA-pm3m-32r3-7mfh](https://github.com/advisories/GHSA-pm3m-32r3-7mfh) |
| GHSA-j86v-2vjr-fg8f | Moderate | Gateway TLS endpoint validation confirms TCP reachability only — not actual TLS acceptance — when using `--discovery-srv` | 3.3.23, 3.4.10 | [GHSA-j86v-2vjr-fg8f](https://github.com/advisories/GHSA-j86v-2vjr-fg8f) |
| GHSA-gmph-wf7j-9gcm / CVE-2021-28235 | Critical (CVSS 9.8) | Debug endpoint in 3.4.10 allows unauthenticated remote privilege escalation | 3.5.8, 3.4 backport (PR #15655) | [GHSA-gmph-wf7j-9gcm](https://github.com/advisories/GHSA-gmph-wf7j-9gcm) |
| GHSA-rfx7-8w68-q57q / CVE-2026-33343 | Low (auth-boundary) | Nested transaction operations bypass RBAC authorization checks — authenticated users can read/write beyond their key-level permissions | 3.6.9, 3.5.28, 3.4.42 | [GHSA-rfx7-8w68-q57q](https://github.com/advisories/GHSA-rfx7-8w68-q57q) |
| GHSA-q8m4-xhhv-38mg / CVE-2026-33413 | High | gRPC API authorization bypass: unauthenticated callers can invoke MemberList, Alarm, Lease, and Compaction APIs in exposed clusters | 3.6.9, 3.5.28, 3.4.42 | [GHSA-q8m4-xhhv-38mg](https://github.com/advisories/GHSA-q8m4-xhhv-38mg) |
| GHSA-x35m-3gp4-4fh5 / CVE-2026-44283 | Low | `PrevKv` and lease-attach in transaction `Put` requests bypass RBAC authorization — authenticated users can access data beyond their grants | 3.6.11, 3.5.30, 3.4.44 | [GHSA-x35m-3gp4-4fh5](https://github.com/advisories/GHSA-x35m-3gp4-4fh5) |

*OSV: https://osv.dev/list?ecosystem=Go&q=go.etcd.io%2Fetcd*

## Security Posture Notes

etcd is a critical piece of Kubernetes and CNCF infrastructure — it backs all Kubernetes cluster state. The project has a formal Product Security Committee (PSC) reachable at security@etcd.io with a defined embargo/release process targeting 1–21 days from disclosure to public release.

A CNCF-commissioned Trail of Bits security audit in 2020 reviewed the full source and is publicly available. The audit directly motivated the large coordinated fix cluster in 3.3.23 / 3.4.10, which addressed 13 advisories simultaneously.

Latest stable is v3.6.12 (June 1, 2026). The 2026 RBAC bypass cluster (CVE-2026-33343, CVE-2026-33413, CVE-2026-44283) was fixed in the 3.6.9–3.6.11 / 3.5.28–3.5.30 / 3.4.42–3.4.44 train.

**Kubernetes deployment note:** Standard Kubernetes deployments tunnel all cluster traffic through the kube-apiserver, which enforces its own RBAC — etcd is not exposed directly. The RBAC-category etcd advisories (CVE-2018-16886, CVE-2026-33343, CVE-2026-33413, CVE-2026-44283) primarily affect clusters where etcd's API is exposed directly to untrusted clients. See [[kubernetes/kube-apiserver]].

## Dependencies of Note

- `go.etcd.io/etcd/client/v3` submodule: the consumer-facing client library; several advisories target this package path explicitly.
- gRPC (`google.golang.org/grpc`): core transport layer — see [[go/google.golang.org/grpc]] for gRPC's own advisory history.
- bbolt: local embedded key-value storage backend.

## Open Questions

- Confirm whether the GHSA-wr2v-9rpq-c35q (gateway TLS DNS-SRV-only validation) remains relevant in v3.5+ / v3.6+ or is confined to the now-EOL 3.3.x / 3.4.x lines.
- Full OSV database query (currently blocked in this environment) should be run to confirm the complete advisory count and surface any records not captured by GHSA code search.
- Verify whether pkg.go.dev's active-vulnerability flags for GO-2024-2528 / GO-2024-2529 / GO-2024-2530 map to advisories already listed above or represent additional un-GHSA-mapped records.

## Related Pages

- [[kubernetes/kube-apiserver]]
- [[kubernetes/kubelet]]
- [[go/google.golang.org/grpc]]
- [[go/index]]

---
*Last updated: 2026-06-18 | Sources: 18*
