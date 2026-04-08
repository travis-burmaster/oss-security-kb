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
| CVE-2019-10744 | High | Prototype pollution in `defaultsDeep` | 4.17.12 | https://security.snyk.io/vuln/SNYK-JS-LODASH-450202 |
| CVE-2020-8203 | High | Prototype pollution via `zipObjectDeep`, `set`, `setWith`, `update`, and `updateWith` | 4.17.19 | https://github.com/advisories/GHSA-p6mc-m468-83gw |
| GHSA-xxjr-mmjv-4gpg | High | Prototype pollution in `_.unset` and `_.omit` | 4.17.23+ / pending exact upstream remediation tracking | https://github.com/lodash/lodash/security/advisories/GHSA-xxjr-mmjv-4gpg |

## Security Posture Notes

- Extremely high-install-base JavaScript utility library.
- Historical prototype pollution issues make it a high-value baseline target for the KB.
- Bug pattern concentration around deep-path mutation helpers suggests lodash deserves dedicated surface mapping by function family, not just CVE enumeration.
- Public evidence exists for multiple prototype-pollution eras (`defaultsDeep`, `zipObjectDeep`, later `unset`/`omit`), which makes lodash useful as a model page for tracking repeated bug-class recurrence over time.

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
*Last updated: 2026-04-07 | Sources: 3*
