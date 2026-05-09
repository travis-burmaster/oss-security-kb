# pydantic (python)

**Registry:** PyPI
**Repository:** https://github.com/pydantic/pydantic
**Security Contact:** https://github.com/pydantic/pydantic/security/advisories
**Disclosure Policy:** none found in repository root during this pass
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-09 | OpenClaw recurring review | package advisory history | manual | 2 unique public vulnerability classes normalized from 3 OSV records; `PYSEC-2021-47` is retained as a duplicate alias of `GHSA-5jqp-qgf6-3pvh` / `CVE-2021-29510` rather than counted separately | https://osv.dev/list?ecosystem=PyPI&q=pydantic |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-29510 / GHSA-5jqp-qgf6-3pvh / PYSEC-2021-47 | Moderate | Denial of service / infinite loop when the string `infinity` is accepted as input for `datetime` or `date` fields. OSV represents the fix across several affected minor-line ranges rather than as one continuous range. | 1.6.2, 1.7.4, 1.8.2 | https://github.com/advisories/GHSA-5jqp-qgf6-3pvh |
| CVE-2024-3772 / GHSA-mr82-8j83-vxmv | Moderate | Regular-expression denial of service in email validation for crafted input; upstream release notes for 1.10.13 describe a backported max-length check to `validate_email`, and the OSV record lists the 2.x fix in 2.4.0. | 1.10.13 and 2.4.0 | https://github.com/advisories/GHSA-mr82-8j83-vxmv |

*Full public advisory query: https://osv.dev/list?ecosystem=PyPI&q=pydantic*

## Security Posture Notes

- Pydantic's direct PyPI advisory surface is compact in the gathered public sources: two unique package-level DoS classes are visible in OSV / GitHub Advisory Database records, with the older PYSEC entry duplicating the 2021 GHSA / CVE rather than representing a third vulnerability.
- Both confirmed records are availability issues in validation boundaries. No public evidence gathered in this pass supports adding direct Pydantic package rows for code execution, authentication bypass, or data exposure.
- The 2024 ReDoS advisory matters for internet-facing APIs because Pydantic is commonly used to validate request bodies and user-controlled strings. Applications pinned to old Pydantic 1.x should be at least on 1.10.13; applications on Pydantic 2.x should be at least on 2.4.0 for this issue.
- The 2021 `infinity` input issue has a non-contiguous fixed-version story in OSV because multiple minor lines were fixed separately. Keep the fixed versions explicit rather than flattening the record into a misleading single range.
- No repository-root `SECURITY.md` was found during this pass, but historical advisories are published through GitHub Security Advisories and OSV records with upstream commit / PR references.

## Dependencies of Note

- Pydantic v2 delegates core validation machinery to `pydantic-core`; that package should be reviewed separately rather than assuming Pydantic's advisory set fully covers the Rust-backed validation engine.
- Email validation paths may involve optional / extra dependencies in real deployments. The KB should avoid attributing dependency-level email validation issues to Pydantic unless a public advisory explicitly names Pydantic as the affected package.

## Open Questions

- Does `pydantic-core` have separate public OSV / GHSA / RustSec records that should be cross-linked from this page?
- Is there a current public security policy or disclosure document for the `pydantic/pydantic` repository outside GitHub's advisory submission flow?
- Should future review add a small operational note for API frameworks that depend on Pydantic, focused on validation DoS risk from large or pathological user-controlled inputs?

## Related Pages

- [[python/fastapi]]
- [[python/starlette]]
- [[python/django]]
- [[python/index]]

---
*Last updated: 2026-05-09 | Sources: OSV package query and vulnerability details, GitHub Advisory Database records, public CVE aliases, upstream commit / PR references, PyPI metadata, GitHub release notes, and local proxy synthesis used as a drafting aid only.*
