# runc (Kubernetes)

**Registry:** k8s / GitHub Releases / OS package managers (bundled with Docker, containerd, CRI-O)
**Weekly Downloads:** N/A — installed via container runtime distributions or OS packages
**Repository:** https://github.com/opencontainers/runc
**Security Contact:** security@opencontainers.org / https://github.com/opencontainers/runc/security/advisories
**Disclosure Policy:** https://github.com/opencontainers/runc/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-22 | OSS Security KB | GHSA database lookup | automated | 6 public advisories mapped (CVE-2019-5736 through CVE-2024-21626) | [github/advisory-database](https://github.com/github/advisory-database) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-5736 / GHSA-gxmr-w5mj-v8hh | High — CVSS 8.6 | Container escape via `/proc/self/exe` overwrite: runc allowed a malicious container image (or an attacker with write access to a running container) to overwrite the host runc binary by opening `/proc/self/exe` for writing, granting full root access to the host. The attacker exploits the brief window during `runc exec` when runc is still the executing process. | 1.0-rc7 | [GHSA-gxmr-w5mj-v8hh](https://github.com/advisories/GHSA-gxmr-w5mj-v8hh) |
| CVE-2021-30465 / GHSA-c3xm-pvg7-gh7r | High — CVSS 7.6 | TOCTOU symlink race during volume mount: runc resolved mount paths without holding locks, allowing an attacker with the ability to create containers with custom volume-mounts to replace a target directory with a symlink (symlink exchange attack) during the check–use window and mount arbitrary host filesystem paths into the container, potentially enabling container escape. | 1.0.0-rc95 | [GHSA-c3xm-pvg7-gh7r](https://github.com/advisories/GHSA-c3xm-pvg7-gh7r) |
| CVE-2022-29162 / GHSA-f3fp-gc8g-vw66 | Moderate | Capabilities elevation via non-empty inheritable Linux capability set: `runc exec --cap` granted additional capabilities to executed processes but also set non-empty inheritable capabilities, allowing programs with matching file capabilities (via `execve`) to receive elevated privileges beyond the bounding set. Patch ensures `runc exec --cap` excludes inheritable capabilities; `runc spec` no longer sets inheritable capabilities in generated OCI specs. | 1.1.2 | [GHSA-f3fp-gc8g-vw66](https://github.com/advisories/GHSA-f3fp-gc8g-vw66) |
| CVE-2023-27561 / GHSA-vpvm-3wq2-2wvm | High — CVSS 7.4 | Incorrect access control / privilege escalation (CVE-2019-19921 regression): `libcontainer/rootfs_linux.go` contained a mount-handling flaw allowing an attacker who can spawn multiple containers with custom volume configurations to escalate privileges. The issue regressed the earlier CVE-2019-19921 fix. | 1.1.5 | [GHSA-vpvm-3wq2-2wvm](https://github.com/advisories/GHSA-vpvm-3wq2-2wvm) |
| CVE-2023-28642 / GHSA-g2j6-57v7-gm8c | Moderate | AppArmor / SELinux bypass via symlinked `/proc`: when `/proc` inside the container was replaced with a symlink under a specific mount configuration, AppArmor (and potentially SELinux) label enforcement could be bypassed. The same runc 1.1.5 release fixes CVE-2023-27561 by prohibiting symlinked `/proc`. | 1.1.5 | [GHSA-g2j6-57v7-gm8c](https://github.com/advisories/GHSA-g2j6-57v7-gm8c) |
| CVE-2024-21626 / GHSA-xr7r-f8xq-vfvv | High — CVSS 8.6 | Container breakout via file descriptor leak and `process.cwd` manipulation: an internal fd leak in runc (introduced in v1.0.0-rc93) allowed `runc init` to retain a handle to the host `/sys/fs/cgroup`. Setting `process.cwd` to a path that resolved through `/proc/self/fd/<n>/` caused the spawned container process's working directory to be in the host mount namespace. Four distinct attack variants were identified: malicious image with crafted `process.cwd` (attack 1), `runc exec --cwd` container breakout (attack 2), and host binary overwrite variants (attacks 3a/3b). All four lead to full host compromise. | 1.1.12 | [GHSA-xr7r-f8xq-vfvv](https://github.com/advisories/GHSA-xr7r-f8xq-vfvv) |

## Security Posture Notes

`runc` is the reference OCI runtime and the lowest-level execution layer for every container workload on Linux. It is used directly by Docker, containerd, CRI-O, and Podman, making it a critical component in virtually all Kubernetes node configurations.

**Recurring vulnerability classes:**

- **File-descriptor leaks into container init:** Internal runc file descriptors leaked into `runc init` have repeatedly been the root cause of container escapes. CVE-2024-21626 is the most recent and severe example; the fix in 1.1.12 applied `O_CLOEXEC` broadly and added a working-directory containment check after `pivot_root`.
- **TOCTOU races on mount paths:** CVE-2021-30465 and the CVE-2019-19921 / CVE-2023-27561 regression class show that resolving mount paths without locking is dangerous. Concurrent symlink-exchange attacks can redirect mounts to host paths.
- **Linux capabilities boundary:** CVE-2022-29162 demonstrates that `exec --cap` capability augmentation must not populate the inheritable set; programs with matching file capabilities can then silently elevate at `execve` time.
- **MAC bypass via `/proc` symlink:** CVE-2023-28642 shows that kernel-level mandatory access controls can be bypassed at the runc layer when the container's `/proc` is replaced; the fix is an explicit pre-mount check.

**Latest release:** v1.5.0 (2026-06-19). The project is actively maintained under the OCI / CNCF umbrella with prompt security responses.

**Interaction with containerd:** See also [[kubernetes/containerd]] — containerd calls runc as its low-level runtime, and vulnerabilities in runc directly affect containerd-managed nodes.

## Dependencies of Note

- **`github.com/opencontainers/runc`** bundles libcontainer, which provides the core namespace/cgroup/seccomp implementation; libcontainer is the primary attack surface for all container-escape advisories listed above.
- **kernel interfaces:** seccomp, Linux capabilities, cgroups v1/v2, namespaces (mount, user, PID, net), `/proc/self/exe` semantics — these are OS-level attack surfaces, not Go library dependencies.

## Open Questions

- Confirm CVSS scores and fixed-version details for CVE-2019-5736 (pre-GitHub advisory era; NVD record may differ from upstream).
- Check for any runc advisories between 1.1.12 and current v1.5.0 (possible advisories in 2025–2026 not yet captured in this pass).
- Review interaction between runc and rootless-container flows (user namespaces) for any advisory-class gaps.

## Related Pages

- [[kubernetes/containerd]]
- [[kubernetes/kubelet]]
- [[kubernetes/index]]

---
*Last updated: 2026-06-22 | Sources: github/advisory-database (GHSA-gxmr-w5mj-v8hh, GHSA-c3xm-pvg7-gh7r, GHSA-f3fp-gc8g-vw66, GHSA-vpvm-3wq2-2wvm, GHSA-g2j6-57v7-gm8c, GHSA-xr7r-f8xq-vfvv), pkg.go.dev/github.com/opencontainers/runc*
