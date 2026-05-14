# setuptools (python)

**Registry:** PyPI
**Current Version:** 82.0.1 (as of 2026-05-13)
**Repository:** https://github.com/pypa/setuptools
**Documentation:** https://setuptools.pypa.io/
**Security Contact:** https://github.com/pypa/setuptools/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-13 | OpenClaw recurring review | public advisory review | OSV / GHSA / PyPA advisory records / CVE / upstream fix commits / PyPI metadata | 4 normalized public vulnerability groups across legacy transport authenticity, `package_index` parsing / command execution, and path traversal in download handling | https://osv.dev/list?ecosystem=PyPI&q=setuptools |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-47273 / GHSA-5rjg-fvgr-3xxf / PYSEC-2025-49 | High | `PackageIndex.download` derived a local filename from a package URL and joined it with the temporary directory in a way that could allow absolute-path / traversal-style writes when processing a crafted URL. | 78.1.1 | https://osv.dev/vulnerability/GHSA-5rjg-fvgr-3xxf |
| CVE-2024-6345 / GHSA-cx63-2mw6-8hw5 | High | The `package_index` download path could permit command injection / remote code execution when download helpers were exposed to user-controlled package URLs or package-index responses. | 70.0.0 | https://osv.dev/vulnerability/GHSA-cx63-2mw6-8hw5 |
| CVE-2022-40897 / GHSA-r9hx-vwmv-q579 / PYSEC-2022-43012 | High | A vulnerable regular expression in `package_index` could allow denial of service when setuptools fetched malicious HTML from PyPI or a custom package index page. | 65.5.1 | https://osv.dev/vulnerability/GHSA-r9hx-vwmv-q579 |
| CVE-2013-1633 / GHSA-27x4-j476-jp5f / PYSEC-2013-22 | High | Legacy `easy_install` used HTTP for PyPI retrieval and lacked integrity checks, allowing man-in-the-middle package replacement before the 0.7-era hardening. | 0.7 | https://osv.dev/vulnerability/GHSA-27x4-j476-jp5f |

## Security Posture Notes

- Setuptools sits on Python's packaging and build boundary; its public package-level advisories concentrate on package-index retrieval and parsing paths rather than ordinary application runtime APIs.
- The 2022-2025 records are all tied to `package_index`-style URL / HTML / filename handling, so downstream tooling that still invokes those helpers on untrusted indexes or URLs is the highest-risk interpretation of the page.
- OSV returns duplicate PyPA `PYSEC-*` records for several vulnerabilities; this page normalizes those aliases into single vulnerability rows rather than counting them as separate issues.
- The PyPIStats recent-download request was rate-limited during this pass, so this page intentionally omits a download estimate rather than reusing stale numbers.

## Dependencies of Note

- Package indexes, direct package URLs, temporary download directories, and generated archive filenames are part of setuptools' security boundary.
- Build frontends and installers that vendor or invoke setuptools may need their own version mapping; this page tracks the upstream PyPI package records only.

## Open Questions

- Should a future pass separate `easy_install` legacy behavior from maintained setuptools build backend / package discovery behavior?
- Which downstream build tools vendor affected setuptools versions and need separate KB normalization?

## Related Pages

- [[python/pip]]
- [[python/index]]

---
*Last updated: 2026-05-13 | Sources: 8 (OSV package query + OSV vulnerability records; GitHub Advisory Database / upstream GitHub security advisories surfaced through OSV; PyPA advisory database records; public CVE/NVD records; upstream setuptools issue / PR / commit references; upstream documentation / changelog links; PyPI metadata; local proxy synthesis used only as drafting aid)*
