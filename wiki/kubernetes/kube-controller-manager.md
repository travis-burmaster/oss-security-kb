# kube-controller-manager (Kubernetes)

**Registry:** k8s
**Weekly Downloads:** N/A — deployed as a static Pod on every Kubernetes control-plane node, distributed as part of the Kubernetes release bundle
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
| CVE-2020-8555 / GHSA-x6mj-w4jf-jmgw | Moderate (CVSS 3.1 AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N) | SSRF via in-tree storage volume provisioners — kube-controller-manager's volume provisioning code for glusterfs, quobyte, storageos, and ScaleIO made HTTP requests to attacker-influenced endpoints; an authorized user with StorageClass creation rights could probe control-plane-accessible endpoints (link-local, loopback services) and exfiltrate up to ~500 bytes per request, bypassing cluster network policies | 1.15.12, 1.16.9, 1.17.4, 1.18.1 | [GHSA-x6mj-w4jf-jmgw](https://github.com/advisories/GHSA-x6mj-w4jf-jmgw) |
| CVE-2020-8566 / GHSA-5x96-j797-5qqw | Moderate (CVSS 7.1 AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N) | Ceph RBD admin secret credential exposure — when logging at verbosity level 4 or higher (`--v=4`), Ceph RBD admin secrets are written to kube-controller-manager log output during persistent volume provisioning; any principal with access to controller-manager logs or log aggregation systems can recover storage credentials | 1.17.13, 1.18.10, 1.19.3 | [GHSA-5x96-j797-5qqw](https://github.com/advisories/GHSA-5x96-j797-5qqw) |
| CVE-2024-0793 / GHSA-h7wq-jj8r-qm7p | High (CVSS 3.1 AV:N/AC:L/PR:L/UI:N/S:C/C:N/I:N/A:H) | HPA controller null pointer dereference DoS — a HorizontalPodAutoscaler object whose `.spec.behavior.scaleUp` field is omitted triggers a nil dereference in the HPA controller reconciler; kube-controller-manager enters a crash-restart churn loop, causing cluster-wide horizontal pod autoscaling to become unavailable for the lifetime of the malformed HPA object | 1.27.0 (first non-alpha release; fix in 1.27.0-alpha.1) | [GHSA-h7wq-jj8r-qm7p](https://github.com/advisories/GHSA-h7wq-jj8r-qm7p) |
| CVE-2025-13281 / GHSA-r6j8-c6r2-37rr | Moderate (CVSS 3.1 AV:N/AC:H/PR:H/UI:N/S:C/C:H/I:N/A:N) | Half-blind SSRF via Portworx StorageClass provisioner — kube-controller-manager's in-tree Portworx volume provisioning path permits authorized users with StorageClass creation or update rights to make the controller issue HTTP requests to attacker-influenced endpoints within the control-plane's network, enabling partial exfiltration of sensitive data from link-local or loopback services inaccessible from tenant namespaces | 1.32.10, 1.33.6, 1.34.2 | [GHSA-r6j8-c6r2-37rr](https://github.com/advisories/GHSA-r6j8-c6r2-37rr) |

*OSV live record: https://osv.dev/list?ecosystem=Go&q=k8s.io%2Fkubernetes*

## Security Posture Notes

kube-controller-manager (KCM) is one of the three critical control-plane components (alongside kube-apiserver and kube-scheduler) and runs with cluster-admin-equivalent access to the Kubernetes API. It hosts dozens of built-in controllers — Deployment, ReplicaSet, HPA, PersistentVolume, ServiceAccount, Namespace, EndpointSlice, CertificateSigningRequest, and others — and has network access to the kube-apiserver and to cloud/storage provider APIs.

**SSRF pattern (CVE-2020-8555, CVE-2025-13281):** Two independent SSRF advisories share a common root cause: KCM's in-tree storage provisioners (historical: glusterfs, quobyte, storageos, ScaleIO; recent: Portworx) made or make HTTP requests using parameters from user-controlled StorageClass objects without sufficient URL validation. Because KCM runs on the control-plane node, these requests can reach link-local (169.254.0.0/16) and loopback (127.0.0.0/8) addresses that are inaccessible from workload pods. Mitigation: restrict StorageClass creation to trusted principals via RBAC; migrate away from deprecated in-tree provisioners to out-of-tree CSI drivers (all in-tree provisioners that triggered CVE-2020-8555 are now either removed or replaced in current Kubernetes versions).

**Credential logging (CVE-2020-8566):** The verbosity-based secret exposure is a common failure class across Kubernetes control-plane components — see also [[go/go.etcd.io/etcd-v3]] and [[kubernetes/kube-apiserver]] for analogous patterns. Production clusters should use log verbosity levels ≤3 for control-plane components and restrict log aggregation access to security-sensitive principals. Audit log pipelines should be reviewed for inadvertent credential capture.

**HPA controller DoS (CVE-2024-0793):** The nil dereference is triggered by a user-submitted HPA object with a missing optional field, not an API validation gap. The practical blast radius is large because HPA autoscaling halts cluster-wide while KCM churns. In Kubernetes deployments with strict PodDisruptionBudgets or production traffic scaling requirements, a single misformed HPA object from an unprivileged namespace-level user can disable autoscaling for all namespaces. Fixed in Kubernetes 1.27; operators on 1.26 or earlier who cannot upgrade should restrict HPA creation permissions or apply admission webhook validation.

**Security disclosures:** Kubernetes security issues are coordinated by the Product Security Committee (PSC) and reported to security@kubernetes.io. The project maintains a HackerOne program at https://hackerone.com/kubernetes. Advisories are published to the `kubernetes-security-announce` Google Group. KCM advisories are tracked under the `k8s.io/kubernetes` Go module in GHSA.

**Current release context (September 2026):** The current stable Kubernetes release line is 1.34.x (with 1.34.2 patching CVE-2025-13281). Kubernetes 1.32.x and 1.33.x remain in active support; earlier lines are EOL. Operators on EOL releases receive no security patches and should treat all unpatched SSRF and DoS advisories above as unresolved risks.

## Dependencies of Note

- `k8s.io/kubernetes` monorepo — KCM ships as part of the Kubernetes monorepo; all `k8s.io/kubernetes` Go module advisories apply at this level.
- In-tree CSI/volume plugins — the historical SSRF advisories target in-tree storage provisioners that have been progressively deprecated and replaced with out-of-tree CSI drivers; verifying whether a cluster still uses in-tree provisioners is prerequisite to assessing SSRF exposure.
- Cloud provider API access — KCM (or the separate cloud-controller-manager for managed clusters) holds credentials for cloud provider APIs; any SSRF or credential-logging advisory may expose cloud IAM material.

## Open Questions

- In-tree provisioner inventory: which in-tree storage provisioners remain active in Kubernetes ≥1.31 and present unresolved SSRF surface analogous to CVE-2020-8555.
- Leader election boundary: KCM uses leader-election; whether an attacker who triggers the HPA DoS can influence which replica holds the lease and whether that matters for privilege escalation deserves investigation.
- Cloud-controller-manager split: since Kubernetes 1.11, cloud-provider logic has been progressively split into a separate `cloud-controller-manager` binary; that component's own advisory history has not been mapped here.

## Related Pages

- [[kubernetes/kube-apiserver]] — control-plane API gateway; KCM authenticates against it
- [[kubernetes/kubelet]] — node agent; KCM manages workloads that kubelet executes
- [[kubernetes/kube-proxy]] — shares the node-level network access concern
- [[go/go.etcd.io/etcd-v3]] — backing store; KCM writes cluster state through kube-apiserver into etcd
- [[kubernetes/index]]

---
*Last updated: 2026-09-11 | Sources: 4 (GHSA-x6mj-w4jf-jmgw, GHSA-5x96-j797-5qqw, GHSA-h7wq-jj8r-qm7p, GHSA-r6j8-c6r2-37rr)*
