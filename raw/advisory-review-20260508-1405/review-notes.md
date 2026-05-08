# Advisory review evidence notes — 2026-05-08 14:05 CT

Reviewed / screened:

- PyPI `pillow`: selected as the substantive KB addition. Public OSV query returned 118 rows; manual normalization found roughly 66 unique CVE/GHSA-style records after accounting for duplicate PYSEC / Bitnami aliases and OSS-Fuzz rows. Representative high-signal records were captured in `pillow-evidence-summary.txt` and mapped into `wiki/python/pillow.md`.
- PyPI `django`: screened as a high-volume future target. OSV query returned 272 rows; deferred because it needs a broader framework/security-support page rather than a quick representative pass.
- npm `koa`: screened as a possible small target. OSV query returned 5 rows; deferred because Python Pillow had a larger obvious KB gap.

Primary public sources used for final edits:

- https://osv.dev/list?ecosystem=PyPI&q=pillow
- https://github.com/python-pillow/Pillow/security/advisories
- https://github.com/advisories?query=pillow
- https://nvd.nist.gov/vuln/search/results?query=pillow
- https://pillow.readthedocs.io/en/stable/releasenotes/

Local proxy synthesis succeeded and was used only as a drafting aid; final wording was manually checked against the public advisory evidence summarized in `pillow-evidence-summary.txt`.
