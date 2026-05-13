# Flask-CORS (python)

**Registry:** PyPI
**Weekly Downloads:** ~12,061,991 (last week, fetched 2026-05-13; PyPIStats)
**Repository:** https://github.com/corydolphin/flask-cors
**Security Contact:** GitHub Security Advisories / repository security policy
**Disclosure Policy:** https://github.com/corydolphin/flask-cors/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-13 | OpenClaw recurring review | package advisory history | public-source curation using OSV package queries, GitHub Advisory Database records surfaced through OSV, public CVE/NVD aliases, upstream fix commits / release references, project changelog, PyPI metadata, PyPIStats downloads, and repository security-policy evidence | Added a new advisory-mapped page for Flask-CORS covering six unique public vulnerability classes across directory traversal, CORS origin/resource matching, private-network header defaults, and debug-log injection through the 6.0.0 fix train. | https://osv.dev/list?ecosystem=PyPI&q=flask-cors |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-25032 / GHSA-xc3p-ff3m-f46v / PYSEC-2020-43 | High | Directory traversal vulnerability in Flask-CORS fixed in the 3.0.9 release line; OSV links the fix to upstream commit `67c4b2c` and the 3.0.9 release tag. | 3.0.9 | https://github.com/advisories/GHSA-xc3p-ff3m-f46v |
| CVE-2024-1681 / GHSA-84pr-m4jr-85g5 | Moderate | Log injection when debug logging is enabled, allowing crafted request/origin data to affect log output integrity. | 4.0.1 | https://github.com/advisories/GHSA-84pr-m4jr-85g5 |
| CVE-2024-6221 / GHSA-hxwh-jpp2-84pm / PYSEC-2024-71 | High | `Access-Control-Allow-Private-Network` could be set to true by default, weakening browser private-network access expectations in affected configurations. | 4.0.2 | https://github.com/advisories/GHSA-hxwh-jpp2-84pm |
| CVE-2024-6839 / GHSA-7rxf-gvfg-47g4 | Moderate | Improper regex path matching could cause CORS policy application to differ from intended resource matching. | 6.0.0 | https://github.com/advisories/GHSA-7rxf-gvfg-47g4 |
| CVE-2024-6844 / GHSA-8vgw-p6qm-5gr7 | Moderate | Inconsistent CORS matching behavior could apply policy decisions unexpectedly across similar request paths / resources. | 6.0.0 | https://github.com/advisories/GHSA-8vgw-p6qm-5gr7 |
| CVE-2024-6866 / GHSA-43qf-4rqw-9q2g | Moderate | Improper handling of case sensitivity in CORS matching could cause policy bypass or unexpected resource/origin matching in affected configurations. | 6.0.0 | https://github.com/advisories/GHSA-43qf-4rqw-9q2g |

## Security Posture Notes

- Flask-CORS has a concentrated 2024 advisory cluster around CORS policy matching, defaults, and logging, plus one older directory-traversal record.
- OSV returns duplicate PYSEC records for `CVE-2020-25032` and `CVE-2024-6221`; this page normalizes them into the canonical GHSA/CVE rows instead of counting them twice.
- The 6.0.0 train is the important public boundary for the 2024 path / case / consistency matching issues, while `4.0.1` and `4.0.2` separately address the debug-log and private-network-header records.
- CORS vulnerabilities are highly configuration-sensitive. Risk depends on allowed origins, credentials, private-network access, route/resource patterns, debug logging, and whether browser-enforced policy is being used as a security boundary.
- Current PyPI metadata in this pass showed `latest=6.0.2`, newer than all fix points captured here.

## Dependencies of Note

- Flask-CORS is usually deployed with Flask / Werkzeug applications; review the surrounding app's route matching, proxy headers, credentialed CORS settings, and session/cookie policy alongside package version.
- Debug-log injection is most relevant where logs feed automated monitoring, SIEM searches, or audit workflows.

## Open Questions

- Should future KB work add a CORS-middleware cluster page linking Flask-CORS, Express `cors`, `gin-contrib/cors`, and other framework-specific CORS packages?
- Which popular Flask templates or extensions still pin Flask-CORS below the 4.0.2 or 6.0.0 security boundaries?
- Are the three 6.0.0 matching advisories best presented as separate vulnerability classes long-term, or should they be grouped under one CORS policy-matching hardening cluster once advisory metadata stabilizes?

## Related Pages

- [[python/flask]]
- [[python/werkzeug]]
- [[npm/cors]]
- [[python/index]]

---
*Last updated: 2026-05-13 | Sources: 8 (OSV package query, GitHub Advisory Database / GHSA pages, public CVE/NVD records, upstream fix commits / release references surfaced through OSV, project changelog, PyPI metadata, PyPIStats downloads, repository security policy)*
