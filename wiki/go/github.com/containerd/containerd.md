# containerd (Go)

**Registry:** pkg.go.dev (github.com/containerd/containerd/v2; v1: github.com/containerd/containerd)
**Weekly Downloads:** N/A — deployed as binary daemon; ~3,300 direct Go module importers (as of 2026-09-29)
**Repository:** https://github.com/containerd/containerd
**Security Contact:** security@containerd.io
**Disclosure Policy:** https://github.com/containerd/containerd/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-09-29 | KB maintainer | advisory-database pass | automated (GHSA search) | 36 total GHSA advisories identified; 4 fully mapped in this pass | [GHSA search](https://github.com/advisories?query=containerd) |

*No independent full-source audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-53493 / GHSA-pg57-6jwg-q645 | Moderate | DoS via malicious OCI image index with deeply nested or heavily fanned-out descriptor graphs causing unbounded CPU/memory consumption before container execution | 1.7.36, 2.0.13, 2.2.9, 2.3.6, 2.4.1 | [GHSA-pg57-6jwg-q645](https://github.com/advisories/GHSA-pg57-6jwg-q645) |
| CVE-2026-53489 / GHSA-rgh6-rfwx-v388 | High (CVSS:4.0/AV:N/AC:L/PR:L/VC:H) | CRI checkpoint restore follows symlinks in container.log path, enabling any user with `kubectl logs` access to read arbitrary host files (CWE-61) | 2.1.9, 2.2.5, 2.3.2 | [GHSA-rgh6-rfwx-v388](https://github.com/advisories/GHSA-rgh6-rfwx-v388) |
| CVE-2026-53488 / GHSA-xhf5-7wjv-pqxp | High | CRI plugin passes unvalidated Dockerfile LABEL instructions to `binary://` logger plugin, enabling host-root command execution during image pulls | 1.7.33, 2.0.10, 2.1.9, 2.2.5, 2.3.2 | [GHSA-xhf5-7wjv-pqxp](https://github.com/advisories/GHSA-xhf5-7wjv-pqxp) |
| CVE-2025-47290 / GHSA-cm76-qm8v-3j95 | High | TOCTOU race condition during image pulls allows arbitrary host file system modification via specially crafted container images | 2.1.1 | [GHSA-cm76-qm8v-3j95](https://github.com/advisories/GHSA-cm76-qm8v-3j95) |

*36 total GHSA advisories on record as of 2026-09-29; 32 additional advisories not fully mapped in this pass. Known historical advisories not yet mapped include: CVE-2020-15257 (Shim API Unix socket exposure in network namespace), CVE-2021-41103 (insufficient file system permissions on container root), CVE-2022-23648 (volume mount path traversal), CVE-2023-25173 (supplemental group permissions bypass). See https://github.com/containerd/containerd/security/advisories for the authoritative list.*

## Security Posture Notes

containerd is the industry-standard container runtime implementing the OCI Runtime Spec and Kubernetes Container Runtime Interface (CRI). It is the core runtime for Docker Engine, Kubernetes (via CRI), Amazon ECS, Google GKE, Azure AKS, and Rancher, and underpins essentially every production container workload. It is a CNCF graduated project since 2019.

The project maintains an active security disclosure process (security@containerd.io, 90-day coordinated disclosure embargo). Advisories are published at https://github.com/containerd/containerd/security/advisories and cross-referenced in the GitHub Advisory Database.

**Module versioning**: the v2 module path (`github.com/containerd/containerd/v2`) was introduced in containerd 2.0 (October 2024). The v1.7.x branch is maintained in LTS mode and continues to receive security patches.

**Recurring advisory themes** across the 36-advisory GHSA history:
- **Container escape / host access**: CRI label injection for logger-binary execution (2026), CRI symlink-following file reads (2026), TOCTOU host FS modification (2025), supplemental group bypass (CVE-2023-25173), volume mount path traversal (CVE-2022-23648), Shim API Unix socket exposed in network namespace (CVE-2020-15257)
- **Privilege escalation**: container root file system insufficient permissions enabling namespace escapes (CVE-2021-41103)
- **Denial of service**: OCI image index descriptor graph amplification (2026), rate-limiting bypass via crafted requests

The combination of supply-chain exposure (image pull as attack vector), ubiquitous deployment, and privileged host access makes containerd a high-priority target for security review in any Kubernetes or container-based environment.

## Dependencies of Note

- `github.com/opencontainers/runc` — container execution engine; historically a vector for container escapes (runc CVE-2019-5736 Critical CVSS 8.6, CVE-2022-29162 High); its advisory history is independent from containerd's
- `github.com/moby/buildkit` — build tooling with a separate, active advisory history (GHSA-72x6-4j93-7w86 / CVE-2026-61712 BuildKit DoS)
- `github.com/opencontainers/image-spec` — OCI image format parsing; malformed OCI images are a recurring attack surface
- `github.com/opencontainers/selinux` — SELinux labeling used by CRI plugin (relevant to label-injection advisories)

## Open Questions

- Map the remaining 32 un-fully-mapped GHSA advisories, especially the 2019–2023 cluster (CVE-2020-15257, CVE-2021-41103, CVE-2022-23648, CVE-2023-25173)
- Check whether CVE-2024-24557 (Moby/Docker) has a corresponding containerd-side advisory
- Verify the GHSA-c9cp-9c75-9v8c (2024-05) and GHSA-cxfp-7pvr-95ff (2025-05) advisories; likely related to CRI or snapshot manager
- Assess whether the runc advisory history (separate crate/module) should be tracked here or in a separate page

## Related Pages

- [[go/github.com/moby/moby]]
- [[go/index]]

---
*Last updated: 2026-09-29 | Sources: 5 (GHSA database, github.com/advisories)*
