# async (npm)

**Registry:** npm
**Weekly Downloads:** ~86,348,910 (as of 2026-04-25)
**Repository:** https://github.com/caolan/async
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** none confirmed in this pass
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No audits on record.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-43138 / GHSA-fwr7-v2mv-hh25 | High | Prototype pollution reachable through the `mapValues()` / `createObjectIterator` path; public records map the affected ranges to `2.x` before `2.6.4` and `3.x` before `3.2.2`. | 2.6.4, 3.2.2 | [GHSA](https://github.com/advisories/GHSA-fwr7-v2mv-hh25), [OSV.dev](https://osv.dev/vulnerability/GHSA-fwr7-v2mv-hh25), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-43138), [PR #1828](https://github.com/caolan/async/pull/1828), [v2.6.4 changelog](https://github.com/caolan/async/blob/v2.6.4/CHANGELOG.md) |

## Security Posture Notes

- Public package-scoped OSV / GHSA evidence gathered in this pass surfaced one direct published `async` advisory: the 2021 prototype-pollution issue fixed on both the maintained `2.x` and `3.x` lines.
- The upstream `v2.6.4` changelog explicitly says “Fix potential prototype pollution exploit (#1828),” which gives the advisory unusually clean maintainer confirmation in public release material.
- As with many prototype-pollution package records, real-world exploitability depends on attacker-controlled object keys reaching the affected helper path in application code, so this page stays careful not to flatten that into a universal remote-code-execution claim.
- Current npm metadata shows `async` is past the public fix points, but the package remains deeply embedded across older build and runtime dependency trees.
- No repository `SECURITY.md` or equivalent disclosure-policy file was confirmed via the GitHub contents API in this pass.

## Dependencies of Note

- None flagged from this compact public-advisory pass.

## Open Questions

- Has any broader public security review been published for `async`'s object-iteration helpers beyond the single normalized prototype-pollution record surfaced here?
- Should older downstream advisories that cite `async` indirectly through bundled copies or vendored code remain out of scope unless they become package-scoped records?

## Related Pages

- [[npm/minimist]]
- [[npm/lodash]]
- [[npm/index]]

---
*Last updated: 2026-04-25 | Sources: 8 (OSV.dev package query and vulnerability record, GitHub Advisory Database, public CVE / NVD record for CVE-2021-43138, upstream PR #1828, upstream fix commits referenced by OSV, v2.6.4 changelog, npm registry metadata, npm downloads API)*
