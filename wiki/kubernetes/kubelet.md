# kubelet (Kubernetes)

**Registry:** k8s
**Weekly Downloads:** N/A — bundled with Kubernetes node installations
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
| CVE-2019-11245 / GHSA-r76g-g87f-vw8f | Medium | Incorrect Privilege Assignment — containers for pods without an explicit `runAsUser` attempt to run as uid 0 (root) on container restart | 1.13.7, 1.14.3 | [GHSA-r76g-g87f-vw8f](https://github.com/advisories/GHSA-r76g-g87f-vw8f) |
| CVE-2020-8557 / GHSA-55qj-gj3x-jq9r | Medium | Denial of Service — kubelet eviction manager does not account for disk usage by pod writes to `/etc/hosts`; a pod can fill node storage | 1.16.13, 1.17.9, 1.18.6 | [GHSA-55qj-gj3x-jq9r](https://github.com/advisories/GHSA-55qj-gj3x-jq9r) |
| CVE-2020-8558 / GHSA-wqv3-8cm6-h6wg | High | Improper Authentication — kubelet and kube-proxy allow adjacent-network hosts to reach TCP/UDP services bound to 127.0.0.1 on the node | 1.18.4, 1.17.7, 1.16.11 | [GHSA-wqv3-8cm6-h6wg](https://github.com/advisories/GHSA-wqv3-8cm6-h6wg) |
| CVE-2020-8559 / GHSA-qhm4-jxv7-j9pq | Medium | Denial of Service — allocation amplification through the unauthenticated kubelet read-only API (port 10255) and authenticated HTTPS API (port 10250) | 1.15.10, 1.16.7, 1.17.3 | [GHSA-qhm4-jxv7-j9pq](https://github.com/advisories/GHSA-qhm4-jxv7-j9pq) |
| CVE-2023-2431 / GHSA-xc8m-28vv-4pjc | Medium | seccomp Profile Enforcement Bypass — pods using `localhost` seccomp type with an empty `profile` field run in unconfined (seccomp disabled) mode | 1.25.9, 1.26.4, 1.27.1 | [GHSA-xc8m-28vv-4pjc](https://github.com/advisories/GHSA-xc8m-28vv-4pjc) |
| CVE-2024-9042 | High | Command Injection on Windows nodes — specially crafted requests to the nodes/`*`/logs/query API allow command injection; affects only Windows worker nodes | 1.28.12, 1.29.7, 1.30.3 | [kubernetes/kubernetes#128885](https://github.com/kubernetes/kubernetes/issues/128885) |
| CVE-2024-10220 / GHSA-27wf-5967-98gx | High | Arbitrary Command Execution via `gitRepo` Volumes — specially crafted gitRepo volume definitions allow arbitrary OS command execution | 1.28.12, 1.29.7, 1.30.3 | [GHSA-27wf-5967-98gx](https://github.com/advisories/GHSA-27wf-5967-98gx) |
| CVE-2025-0426 / GHSA-jgfp-53c3-624w | Medium | Node DoS via Checkpoint API — large numbers of container checkpoint requests to the unauthenticated kubelet read-only HTTP endpoint can fill node disk storage | 1.29.13, 1.30.9, 1.31.5, 1.32.1 | [GHSA-jgfp-53c3-624w](https://github.com/advisories/GHSA-jgfp-53c3-624w) |

*OSV live record: https://osv.dev/list?ecosystem=Go&q=k8s.io%2Fkubernetes*

## Security Posture Notes

kubelet is the primary node agent in every Kubernetes cluster. It executes workloads, manages volumes, exposes health/metrics APIs on ports 10250 (authenticated HTTPS) and historically 10255 (unauthenticated read-only HTTP, now disabled by default in current versions), and interacts with the container runtime. Its attack surface is therefore among the most sensitive in the cluster: a compromise of kubelet on any node provides control over all pods scheduled to that node plus host-level access.

**Read-only port (10255):** Disabled by default in Kubernetes ≥ 1.16 but still present in many configurations and is the surface for CVE-2020-8559 and CVE-2025-0426.

**gitRepo volumes:** Deprecated since Kubernetes 1.11. CVE-2024-10220 underscores that their use on any still-supported minor line carries RCE risk; the recommended mitigation is to disable gitRepo volume usage via admission policy.

**Windows node surface:** CVE-2024-9042 is a Windows-only command injection path in the logs API — Linux nodes are not affected. Clusters running Windows worker nodes should prioritize patching to the fix versions.

**seccomp enforcement:** CVE-2023-2431 is a configuration-correctness issue: an empty `profile` field on a `localhost`-type seccomp entry silently disables seccomp rather than failing closed. Admission-webhook enforcement of explicit profiles is the recommended defense-in-depth.

Security disclosures for Kubernetes components are coordinated by the Kubernetes Product Security Committee and published to the `kubernetes-security-announce` mailing list. The project maintains a published `SECURITY.md` and a HackerOne program.

## Dependencies of Note

- Container runtimes (containerd, CRI-O) — kubelet communicates over CRI; runtime-level escapes are a distinct but adjacent attack surface.
- CNI plugins — network configuration plugins run with elevated privileges; vulnerabilities in CNI plugins can provide lateral movement paths accessible from the node where kubelet runs.
- `k8s.io/kubernetes` — kubelet ships as part of the monorepo; all `k8s.io/kubernetes` Go package advisories apply at the monorepo level.

## Open Questions

- Which currently supported minor lines still ship with a default-enabled read-only port 10255, and what is the distro-backport status of CVE-2025-0426 for managed k8s offerings (EKS, GKE, AKS)?
- Is there a published list of admission policies (OPA/Gatekeeper/Kyverno) recommended by the Kubernetes security committee to block deprecated volume types like `gitRepo`?
- What is the CVE-2025-1767 "inadvertent local repository access" scope (surfaced in the March 2025 k8s security announce archive as a follow-on gitRepo advisory)?

## Related Pages

- [[kubernetes/kube-apiserver]]
- [[kubernetes/index]]

---
*Last updated: 2026-06-15 | Sources: 3 (GHSA/github advisory-database code search, kubernetes-sigs/cve-feed-osv, golang/vulndb)*
