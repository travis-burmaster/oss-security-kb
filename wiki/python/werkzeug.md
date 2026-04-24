# werkzeug (python)

**Registry:** PyPI
**Weekly Downloads:** ~60,418,881 (as of 2026-04-24)
**Repository:** https://github.com/pallets/werkzeug
**Security Contact:** GitHub Security Advisory
**Disclosure Policy:** https://github.com/pallets/werkzeug/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-24 | OpenClaw recurring review | package advisory history | manual | 14 publicly disclosed Werkzeug package vulnerabilities normalized from OSV, GHSA, CVE, PyPA advisory, changelog, and release-note material, including one disputed record tracked separately | https://osv.dev/list?ecosystem=PyPI&q=werkzeug |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2016-10516 / GHSA-h2fp-xgx6-xh6f / PYSEC-2017-43 | High | XSS in the interactive debugger's traceback rendering (`render_full`) could execute attacker-controlled content in debug views. | 0.11.11 | https://github.com/advisories/GHSA-h2fp-xgx6-xh6f |
| CVE-2019-14806 / GHSA-gq9m-qvpx-68hc / PYSEC-2019-140 | Moderate | Debugger PIN generation had insufficient entropy in Docker because containers could share the same machine identifier. | 0.15.3 | https://github.com/advisories/GHSA-gq9m-qvpx-68hc |
| CVE-2019-14322 / GHSA-j544-7q9p-6xp8 | High | `SharedDataMiddleware` mishandled Windows drive names, enabling path traversal on affected Windows deployments. | 0.15.5 | https://github.com/advisories/GHSA-j544-7q9p-6xp8 |
| CVE-2020-28724 / GHSA-3p3h-qghp-hvh2 / PYSEC-2020-157 | Moderate | Open redirect via URLs beginning with a double slash. | 0.11.6 | https://github.com/advisories/GHSA-3p3h-qghp-hvh2 |
| CVE-2022-29361 / PYSEC-2022-203 | Disputed | Public records describe HTTP request smuggling in older Werkzeug development-server handling, but the record is disputed and should not be treated as a clean confirmed package vulnerability without that context. | 2.1.1 | https://nvd.nist.gov/vuln/detail/CVE-2022-29361 |
| CVE-2023-23934 / GHSA-px8h-6qxv-m22q / PYSEC-2023-57 | Moderate | Incorrect parsing of nameless cookies could let adjacent subdomains bypass `__Host-` cookie expectations in vulnerable browser / deployment combinations. | 2.2.3 | https://github.com/advisories/GHSA-px8h-6qxv-m22q |
| CVE-2023-25577 / GHSA-xg9f-g7g7-2323 / PYSEC-2023-58 | Moderate | Multipart form parsing accepted an unbounded number of parts, enabling CPU and memory exhaustion with many small fields. | 2.2.3 | https://github.com/advisories/GHSA-xg9f-g7g7-2323 |
| CVE-2023-46136 / GHSA-hrfv-mqp8-q5rw / PYSEC-2023-221 | Moderate | Multipart parsing could consume excessive resources when a large part began with CR/LF and delayed boundary detection. | 2.3.8, 3.0.1 | https://github.com/advisories/GHSA-hrfv-mqp8-q5rw |
| CVE-2024-34069 / GHSA-2g68-c3qc-8985 | High | The debugger could permit code execution on a developer machine if an attacker induced interaction with an attacker-controlled domain while debug tooling was exposed. | 3.0.3 | https://github.com/advisories/GHSA-2g68-c3qc-8985 |
| CVE-2024-49766 / GHSA-f9vj-2wh5-fj8j | High | On Windows with Python < 3.11, `safe_join()` could miss UNC-style absolute paths, weakening path containment. | 3.0.6 | https://github.com/advisories/GHSA-f9vj-2wh5-fj8j |
| CVE-2024-49767 / GHSA-q34m-jh98-gwm2 | Moderate | Multipart form parsing could bypass `Request.max_form_memory_size` for large non-file fields, enabling resource exhaustion. | 3.0.6 | https://github.com/advisories/GHSA-q34m-jh98-gwm2 |
| CVE-2025-66221 / GHSA-hgf8-39gv-g3f2 | High | `safe_join()` allowed Windows special device names such as `CON` and `AUX`, which could expose unintended files or devices via `send_from_directory`-style paths. | 3.1.4 | https://github.com/advisories/GHSA-hgf8-39gv-g3f2 |
| CVE-2026-21860 / GHSA-87hc-h4r5-73f7 | High | Incomplete follow-on fix: additional Windows device-name variants with extensions or surrounding spaces still bypassed `safe_join()` checks. | 3.1.5 | https://github.com/advisories/GHSA-87hc-h4r5-73f7 |
| CVE-2026-27199 / GHSA-29vq-49wr-vm6x | High | Another follow-on Windows `safe_join()` fix closed multi-segment path cases that still allowed special device names. | 3.1.6 | https://github.com/advisories/GHSA-29vq-49wr-vm6x |

*Full CVE history: https://osv.dev/list?ecosystem=PyPI&q=werkzeug*

## Security Posture Notes

- Werkzeug has a broad public advisory history spanning **debugger security**, **multipart parser denial of service**, **URL / cookie parsing edge cases**, and a repeated **Windows path-containment** fix chain.
- Two clusters stand out most clearly in current public evidence:
  - **Development / debugger exposure**: XSS in 2016, weak Docker PIN entropy in 2019, and the 2024 attacker-controlled-domain debugger RCE conditions all reinforce that Werkzeug's debug features are security-sensitive and should never be treated as production-safe.
  - **Multipart parsing and request-body resource limits**: public fixes in `2.2.3`, `2.3.8` / `3.0.1`, and `3.0.6` show a multi-release hardening trail rather than a one-off bug.
- The newer **Windows `safe_join()` sequence** is especially important operationally because it required three successive public fixes in `3.1.4`, `3.1.5`, and `3.1.6`, after the earlier `3.0.6` UNC-path issue. Downstream Windows users should not stop at the first patch in that chain.
- Upstream `CHANGES.rst` is unusually useful for maintenance here: it explicitly ties the 2024-2026 fixes to released versions, including `3.0.3`, `3.0.6`, `3.1.4`, `3.1.5`, and `3.1.6`.
- `CVE-2022-29361` should be handled carefully. Public records exist, but the NVD entry marks it **DISPUTED**, so it belongs in the KB only with that dispute context rather than as a clean confirmed package flaw.
- A conservative current-version floor for the gathered public security history is **3.1.6**, because that closes the latest published follow-on `safe_join()` bypass in this review pass.

## Dependencies of Note

- Flask should cross-link here because Werkzeug remains its core WSGI / request-handling substrate even when Flask package advisories do not duplicate Werkzeug's lower-level parser and debugger history.
- Applications exposing `send_file`, `send_from_directory`, static-file helpers, or custom multipart upload paths inherit the most security-relevant portions of Werkzeug's public history.
- Windows deployments deserve explicit attention because several recent public advisories are platform-specific rather than generic cross-platform flaws.

## Open Questions

- Are there public third-party audits of Werkzeug's debugger, multipart parser, or Windows path-handling logic worth tracking separately from maintainer advisories?
- Should the KB eventually split Werkzeug's **debugger** and **multipart parser** histories into sub-surface notes if future advisories keep accumulating in those clusters?
- Which widely deployed Flask or standalone WSGI stacks still pin Werkzeug below `3.1.6`, especially on Windows?

## Related Pages

- [[python/flask]]
- [[python/jinja2]]
- [[python/index]]

---
*Last updated: 2026-04-24 | Sources: 14 (OSV package query, normalized GHSA / CVE / PyPA advisory records, upstream CHANGES.rst, PyPI metadata, pypistats recent downloads, NVD dispute record for CVE-2022-29361)*
