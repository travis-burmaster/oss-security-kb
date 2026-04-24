# react (npm)

**Registry:** npm
**Weekly Downloads:** ~131,000,000 (as of 2026-04-23)
**Repository:** https://github.com/facebook/react
**Security Contact:** Facebook Whitehat / React security process
**Disclosure Policy:** https://github.com/facebook/react/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No audits on record.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2013-7035 / GHSA-g53w-52xc-2j85 | Moderate | Cross-site scripting when attacker-controlled input was used as a React key in older `0.4.x` and `0.5.x` lines. | 0.4.2, 0.5.2 | [GHSA](https://github.com/advisories/GHSA-g53w-52xc-2j85), [React blog](https://legacy.reactjs.org/blog/2013/12/18/react-v0.5.2-v0.4.2.html) |
| GHSA-hg79-j56m-fxgv | High | Cross-site scripting in versions prior to `0.14.0` because `createElement` did not properly validate a spoofed input object. | 0.14.0 | [GHSA](https://github.com/advisories/GHSA-hg79-j56m-fxgv), [React v0.14 blog](https://legacy.reactjs.org/blog/2015/10/07/react-v0.14.html#notable-enhancements) |

## Security Posture Notes

- The currently published direct `react` package advisories in OSV / GitHub Advisory Database are both old XSS issues affecting pre-`1.0` releases.
- Public evidence gathered in this pass did not surface a newer direct package-scoped GHSA / OSV record for the modern `react` line.
- React does publish a repository-level security policy and routes reports through its security process, which is a useful positive signal even though the public package advisory set is small.
- Because the published package-level history is concentrated in legacy versions, downstream application security risk in modern React deployments is much more likely to come from surrounding framework / rendering patterns, unsafe HTML sinks, or adjacent packages than from these two old core-package records.

## Dependencies of Note

- `react-dom` — paired rendering package with its own security and DOM-boundary considerations; keep package history separate from core `react`.

## Open Questions

- Has a more recent modern-line React package advisory been published outside OSV / GitHub Advisory Database and not yet normalized here?
- Would a future page for `react-dom` or the wider React rendering/tooling surface provide more practical security value than further expanding this legacy-heavy core-package page?

## Related Pages

- [[npm/react-router]]
- [[npm/index]]

---
*Last updated: 2026-04-24 | Sources: 7 (OSV.dev package query and vulnerability records, GitHub Advisory Database, public CVE / NVD alias for CVE-2013-7035, archived React release blog posts for v0.5.2 / v0.4.2 and v0.14, repository security policy, npm registry metadata, npm downloads API)*
