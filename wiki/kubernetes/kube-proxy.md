# kube-proxy (Kubernetes)

**Registry:** k8s
**Weekly Downloads:** N/A — deployed as a privileged DaemonSet on every Kubernetes node, distributed as part of the Kubernetes release bundle
**Repository:** https://github.com/kubernetes/kubernetes
**Security Contact:** security@kubernetes.io
**Disclosure Policy:** https://kubernetes.io/docs/reference/issues-security/security/
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-8558 / GHSA-wqv3-8cm6-h6wg | High (CVSS 8.8 AV:A/AC:L/PR:N) | Improper Authentication — kube-proxy (and kubelet) allow adjacent-network hosts to reach TCP/UDP services bound to 127.0.0.1 on the node or in its network namespace; loopback-only services that assume localhost-only access and lack additional authentication are exposed to any host on the same L2 segment or any container on the same node | 1.18.4, 1.17.7, 1.16.11 | [GHSA-wqv3-8cm6-h6wg](https://github.com/advisories/GHSA-wqv3-8cm6-h6wg) |
| CVE-2021-25736 / GHSA-35c7-w35f-xwgh | Moderate (CVSS 6.8 AV:N/AC:H/PR:H/S:C/C:H) | Unintentional Traffic Forwarding on Windows — kube-proxy on Windows forwards traffic to local processes listening on the same port as a LoadBalancer Service when the LoadBalancer controller does not set `status.loadBalancer.ingress[].ip`; Linux nodes are unaffected | 1.21.0 (affected: `k8s.io/kubernetes` < 1.21.0) | [GHSA-35c7-w35f-xwgh](https://github.com/advisories/GHSA-35c7-w35f-xwgh) |

*OSV live record: https://osv.dev/list?ecosystem=Go&q=k8s.io%2Fkubernetes*

## Security Posture Notes

kube-proxy runs as a DaemonSet on every Kubernetes node and is responsible for implementing the Kubernetes Service abstraction by programming iptables, IPVS, or nftables rules on the host network namespace. It runs with host network access and, in the default DaemonSet manifest, with `hostNetwork: true` and elevated Linux capabilities.

**CVE-2020-8558 (shared with kubelet):** The loopback-access bypass affects both kube-proxy and kubelet simultaneously (see [[kubernetes/kubelet]] for the full advisory context). The practical consequence is that any host on the same Layer 2 segment — or any container running on the node with network access — could reach services intended to be accessible only on 127.0.0.1. The fix restricts iptables rules to prevent routing loopback-destined traffic through the node's physical interfaces.

**Kernel-level chained exploitation (CVE-2026-31431 / copy.fail):** The Talos Linux advisory GHSA-m38g-vww2-mvgx documents kube-proxy as a privilege escalation vector independent of any kube-proxy code defect: an attacker with pod-scheduling permissions can poison the page-cache of an executable shared via overlayfs (e.g., `/usr/sbin/nft`) used by kube-proxy's nftables reconciliation loop, achieving arbitrary code execution inside kube-proxy's privileged context. This is a Linux kernel vulnerability (algif_aead, CVE-2026-31431) fixed in kernel ≥ 6.18.22, not a kube-proxy defect; upgrade the underlying kernel or disable AF_ALG socket creation via seccomp to mitigate.

**iptables vs. nftables mode:** kube-proxy is transitioning from iptables to nftables mode (`nftables` backend introduced in Kubernetes 1.29; becoming the default in later releases). The two backends have distinct rule-processing paths and the nftables path has less deployment history; its security surface should be considered when assessing production clusters.

**Windows-specific surface:** CVE-2021-25736 affects only Windows nodes. Linux deployments are unaffected. Clusters running Windows worker nodes should ensure LoadBalancer controllers set the `status.loadBalancer.ingress[].ip` field appropriately, or upgrade to ≥ 1.21.0.

**Security disclosures:** Kubernetes security advisories are coordinated by the Product Security Committee and published to the `kubernetes-security-announce` mailing list. The project maintains a HackerOne program at https://hackerone.com/kubernetes.

## Dependencies of Note

- `k8s.io/kubernetes` monorepo — kube-proxy ships as part of the Kubernetes monorepo; all `k8s.io/kubernetes` Go module advisories apply at the monorepo level.
- CNI plugins — kube-proxy operates alongside CNI plugins (Cilium, Calico, Flannel); some CNI configurations replace kube-proxy entirely and have separate advisory histories.
- Linux kernel netfilter / nftables — kube-proxy's operation depends on kernel networking subsystems; kernel vulnerabilities (e.g., CVE-2026-31431) can be chained through kube-proxy's privileged host-network execution context.

## Open Questions

- nftables mode security posture: whether the Kubernetes 1.29+ nftables backend introduces new parsing or rule-injection boundaries vs. the legacy iptables path.
- IPVS mode surface: kube-proxy IPVS mode has a distinct attack surface from iptables; no IPVS-mode-specific public advisory has been identified to date, but it warrants a dedicated future search pass.

## Related Pages

- [[kubernetes/kubelet]] — shares CVE-2020-8558; node agent on the same host
- [[kubernetes/containerd]] — container runtime on the same node
- [[kubernetes/kube-apiserver]] — control plane that kube-proxy authenticates against for configuration
- [[kubernetes/index]]

---
*Last updated: 2026-07-20 | Sources: 2 (GHSA-wqv3-8cm6-h6wg, GHSA-35c7-w35f-xwgh)*
