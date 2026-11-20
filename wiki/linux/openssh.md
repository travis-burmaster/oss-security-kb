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
| CVE-2026-35387 / GHSA-hpxh-vgmp-3qp6 | Low (CVSS 3.1) | **ECDSA algorithm config over-permissioning**: Mentioning any ECDSA algorithm in `PubkeyAcceptedAlgorithms` or `HostbasedAcceptedAlgorithms` causes OpenSSH to treat all ECDSA algorithms as permitted rather than only the named one. Allows a broader algorithm surface than the operator intended. CWE-670. | 10.3 | [GHSA-hpxh-vgmp-3qp6](https://github.com/advisories/GHSA-hpxh-vgmp-3qp6) |
| CVE-2026-35388 / GHSA-9fjj-jvxf-738c | Low (CVSS 3.1) | **Multiplexing confirmation omission**: `ssh` in proxy-mode multiplexing sessions omits the expected connection-establishment confirmation, potentially enabling a client to proceed without proper session validation. CWE-420. | 10.3 | [GHSA-9fjj-jvxf-738c](https://github.com/advisories/GHSA-9fjj-jvxf-738c) |
| CVE-2026-35414 / GHSA-f6c7-fj8h-5898 | Moderate (CVSS 5.1) | **`authorized_keys` principals option bypass**: A parsing boundary flaw in the principals option processing allows a certificate-based authentication scenario to bypass the intended principal restriction. Requires authentication; limited C:L/I:L impact. CWE-670. | 10.3p1 | [GHSA-f6c7-fj8h-5898](https://github.com/advisories/GHSA-f6c7-fj8h-5898) |
| CVE-2026-59996 / GHSA-8v2x-fhq9-4fv3 | Moderate (CVSS ~4.2) | **`scp` remote-to-remote path traversal**: When copying files between two remote destinations, `scp` may place a file in the parent directory of the intended destination directory due to a relative path handling flaw. CWE-23. | 10.4p1 | [GHSA-8v2x-fhq9-4fv3](https://github.com/advisories/GHSA-8v2x-fhq9-4fv3) |
| CVE-2026-60002 / GHSA-gp5v-jg37-fvg6 | High (CVSS ~7.5) | **Client-side use-after-free during key re-exchange**: A use-after-free condition in the SSH client occurs when a server modifies its host key during key re-exchange operations. A malicious server could exploit this to achieve code execution on the client. CWE-416. | 10.4p1 | [GHSA-gp5v-jg37-fvg6](https://github.com/advisories/GHSA-gp5v-jg37-fvg6) |
| CVE-2026-123158 / GHSA-4fcc-vm97-gx3x | High (AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H) | **sshhole: musl-libc/no-PAM password authentication bypass** (Alpine Linux and similar). **On CISA KEV (added 2026-11-09).** sshd in OpenSSH before 10.6p2 on Linux, when musl libc is used without PAM, lacks a workaround for a password authentication bypass (related to misinterpretation of whether a string is intended to be a password hash). For some configurations of accounts, any password between 256 and 1024 characters succeeds. An example of a platform using musl libc without PAM is Alpine Linux. CWE-394. Published 2026-11-05. | 10.6p2 | [GHSA-4fcc-vm97-gx3x](https://github.com/advisories/GHSA-4fcc-vm97-gx3x), [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-123158), [Alpine notice](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass), [upstream commit](https://github.com/openssh/openssh-portable/commit/4353fdc43ef646c43a8dda7025cc1a898caf1482) |
| CVE-2026-106552 / GHSA-695p-3q57-gff4 | Moderate (AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:L/A:L) | In sftp in OpenSSH before 10.6, a server can trigger directory traversal (causing files to be written to unintended locations) during a recursive copy operation. CWE-23. Published 2026-10-06. | 10.6 | [GHSA-695p-3q57-gff4](https://github.com/advisories/GHSA-695p-3q57-gff4) |
| CVE-2026-106585 / GHSA-j4h6-744f-q3hq | Moderate (AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:L) | In sshd and ssh in OpenSSH before 10.6, there is no check for whether the maximum packet length is exceeded during decompression of highly compressed data. CWE-409. Published 2026-10-06. | 10.6 | [GHSA-j4h6-744f-q3hq](https://github.com/advisories/GHSA-j4h6-744f-q3hq) |
| CVE-2026-106553 / GHSA-2xxv-m3rc-rvrm | Low (AV:L/AC:H/PR:L/UI:R/S:U/C:L/I:N/A:N) | In sshd in OpenSSH before 10.6, credentials can incorrectly persist after failure of a GSSAPIAuthentication authentication attempt. CWE-669. Published 2026-10-06. | 10.6 | [GHSA-2xxv-m3rc-rvrm](https://github.com/advisories/GHSA-2xxv-m3rc-rvrm) |
| CVE-2026-106555 / GHSA-j45v-7hgc-xv9x | Low (AV:L/AC:H/PR:L/UI:R/S:U/C:L/I:N/A:N) | In sshd in OpenSSH before 10.6, GSSAPIAuthentication authentication state can incorrectly be persisted across authentication attempts. CWE-669. Published 2026-10-06. | 10.6 | [GHSA-j45v-7hgc-xv9x](https://github.com/advisories/GHSA-j45v-7hgc-xv9x) |
| CVE-2026-106586 / GHSA-jrjw-pc9r-c624 | Low (AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:N) | In sshd in OpenSSH before 10.6, the restrict keyword (in authorized_keys) was supposed to be applicable to tunnel forwarding but was not, a different vulnerability than CVE-2026-73283. CWE-670. Published 2026-10-06. | 10.6 | [GHSA-jrjw-pc9r-c624](https://github.com/advisories/GHSA-jrjw-pc9r-c624) |
| CVE-2026-106583 / GHSA-99hr-wq4p-x49q | Low (AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:N) | In ssh in OpenSSH before 10.6, a $ or \ character can occur in a command-line username, leading to injection. CWE-99. Published 2026-10-07. | 10.6 | [GHSA-99hr-wq4p-x49q](https://github.com/advisories/GHSA-99hr-wq4p-x49q) |
| CVE-2026-106582 / GHSA-9xxf-58mh-q784 | Low (AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N) | In sshd and ssh in OpenSSH before 10.6, an LZ77 dictionary coder can be used even though this is contraindicated by the arXiv 2609.07709 "Crossing the Streams" findings. CWE-514. Published 2026-10-06. | 10.6 | [GHSA-9xxf-58mh-q784](https://github.com/advisories/GHSA-9xxf-58mh-q784) |
| CVE-2026-106587 / GHSA-8fmq-pfxf-6hmc | Low (AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:L) | In sshd in OpenSSH before 10.6, the value "none" for a configuration option is sometimes interpreted as a filename but was intended to mean that a feature is disabled. CWE-843. Published 2026-10-07. | 10.6 | [GHSA-8fmq-pfxf-6hmc](https://github.com/advisories/GHSA-8fmq-pfxf-6hmc) |
| CVE-2026-106584 / GHSA-9hq3-hc6p-gc8q | Low (AV:L/AC:H/PR:N/UI:R/S:U/C:N/I:L/A:N) | In ssh-keygen in OpenSSH before 10.6, certificates could have incorrect expiration times because of Daylight Saving mishandling. There can be a slightly more severe effect on users in certain Antarctic locations. CWE-193. Published 2026-10-06. | 10.6 | [GHSA-9hq3-hc6p-gc8q](https://github.com/advisories/GHSA-9hq3-hc6p-gc8q) |
| CVE-2026-106588 / GHSA-74g8-x9g6-gwmc | Low (AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:N) | In sshd in OpenSSH through 10.6, use of the macOS 27 (or later) SDK has the side effect of loss of sandboxing, which is potentially unexpected. CWE-653. Published 2026-10-07. | Not stated ("through 10.6") | [GHSA-74g8-x9g6-gwmc](https://github.com/advisories/GHSA-74g8-x9g6-gwmc) |
| CVE-2026-106589 / GHSA-8wpc-x9xg-9q94 | Low (AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N) | In sshd in OpenSSH through 10.6, in certain environments such as QNX 6 and SCO OpenServer 5, sshd-session can unexpectedly have root privileges. This is related to the GatewayPorts and StreamLocalForwarding configuration options, and lack of support for file-descriptor passing and unprivileged allocation of PTY devices. CWE-272. Published 2026-10-07. | Not stated ("through 10.6"); QNX 6 / SCO OpenServer 5 only | [GHSA-8wpc-x9xg-9q94](https://github.com/advisories/GHSA-8wpc-x9xg-9q94) |
| CVE-2026-110923 / GHSA-cv5v-cq2q-vv46 | Moderate (AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N) | A flaw was found in OpenSSH. During an sftp copy, a malicious server can supply an empty name, a slash-only path, or a ".." basename that sftp uses as the local destination, writing outside the directory the user selected. CWE-22. Published 2026-10-15. | Not stated in GHSA record; see RHSA-2026:82247 | [GHSA-cv5v-cq2q-vv46](https://github.com/advisories/GHSA-cv5v-cq2q-vv46), [Red Hat](https://access.redhat.com/security/cve/CVE-2026-110923) |
| CVE-2026-110924 / GHSA-q953-q6mf-pwpq | Moderate (AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N) | A flaw was found in OpenSSH. With GSSAPI authentication enabled, a failed GSSAPI attempt can leave delegated credentials stored for the connection even though user authorization did not succeed. A later successful login on that connection is not authorized by the leftover state. CWE-459. Published 2026-10-15. | Not stated in GHSA record; see RHSA-2026:82247 | [GHSA-q953-q6mf-pwpq](https://github.com/advisories/GHSA-q953-q6mf-pwpq), [Red Hat](https://access.redhat.com/security/cve/CVE-2026-110924) |
| CVE-2026-110925 / GHSA-h54q-2vm3-97qv | Moderate (AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N) | A flaw was found in OpenSSH. A username entered on the ssh command line can still contain '$' or a non-trailing backslash. When a configuration expands %u inside ProxyCommand or Match exec, those characters are passed into the shell. CWE-78. Published 2026-10-15. | Not stated in GHSA record; see RHSA-2026:82247 | [GHSA-h54q-2vm3-97qv](https://github.com/advisories/GHSA-h54q-2vm3-97qv), [Red Hat](https://access.redhat.com/security/cve/CVE-2026-110925) |
| CVE-2026-110926 / GHSA-3j57-3pc4-v67v | Moderate (AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:N) | A flaw was found in OpenSSH. When compression is negotiated, channels on the same connection share one LZ77 dictionary. A peer who can write on one channel can recover plaintext from another channel by chosen-plaintext lengths. CWE-203. Published 2026-10-15. | Not stated in GHSA record; see RHSA-2026:82247 | [GHSA-3j57-3pc4-v67v](https://github.com/advisories/GHSA-3j57-3pc4-v67v), [Red Hat](https://access.redhat.com/security/cve/CVE-2026-110926) |
| CVE-2026-110927 / GHSA-hq2f-vwrj-48j9 | Moderate (AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L) | A flaw was found in OpenSSH. After compression is negotiated, a compressed payload can expand past the maximum supported packet size because the inflate loop does not stop at that limit. Memory use grows in the process handling that connection. CWE-770. Published 2026-10-15. | Not stated in GHSA record; see RHSA-2026:82247 | [GHSA-hq2f-vwrj-48j9](https://github.com/advisories/GHSA-hq2f-vwrj-48j9), [Red Hat](https://access.redhat.com/security/cve/CVE-2026-110927) |

*2026-11-20 pass: 17 rows added above (from CVE-2026-123158 onward). The 10.6 / 10.6p2 rows come from unreviewed GHSA records that cite the OpenSSH 10.6 and 10.6p2 release notes. The five CVE-2026-1109xx rows are Red Hat-assigned records; their GHSA text does not state an upstream fixed version, and several describe the same flaw classes as the 10.6 CVEs (compression dictionary sharing, decompression size, GSSAPI credential persistence, sftp destination traversal, command-line username metacharacters). They are listed separately because they carry distinct CVE IDs; treat the pairing as unverified. Excluded as different products: nine Microsoft "OpenSSH for Windows" records (CVE-2026-69397, CVE-2026-70163, CVE-2026-83754, CVE-2026-83769, CVE-2026-83871, CVE-2026-83923, CVE-2026-88157, CVE-2026-97811, CVE-2026-97816), Apache MINA SSHD (CVE-2026-93994, CVE-2026-94029), and fail2ban's sshd filter (CVE-2026-109786).*

*OpenSSH security history: https://www.openssh.com/security.html*

## Security Posture Notes

OpenSSH (Secure Shell) is installed on effectively all Linux server deployments as the default remote access tool. The sshd daemon runs as root on TCP/22 and is directly reachable by unauthenticated network principals, making it a tier-1 attack surface.

The project has an active security policy and coordinates disclosures through openssh@openssh.com with a dedicated release process (portable releases track the upstream OpenBSD source).

**sshhole (CVE-2026-123158) context**: Added to CISA KEV on 2026-11-09 with a 2026-11-12 due date and forensic triage required. Only sshd on Linux built against musl libc without PAM is affected (Alpine Linux is the main example, including many Alpine-based container images that run sshd). For some account configurations, any password between 256 and 1024 characters is accepted. Fixed in 10.6p2. Mitigations short of upgrading: disable `PasswordAuthentication`, or rebuild with PAM.

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
- Enumerate the Debian/Ubuntu/RHEL fixed package versions for CVE-2026-60002 (10.4p1 upstream; distro backports differ).
- CVE-2026-60002 (client UAF) has no known public PoC as of 2026-09-30; track exploitation reports.
- Query osv.dev with Debian/Ubuntu/Alpine ecosystem keys to enumerate distro-specific openssh records.
- 52 total GHSA entries for openssh in advisory-database as of the 2026-09-30 pass; 2026 batch (April and July) captured then. 2026-11-20 pass added the September-November batch (10.6, 10.6p2, Red Hat CVE-2026-1109xx).
- Confirm the upstream fixed version for the Red Hat CVE-2026-110923 through CVE-2026-110927 records and whether each duplicates a CVE-2026-1065xx record (openssh.org was unreachable from this environment).
- CVE-2026-106588 (macOS 27 SDK sandbox loss) and CVE-2026-106589 (QNX / SCO privilege) are described as "through 10.6" with no fix stated; check later release notes.

## Related Pages

- [[linux/openssl]]
- [[linux/sudo]]
- [[linux/index]]

---
*Last updated: 2026-11-20 | Sources: 27 GHSA records (github/advisory-database via GitHub code search and raw.githubusercontent.com); CISA KEV catalog 2026.11.18*
