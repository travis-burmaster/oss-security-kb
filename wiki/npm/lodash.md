# lodash (npm)

**Registry:** npm
**Weekly Downloads:** unknown (as of 2026-04-07)
**Repository:** https://github.com/lodash/lodash
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-10744 | High | Prototype pollution in `defaultsDeep` | 4.17.12 | https://github.com/advisories/GHSA-jf85-cpcp-j695 |
| CVE-2020-8203 | High | Prototype pollution via `zipObjectDeep` | 4.17.19 | https://github.com/advisories/GHSA-p6mc-m468-83gw |

## Security Posture Notes

- Extremely high-install-base JavaScript utility library.
- Historical prototype pollution issues make it a high-value baseline target for the KB.
- Good candidate for a deep review page because bug class history is already known and widely referenced.

## Dependencies of Note

- Minimal relevance; lodash is primarily important as a direct application dependency.

## Open Questions

- Has any full-source modern audit been published post-2020 fixes?
- Are there remaining dangerous deep-object mutation patterns not covered by prior fixes?
- Which downstream packages still expose vulnerable versions indirectly?

## Related Pages

- [[npm/index]]
- [[npm/minimist]]
- [[npm/semver]]

---
*Last updated: 2026-04-07 | Sources: 2*
