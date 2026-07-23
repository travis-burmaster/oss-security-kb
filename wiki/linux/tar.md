# tar (Linux)

**Registry:** distro (GNU project)
**Weekly Downloads:** unknown (pre-installed on all major Linux distributions; package `tar` in Debian/Ubuntu/Alpine/RHEL)
**Repository:** https://git.savannah.gnu.org/cgit/tar.git
**Security Contact:** bug-tar@gnu.org
**Disclosure Policy:** GNU security disclosure process; coordinated via oss-security mailing list
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

GNU tar is the standard archive utility pre-installed on virtually every Linux system; it is used in deployment scripts, package managers, and build pipelines. The dominant risk class across its history is path traversal and file overwrite during extraction — all stem from insufficient validation of archive member names or symlink targets. Five public advisories are on record.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-45582 / GHSA-f93m-9mq4-2fjj | Moderate (CVSS:3.1 AV:L/AC:H/PR:N/UI:R) | Two-step symlink traversal bypass: GNU tar ≤ 1.35 blocks single-archive `../` member names ("Member name contains '..'"') but not a two-archive attack. Step 1: extract an archive containing `x -> ../../../../../home/victim/.ssh` (a symlink pointing outside the extraction root). Step 2: extract a second archive containing `x/authorized_keys` — tar follows the symlink and overwrites a critical file outside the intended directory. Affects server applications that auto-extract multiple user-supplied archives sequentially. Disclosed 2025-07-11. | No fixed tagged release confirmed; affects through 1.35 | [GHSA-f93m-9mq4-2fjj](https://github.com/advisories/GHSA-f93m-9mq4-2fjj) |
| CVE-2022-48303 / GHSA-h2v4-4v4p-2qvc | High (CVSS:3.1 AV:L/AC:L/PR:N/UI:R CWE-125) | One-byte out-of-bounds read in `from_header` in `list.c` when processing a V7 archive whose `mtime` field contains approximately 11 whitespace characters. The OOB read results in use of uninitialized memory in a conditional jump; control-flow exploitation has not been demonstrated. Classified High due to memory safety violation. Local attack vector (user must extract a crafted archive). Affects ≤ 1.34. | ≥ 1.35 (likely; no explicit fixed version stated in advisory) | [GHSA-h2v4-4v4p-2qvc](https://github.com/advisories/GHSA-h2v4-4v4p-2qvc) |
| CVE-2016-6321 / GHSA-4qpm-74c6-fg44 ("POINTYFEATHER") | High (CVSS:3.0 7.5 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N) | Bypass of path traversal protection via the `safer_name_suffix` function in GNU tar 1.14–1.29. Improper sanitization of the `file_name` parameter allows an attacker-controlled archive to write to arbitrary files outside the extraction directory, circumventing the intended protection mechanism. Network-reachable when the archive is downloaded from attacker-controlled infrastructure. | GNU tar ≥ 1.30 (2016) | [GHSA-4qpm-74c6-fg44](https://github.com/advisories/GHSA-4qpm-74c6-fg44) |
| CVE-2007-4131 / GHSA-43w6-q9mv-9cwf | Moderate | Directory traversal via `//..` (slash slash dot dot) sequences embedded in directory symlinks within a TAR archive. The `contains_dot_dot` function in `src/names.c` fails to detect the `//..` pattern, allowing archive extraction to overwrite arbitrary files outside the extraction directory. No CVSS score in GHSA; classified Moderate based on attack surface. | Upstream patch applied 2007; fixed in vendor-shipped versions by 2007 | [GHSA-43w6-q9mv-9cwf](https://github.com/advisories/GHSA-43w6-q9mv-9cwf) |
| CVE-2002-0399 / GHSA-c6fq-h555-8326 | Moderate (historical) | Directory traversal in GNU tar 1.13.19–1.13.25 via archive members named `/../..` or `./..`. The leading slash is stripped but the `..` component is retained, enabling writes outside the extraction root. A variant of CVE-2001-1267. Historical; all maintained versions unaffected. | GNU tar ≥ 1.13.26 (2002) | [GHSA-c6fq-h555-8326](https://github.com/advisories/GHSA-c6fq-h555-8326) |

## Security Posture Notes

GNU tar's security history is dominated by path traversal and file-overwrite issues during extraction. The recurring root cause is that constructing a safe extraction path from attacker-controlled archive member names and symlink targets is non-trivial: symlink chains, double-slash sequences, dot-dot variants, and multi-step workflows all create bypass opportunities that per-member name checks do not anticipate.

CVE-2025-45582 (disclosed July 2025) is the most recent and architecturally interesting finding: it bypasses the existing `../` check by distributing the traversal across two separate archives, making it a risk for any application that extracts multiple untrusted archives sequentially (package managers, build systems, CI pipelines, server-side upload handlers). As of July 2026, no tagged patched release is confirmed in the public advisory.

Partial mitigations: `--no-same-permissions`, `--no-overwrite-dir`, and an explicit extraction destination (`-C /safe/dest`) reduce risk but do not fully prevent symlink-based traversal attacks. Server-side applications handling user-supplied archives should extract into temporary directories, verify extracted paths before operating on them, and avoid multi-archive sequential extraction from untrusted sources.

Current upstream stable: GNU tar 1.35 (2023). Security contact: bug-tar@gnu.org.

## Dependencies of Note

- GNU tar is used by most Linux package managers (`apt`, `rpm`, `apk`) for archive extraction; vulnerabilities here may be chainable with package manager workflows if attacker-controlled archives are processed.
- Language-level archive libraries (npm `tar`, Python `tarfile`, Go `archive/tar`) share some historical vulnerability patterns but have separate advisory records — see [[npm/tar]] and [[npm/tar-fs]].

## Open Questions

- Confirm whether GNU tar 1.35 (current stable) includes a fix for CVE-2022-48303; the GHSA does not specify a patched version.
- Confirm whether a patched release exists for CVE-2025-45582; as of 2026-07-23 the advisory does not specify a fixed version.
- Review Debian/Ubuntu security trackers for distro-specific backport patch status on CVE-2025-45582.
- Map any additional advisories from the oss-security mailing list for GNU tar not yet captured in GHSA (tar has limited GHSA coverage relative to its full CVE history).

## Related Pages

- [[npm/tar]]
- [[npm/tar-fs]]
- [[linux/index]]

---
*Last updated: 2026-07-23 | Sources: 5*
