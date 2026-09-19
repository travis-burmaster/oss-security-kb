# kube-controller-manager (Kubernetes)

**Registry:** k8s
**Weekly Downloads:** N/A (control-plane binary, distributed as part of Kubernetes releases)
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
| CVE-2020-8555 / GHSA-x6mj-w4jf-jmgw | Moderate CVSS 6.3 | SSRF via in-tree storage volume plugins (FlexVolume, CephFS, GlusterFS, iSCSI, and others) — authorized users can issue crafted GET requests causing KCM to leak up to 500 bytes from unprotected endpoints on the control plane's host network (link-local, loopback) | ≥ 1.15.12, 1.16.9, 1.17.5, 1.18.1 | [GHSA-x6mj-w4jf-jmgw](https://github.com/advisories/GHSA-x6mj-w4jf-jmgw) |
| CVE-2020-8566 / GHSA-5x96-j797-5qqw | Moderate CVSS 6.5 | Ceph RBD admin credentials written to kube-controller-manager logs during PVC provisioning when logging verbosity is ≥ 4; affects clusters using the Ceph RBD in-tree storage provisioner | ≥ 1.17.13, 1.18.10, 1.19.3 | [GHSA-5x96-j797-5qqw](https://github.com/advisories/GHSA-5x96-j797-5qqw) |
| CVE-2024-0793 / GHSA-h7wq-jj8r-qm7p | High CVSS 7.1 | Nil pointer dereference in the KCM Horizontal Pod Autoscaler controller triggered by an HPA resource missing the `.spec.behavior.scaleUp` block — causes KCM pods to enter continuous restart churn (DoS affecting all workloads relying on KCM); requires cluster write access for HPA resources | ≥ 1.27.0-alpha.1 (stable: 1.27.0) | [GHSA-h7wq-jj8r-qm7p](https://github.com/advisories/GHSA-h7wq-jj8r-qm7p) |
| CVE-2025-13281 / GHSA-r6j8-c6r2-37rr | Moderate CVSS 6.5 | Half-blind SSRF via the in-tree Portworx StorageClass — authorized users can cause KCM to issue HTTP requests to arbitrary endpoints on the control plane's host network and observe a subset of the response; affects clusters using the Portworx in-tree volume plugin | ≥ 1.32.10, 1.33.6, 1.34.2 | [GHSA-r6j8-c6r2-37rr](https://github.com/advisories/GHSA-r6j8-c6r2-37rr) |

*OSV link: https://osv.dev/list?ecosystem=Go&q=kube-controller-manager*

## Security Posture Notes

kube-controller-manager (KCM) is one of the two primary Kubernetes control-plane binaries (alongside kube-apiserver). It runs reconciliation loops for Deployments, ReplicaSets, StatefulSets, DaemonSets, HPA, Node lifecycle, ServiceAccounts, PersistentVolumeClaims, and storage provisioners. It runs in the control-plane's host network namespace with cluster-admin equivalent privileges.

Kubernetes follows a coordinated disclosure process via the Kubernetes Product Security Committee (PSC) at security@kubernetes.io; advisories are published to the kubernetes-security-announce mailing list and as GitHub Security Advisories on kubernetes/kubernetes.

The recurring KCM advisory pattern is SSRF through in-tree storage volume plugins: because KCM's storage controller makes HTTP requests to external services to provision volumes, adversarial StorageClass or PVC configurations can redirect those requests to internal endpoints not intended to be reachable from cluster workloads. CVE-2020-8555 covered a wide range of in-tree provisioners; CVE-2025-13281 shows this pattern persists for the Portworx provider five years later.

The CVE-2024-0793 HPA nil pointer dereference is representative of a second class: logic errors in controller reconciliation loops that allow a low-privileged cluster user to crash KCM by submitting valid-but-unexpected resource configurations. A crashed KCM halts all reconciliation (new Deployments won't schedule, autoscaling stops, failed nodes won't be evicted), making this category effectively a cluster-wide DoS.

KCM is delivered as part of the Kubernetes release train. All fixes require upgrading the Kubernetes control plane to a patched minor release.

## Dependencies of Note

- KCM embeds the entire k8s.io/kubernetes monorepo; its in-tree volume plugin surface is extensive and includes legacy provisioners (Ceph, GlusterFS, iSCSI, NFS, Portworx, and others) that are the source of recurring SSRF advisories.
- Migration from in-tree plugins to out-of-tree CSI drivers (recommended since Kubernetes 1.23) removes the largest SSRF attack surface.

## Open Questions

- Have the remaining in-tree volume provisioners (iSCSI, NFS, GlusterFS, StorageOS, ScaleIO) been reviewed for the same SSRF pattern as CVE-2020-8555?
- Full KCM advisory history against k8s.io/kubernetes pre-2020 not yet mapped.

## Related Pages

- [[kubernetes/kube-apiserver]]
- [[kubernetes/kubelet]]
- [[kubernetes/kube-proxy]]
- [[kubernetes/index]]

---
*Last updated: 2026-09-19 | Sources: 4*
