# containerd (Kubernetes)

**Registry:** k8s / GitHub Container Registry / OS package repositories
**Weekly Downloads:** N/A — installed via OS package manager or bundled with Kubernetes distributions
**Repository:** https://github.com/containerd/containerd
**Security Contact:** security@containerd.io / https://github.com/containerd/containerd/security/advisories
**Disclosure Policy:** https://github.com/containerd/containerd/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-21 | OSS Security KB | GHSA database lookup | automated | 21 public advisories mapped | [github/advisory-database](https://github.com/github/advisory-database) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-15257 / GHSA-36xw-fx78-c5r4 | Moderate — CVSS 5.7 | containerd-shim API socket exposed to host-network containers: the shim verified root ownership of connecting processes but failed to restrict access to the abstract Unix domain socket, allowing privileged containers in the same network namespace to execute processes with elevated privileges. Existing containers must be stopped and restarted after upgrading. | 1.3.9, 1.4.3 | [GHSA-36xw-fx78-c5r4](https://github.com/advisories/GHSA-36xw-fx78-c5r4) |
| CVE-2021-21334 / GHSA-6g2q-w5j3-fwh4 | High — CVSS 7.1 | Environment variable leak in CRI: containers sharing the same image could receive environment variables from other containers in different security contexts, potentially exposing secrets when multiple pods from the same image are launched in rapid succession. | 1.3.10, 1.4.4 | [GHSA-6g2q-w5j3-fwh4](https://github.com/advisories/GHSA-6g2q-w5j3-fwh4) |
| CVE-2021-32760 / GHSA-c72p-9xmj-rx3w | Moderate — CVSS 5.3 | Maliciously crafted container images can alter Unix file permissions on the host during extraction, including special bits (setuid, setgid). The flaw does not independently grant file access or execution. | 1.4.8, 1.5.4 | [GHSA-c72p-9xmj-rx3w](https://github.com/advisories/GHSA-c72p-9xmj-rx3w) |
| CVE-2021-41103 / GHSA-c2h3-6mxw-7mvq | Moderate — CVSS 5.4 | Insufficiently restricted plugin directory permissions: unprivileged host users can traverse container root directories and execute programs, particularly when containers have setuid/setgid bits or when host/container UIDs collide. Running containers must be restarted after upgrading. | 1.4.11, 1.5.7 | [GHSA-c2h3-6mxw-7mvq](https://github.com/advisories/GHSA-c2h3-6mxw-7mvq) |
| CVE-2021-43816 / GHSA-mvff-h3cj-wj9c | High — CVSS 8.1 | SELinux LSM bypass via `hostPath`: on SELinux-enabled systems, specially configured `hostPath` bind mounts allow relabeling arbitrary host files and directories, granting read/write access beyond the intended container boundary. Mitigation: restrict `hostPath` volume sources via Kubernetes Pod Security Policy or equivalent admission control. | 1.5.9 | [GHSA-mvff-h3cj-wj9c](https://github.com/advisories/GHSA-mvff-h3cj-wj9c) |
| CVE-2022-23648 / GHSA-crp2-qrr5-8pq7 | High — CVSS 9.1 | Insecure handling of image volumes in the CRI plugin: containers launched with specially crafted image configs can access read-only copies of arbitrary host files and directories, bypassing Pod Security Policy and leaking sensitive host data. Use only trusted images as interim mitigation. | 1.4.13, 1.5.10, 1.6.1 | [GHSA-crp2-qrr5-8pq7](https://github.com/advisories/GHSA-crp2-qrr5-8pq7) |
| GHSA-c9cp-9c75-9v8c | Low | Non-empty inheritable Linux process capabilities on container start: containerd started containers with non-empty inheritable capability sets, creating an atypical environment where programs with inheritable file capabilities can elevate privileges. The container sandbox is not breached (inheritable sets stay within the bounding set), but privilege-separated workloads may be affected. Running containers must be recreated after upgrading. | 1.5.11, 1.6.2 | [GHSA-c9cp-9c75-9v8c](https://github.com/advisories/GHSA-c9cp-9c75-9v8c) |
| CVE-2022-31030 / GHSA-5ffw-gxpp-mxpf | Moderate — CVSS 5.5 | Host memory exhaustion via ExecSync: programs inside containers can trigger unbounded memory consumption in the containerd daemon through ExecSync API calls (used by Kubernetes health probes and `kubectl exec`). | 1.5.13, 1.6.6 | [GHSA-5ffw-gxpp-mxpf](https://github.com/advisories/GHSA-5ffw-gxpp-mxpf) |
| CVE-2022-23471 / GHSA-2qjp-425j-52j9 | Moderate | CRI stream server goroutine leak via terminal: when a TTY is requested but process launch fails, a goroutine stalls waiting without a receiver, causing a memory leak. Repeated invocations exhaust host memory. Mitigation: use only trusted images and commands; restrict `kubectl exec` access. | 1.5.16, 1.6.12 | [GHSA-2qjp-425j-52j9](https://github.com/advisories/GHSA-2qjp-425j-52j9) |
| CVE-2023-25173 / GHSA-hmfx-3pcx-653p | Moderate — CVSS 5.3 | Supplementary groups not set up properly inside containers: an attacker with container access can manipulate group permissions to bypass primary group restrictions, potentially accessing sensitive data. Mitigation: recreate containers; use `ENTRYPOINT ["su", "-", "user"]` instead of `USER $USERNAME` in Dockerfiles. | 1.5.18, 1.6.18 | [GHSA-hmfx-3pcx-653p](https://github.com/advisories/GHSA-hmfx-3pcx-653p) |
| GHSA-7ww5-4wqc-m92c | Moderate | RAPL (Running Average Power Limit) interface exposed to containers by default via `/sys/devices/virtual/powercap`: unprivileged access to RAPL readings enables a power-based side-channel attack against AES-NI and KASLR. Fix masks the powercap path in default mount configuration and adds AppArmor rules to deny access. | 1.6.26, 1.7.11 | [GHSA-7ww5-4wqc-m92c](https://github.com/advisories/GHSA-7ww5-4wqc-m92c) |
| CVE-2024-25621 / GHSA-pwhc-rpq9-4c8w | High — CVSS 7.1 | Overly broad default permissions on three containerd directories (`/var/lib/containerd` 0o711, `/run/containerd/io.containerd.grpc.v1.cri` 0o755, `/run/containerd/io.containerd.sandbox.controller.v1.shim` 0o711): local host users can access the metadata store, content store, and Kubernetes local volumes, enabling local privilege escalation via setuid binaries. | 1.7.29, 2.0.7, 2.1.5, 2.2.0 | [GHSA-pwhc-rpq9-4c8w](https://github.com/advisories/GHSA-pwhc-rpq9-4c8w) |
| CVE-2024-40635 / GHSA-265r-hfxg-fhmg | Moderate — CVSS 5.3 | Integer overflow in User ID handling: containers configured with UIDs or GIDs exceeding the maximum 32-bit signed integer overflow to UID 0 (root), bypassing non-root execution requirements configured in pod security contexts. | 2.0.4, 1.7.27, 1.6.38 | [GHSA-265r-hfxg-fhmg](https://github.com/advisories/GHSA-265r-hfxg-fhmg) |
| CVE-2025-47290 / GHSA-cm76-qm8v-3j95 | High | TOCTOU (time-of-check to time-of-use) in image unpacking: malicious container images can modify the host filesystem without authorization during the unpack phase. Restrict image imports to trusted sources as interim mitigation. Affects only 2.1.0. | 2.1.1 | [GHSA-cm76-qm8v-3j95](https://github.com/advisories/GHSA-cm76-qm8v-3j95) |
| CVE-2025-47291 / GHSA-cxfp-7pvr-95ff | Moderate | CRI plugin: user-namespaced pods not placed under the Kubernetes cgroup hierarchy, preventing enforcement of resource limits; workloads can consume resources beyond configured bounds and cause node denial of service. | 2.0.5, 2.1.0 | [GHSA-cxfp-7pvr-95ff](https://github.com/advisories/GHSA-cxfp-7pvr-95ff) |
| CVE-2025-64329 / GHSA-m6hq-p25p-ffr2 | Moderate | CRI Attach goroutine leak causing host memory exhaustion: repeated `kubectl attach` invocations cause progressive memory growth in containerd. Mitigation: apply admission controller restricting pods/attach access. | 1.7.29, 2.0.7, 2.1.5, 2.2.0 | [GHSA-m6hq-p25p-ffr2](https://github.com/advisories/GHSA-m6hq-p25p-ffr2) |
| CVE-2026-46680 / GHSA-fqw6-gf59-qr4w | High | User ID handling bypass enabling `runAsNonRoot` evasion: containers with numeric User directives exceeding 32-bit integer limits are mishandled as usernames, allowing crafted `/etc/passwd` entries to map large numeric strings to UID 0 and bypass Kubernetes `runAsNonRoot`. Note: containerd v2.1 reached end-of-life and received no patch. | 1.7.32, 2.0.9, 2.2.4, 2.3.1 | [GHSA-fqw6-gf59-qr4w](https://github.com/advisories/GHSA-fqw6-gf59-qr4w) |
| CVE-2026-50195 / GHSA-cvxm-645q-p574 | Moderate | CRI checkpoint import local image tag poisoning: unvalidated image references in checkpoint configs allow users with pod creation permissions to assign arbitrary local tags to pulled images, poisoning the node image cache; other pods with permissive pull policies may inadvertently execute the attacker's image. | 2.1.9, 2.2.5, 2.3.2 | [GHSA-cvxm-645q-p574](https://github.com/advisories/GHSA-cvxm-645q-p574) |
| CVE-2026-53488 / GHSA-xhf5-7wjv-pqxp | High | Image-config `LABEL` flows to restart-monitor `binary://` logger: the CRI plugin does not validate labels from Docker image configs, allowing arbitrary host commands to execute via container labels when the restart-monitor processes them. Affects 1.7.x, 2.0.x, 2.1.x, 2.2.x, and 2.3.x. Use only trusted images until upgraded. | 1.7.33, 2.0.10, 2.1.9, 2.2.5, 2.3.2 | [GHSA-xhf5-7wjv-pqxp](https://github.com/advisories/GHSA-xhf5-7wjv-pqxp) |
| CVE-2026-53489 / GHSA-rgh6-rfwx-v388 | High | Arbitrary host CRI log file read via symlink following in checkpoint restore: containerd processes container log paths without validating symlinked targets during checkpoint restoration, exposing arbitrary host files to users who run `kubectl logs` on restored containers. | 2.1.9, 2.2.5, 2.3.2 | [GHSA-rgh6-rfwx-v388](https://github.com/advisories/GHSA-rgh6-rfwx-v388) |
| CVE-2026-53492 / GHSA-33vj-92qq-66hc | High | CDI annotation smuggling via checkpoint restoration: containerd preserves CDI-related annotations from checkpoint archives rather than using the pod's create-time spec, allowing users with pod creation permissions to bypass device plugin enforcement and inject arbitrary CDI configurations into restored containers. | 2.1.9, 2.2.5, 2.3.2 | [GHSA-33vj-92qq-66hc](https://github.com/advisories/GHSA-33vj-92qq-66hc) |

*GHSA source: https://github.com/containerd/containerd/security/advisories*

## Security Posture Notes

`containerd` is the reference OCI container runtime and the Kubernetes Container Runtime Interface (CRI) implementation used in GKE, EKS, AKS, and most Kubernetes distributions. Compromise of or privilege escalation through containerd on a node provides control over every pod on that node plus host-level access.

**Recurring vulnerability classes:**

- **CRI plugin boundary failures** — image volumes, ExecSync, Attach, and stream-server paths that allow containers to exhaust host resources or access host data (CVE-2022-23648, CVE-2022-31030, CVE-2022-23471, CVE-2025-64329).
- **User ID / capability mishandling** — integer overflows and non-empty inheritable capabilities that result in containers running as root despite non-root specifications (GHSA-c9cp-9c75-9v8c, CVE-2024-40635, CVE-2026-46680). Two distinct integer-overflow pathways were found in separate years.
- **Checkpoint/restore exploitation cluster (2026-06-19)** — four high/moderate advisories filed on the same date targeting the checkpoint/restore (CRIU) feature: image tag poisoning (GHSA-cvxm-645q-p574), CDI annotation smuggling (GHSA-33vj-92qq-66hc), symlink log-file read (GHSA-rgh6-rfwx-v388), and host command execution via image `LABEL` (GHSA-xhf5-7wjv-pqxp). Users not relying on checkpoint/restore can disable the feature as an interim measure.
- **Side-channel exposure** — RAPL powercap path accessible by default in containers (GHSA-7ww5-4wqc-m92c); relevant in multi-tenant and cloud settings.

**Version support policy:** The 1.6.x line reached end-of-life before the 2026 advisories; containerd 2.1.x also appears to have reached end-of-life without receiving a patch for CVE-2026-46680. Upgrade to 2.2.x or 2.3.x is the recommended path for current security coverage.

Security disclosures are reported to `security@containerd.io` and coordinated through GitHub Security Advisories. The `SECURITY.md` documents the supported version policy.

## Dependencies of Note

- `runc` — low-level OCI container execution runtime called by containerd; carries an independent CVE history (CVE-2019-5736 container escape, CVE-2024-21626 path traversal). Containerd version compatibility must be verified against a patched runc.
- `kubelet` — Kubernetes node agent that communicates with containerd over CRI; see [[kubernetes/kubelet]].

## Open Questions

- Audit the checkpoint/restore (CRIU) feature surface more broadly: the 2026-06-19 cluster of 4 advisories suggests it is under active adversarial research.
- Verify whether `runc` CVE-2024-21626 (path traversal / container escape) is independently patched in common containerd distribution packages.
- What is the exact EOL date for containerd 2.1.x, and which GHSA records apply only to 2.1.x?

## Related Pages

- [[kubernetes/kubelet]]
- [[kubernetes/kube-apiserver]]
- [[kubernetes/index]]

---
*Last updated: 2026-06-21 | Sources: 2 (github/advisory-database code search, containerd/containerd GitHub Security Advisories)*
