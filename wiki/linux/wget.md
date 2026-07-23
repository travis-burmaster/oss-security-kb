# wget (Linux)

**Registry:** distro (GNU project)
**Weekly Downloads:** unknown (pre-installed or package-managed; present in a large fraction of Linux Docker images and CI pipelines; package `wget` in Debian/Ubuntu/Alpine/RHEL)
**Repository:** https://git.savannah.gnu.org/cgit/wget.git
**Security Contact:** bug-wget@gnu.org
**Disclosure Policy:** GNU security disclosure process; coordinated via oss-security mailing list; upstream release notes at https://www.gnu.org/software/wget/
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

GNU Wget is a non-interactive command-line network downloader supporting HTTP, HTTPS, and FTP. It is widely pre-installed on Linux distributions and heavily used in shell scripts, Dockerfiles, and CI pipelines for automated file retrieval. Six public advisories are on record covering URL parsing, redirect handling, and xattr information disclosure.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-15146 / GHSA-77jw-q7w3-q2hw | Moderate (CVSS:3.1 5.4 AV:N CWE-918) | wget operating in FTP passive mode does not validate the IP address returned in an FTP PASV response. A malicious FTP server (or an HTTP server that redirects to an FTP URL) can redirect wget's data connection to an arbitrary IP address and port, enabling SSRF to access localhost services or internal network resources. Disclosed 2026-07-10. | Commit 4f85853; no tagged release yet as of 2026-07-23 | [GHSA-77jw-q7w3-q2hw](https://github.com/advisories/GHSA-77jw-q7w3-q2hw) |
| CVE-2024-38428 / GHSA-2j66-vp53-phjj | Critical (CVSS:3.1 9.1 AV:N/AC:L/PR:N/UI:N CWE-436) | `url.c` mishandles semicolons in the userinfo subcomponent of a URI (interpretation conflict): data intended as `user:password@` credentials is misinterpreted as part of the host subcomponent when a semicolon appears in the userinfo field. This causes wget to connect to an unintended host, enabling SSRF-class misdirection and potential credential exposure. Affects wget ≤ 1.24.5. | wget ≥ 1.25.0 (2024) | [GHSA-2j66-vp53-phjj](https://github.com/advisories/GHSA-2j66-vp53-phjj) |
| CVE-2024-10524 / GHSA-mqrm-h2pw-9j9r | Moderate (CVSS:3.1 3.1 AV:N/AC:H CWE-918) | Shorthand URL processing: crafted credentials from an attacker-controlled server redirect cause wget to access an arbitrary host (SSRF). High attack complexity (requires an attacker-controlled redirect chain) limits practical exploitability. | Commit c419542; no separate tagged release confirmed in advisory | [GHSA-mqrm-h2pw-9j9r](https://github.com/advisories/GHSA-mqrm-h2pw-9j9r) |
| CVE-2019-5953 / GHSA-fhwx-v7qv-pjh3 | Critical (CVSS:3.0 9.8 AV:N/AC:L/PR:N/UI:N CWE-787) | Buffer overflow (out-of-bounds write) in GNU Wget ≤ 1.20.1 allows remote attackers to cause a denial-of-service or potentially execute arbitrary code via unspecified vectors. Exact fixed version not specified in GHSA; likely ≥ 1.20.2. | wget ≥ 1.20.2 (approx. 2019) | [GHSA-fhwx-v7qv-pjh3](https://github.com/advisories/GHSA-fhwx-v7qv-pjh3) |
| CVE-2018-20483 / GHSA-mxm6-6r3r-6wj4 | High (CVSS:3.0 7.1 AV:L CWE-200) | `set_file_metadata` in `xattr.c` stores the downloaded file's origin URL in the `user.xdg.origin.url` extended attribute and the referrer in `user.xdg.referrer.url`. Local users can read these attributes via `getfattr`, exposing credentials or sensitive data embedded in download URLs. Local attack vector only. | wget ≥ 1.20.1 (December 2018) | [GHSA-mxm6-6r3r-6wj4](https://github.com/advisories/GHSA-mxm6-6r3r-6wj4) |
| CVE-2016-4971 / GHSA-5w8p-rj9f-xvj7 | High (CVSS:3.1 8.8 AV:N/AC:L/PR:N/UI:R) | wget < 1.18 follows HTTP-to-FTP redirects without restricting the FTP destination path. A remote server can redirect an HTTP request to a crafted FTP URL specifying an arbitrary local file path, causing wget to write the downloaded content to that attacker-chosen location outside the intended download directory. | wget ≥ 1.18 (2016) | [GHSA-5w8p-rj9f-xvj7](https://github.com/advisories/GHSA-5w8p-rj9f-xvj7) |

## Security Posture Notes

GNU Wget is a ubiquitous CLI download tool present in a large fraction of Linux Docker images, CI pipelines, and shell scripts. Its long security history is dominated by URL-parsing and redirect-handling bugs: the tool's design (follow redirects by default, support multiple protocols, accept server-provided paths) creates recurring opportunities for server-controlled SSRF and file-write attacks. All six advisories above are network-reachable or triggered by attacker-controlled server responses.

The most impactful current advisory is CVE-2024-38428 (CVSS 9.1), where a semicolon in the userinfo portion of a URI is misinterpreted as a host delimiter — a subtle URI parsing ambiguity that can be silently triggered via a redirect chain. CVE-2026-15146 (FTP PASV SSRF) was disclosed July 2026 and may not yet have a tagged release fix; check the upstream repository and distro security trackers before assuming a patched package is available.

The project does not maintain a formal SECURITY.md or bug-bounty program. Security reports go to bug-wget@gnu.org and the oss-security mailing list. Current upstream stable: wget 1.25.0 (2024).

## Dependencies of Note

- wget itself downloads files from potentially untrusted servers; redirect-following is on by default. Any wget invocation that processes attacker-influenced URLs is in scope for redirect-class vulnerabilities.
- Linux distribution packages (Debian, Ubuntu, RHEL, Alpine) may lag upstream releases; check distro-specific security trackers (Debian Security Tracker, Ubuntu CVE Tracker, Red Hat Errata) for patch status.

## Open Questions

- Confirm exact fixed version for CVE-2024-10524; the GHSA references a commit but no tagged version.
- Confirm whether CVE-2026-15146 has a tagged fixed release; as of 2026-07-23 the advisory references commit 4f85853 only.
- Review NVD entry for CVE-2019-5953 to confirm fixed version; not specified in GHSA.
- CVE-2017-13090 (heap buffer overflow in `process_html`): not mapped in this pass; pending confirmation of affected version range and GHSA coverage.

## Related Pages

- [[homebrew/wget]]
- [[linux/curl]]
- [[linux/index]]

---
*Last updated: 2026-07-23 | Sources: 6*
