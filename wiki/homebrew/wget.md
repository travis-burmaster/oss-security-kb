# wget (Homebrew)

**Registry:** Homebrew
**Weekly Downloads:** unknown (Homebrew analytics blocked; one of the most-installed CLI download tools on macOS via Homebrew)
**Repository:** https://git.savannah.gnu.org/cgit/wget.git
**Security Contact:** bug-wget@gnu.org
**Disclosure Policy:** GNU security disclosure process; coordinated via oss-security mailing list
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

GNU Wget is a non-interactive command-line network downloader supporting HTTP, HTTPS, and FTP. It is widely used in shell scripts, Dockerfiles, and CI pipelines for automated file retrieval. Two public advisories are on record.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-38428 / GHSA-2j66-vp53-phjj | Critical (CVSS:3.1 9.1 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N) | `url.c` semicolon mishandling in the userinfo subcomponent (CWE-436 / interpretation conflict): data intended for the `user:password@` portion of a URL is misinterpreted as part of the host subcomponent when a semicolon appears in the userinfo field. This can cause wget to connect to an unintended host, enabling SSRF-class misdirection and potential credential exposure. Fixed upstream in commit `ed0c7c7`. | wget ≥ 1.25.0 (2024) | [GHSA-2j66-vp53-phjj](https://github.com/advisories/GHSA-2j66-vp53-phjj) |
| CVE-2016-4971 / GHSA-5w8p-rj9f-xvj7 | High (CVSS:3.1 8.8) | wget < 1.18: an HTTP-to-FTP redirect allows a remote server to specify an arbitrary client-side file path, enabling an attacker to cause wget to write downloaded content to an attacker-chosen location outside the intended download directory. | wget ≥ 1.18 (2016) | [GHSA-5w8p-rj9f-xvj7](https://github.com/advisories/GHSA-5w8p-rj9f-xvj7) |

## Security Posture Notes

GNU Wget is a ubiquitous CLI download tool installed by default or via Homebrew on virtually all developer macOS environments and present in a large fraction of Linux Docker images. Both published advisories are network-reachable with no authentication required, making them relevant for any automated pipeline that fetches files from attacker-influenced URLs.

CVE-2024-38428 (CVSS 9.1) affects the URL parser's handling of semicolons in userinfo, which is an ambiguous character in RFC 3986 but was historically used as a separator in some URI schemes; wget's misinterpretation can be triggered by a server redirect to a carefully crafted URL. Homebrew formula `wget` tracks upstream releases and would have received the fix in the 1.25.0 bottle update.

The upstream project does not maintain a formal SECURITY.md or bug-bounty program; security reports go to bug-wget@gnu.org and the oss-security mailing list.

## Dependencies of Note

- Scripts and Dockerfiles using wget for artifact retrieval are affected when the download source URL is not fully trusted or can be influenced by a redirect chain.
- Homebrew formula installs the upstream binary directly; patch lag equals the time between upstream release and Homebrew bottle publication.

## Open Questions

- Verify the exact Homebrew bottle version at which CVE-2024-38428 was patched (1.25.0 bottle publication date vs upstream release date).
- Assess whether additional wget CVEs beyond this set have GHSA records: CVE-2017-13090 (heap-based buffer overflow in `process_html`), CVE-2019-5953 (buffer overflow in `store_hostaddr`), and others in the upstream changelog.

## Related Pages

- [[homebrew/git]]
- [[homebrew/openssl@3]]
- [[linux/curl]]
- [[linux/index]]

---
*Last updated: 2026-07-08 | Sources: 3*
