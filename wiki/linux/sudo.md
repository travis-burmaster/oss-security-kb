# sudo (linux)

**Registry:** distro
**Weekly Downloads:** unknown (as of 2026-05-08)
**Repository:** https://github.com/sudo-project/sudo
**Security Contact:** https://www.sudo.ws/security/
**Disclosure Policy:** https://www.sudo.ws/security/
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-08 | OpenClaw recurring review | upstream Sudo privilege-boundary advisories | public-source curation (upstream Sudo advisories and release notes, OSV.dev, GitHub Advisory Database, public CVE/NVD records) | Added a Linux package page for `sudo` covering representative public local-privilege-escalation and privilege-boundary advisories, with distro-version caveats preserved. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No distro-normalized proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-18634 | High | Stack-based buffer overflow when the non-default `pwfeedback` sudoers option is enabled. Upstream says affected versions are 1.7.1 through 1.8.30 inclusive, impact exists only when `pwfeedback` is enabled, and the bug can be triggered by a local user even if they are not listed in sudoers. | 1.8.31 | https://www.sudo.ws/security/advisories/pwfeedback/ |
| CVE-2021-3156 / GHSA-w5vh-2923-gp5c | High | “Baron Samedit” heap-based buffer overflow / off-by-one in sudo command-line and sudoers argument handling. Upstream says 1.7.7 through 1.7.10p9, 1.8.2 through 1.8.31p2, and 1.9.0 through 1.9.5p1 are affected and that a local user may elevate to root when sudoers is present. | 1.8.32 / 1.9.5p2, or vendor-supported patched builds | https://www.sudo.ws/security/advisories/unescape_overflow/ |
| CVE-2025-32462 | High | Local privilege-boundary issue in the `-h` / `--host` option: upstream says the option was intended for listing privileges on another host, but was not restricted to list mode and could influence sudoers host matching when running commands or using sudoedit. Requires the user to be listed in sudoers, but may bypass current-host restrictions in shared sudoers configurations. | 1.9.17p1 | https://www.sudo.ws/security/advisories/host_any/ |
| CVE-2025-32463 | Critical | Local privilege escalation via the `-R` / `--chroot` option in sudo 1.9.14 through 1.9.17 inclusive. Upstream says path resolution during sudoers evaluation could load attacker-controlled NSS configuration from the chosen root directory, allowing arbitrary commands as root on systems that support `/etc/nsswitch.conf`. The chroot feature was marked deprecated. | 1.9.17p1 | https://www.sudo.ws/security/advisories/chroot_bug/ |

## Security Posture Notes

- `sudo` is a Linux/Unix privilege-boundary package rather than a library: local bugs can have root-level impact even when no network service is exposed.
- Version mapping is distribution-specific. This page records upstream Sudo fix versions and selected advisory identifiers; downstream readers still need to check their distribution's patched package status because vendors often backport fixes without matching upstream version strings.
- The 2025 pair is an important current patch-level marker: upstream fixed both CVE-2025-32462 and CVE-2025-32463 in `1.9.17p1`; the `--chroot` path was also deprecated after the CVE-2025-32463 analysis.
- Configuration can materially change exposure. CVE-2019-18634 depended on the non-default `pwfeedback` option, while CVE-2025-32462 mainly matters where sudoers rules distinguish hosts in shared or centrally managed policy.
- This page intentionally avoids exploit steps and focuses on advisory-level facts, affected ranges, fixes, and distro-normalization caveats.

## Dependencies of Note

- Distro package trackers for Debian, Ubuntu, Red Hat, Fedora, Alpine, and SUSE should eventually be normalized against the upstream advisory set.
- PAM, NSS, LDAP/SSSD sudoers sources, and centrally distributed sudoers policy are relevant adjacent surfaces, but they should not be collapsed into `sudo` package CVEs without public evidence.

## Open Questions

- What is the cleanest KB structure for recording upstream Sudo fixed versions alongside distro backports and vendor advisory identifiers?
- Which supported distributions had default or common configurations that materially affected exposure to CVE-2019-18634 or CVE-2025-32462?
- Should Linux privilege-boundary pages include an explicit “configuration-dependent exposure” field separate from “affected upstream versions”?

## Related Pages

- [[linux/index]]
- [[linux/openssl]]
- [[linux/cve-2026-31431-copy-fail]]

---
*Last updated: 2026-05-08 | Sources: 9 (upstream Sudo advisory index and release notes, four upstream Sudo advisories, OSV.dev records, GitHub Advisory Database, and public CVE/NVD records)*
