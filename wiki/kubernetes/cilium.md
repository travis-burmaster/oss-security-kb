# Cilium (kubernetes)

**Registry:** k8s
**Weekly Downloads:** unknown (deployed as CNI plugin, not a registry package)
**Repository:** https://github.com/cilium/cilium
**Security Contact:** security@cilium.io
**Disclosure Policy:** https://github.com/cilium/cilium/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-30851 / GHSA-2h44-x2wx-49f4 | Moderate | HTTP policies combining allow-all and restricted rules can be circumvented, potentially leaking data between endpoints | v1.11.16, v1.12.9, v1.13.2 | [GHSA-2h44-x2wx-49f4](https://github.com/advisories/GHSA-2h44-x2wx-49f4) |
| CVE-2023-39347 / GHSA-gj2r-phwg-6rww | Moderate CVSS 6.1 | Attacker with pod-label update permission causes Cilium to apply incorrect network policies, bypassing intended restrictions via non-existent construct names in label values | v1.12.14, v1.13.7, v1.14.2 | [GHSA-gj2r-phwg-6rww](https://github.com/advisories/GHSA-gj2r-phwg-6rww) |
| CVE-2024-25631 / GHSA-x989-52fc-4vr4 | Moderate CVSS 6.1 | Traffic between pods on different nodes transmitted unencrypted when WireGuard encryption is enabled with an external kvstore (etcd) | v1.14.7 | [GHSA-x989-52fc-4vr4](https://github.com/advisories/GHSA-x989-52fc-4vr4) |
| CVE-2024-37307 / GHSA-wh78-7948-358j | High | `cilium-bugtool --envoy-dump` captures TLS certificates, private keys, and Kafka API keys into diagnostic output, leaking secrets to anyone with access to the bundle | v1.13.17, v1.14.12, v1.15.6 | [GHSA-wh78-7948-358j](https://github.com/advisories/GHSA-wh78-7948-358j) |
| CVE-2024-42487 / GHSA-qcm3-7879-xcww | Moderate CVSS 5.3 | Gateway API HTTPRoutes and GRPCRoutes do not follow match precedence per the Gateway API spec; headers are matched before methods, leading to unintended traffic routing | v1.15.8, v1.16.1 | [GHSA-qcm3-7879-xcww](https://github.com/advisories/GHSA-qcm3-7879-xcww) |
| CVE-2024-52529 / GHSA-xg58-75qf-9r67 | Moderate CVSS 5.3 | L7 policy enforcement may not apply to policies with wildcarded port ranges, creating a policy bypass opportunity | v1.16.4 | [GHSA-xg58-75qf-9r67](https://github.com/advisories/GHSA-xg58-75qf-9r67) |

*6 of 49 public GHSA advisories mapped (representative sample by recency). Full advisory list: https://osv.dev/list?ecosystem=Go&q=cilium/cilium*

## Security Posture Notes

CNCF-graduated project (graduated 2023) with 25,071 GitHub stars. Implements Kubernetes CNI networking, network policy enforcement, distributed load balancing, and observability using eBPF. The Hubble observability platform is integrated. Security team reachable at security@cilium.io with a documented responsible-disclosure policy.

Recurring advisory themes: policy-bypass flaws in the L7 HTTP enforcement engine, WireGuard encryption configuration gaps, and credential leakage via diagnostic tooling. Most advisories affect multiple maintained stable branches simultaneously (1.12–1.16 range), indicating Cilium back-ports fixes across its maintained stable window.

Current stable: v1.20.1 (released 2026-08-18). The companion `github.com/cilium/ebpf` library has a separate Low advisory: CVE-2026-10722 / GHSA-xhgw-qwwf-pg32 (integer overflow in `LoadCollectionSpecFromReader`, fixed 0.22.0).

## Dependencies of Note

- `github.com/cilium/ebpf` — companion eBPF library; CVE-2026-10722 (Low, integer overflow in `LoadCollectionSpecFromReader`, fixed 0.22.0)
- Linux kernel eBPF subsystem — Cilium correctness depends on kernel eBPF behavior; CVE-2025-22021 (Linux kernel netfilter IPv6 SNAT socket-match failure) specifically affects environments using Cilium with Envoy for L7 policy enforcement

## Open Questions

- 43 of 49 GHSA advisories for cilium packages not yet mapped in this pass; future pass should prioritize Critical/High records and any in the unreviewed set
- Hubble observability API surface and Cilium Cluster Mesh configuration not specifically assessed in this pass

## Related Pages

- [[kubernetes/ingress-nginx]]
- [[kubernetes/coredns]]
- [[kubernetes/index]]

---
*Last updated: 2026-09-05 | Sources: 6 GHSA advisories mapped of 49 total (github/advisory-database)*
