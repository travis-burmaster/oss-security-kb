# polkit (Linux)

**Registry:** distro (policykit-1 on Debian/Ubuntu; polkit on Fedora/RHEL/Alpine)
**Weekly Downloads:** N/A — distro package (installed by default on all systemd-based Linux desktops and most server distributions)
**Repository:** https://github.com/polkit-org/polkit (canonical); also https://gitlab.freedesktop.org/polkit/polkit
**Security Contact:** https://github.com/polkit-org/polkit/security
**Disclosure Policy:** https://github.com/polkit-org/polkit/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-4034 / GHSA-qgr2-xgqv-24x8 | High (CVSS 7.8 AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) | **PwnKit — pkexec local privilege escalation**: polkit's `pkexec` binary (setuid-root) mishandles `argc == 0` or an empty `argv` array. The program indexes past the end of `argv[]` into `envp[]`, reads an environment variable as a command path, writes a rewritten value back into `argv[-1]` (which is within `envp[]`), and ultimately passes an attacker-controlled entry to `execve()` via `g_find_program_in_path()`. An unprivileged local user can craft environment variables to cause `pkexec` to execute arbitrary code with root privileges. The flaw was present in every version of `pkexec` since its initial 2009 commit — over 12 years. Discovered by Qualys Research Team; published 2022-01-25. CISA Known Exploited Vulnerability; in-the-wild exploitation reported within hours of disclosure. | polkit 0.120; all major distros (Debian 9/10/11, Ubuntu 14.04–21.10, RHEL 6/7/8/9, Fedora, openSUSE) issued emergency patches within 24 hours of disclosure | [GHSA-qgr2-xgqv-24x8](https://github.com/advisories/GHSA-qgr2-xgqv-24x8) |
| CVE-2021-3560 / GHSA-7c49-j253-wq5r | High (CVSS 7.8 AV:L/AC:L/PR:L/UI:N) | **D-Bus timeout authentication bypass — unprivileged local root**: When a D-Bus caller requests a privileged action and then rapidly disconnects, polkit attempts to resolve the requestor's UID via `dbus-daemon`. If the caller has already disconnected before polkit completes the lookup, polkit's error handling returns a fallback UID of 0 (root) and grants the request rather than denying it. An unprivileged local user can exploit this race window (~3–7 ms) to create a new administrator account or perform other root-level D-Bus actions. Discovered by Kevin Backhouse (GitHub Security Lab); published 2021-06-03. CISA Known Exploited Vulnerability. Affects polkit < 0.119 on distributions using `dbus_g_proxy_call()` for UID resolution (Fedora 34/33, RHEL 8, Ubuntu 20.04; some distros not affected due to differing polkit/D-Bus integration). | polkit 0.119; distro patches for Fedora 34/33, RHEL 8, Ubuntu 20.04 | [GHSA-7c49-j253-wq5r](https://github.com/advisories/GHSA-7c49-j253-wq5r) |

## Security Posture Notes

polkit (formerly PolicyKit) is the system-level authorization framework on Linux. Its `pkexec` binary is setuid-root, and its `polkitd` daemon mediates privilege grants for D-Bus services system-wide — making polkit a tier-1 local privilege escalation target present on virtually every mainstream Linux desktop and most server deployments.

**CVE-2021-4034 (PwnKit) context**: The Qualys analysis demonstrated that the vulnerable codepath has existed since pkexec's 2009 initial commit, meaning every major Linux distribution has shipped the flaw for over 12 years. Exploitation is simple, reliable, and requires only a local shell (no special permissions needed). Public exploit code appeared within hours of the Qualys disclosure; defenders should treat any unpatched system as compromised if it was reachable by untrusted local users after 2022-01-25. The `-u` remediation (setting the SUID bit) is the correct immediate mitigation where patching is not yet possible.

**CVE-2021-3560 context**: The race window is narrow but the attack is deterministic on most targets with repeated attempts (successful in seconds on test systems in Backhouse's writeup). The flaw is specific to polkit versions that used the deprecated `dbus_g_proxy_call()` UID-resolution path; distributions that used alternate D-Bus integration were unaffected. The GitHub Security Lab blog post (https://github.blog/2021-06-10-privilege-escalation-polkit-root-on-linux-with-bug/) includes full technical details.

**Additional historical NVD advisories (not yet fully mapped):**
- CVE-2019-6133: Race condition via PID reuse between `fork()` and `exec()` in polkit UID resolution, allowing a local user to impersonate a privileged process (CVSS ~7.3 AV:L; discovered by Jann Horn, Google Project Zero; fixed polkit 0.116).
- CVE-2018-19788: Privilege escalation via UID values above `INT_MAX` on systems with crafted user UID assignments (discovered by Rick Mitchell; fixed polkit 0.116).

**Disclosure posture**: polkit now uses GitHub Security Advisories (https://github.com/polkit-org/polkit/security/advisories) for coordinated disclosure under the polkit-org GitHub organization. The project has active maintainers (Red Hat/freedesktop.org funded).

**Distro backport note**: All fixed-version numbers above refer to upstream polkit releases. Major distributions (Debian, Ubuntu, Fedora, RHEL, openSUSE, Alpine) backport security fixes to supported package versions without necessarily upgrading to the upstream release number. Always verify your distro's security tracker for the specific fixed package version.

## Dependencies of Note

- **D-Bus / dbus-daemon**: polkit uses D-Bus for inter-process communication; D-Bus integration behavior affects which polkit versions are exploitable for CVE-2021-3560.
- **systemd**: On systemd-based distributions, systemd and polkit interact for privilege-escalation delegation and service management.
- **GLib / GObject**: Core runtime dependency; `pkexec` uses GLib string and path functions.

## Open Questions

- Enumerate 2022–2026 polkit advisories at https://github.com/polkit-org/polkit/security/advisories for completeness.
- Map CVE-2019-6133 and CVE-2018-19788 into the vulnerability table with NVD primary-source links on a future pass.
- Confirm fixed package versions for CVE-2021-3560 across Alpine Linux and Arch Linux.
- Track whether polkit 124+ (current development line) has any new advisories.

## Related Pages

- [[linux/sudo]]
- [[linux/systemd]]
- [[linux/glibc]]
- [[linux/index]]

---
*Last updated: 2026-09-03 | Sources: 2 GHSA records (GHSA-qgr2-xgqv-24x8, GHSA-7c49-j253-wq5r via github/advisory-database); Qualys PwnKit writeup https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt; GitHub Security Lab https://github.blog/2021-06-10-privilege-escalation-polkit-root-on-linux-with-bug/*
