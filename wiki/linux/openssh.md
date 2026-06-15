# openssh (Linux)

**Registry:** distro (openssh-server / openssh-client across Debian, Ubuntu, RHEL, Alpine, etc.)
**Weekly Downloads:** unknown (as of 2026-06-15)
**Repository:** https://github.com/openssh/openssh-portable (portable fork) / https://www.openssh.com/
**Security Contact:** openssh@openssh.com
**Disclosure Policy:** https://www.openssh.com/security.html
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-38408 / GHSA-px36-p9hv-7h2v | Critical | **PKCS#11 ssh-agent RCE**: `ssh-agent` has an insufficiently trustworthy PKCS#11 provider search path. When agent forwarding is in use, a malicious or attacker-controlled remote server can load arbitrary PKCS#11 shared libraries from the client's filesystem, achieving unauthenticated RCE on the client machine. Root cause is an incomplete fix for CVE-2016-10009. | 9.3p2 | [GHSA-px36-p9hv-7h2v](https://github.com/advisories/GHSA-px36-p9hv-7h2v) |
| CVE-2023-48795 / GHSA-45x7-px36-x8w8 | Medium | **Terrapin SSH prefix truncation**: Protocol-level attack enabling an active MitM to truncate the negotiation transcript, potentially downgrading handshake extension negotiation (e.g., disabling `chacha20-poly1305` or `*-etm@openssh.com` MACs) or stripping security-relevant extensions. OpenSSH mitigated via strict key exchange mode (`-oStrictHostKeyChecking`). Both endpoints must support the mitigation for full protection. | 9.6 (with strict kex) | [GHSA-45x7-px36-x8w8](https://github.com/advisories/GHSA-45x7-px36-x8w8) |
| CVE-2023-51767 / GHSA-44xq-r8h3-q4q6 | Medium | **PKCS#11 destination constraint bypass**: When adding PKCS#11-hosted private keys to `ssh-agent` with destination constraints, the constraints are only applied to the first returned key even if the PKCS#11 token returns multiple keys — remaining keys are added without the intended constraint. | 9.6 | [GHSA-44xq-r8h3-q4q6](https://github.com/advisories/GHSA-44xq-r8h3-q4q6) |
| CVE-2024-6387 / GHSA-2x8c-95vh-gfv4 | High (CVSS 8.1) | **regreSSHion — SIGALRM race condition RCE** (glibc Linux): When a client fails to authenticate within `LoginGraceTime` (default 120 s), `sshd` delivers `SIGALRM` asynchronously. The signal handler calls async-signal-unsafe functions (e.g., `syslog()`), creating a race condition in the privileged `sshd` code path that a determined attacker may exploit for unauthenticated RCE as root on glibc-based Linux systems. A regression from the fix for CVE-2006-5051. | 9.8p1 | [GHSA-2x8c-95vh-gfv4](https://github.com/advisories/GHSA-2x8c-95vh-gfv4) |
| CVE-2025-26465 / GHSA-jrwv-mv4h-7rrq | Medium | **VerifyHostKeyDNS MITM**: When `VerifyHostKeyDNS` is enabled, OpenSSH's `ssh` client mishandles certain error codes during host key verification, allowing a malicious server to impersonate a legitimate server (MitM). Exploitation additionally requires the attacker to exhaust the client's memory, making attack complexity high in practice. | 9.9p2 | [GHSA-jrwv-mv4h-7rrq](https://github.com/advisories/GHSA-jrwv-mv4h-7rrq) |

*OpenSSH security history: https://www.openssh.com/security.html*

## Security Posture Notes

OpenSSH (Secure Shell) is installed on effectively all Linux server deployments as the default remote access tool. The sshd daemon runs as root on TCP/22 and is directly reachable by unauthenticated network principals, making it a tier-1 attack surface.

The project has an active security policy and coordinates disclosures through openssh@openssh.com with a dedicated release process (portable releases track the upstream OpenBSD source).

**Distro backport caveat**: Distro packages (e.g., Debian `openssh-server`, RHEL `openssh`) frequently backport fixes to older upstream versions rather than upgrading to the latest release. The fixed version numbers above refer to upstream OpenSSH releases; verify your distro's security tracker for the exact fixed package version.

**CVE-2024-6387 (regreSSHion) context**: This vulnerability only affects glibc-based Linux (not OpenBSD or musl-based distributions). While CVSS is 8.1, reliable exploitation requires winning a precise race condition. Qualys reported successful PoC exploitation on 32-bit systems in ~6–8 hours. Mitigation: set `LoginGraceTime 0` in `sshd_config` (disables the grace timeout, eliminating the race) or restrict SSH to known IP ranges.

**CVE-2023-38408 context**: The most direct remediation beyond patching is to **disable ssh-agent forwarding** (`ForwardAgent no` in `~/.ssh/config` or `sshd_config`). Agent forwarding is a persistent security risk even absent this specific CVE.

**Terrapin (CVE-2023-48795)**: Not strictly an OpenSSH-only vulnerability — it affects all SSH implementations. Full mitigation requires both client and server to negotiate strict key exchange. OpenSSH 9.6+ enables this by default for supported cipher suites.

## Dependencies of Note

- **libssl / libcrypto** (OpenSSL or LibreSSL): upstream TLS/crypto library — see `[[linux/openssl]]`
- **PAM**: privilege separation and authentication stack; PAM configuration affects the openssh attack surface (e.g., `PermitPAMUserChange`)
- **glibc**: CVE-2024-6387 is specific to glibc systems; musl-based distributions are unaffected

## Open Questions

- Enumerate the Debian/Ubuntu/RHEL fixed package versions for CVE-2024-6387 (9.8p1 upstream; distro backports differ).
- Check whether CVE-2025-26465 has been confirmed in default distributions that ship with `VerifyHostKeyDNS` enabled.
- Track any 2026 advisories via https://www.openssh.com/security.html on next pass.
- Query osv.dev with Debian/Ubuntu/Alpine ecosystem keys to enumerate distro-specific openssh records.

## Related Pages

- [[linux/openssl]]
- [[linux/sudo]]
- [[linux/index]]

---
*Last updated: 2026-06-15 | Sources: 5 GHSA records (github/advisory-database via GitHub code search)*
