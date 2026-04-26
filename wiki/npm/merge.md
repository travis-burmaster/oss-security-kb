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
| GHSA-f9cm-qmx5-m98h | High | Prototype Pollution in `merge` affecting versions `< 1.2.1`. | 1.2.1 | https://github.com/advisories/GHSA-f9cm-qmx5-m98h |
| GHSA-7wpw-2hjm-89gp | High | Prototype Pollution in `merge` affecting versions `< 2.1.1`. | 2.1.1 | https://github.com/advisories/GHSA-7wpw-2hjm-89gp |

## Security Posture Notes

- Both published advisories are **prototype-pollution** class issues, disclosed in 2018 and again in 2021. This is a useful cautionary example for consumers: security fixes in one major line do not always carry forward automatically.
- In this pass, public sources reviewed did **not** provide CVE IDs for these GHSAs; the KB records them by GHSA identifier.
- npm registry metadata reports `latest` as **2.1.1**, which matches the patched version for the newer advisory.

## Dependencies of Note

- Not reviewed in this pass.

## Open Questions

- Do OSV / public CVE records assign CVE IDs to either GHSA (not observed in this pass)?
- Is there any published maintainer advisory / release note text describing the exact patch behavior in 1.2.1 and 2.1.1?

## Related Pages

- [[npm/index]]

---
*Last updated: 2026-04-26 | Sources: GitHub Advisory Database (2 advisories), OSV.dev (2 entries), npm registry metadata*
