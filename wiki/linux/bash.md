# bash (Linux)

**Registry:** distro
**Weekly Downloads:** unknown (system shell on virtually all Linux systems; not tracked through a single registry)
**Repository:** https://git.savannah.gnu.org/cgit/bash.git (mirror: https://github.com/bminor/bash)
**Security Contact:** bug-bash@gnu.org
**Disclosure Policy:** GNU security disclosure process; coordinated via oss-security mailing list
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

Bash is the default login shell and interactive shell on most Linux distributions and macOS (pre-Catalina). CVEs affect the upstream shell and are then backported by downstream distributions. The most significant cluster is the 2014 ShellShock family (CVE-2014-6271 and follow-on incomplete fixes), which exposed every CGI-based web server, DHCP hook script, and OpenSSH ForceCommand deployment on the internet. Current upstream stable: bash 5.2.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2014-6271 / GHSA-6hfc-grwp-2p9c | Critical (CVSS:3.1 9.8 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | ShellShock: Bash through 4.3 processes trailing strings after function definitions in environment variable values, allowing remote attackers to execute arbitrary code. Primary attack vectors include Apache mod_cgi / mod_cgid, OpenSSH ForceCommand deployments, DHCP client hooks, and any program that passes attacker-controlled data into a bash environment. Affects bash 1.14 through 4.3. | bash ≥ 4.3 patch 25 (released 2014-09-26) | [GHSA-6hfc-grwp-2p9c](https://github.com/advisories/GHSA-6hfc-grwp-2p9c) |
| CVE-2014-7169 / GHSA-f7j6-xrjp-vffg | Critical (CVSS:3.1 9.8) | ShellShock incomplete fix (round 1): bash43-025 still processes malformed trailing strings after function definitions in certain configurations, allowing continued RCE via the same attack vectors as CVE-2014-6271. | bash ≥ 4.3 patch 26 (released 2014-09-27) | [GHSA-f7j6-xrjp-vffg](https://github.com/advisories/GHSA-f7j6-xrjp-vffg) |
| CVE-2014-6277 / GHSA-55cc-h8m2-x3mp | High | ShellShock incomplete fix (round 2): uninitialized memory access in bash related to the parsing of function definitions in environment variables; follow-on to CVE-2014-6271 and CVE-2014-7169. | bash ≥ 4.3 patch 27 (released 2014-10-01) | [GHSA-55cc-h8m2-x3mp](https://github.com/advisories/GHSA-55cc-h8m2-x3mp) |
| CVE-2014-6278 / GHSA-6493-28fj-f93w | Critical (CVSS:3.1 9.8) | ShellShock incomplete fix (round 3): allows remote attackers to execute arbitrary commands via a crafted environment; another incomplete fix in the ShellShock remediation chain. | bash ≥ 4.3 patch 27 (released 2014-10-01) | [GHSA-6493-28fj-f93w](https://github.com/advisories/GHSA-6493-28fj-f93w) |
| CVE-2022-3715 / GHSA-cr4j-fv7c-759c | Critical (CVSS:3.1 9.8) | Heap-buffer overflow in `valid_parameter_transform` (parameter_transform.c line 96): when bash processes a crafted `${parameter@operator}` expansion, it can write past the end of an allocated buffer, potentially allowing arbitrary code execution. | bash ≥ 5.2 (released 2022-10-22) | [GHSA-cr4j-fv7c-759c](https://github.com/advisories/GHSA-cr4j-fv7c-759c) |

## Security Posture Notes

GNU Bash is the standard system shell on Linux and pre-Catalina macOS; it runs as the default login shell, executes CGI scripts under Apache, processes DHCP event hooks, and is invoked by countless system scripts. The 2014 ShellShock cluster (CVE-2014-6271 and three incomplete-fix follow-ons) remains one of the most impactful vulnerabilities in Internet history — it was remotely exploitable against any system running a CGI web server and was added to the CISA KEV catalog. Mass exploitation began within hours of disclosure and included automated worm campaigns.

The four ShellShock CVEs (CVE-2014-6271, CVE-2014-7169, CVE-2014-6277, CVE-2014-6278) were remediated in a rapid sequence of upstream patches (bash43-025 through bash43-028) across 2014-09-26 to 2014-10-01. Distros that shipped only bash43-025 remained vulnerable to the follow-on bypasses.

CVE-2022-3715 is a separate heap-buffer overflow in parameter transformation (unrelated to ShellShock) that scored Critical CVSS 9.8 and was fixed in the bash 5.2 release.

The upstream project does not maintain a formal SECURITY.md or bug-bounty program; security reports go to bug-bash@gnu.org and the oss-security mailing list.

## Dependencies of Note

- All Linux system scripts and CGI deployments that invoke bash with environment variables sourced from untrusted input are affected by the ShellShock cluster — the exposure is broader than any single application.
- Distros running Apache mod_cgi or mod_cgid on pre-patch systems (bash < 4.3 patch 25) were universally vulnerable to CVE-2014-6271 without any application-level mitigation possible.

## Open Questions

- Enumerate and document CVE-2014-6277 and CVE-2014-6278 patched versions across major distros (exact package versions and advisory links may differ from upstream patch numbers).
- Assess additional bash advisories beyond this set — the bash changelog lists further security-relevant commits between 4.3 and 5.x.

## Related Pages

- [[linux/glibc]]
- [[linux/openssh]]
- [[linux/sudo]]
- [[linux/index]]

---
*Last updated: 2026-07-08 | Sources: 5*
