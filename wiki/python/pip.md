# pip (python)

**Registry:** PyPI
**Weekly Downloads:** ~176,037,165 (as of 2026-05-13)
**Repository:** https://github.com/pypa/pip
**Security Contact:** https://www.python.org/dev/security/
**Disclosure Policy:** https://github.com/pypa/pip/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-13 | OpenClaw recurring review | public advisory review | OSV / GHSA / PyPA advisory database / CVE / upstream changelog | 11 normalized public vulnerability groups across archive extraction, VCS reference handling, installer execution order, and legacy transport / temp-directory behavior | https://osv.dev/list?ecosystem=PyPI&q=pip |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-6357 / GHSA-jp4c-xjxw-mgf9 | Moderate | Pip's version-self-check ordering could import functionality from newly installed packages after a wheel installation had begun, creating an untrusted-control-sphere risk. | 26.1 | https://osv.dev/vulnerability/GHSA-jp4c-xjxw-mgf9 |
| CVE-2026-3219 / GHSA-58qw-9mgm-455v | Moderate | Pip treated concatenated tar+ZIP archive polyglots as ZIP files regardless of filename, creating an interpretation-conflict risk where installed contents might not match the archive type a user expected. OSV lists `last_affected: 26.0.1` but does not publish a `fixed` event in the saved record. | after 26.0.1 per OSV `last_affected` (no fixed event in saved OSV record) | https://osv.dev/vulnerability/GHSA-58qw-9mgm-455v |
| CVE-2026-1703 / GHSA-6vgw-5pg2-w6jp | Low | Malicious wheel archives could extract files outside the intended installation directory, though OSV notes the traversal was limited to prefixes of the installation directory and was not typically able to overwrite executable files. | 26.0 | https://osv.dev/vulnerability/GHSA-6vgw-5pg2-w6jp |
| CVE-2025-8869 / GHSA-4xh5-x5gv-qwph | Moderate | On Python versions without PEP 706 tarfile protections, pip's fallback source-distribution extraction did not fully reject symlinks pointing outside the extraction directory. | 25.3 | https://osv.dev/vulnerability/GHSA-4xh5-x5gv-qwph |
| CVE-2023-5752 / GHSA-mq26-g339-26xf | Moderate | Mercurial VCS URLs could inject arbitrary `hg clone --config` options when pip was used to install from Mercurial repositories. | 23.3 | https://osv.dev/vulnerability/GHSA-mq26-g339-26xf |
| CVE-2021-3572 / GHSA-5xp3-jfq3-5q8x | High | Unicode separators in Git references could cause pip to install a different repository revision than the one the user intended. | 21.1 | https://osv.dev/vulnerability/GHSA-5xp3-jfq3-5q8x |
| CVE-2019-20916 / GHSA-gpvv-69j7-gwj8 | High | Pip's handling of `Content-Disposition` during downloads could allow path traversal via crafted HTTP response headers. | 19.2 | https://osv.dev/vulnerability/GHSA-gpvv-69j7-gwj8 |
| CVE-2014-8991 / GHSA-53mr-44pp-crf4 | Moderate | Pip 1.3 through 1.5.6 used insufficiently random build directories, allowing local users to pre-create paths and cause package-installation denial of service. | 6.0 | https://osv.dev/vulnerability/GHSA-53mr-44pp-crf4 |
| CVE-2013-5123 / GHSA-c5h8-cq4v-cvfm | High | Legacy mirror support used insecure DNS / mirror behavior that could enable man-in-the-middle package installation risks before the feature was removed. | 1.5 | https://osv.dev/vulnerability/GHSA-c5h8-cq4v-cvfm |
| CVE-2013-1888 / GHSA-4gv5-qhvr-36vv | Moderate | Pip before 1.3 used temporary build directories in a way that allowed local symlink attacks against files in `/tmp/pip-build`. | 1.3 | https://osv.dev/vulnerability/GHSA-4gv5-qhvr-36vv |
| CVE-2013-1629 / GHSA-g3p5-fjj9-h8gj | High | Pip before 1.3 did not default to HTTPS / certificate verification for package retrieval, enabling package replacement on untrusted networks. | 1.3 | https://osv.dev/vulnerability/GHSA-g3p5-fjj9-h8gj |

## Security Posture Notes

- Pip is Python's default package installer and therefore has a very high blast radius: it routinely processes package indexes, HTTP responses, source archives, wheel archives, and VCS URLs supplied by users or automation.
- The public advisory history clusters around **installer trust boundaries** rather than application runtime bugs: archive extraction, build / temporary-directory handling, VCS reference parsing, and transport / mirror authenticity.
- Recent records show active hardening in the 25.x / 26.x release train: fallback tar extraction was tightened in 25.3, wheel path-prefix handling in 26.0, and installer import-order behavior in 26.1; the tar-vs-ZIP archive interpretation record should be rechecked once OSV publishes an explicit fixed-version event.
- CVE-2025-8869 is partly runtime-dependent: OSV and the Python security announcement call out that Python versions with PEP 706 tarfile filtering reduce reliance on pip's fallback extraction path.
- The older 2013-2014 records are mostly relevant to long-lived legacy environments, but they document the security watershed where pip moved toward HTTPS-by-default package retrieval and safer temporary build directories.

## Dependencies of Note

- Python's `tarfile` behavior matters for source-distribution extraction, especially for PEP 706 coverage on older supported Python branches.
- VCS backends such as Git and Mercurial are security-relevant when users install directly from VCS URLs.
- Package indexes, local caches, wheels, and sdists are part of pip's effective trust boundary even when they are not Python package dependencies.

## Open Questions

- Should this page eventually separate installer-core vulnerabilities from vendored-dependency CVEs that appear in pip release notes but are not package-scoped pip advisories?
- Which pip hardening guidance can be captured from upstream docs without turning this KB page into operational install-policy advice?
- Are distro-patched pip builds carrying backported fixes that should be normalized separately from upstream PyPI versions?

## Related Pages

- [[python/index]]

---
*Last updated: 2026-05-13 | Sources: 9 (OSV package query + OSV vulnerability records for GHSA/CVE aliases; PyPA advisory database records surfaced through OSV; public CVE/NVD records; upstream pip `NEWS.rst`; upstream `SECURITY.md`; Python security-announcement mailing-list references surfaced through OSV; PyPI metadata; PyPIStats recent download metadata)*
