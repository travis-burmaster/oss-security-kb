# Kubernetes Index

## Seed Pages
- [[kubernetes/kube-apiserver]] — control-plane API surface with authentication, authorization, admission, and request parsing risk

## Advisory-Mapped Pages
- [[kubernetes/containerd]] — container runtime (OCI/CRI) · advisory mapped · 21 GHSA advisories spanning CRI plugin boundary failures, UID mishandling, side-channel exposure, and 2026 checkpoint/restore exploitation cluster through CVE-2026-53492
- [[kubernetes/helm]] — CNCF-graduated Kubernetes package manager · advisory mapped · 27 GHSA advisories spanning Helm 2 Tiller TLS/symlink, plugin zip-slip and injection, lookup-function cluster data leakage, credential forwarding, strvals OOM/stack-overflow, chartutil JSON-schema panics, getHostByName DNS leakage, metadata-panic DoS, chart path traversal, decompression bomb, $ref stack exhaustion, Chart.yaml code-execution symlink, and Helm v4 plugin signing bypass / path traversal cluster through CVE-2026-35204
- [[kubernetes/kube-proxy]] — network rules / service proxy DaemonSet · advisory mapped · loopback-access bypass (CVE-2020-8558 High AV:A, shared with kubelet) and Windows LoadBalancer traffic-forwarding bypass (CVE-2021-25736 Moderate); also a chained exploitation target in CVE-2026-31431 (copy.fail) kernel privilege escalation
- [[kubernetes/kubelet]] — node agent · advisory mapped · privilege assignment, DoS, adjacent-network access, seccomp bypass, Windows command injection, gitRepo RCE, and checkpoint-API disk-fill history through CVE-2025-0426
- [[kubernetes/runc]] — OCI low-level container execution runtime · advisory mapped · CVE-2019-5736 /proc/self/exe container escape, TOCTOU mount race, capabilities elevation, access-control regression, AppArmor/SELinux bypass, and CVE-2024-21626 fd-leak container breakout through 1.1.12

## Future Targets
- `argo-cd` — GitOps continuous delivery tool (CNCF graduated, active advisory history)
