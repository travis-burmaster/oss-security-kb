# moby/moby (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (Docker Engine is deployed as a standalone daemon, not typically imported as a Go module library; hundreds of millions of installations globally)
**Repository:** https://github.com/moby/moby
**Security Contact:** security@docker.com
**Disclosure Policy:** https://github.com/moby/moby/blob/master/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-07-06 | OSS Security KB | GitHub security advisory lookup (moby/moby) | automated | 21 advisory rows mapped from moby/moby GitHub security advisories (2021–2026) | [moby/moby security advisories](https://github.com/moby/moby/security/advisories) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-41091 / GHSA-3fwx-pjgw-3558 | Moderate (CVSS 7.4) | Insufficiently restricted permissions on main data directory (`/var/lib/docker`): subdirectories accessible by unprivileged Linux users, enabling execution of setuid binaries and, when UIDs match, access to or alteration of container files. | ≥ 20.10.9 | [GHSA-3fwx-pjgw-3558](https://github.com/advisories/GHSA-3fwx-pjgw-3558) |
| CVE-2021-41190 / GHSA-xmmx-7jpf-fx42 | Moderate | Ambiguous OCI image manifest parsing: when manifest documents lack definitive type markers, moby relies on the HTTP Content-Type header. Changing the header between successive pulls of the same digest allows the same content to be deserialized differently, breaking content verification. | ≥ 20.10.11 | [GHSA-xmmx-7jpf-fx42](https://github.com/advisories/GHSA-xmmx-7jpf-fx42) |
| CVE-2022-24769 / GHSA-2mm7-x5h6-5pvq | Moderate (CVSS 5.4) | Containers started with non-empty inheritable Linux process capabilities: programs with inheritable file capabilities can elevate those capabilities to the permitted set during `execve(2)`. Container security sandbox boundary not crossed; inheritable set never exceeded bounding set. | ≥ 20.10.14 | [GHSA-2mm7-x5h6-5pvq](https://github.com/advisories/GHSA-2mm7-x5h6-5pvq) |
| CVE-2022-36109 / GHSA-rc4r-wh2q-q6c4 | Low | Supplementary group permissions misconfiguration: attacker with container access may manipulate supplementary group membership to bypass primary group restrictions, potentially accessing sensitive data or executing code in certain `USER $USERNAME` Dockerfile configurations. | ≥ 20.10.18 | [GHSA-rc4r-wh2q-q6c4](https://github.com/advisories/GHSA-rc4r-wh2q-q6c4) |
| GHSA-vp35-85q5-9f25 | Low | Container build leaks host paths via Git CVE-2022-39253: Docker build process triggering git operations can be manipulated through symlink abuse to include files from outside the intended build context. Follows upstream git vulnerability. | — | [GHSA-vp35-85q5-9f25](https://github.com/advisories/GHSA-vp35-85q5-9f25) |
| CVE-2023-28840 / GHSA-232p-vwff-86mp | High (CVSS 7.5) | Swarm encrypted overlay network may be unauthenticated: iptables rules relying on the `xt_u32` kernel module to enforce IPsec on VXLAN traffic may be bypassed by administrator-set rules or absent on RHEL 9 (where `xt_u32` was removed), enabling injection of arbitrary Ethernet frames into encrypted overlay networks and denial of service or firewall evasion. | ≥ 23.0.3, ≥ 20.10.24 | [GHSA-232p-vwff-86mp](https://github.com/advisories/GHSA-232p-vwff-86mp) |
| CVE-2023-28841 / GHSA-33pg-m6jh-5237 | Moderate (CVSS 6.8) | Swarm encrypted overlay network traffic unencrypted on RHEL 9+: `xt_u32` module absence causes iptables rules that enforce outgoing VXLAN IPsec encapsulation to be silently skipped, transmitting data in plaintext despite appearing functional. Network-positioned attackers can intercept application traffic, database communications, and API data. | ≥ 23.0.3, ≥ 20.10.24 | [GHSA-33pg-m6jh-5237](https://github.com/advisories/GHSA-33pg-m6jh-5237) |
| CVE-2023-28842 / GHSA-6wrf-mxfj-pf5p | Moderate (CVSS 6.8) | Swarm encrypted overlay with single endpoint unauthenticated: iptables rules preventing unencrypted VXLAN ingress are not created until a peer is available, leaving a window during which cleartext packets tagged with an encrypted network's VNI can be injected (CWE-420/636). | ≥ 23.0.3, ≥ 20.10.24 | [GHSA-6wrf-mxfj-pf5p](https://github.com/advisories/GHSA-6wrf-mxfj-pf5p) |
| GHSA-vwm3-crmr-xfxw | High (documentation) | VXLAN port (UDP 4789) documentation advisory: ambiguous documentation failed to warn that VXLAN has no built-in confidentiality or authentication; the port must be restricted to trusted networks. No code defect; documentation updated to reflect correct firewall guidance. No CVE assigned. | N/A (guidance update) | [GHSA-vwm3-crmr-xfxw](https://github.com/advisories/GHSA-vwm3-crmr-xfxw) |
| GHSA-jq35-85cj-fj4p | Moderate | `/sys/devices/virtual/powercap` accessible to containers: Intel RAPL power-management sysfs interface usable as a side-channel against AES-NI and KASLR (CVE-2020-8694/8695/12912 class). Kernel 5.10+ restricts this, but container root bypasses the restriction via read-only sysfs mount. Fix: masks powercap path in default mount config and tightens AppArmor profile. | ≥ 24.0.7 | [GHSA-jq35-85cj-fj4p](https://github.com/advisories/GHSA-jq35-85cj-fj4p) |
| CVE-2024-24557 / GHSA-xw73-rw38-6vjc | Moderate (CVSS 6.3) | Classic builder cache poisoning: when images are built `FROM scratch` or when `HEALTHCHECK`/`ONBUILD` Dockerfile instructions change without triggering full cache invalidation, an attacker with knowledge of the target Dockerfile can inject a malicious image as a false cache candidate, compromising build integrity. Primarily affects callers who explicitly disable BuildKit or use the `/build` API endpoint. | ≥ 23.0.10, ≥ 24.0.9, ≥ 25.0.2 | [GHSA-xw73-rw38-6vjc](https://github.com/advisories/GHSA-xw73-rw38-6vjc) |
| CVE-2024-29018 / GHSA-mq39-4gv4-mvpx | Moderate (CVSS 5.9) | External DNS requests from internal-network containers: dockerd's resolver detects a loopback forwarding resolver and forwards DNS queries from the host network namespace rather than the container namespace, bypassing `--internal` network isolation. Attacker-controlled container can exfiltrate data via DNS queries to a nameserver they control. | ≥ 23.0.11, ≥ 25.0.5, ≥ 26.0.0-rc3 | [GHSA-mq39-4gv4-mvpx](https://github.com/advisories/GHSA-mq39-4gv4-mvpx) |
| CVE-2024-32473 / GHSA-x84c-p2g9-rqv9 | Moderate (CVSS 4.7) | IPv6 unintentionally enabled on IPv4-only `ipvlan`/`macvlan` network interfaces: containers can communicate with other hosts over link-local IPv6 addresses and are exposed to Router Advertisement attacks despite IPv6 being disabled in configuration. | ≥ 26.0.2 | [GHSA-x84c-p2g9-rqv9](https://github.com/advisories/GHSA-x84c-p2g9-rqv9) |
| CVE-2024-41110 / GHSA-v23v-6jw2-98fq | Critical (CVSS 9.9) | AuthZ plugin bypass via zero-length Content-Length regression: crafting API requests with `Content-Length: 0` causes the daemon to forward requests to authorization plugins without the message body, potentially allowing unauthorized API actions. Originally fixed in v18.09.1 (Jan 2019) but the fix was not carried forward to later major versions; regression persisted undetected until April 2024. Affects all deployments relying on AuthZ plugins for access control. | ≥ 23.0.15, ≥ 26.1.5, ≥ 27.1.1 | [GHSA-v23v-6jw2-98fq](https://github.com/advisories/GHSA-v23v-6jw2-98fq) |
| CVE-2025-54410 / GHSA-4vq8-7jfc-9cvp | Low (CVSS 3.3) | Firewalld reload removes bridge network isolation: after `firewall-cmd --reload`, Docker fails to restore iptables rules preventing cross-network container communication. Containers can access ports on containers in other non-internal bridge networks on the same host. Not exploitable in rootless mode or Docker Desktop. | ≥ 25.0.13, ≥ 28.0.0 | [GHSA-4vq8-7jfc-9cvp](https://github.com/advisories/GHSA-4vq8-7jfc-9cvp) |
| CVE-2025-54388 / GHSA-x4rx-4gw3-53p4 | Moderate (CVSS 5.1) | Firewalld reload makes published ports accessible from remote hosts: iptables rules preventing remote access to ports bound only to loopback are not re-created after firewalld reloads; unpublished ports remain protected. Requires daemon to run in host network namespace (not applicable to rootless or Docker Desktop). | ≥ 28.3.3 | [GHSA-x4rx-4gw3-53p4](https://github.com/advisories/GHSA-x4rx-4gw3-53p4) |
| CVE-2026-33997 / GHSA-pxq6-2prw-chj9 | Moderate (CVSS 6.8) | Off-by-one error in plugin privilege validation: two distinct issues — (1) malicious plugins can exploit the flawed comparison to trick the daemon into accepting privileges differing from user-approved ones; (2) plugins requesting exactly one privilege bypass validation entirely as no comparison is performed. Requires user interaction to install a plugin. Docker Desktop unaffected (no plugin support). | ≥ 29.3.1 (Docker Engine v1) | [GHSA-pxq6-2prw-chj9](https://github.com/advisories/GHSA-pxq6-2prw-chj9) |
| CVE-2026-34040 / GHSA-x744-4wpc-v9h2 | High (CVSS 8.8) | AuthZ plugin bypass with oversized request body — incomplete fix for CVE-2024-41110: a follow-on bypass that allows requests with a large body to bypass AuthZ plugin validation, reintroducing the class of vulnerability from CVE-2024-41110 via a different code path. Affects deployments relying on AuthZ plugins. | ≥ 29.3.1 (Docker Engine v1) | [GHSA-x744-4wpc-v9h2](https://github.com/advisories/GHSA-x744-4wpc-v9h2) |
| CVE-2026-41568 / GHSA-vp62-88p7-qqf5 | Moderate (CVSS 6.1) | Race condition in `docker cp` allows creation of empty files/directories at arbitrary host paths: path resolution and mountpoint creation occur as separate operations, allowing a container process to swap path components with symlinks to escape the container root between steps. Fix uses Go 1.24's `os.Root` for scoped filesystem operations preventing symlink escape. | ≥ 29.5.1 (Docker Engine v1), ≥ v2.0.0-beta.14 (moby/moby/v2) | [GHSA-vp62-88p7-qqf5](https://github.com/advisories/GHSA-vp62-88p7-qqf5) |
| CVE-2026-41567 / GHSA-x86f-5xw2-fm2r | High (CVSS 7.2) | `PUT /containers/{id}/archive` executes container binary on the host: decompression binaries (for xz/gzip-compressed archives) are resolved from within the container filesystem rather than the host system, allowing a container image containing a compromised decompression binary to execute arbitrary code with daemon (root) privileges when a user pipes a compressed archive into the container. Standard `docker cp` without compression is unaffected. | ≥ 29.5.1 (Docker Engine v1), ≥ v2.0.0-beta.14 (moby/moby/v2) | [GHSA-x86f-5xw2-fm2r](https://github.com/advisories/GHSA-x86f-5xw2-fm2r) |
| CVE-2026-42306 / GHSA-rg2x-37c3-w2rh | High (CVSS 7.2) | Race condition in `docker cp` allows bind mount redirection to arbitrary host paths: a malicious container process can replace the mount destination directory with a symbolic link pointing elsewhere on the host filesystem between when the destination is created and when the mount syscall executes; writes by the daemon persist after the mount is torn down. Requires an active volume mount in the container and operator-initiated `docker cp`. | ≥ 29.5.1 (Docker Engine v1), ≥ v2.0.0-beta.14 (moby/moby/v2) | [GHSA-rg2x-37c3-w2rh](https://github.com/advisories/GHSA-rg2x-37c3-w2rh) |

*OSV live record: https://osv.dev/list?ecosystem=Go&q=github.com%2Fmoby%2Fmoby*

## Security Posture Notes

`github.com/moby/moby` is the Go module for Moby, the open-source project that underlies Docker Engine. It is the most widely deployed container runtime in the world and a core infrastructure dependency across cloud-native environments. Unlike typical Go libraries, moby/moby is consumed primarily as a compiled binary (the Docker daemon) rather than as an imported Go module; its security posture therefore matters most to platform operators, CI/CD pipeline builders, and container-as-a-service providers rather than application developers importing it as a library.

**Module versioning:** The Go module was historically tracked as `github.com/docker/docker` (legacy alias, also appears in some advisories). The current v1 module path is `github.com/moby/moby`; versions ≥ 28.x are published as `+incompatible` since the module has not migrated to explicit major-version import paths. Docker Engine v29.x is tracked under the new `github.com/moby/moby/v2` module path. Advisory fixed-version fields above use Docker Engine version numbers (e.g. "29.5.1") which map to the corresponding module version.

**Advisory clustering:**

- *2021 cluster:* Data directory permissions (CVE-2021-41091), OCI manifest ambiguity (CVE-2021-41190), and inheritable capabilities (CVE-2022-24769) formed three independent hardening issues in the 20.10.x line.
- *2023 Swarm cluster (April 2023 — CVE-2023-28840/28841/28842 + GHSA-vwm3-crmr-xfxw):* Four advisories targeting Docker Swarm's encrypted overlay network implementation in a coordinated disclosure. The root causes include reliance on the `xt_u32` kernel module (absent in RHEL 9+), missing iptables rules during the initial single-endpoint state, and documentation failing to communicate VXLAN's inherent lack of confidentiality. All code issues fixed in 23.0.3 / 20.10.24.
- *2024 AuthZ regression (CVE-2024-41110, Critical CVSS 9.9):* A fix from Docker v18.09.1 (January 2019) that stripped the request body before forwarding to AuthZ plugins when `Content-Length: 0` was set was not carried forward to subsequent major-version rewrites; the regression persisted for ~5 years before re-discovery. The incomplete fix in CVE-2026-34040 demonstrates that the AuthZ plugin boundary remains an active security surface requiring ongoing attention.
- *2025 Firewalld cluster (July 2025 — CVE-2025-54388/54410):* Two related issues where firewalld reload events flush Docker's iptables rules without triggering daemon-side restoration; one affects bridge network isolation (Low), the other published port exposure to remote hosts (Moderate). Fixed across two Docker Engine releases (28.0.0 and 28.3.3).
- *2026 docker-cp / archive cluster (May 2026 — CVE-2026-41567/41568/42306):* Three advisories in rapid succession targeting `docker cp` and the `PUT /containers/{id}/archive` API. CVE-2026-41568 and CVE-2026-42306 are race conditions allowing a container to create files or redirect mounts to arbitrary host paths; CVE-2026-41567 allows a malicious container image to execute arbitrary code on the host via decompression binary substitution. All fixed in Docker Engine 29.5.1.

**Disclosure posture:** Docker/Moby maintains a documented security policy at https://github.com/moby/moby/blob/master/SECURITY.md with a dedicated security email (security@docker.com) and publishes advisories through the GitHub advisory system with CVE assignment via MITRE/NVD.

**pkg.go.dev vulnerability tracking:** As of 2026-07-06, pkg.go.dev lists 5 active vulnerabilities against the moby/moby module (GO-2026-4883, GO-2026-4887, GO-2026-5617, GO-2026-5668, GO-2026-5746), corresponding to a subset of the most recent 2026 advisories.

## Dependencies of Note

- `containerd` — moby uses containerd as the container lifecycle manager; see [[kubernetes/containerd]] for its independent advisory history.
- `runc` — low-level OCI runtime invoked by containerd; see [[kubernetes/runc]] for its container-escape history.
- `golang.org/x/net` — foundational networking module; see [[go/golang.org-x-net]] for HTTP/2 DoS history.
- `golang.org/x/crypto` — cryptographic primitives; see [[go/golang.org-x-crypto]] for SSH boundary history.

## Open Questions

- Monitor the AuthZ plugin boundary closely given the recurring CVE-2024-41110 / CVE-2026-34040 incomplete-fix chain; confirm whether any third bypass vector remains unaddressed.
- Clarify the complete security scope of the `github.com/moby/moby/v2` module vs. the legacy v1 module for Docker Engine v29+ deployments.
- Assess whether the `docker cp` race conditions (CVE-2026-41568/42306) have practical exploitation paths in production deployments where container process code-execution is required as a precondition.

## Related Pages

- [[kubernetes/containerd]]
- [[kubernetes/runc]]
- [[go/golang.org-x-net]]
- [[go/golang.org-x-crypto]]
- [[go/index]]

---
*Last updated: 2026-07-06 | Sources: 21*
