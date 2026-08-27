# rsync (Linux)

**Registry:** distro (apt: `rsync`, rpm: `rsync`; upstream: rsync.samba.org / github.com/RsyncProject/rsync)
**Weekly Downloads:** pre-installed on most Linux distributions; estimated hundreds of millions of deployments
**Repository:** https://github.com/RsyncProject/rsync
**Security Contact:** https://rsync.samba.org/security.html
**Disclosure Policy:** https://rsync.samba.org/security.html
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2025-01-14 | Google Open Source Security Team | partial-source (checksum, symlink, recursive-transfer code paths) | manual | 6 bugs filed (all fixed in 3.4.0) | [OSS-Security disclosure](https://www.openwall.com/lists/oss-security/2025/01/14/3) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-12084 / GHSA-85h7-m8c3-v9wc | **Critical CVSS 9.8** AV:N/AC:L/PR:N/UI:N | Heap-based buffer overflow in checksum parsing: when the attacker-controlled `s2length` field exceeds the fixed `SUM_LENGTH` (16 bytes), rsync daemon writes out of bounds into the `sum2` buffer, enabling remote code execution with no authentication | 3.4.0 | [GHSA-85h7-m8c3-v9wc](https://github.com/advisories/GHSA-85h7-m8c3-v9wc) |
| CVE-2024-12085 / GHSA-xh5q-pch5-g3xq | **High CVSS 7.5** AV:N/AC:L/PR:N/UI:N | Info leak via uninitialized stack data: attacker manipulates `s2length` to force checksum comparison against uninitialized stack memory, leaking one byte of memory per comparison (unauthenticated) | 3.4.0 | [GHSA-xh5q-pch5-g3xq](https://github.com/advisories/GHSA-xh5q-pch5-g3xq) |
| CVE-2024-12086 / GHSA-82c6-8mfc-c23h | **Moderate CVSS 7.1** AV:N/AC:H/PR:N/UI:R | Malicious server enumerates arbitrary client files byte-by-byte via crafted checksum values during a client→server transfer; user must connect to malicious server | 3.4.0 | [GHSA-82c6-8mfc-c23h](https://github.com/advisories/GHSA-82c6-8mfc-c23h) |
| CVE-2024-12087 / GHSA-9x68-7qq6-v523 | **Moderate CVSS 6.5** AV:N/AC:L/PR:N/UI:R | Path traversal via `--inc-recursive`: improper symlink verification allows a malicious server to write files outside the client's destination directory; requires user interaction (connecting to malicious server) | 3.4.0 | [GHSA-9x68-7qq6-v523](https://github.com/advisories/GHSA-9x68-7qq6-v523) |
| CVE-2024-12088 / GHSA-ffph-g3pc-8r3g | **Moderate CVSS 7.1** AV:N/AC:L/PR:N/UI:R | `--safe-links` option bypass: rsync fails to verify whether a symlink's destination itself contains another symlink, enabling nested-symlink path traversal and arbitrary file write despite the protection flag | 3.4.0 | [GHSA-ffph-g3pc-8r3g](https://github.com/advisories/GHSA-ffph-g3pc-8r3g) |
| CVE-2024-12747 / GHSA-gp7r-m4cc-qhwq | **Moderate CVSS 7.1** AV:L/AC:H/PR:L/UI:N | Race condition in symlink handling: a local attacker can replace a regular file with a symlink at a precise timing window, bypassing rsync's symlink-skip protections and enabling information disclosure or privilege escalation | 3.4.0 | [GHSA-gp7r-m4cc-qhwq](https://github.com/advisories/GHSA-gp7r-m4cc-qhwq) |

## Security Posture Notes

rsync is a near-universal Linux file-synchronization tool, pre-installed on most server distributions and used heavily in backup systems, CI/CD pipelines, and deployment automation. All six January 2025 CVEs were discovered by the Google Open Source Security Team and disclosed coordinated via the Samba security team. The critical heap overflow (CVE-2024-12084) requires no authentication when rsync is running as a daemon and is the most urgent to patch.

**Patch status:** All six CVEs are fixed in rsync **3.4.0** (released 2025-01-14). Major distributions (RHEL, Debian, Ubuntu) released backported packages within days of disclosure. Users of rsync as a daemon should treat upgrade as urgent; rsync used as a local file-copy tool is not exposed to the network-facing CVEs.

**Disclosure policy:** The rsync project maintains a security contact at security@samba.org (same as Samba). Advisories are published at rsync.samba.org/security.html.

**Older history:** rsync has a long history of path-traversal and symlink-escape issues (pre-2.6.x era) but these have generally been addressed; the Jan 2025 batch is the most significant cluster in over a decade.

## Dependencies of Note

rsync on Linux links against the system's libz (zlib), libacl, libattr, and optionally libpopt and OpenSSL. See [[linux/zlib]] for zlib's own CVE history (particularly CVE-2022-37434 Critical) — distros ship rsync dynamically linked so a zlib update patches both without rsync rebuild.

## Open Questions

- Are rsync 3.4.0 packages available for all RHEL/CentOS/Rocky minor-version streams, or only selected ones?
- Post-3.4.0 release: has the Google team published a full write-up? Confirm full GHSA review status for CVE-2024-12086/12087/12088/12747.
- rsync daemon (`rsync --daemon`) exposure surface: default config requires explicit module definitions; document whether any common distro installs ship with open modules by default.

## Related Pages

- [[linux/index]]
- [[linux/tar]] — similar archive/transfer tool with its own traversal history
- [[linux/zlib]] — statically/dynamically linked compression dependency
- [[linux/openssh]] — often used alongside rsync for authenticated remote transfers

---
*Last updated: 2026-08-27 | Sources: 6 GHSA unreviewed advisories (CVE-2024-12084 through CVE-2024-12088, CVE-2024-12747); Google OSS-Security disclosure 2025-01-14*
