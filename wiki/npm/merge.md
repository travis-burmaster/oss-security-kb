# merge (npm)

**Registry:** npm
**Repository:** https://github.com/yeikos/js.merge
**Security Contact:** none listed (public sources not checked beyond registry metadata in this pass)
**Disclosure Policy:** none listed (not identified in this pass)
**Current Status:** advisory mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-26 | OpenClaw recurring review | package advisory refresh | public-source curation (GitHub Advisory Database, OSV.dev, npm registry metadata) | Added/confirmed two published GitHub advisories (both prototype-pollution) and aligned the recommended fixed version with npm `latest` (2.1.1). | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2018-16469 / GHSA-f9cm-qmx5-m98h | High | Prototype Pollution in `merge` affecting versions `< 1.2.1`. | 1.2.1 | https://github.com/advisories/GHSA-f9cm-qmx5-m98h |
| CVE-2020-28499 / GHSA-7wpw-2hjm-89gp | High | Prototype Pollution in `merge` affecting versions `< 2.1.1`. | 2.1.1 | https://github.com/advisories/GHSA-7wpw-2hjm-89gp |

## Security Posture Notes

- Both published advisories are **prototype-pollution** class issues, disclosed in 2018 and again in 2021. This is a useful cautionary example for consumers: security fixes in one major line do not always carry forward automatically.
- A 2026-05-14 public-source refresh confirmed CVE aliases for both advisories through OSV and the GitHub Advisory API: `CVE-2018-16469` for `GHSA-f9cm-qmx5-m98h` and `CVE-2020-28499` for `GHSA-7wpw-2hjm-89gp`.
- GitHub's advisory record for `GHSA-f9cm-qmx5-m98h` references the public NVD record, HackerOne report 381194, and npm advisory 722; the record for `GHSA-7wpw-2hjm-89gp` references the public NVD record and upstream fix commit `7b0ddc2701d813f2ba289b32d6a4b9d4cc235fb4`.
- npm registry metadata reports `latest` as **2.1.1**, which matches the patched version for the newer advisory.

## Dependencies of Note

- Not reviewed in this pass.

## Open Questions

- Is there any published maintainer advisory / release note text describing the exact patch behavior in 1.2.1 and 2.1.1?

## Related Pages

- [[npm/index]]

---
*Last updated: 2026-05-14 | Sources: GitHub Advisory Database (2 advisories, including GitHub Advisory API CVE aliases), OSV.dev package query and vulnerability details (2 entries), public NVD aliases referenced by GHSA/OSV, HackerOne report / npm advisory reference for CVE-2018-16469, upstream fix-commit reference for CVE-2020-28499, npm registry metadata, local Claude-compatible proxy synthesis saved under `raw/advisory-review-20260514-1806/` and used only as a drafting aid*
