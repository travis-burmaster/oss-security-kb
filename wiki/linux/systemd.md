# systemd (Linux)

**Registry:** distro
**Weekly Downloads:** unknown (default init system and service manager on virtually all major Linux distributions including Debian, Ubuntu, Fedora, RHEL/CentOS, Arch Linux, openSUSE, and their derivatives; as of 2026-07-10)
**Repository:** https://github.com/systemd/systemd
**Security Contact:** security@systemd.io
**Disclosure Policy:** https://github.com/systemd/systemd/blob/main/docs/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No third-party audits on record at the Linux-package level. The systemd project maintains its own security advisory history via GitHub security advisories and the oss-security mailing list.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2017-1000082 / GHSA-pp67-7cmm-9pp7 | Critical (CVSS:3.1 9.8 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Numeric-prefix username privilege escalation — systemd v233 and earlier fails to safely parse usernames starting with a numeric digit (e.g. "0day"), causing the associated service to run with root privileges rather than the intended user account | systemd > 233 | [GHSA-pp67-7cmm-9pp7](https://github.com/advisories/GHSA-pp67-7cmm-9pp7) |
| CVE-2017-9217 / GHSA-pv82-vf69-rqqm | High (CVSS:3.1 7.5 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) | systemd-resolved DNS daemon crash — a crafted DNS response with an empty question section causes systemd-resolved through 233 to crash; no authentication required from network | systemd > 233 | [GHSA-pv82-vf69-rqqm](https://github.com/advisories/GHSA-pv82-vf69-rqqm) |
| CVE-2020-1712 / GHSA-wggx-8wf7-vg3g | High (CVSS:3.1 7.8 AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) | Heap use-after-free in async Polkit dbus handling — systemd before v245-rc1 performs asynchronous Polkit queries while handling dbus messages; a local unprivileged attacker can send specially crafted dbus messages to crash systemd services or potentially elevate privileges | systemd ≥ v245-rc1 | [GHSA-wggx-8wf7-vg3g](https://github.com/advisories/GHSA-wggx-8wf7-vg3g) |
| CVE-2020-13529 / GHSA-44p7-qpr4-rgvf | Moderate (CVSS:3.1 7.1 AV:A/AC:H/PR:N/UI:N/S:C/C:N/I:N/A:H) | DHCP FORCERENEW spoofing DoS — an adjacent-network attacker forging paired FORCERENEW + DHCP ACK packets can cause systemd-networkd in Systemd 245 to reconfigure the network interface, disrupting availability | systemd > 245 | [GHSA-44p7-qpr4-rgvf](https://github.com/advisories/GHSA-44p7-qpr4-rgvf) |
| CVE-2021-3997 / GHSA-4p54-q58q-8mpc | Moderate (CVSS:3.1 AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | systemd-tmpfiles uncontrolled recursion DoS — an uncontrolled recursion flaw in systemd-tmpfiles triggered by too many nested directories in /tmp can cause denial of service at boot time; a local attacker able to create deeply nested directories under /tmp before a reboot can exploit this | version range not specified in advisory | [GHSA-4p54-q58q-8mpc](https://github.com/advisories/GHSA-4p54-q58q-8mpc) |
| CVE-2023-26604 / GHSA-8989-8fhv-vq42 | High (CVSS:3.1 7.8 AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) | systemctl status less-pager local privilege escalation — systemd before 247 does not set LESSSECURE=1 when invoking the `less` pager for `systemctl status`; when systemctl is run via sudo (a common sudoers configuration), the pager runs as root and can be used to launch arbitrary programs via less key bindings | systemd ≥ 247 | [GHSA-8989-8fhv-vq42](https://github.com/advisories/GHSA-8989-8fhv-vq42) |

## Security Posture Notes

systemd is the init system and service manager on virtually all modern Linux distributions; it is PID 1 and runs throughout the entire system lifetime with maximum privilege. Vulnerabilities in systemd, systemd-resolved, systemd-networkd, or systemd-journald therefore have disproportionate blast radius compared to userland packages.

**CVE-2023-26604 (High CVSS 7.8)** is the most practically significant recent advisory: a local attacker with sudo privileges for `systemctl status` can escalate to root by exploiting the `less` pager's shell-escape functionality when the terminal is too small to display all output. This affects any system where a sudoers configuration permits `systemctl status` (a common DevOps hardening pattern) and systemd < 247. Many enterprise Linux distributions backported the LESSSECURE fix; check distro-specific errata.

**CVE-2020-1712 (High LPE)** involved a heap use-after-free in the dbus message processing path while asynchronous Polkit authorization queries were in flight. This is especially relevant on distributions where systemd services use Polkit for privilege checks (e.g., NetworkManager, GNOME system services).

**Systemd-resolved (CVE-2017-9217)**: The DNS resolver component has a history of network-reachable DoS vulnerabilities; operators relying on systemd-resolved as the primary DNS resolver (default on Ubuntu, Fedora, etc.) should ensure they are on a patched version and consider limiting resolver exposure.

**Distro backport tracking:** Distros typically ship fixed versions within days of upstream release for Critical/High severities. Check:
- Debian Security Tracker: https://security-tracker.debian.org/tracker/source-package/systemd
- Ubuntu Security Notices: https://ubuntu.com/security/CVE/\<CVE-ID\>
- Red Hat Errata: https://access.redhat.com/security/updates/backport

**Security policy:** systemd maintains a documented SECURITY.md, accepts reports at security@systemd.io, and coordinates disclosure via GitHub private security advisories before publishing to oss-security.

## Dependencies of Note

- `dbus` — systemd uses D-Bus for inter-process communication with other system components; D-Bus CVEs can intersect with systemd's attack surface.
- `PAM` — `pam_systemd` and related session-management code bridges PAM and systemd; PAM CVEs may affect privilege boundaries managed by systemd user sessions.
- `polkit` — used for fine-grained privilege delegation; the CVE-2020-1712 heap-UAF originates in the interaction between systemd's dbus handler and async Polkit queries.
- `systemd-resolved` — a separate daemon within the systemd project with its own CVE history; operators can disable it and use alternative resolvers.

## Open Questions

- What is the exact affected/fixed version boundary for CVE-2021-3997 (systemd-tmpfiles recursion)? The GHSA record does not specify; upstream commit history should be checked.
- Are there more recent (2024–2026) systemd advisories beyond this mapping? The upstream security advisory feed and oss-security archives should be checked for the 252–257 version range.
- Does CVE-2023-26604 affect any distributions that have backported the `systemctl status` pager logic without upgrading to systemd ≥ 247?

## Related Pages

- [[linux/glibc]]
- [[linux/sudo]]
- [[linux/openssh]]
- [[linux/index]]

---
*Last updated: 2026-07-10 | Sources: 4 (github/advisory-database GHSA records × 6, systemd GitHub project SECURITY.md, oss-security references)*
