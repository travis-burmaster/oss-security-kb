# graphql (npm)

**Registry:** npm
**Weekly Downloads:** ~34,768,779 (as of 2026-04-25)
**Repository:** https://github.com/graphql/graphql-js
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
| CVE-2023-26144 / GHSA-9pv7-vfvm-6vr7 | Moderate | Uncontrolled resource consumption / denial of service from insufficient checks in `OverlappingFieldsCanBeMergedRule`, affecting `16.3.0` through before `16.8.1` in the public record. | 16.8.1 | [GHSA](https://github.com/advisories/GHSA-9pv7-vfvm-6vr7), [OSV.dev](https://osv.dev/vulnerability/GHSA-9pv7-vfvm-6vr7), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-26144), [issue #3955](https://github.com/graphql/graphql-js/issues/3955), [v16.8.1 release](https://github.com/graphql/graphql-js/releases/tag/v16.8.1) |

## Security Posture Notes

- Public package-scoped OSV / GHSA evidence gathered in this pass surfaced one direct published `graphql` advisory: the 2023 resource-exhaustion / denial-of-service issue fixed in `16.8.1`.
- The public issue thread gives unusually useful exploit-shape context for a KB page: repeated overlapping-field queries could drive significant CPU and response-time degradation before downstream query-complexity hooks had a chance to help.
- The `v16.8.1` release notes explicitly tie the fix to `OverlappingFieldsCanBeMergedRule: Fix performance degradation`, which cleanly corroborates the advisory without needing to overclaim process-crash or memory-corruption outcomes.
- This page intentionally stays narrow around the direct package advisory and does not collapse the much larger GraphQL application-security universe into package-level claims against `graphql-js` itself.
- No repository `SECURITY.md` or equivalent disclosure-policy file was confirmed via the GitHub contents API in this pass.

## Dependencies of Note

- None flagged from this compact public-advisory pass.

## Open Questions

- Are there other published parser- or validator-complexity bugs in `graphql-js` that later matured into package-scoped advisories and should be normalized here if they become public?
- Should future KB passes separately track ecosystem tooling that relies on `graphql-js` but adds its own query-planning or complexity boundaries?

## Related Pages

- [[npm/react]]
- [[npm/react-router]]
- [[npm/index]]

---
*Last updated: 2026-04-25 | Sources: 9 (OSV.dev package query and vulnerability record, GitHub Advisory Database, public CVE / NVD record for CVE-2023-26144, upstream issue #3955, upstream PR #3972 and fix commit surfaced through OSV/NVD, v16.8.1 release notes, npm registry metadata, npm downloads API)*
