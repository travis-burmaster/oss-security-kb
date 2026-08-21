# zlib (Linux)

**Registry:** distro (zlib1g on Debian/Ubuntu; zlib on RHEL/Fedora/RPM-based)
**Weekly Downloads:** N/A — C library bundled in Linux distributions; not a per-package download metric
**Repository:** https://github.com/madler/zlib
**Security Contact:** No formal security contact; patches submitted via GitHub PRs to madler/zlib
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2018-25032 | High (CVSS 7.5 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) | Memory corruption in deflate (compression) path when input has many distant matches; can cause out-of-bounds write during zlib compression of crafted input | zlib 1.2.12 | [GHSA-v6gp-9mmm-c6p5](https://github.com/advisories/GHSA-v6gp-9mmm-c6p5) |
| CVE-2022-37434 | Critical (CVSS 9.8 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Heap buffer over-read or buffer overflow in `inflate()` in inflate.c via a large gzip header extra field when the caller has invoked `inflateGetHeader()`; processing crafted gzip data can cause memory corruption or RCE | zlib 1.2.12.1 | [GHSA-cfmr-vrgj-vqwv](https://github.com/advisories/GHSA-cfmr-vrgj-vqwv) |
| CVE-2023-45853 | Critical (CVSS 9.8 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Integer overflow → heap buffer overflow in `zipOpenNewFileInZip4_64()` in MiniZip contrib component via a long filename, comment, or extra field; affects applications that use zlib's MiniZip utility directly; zlib's core inflate/deflate library is not affected | zlib 1.3.1 (MiniZip contrib fix; core library unaffected) | [NVD CVE-2023-45853](https://nvd.nist.gov/vuln/detail/CVE-2023-45853) |

*OSV reference: https://osv.dev/list?ecosystem=&q=CVE-2018-25032+CVE-2022-37434*

## Security Posture Notes

zlib is one of the most widely deployed C libraries in existence — bundled in virtually every Linux distribution, macOS, and Windows system, and statically linked into a large number of applications (nginx, git, CPython, OpenSSH, curl, and thousands more). Its blast radius for any vulnerability is therefore very high.

The library has two distinct vulnerability classes historically:
- **Core inflate/deflate path** (CVE-2018-25032, CVE-2022-37434): Bugs in the core compression/decompression routines affect every application that uses zlib. Both were fixed in rapid succession in 2022 (1.2.12 and 1.2.12.1 respectively).
- **MiniZip contrib component** (CVE-2023-45853): MiniZip is a higher-level ZIP archive utility bundled in zlib's `contrib/minizip/` directory. It is not part of the core zlib library and is not linked by default in most distributions' `zlib1g` / `zlib` packages. Applications that explicitly link MiniZip are at risk; most system-installed zlib consumers are not.

Maintained by Mark Adler (original author). The project receives patches infrequently but promptly for security issues. No formal security disclosure process exists; researchers typically open GitHub issues or PRs.

Linux distributions ship zlib as a core system dependency:
- **Debian/Ubuntu**: `zlib1g` / `zlib1g-dev` — Debian Security Tracker tracks as `zlib`
- **RHEL/Fedora**: `zlib` / `zlib-devel` — Red Hat Errata at access.redhat.com

## Dependencies of Note

zlib has no external runtime dependencies. However, many critical packages statically bundle zlib (especially in Alpine/musl environments), meaning distro-level zlib updates may not reach statically-linked binaries. Container images built on Alpine are a common example where bundled zlib versions lag.

## Open Questions

- What is the current stable zlib release and does it include patches for all three advisories above? (1.3.1 released January 2024 should cover all three; confirm.)
- Do major Linux distributions' current packages (Debian 12 bookworm, Ubuntu 24.04 LTS, RHEL 9) carry a patched version covering CVE-2023-45853 MiniZip?
- Are any widely-deployed applications (nginx, curl, git) shipping statically-bundled zlib older than 1.2.12.1?

## Related Pages

- [[linux/curl]] — links against system zlib
- [[linux/git]] — links against system zlib
- [[linux/nginx]] — links against system zlib
- [[linux/openssl]] — co-dependency on many TLS stacks
- [[linux/index]]

---
*Last updated: 2026-08-21 | Sources: 3*
