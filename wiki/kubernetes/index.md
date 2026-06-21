# Kubernetes Index

## Seed Pages
- [[kubernetes/kube-apiserver]] — control-plane API surface with authentication, authorization, admission, and request parsing risk

## Advisory-Mapped Pages
- [[kubernetes/containerd]] — container runtime (OCI/CRI) · advisory mapped · 21 GHSA advisories spanning CRI plugin boundary failures, UID mishandling, side-channel exposure, and 2026 checkpoint/restore exploitation cluster through CVE-2026-53492
- [[kubernetes/kubelet]] — node agent · advisory mapped · privilege assignment, DoS, adjacent-network access, seccomp bypass, Windows command injection, gitRepo RCE, and checkpoint-API disk-fill history through CVE-2025-0426

## Future Targets
- `kube-proxy` — traffic steering and packet-filtering component
- `runc` — low-level OCI container execution runtime; several high-severity CVEs including CVE-2019-5736 and CVE-2024-21626
