# jinja2 (python)

**Registry:** PyPI
**Weekly Downloads:** ~129,204,789 (as of 2026-04-18)
**Repository:** https://github.com/pallets/jinja
**Security Contact:** GitHub Security Advisory
**Disclosure Policy:** https://github.com/pallets/jinja/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-18 | OpenClaw recurring review | package advisory history | manual | 10 unique publicly disclosed Jinja2 vulnerabilities normalized from OSV, GHSA, CVE, PyPA advisory, changelog, and release-note material | https://osv.dev/list?ecosystem=PyPI&q=jinja2 |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2014-0012 / GHSA-fqh9-2qgg-h84h / PYSEC-2014-82 | Moderate | Insecure temporary-file / bytecode-cache directory handling in older Jinja2 releases. Public records disagree slightly on the first fully corrected release, with the upstream changelog noting a corrected follow-on fix in `2.7.3`. | 2.7.3 | https://osv.dev/vulnerability/GHSA-fqh9-2qgg-h84h |
| CVE-2014-1402 / GHSA-8r7q-cvjq-x353 / PYSEC-2014-8 | High | Incorrect privilege assignment issue in older releases; the upstream 2.7.2 changelog ties the security fix to the filesystem cache directory handling change. | 2.7.2 | https://osv.dev/vulnerability/GHSA-8r7q-cvjq-x353 |
| CVE-2016-10745 / GHSA-hj2j-77xm-mc5v / PYSEC-2019-220 | High | Sandbox escape / information-leakage issue involving format expressions in sandbox mode. | 2.8.1 | https://osv.dev/vulnerability/GHSA-hj2j-77xm-mc5v |
| CVE-2019-10906 / GHSA-462w-v97r-4m45 / PYSEC-2019-217 | High | `SandboxedEnvironment` did not securely handle `str.format_map`, allowing sandbox escape / code-execution-style abuse when rendering untrusted templates. | 2.10.1 | https://palletsprojects.com/blog/jinja-2-10-1-released/ |
| CVE-2020-28493 / GHSA-g3rq-g295-4j3m / PYSEC-2021-66 | Moderate | ReDoS in the `urlize` filter; upstream 2.11.3 notes explicitly cite reduced regex backtracking as the fix. | 2.11.3 | https://osv.dev/vulnerability/GHSA-g3rq-g295-4j3m |
| CVE-2024-22195 / GHSA-h5c8-rqwp-cp95 | Moderate | HTML attribute injection when attacker-controlled keys were passed to the `xmlattr` filter; 3.1.3 blocked keys containing spaces. | 3.1.3 | https://github.com/pallets/jinja/security/advisories/GHSA-h5c8-rqwp-cp95 |
| CVE-2024-34064 / GHSA-h75v-3vvj-5mfj | Moderate | Incomplete follow-on fix for the `xmlattr` filter issue; 3.1.4 further blocked `/`, `>`, and `=` in keys. | 3.1.4 | https://github.com/pallets/jinja/security/advisories/GHSA-h75v-3vvj-5mfj |
| CVE-2024-56201 / GHSA-gmj6-6f8f-6699 | Moderate | Sandbox breakout through malicious template filenames used in error-message formatting. | 3.1.5 | https://github.com/pallets/jinja/security/advisories/GHSA-gmj6-6f8f-6699 |
| CVE-2024-56326 / GHSA-q2x7-8rv6-6q7h | Moderate | Sandbox breakout through indirect references to `str.format`; upstream 3.1.5 release notes call out the new sandbox handling. | 3.1.5 | https://github.com/pallets/jinja/security/advisories/GHSA-q2x7-8rv6-6q7h |
| CVE-2025-27516 / GHSA-cpwx-vrp4-4pq7 | Moderate | The `|attr` filter could bypass environment attribute lookup and select the `format` method, creating another sandbox breakout path. | 3.1.6 | https://github.com/pallets/jinja/security/advisories/GHSA-cpwx-vrp4-4pq7 |

*Full CVE history: https://osv.dev/list?ecosystem=PyPI&q=jinja2*

## Security Posture Notes

- Jinja2 has a long published vulnerability history spanning **sandbox escape**, **attribute / HTML injection**, **regex-based denial of service**, and older **temporary-file / cache-directory** security mistakes.
- The clearest recurring pattern is **sandbox hardening**: public records show repeated fixes in `2.8.1`, `2.10.1`, `3.1.5`, and `3.1.6`, which means the sandbox should be treated as security-sensitive code rather than a one-and-done feature.
- The `xmlattr` filter required two consecutive security releases in 2024 (`3.1.3` then `3.1.4`), a useful signal that downstream users should not stop at the first partial fix when public advisories indicate follow-on hardening.
- Upstream changelog entries are unusually helpful here: they explicitly connect `2.11.3` to the `urlize` ReDoS fix and `3.1.3`-`3.1.6` to the newer GHSA-tagged security fixes.
- Operationally, the highest-risk use case remains **rendering attacker-controlled templates or relying on the sandbox as a hard trust boundary**. Applications treating Jinja2 as purely developer-authored template infrastructure face a different risk profile than applications exposing templating features to users.
- A conservative current-version floor for public advisory coverage is **3.1.6**, because that release closes the latest published sandbox-breakout path in the gathered evidence.

## Dependencies of Note

- Flask should cross-link here because it commonly embeds Jinja2 as the default templating layer, even though Flask's package advisories do not necessarily duplicate Jinja2's sandbox history.
- MarkupSafe is the other obvious adjacent page for future work because template escaping guarantees and templating safety claims often depend on it.

## Open Questions

- Are there public third-party Jinja2 security audits worth tracking separately from the maintainer-driven advisory trail?
- Should the older 2014 cache-directory issues be described more explicitly as bytecode-cache / temporary-file handling flaws after a future code-history pass?
- Which high-usage downstream packages still pin Jinja2 below `3.1.6`, especially in long-lived enterprise distributions?

## Related Pages

- [[python/flask]]
- [[python/index]]

---
*Last updated: 2026-04-18 | Sources: 10 (OSV package query, 10 normalized GHSA / CVE / PyPA advisory records, upstream changelog, upstream release notes, PyPI metadata, pypistats recent downloads)*
