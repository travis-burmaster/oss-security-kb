# debug (npm)

**Registry:** npm
**Weekly Downloads:** ~533,000,000 (as of 2026-04-12)
**Repository:** https://github.com/debug-js/debug
**Security Contact:** none listed
**Disclosure Policy:** https://github.com/debug-js/debug/security/policy (GitHub reports no SECURITY.md / no security policy detected)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-12 | [@travis-burmaster](https://github.com/travis-burmaster) | package advisory review | public-source curation (GitHub Advisory Database, OSV.dev, public CVE records, upstream issue / release metadata, npm registry metadata) | 3 published package advisories mapped (including one malware / supply-chain incident) | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-4x49-vf9v-38px / CVE-2025-59144 | High | `debug@4.4.2` was published with malicious code after an npm account takeover; the maintainer advisory says browser-targeted cryptocurrency-transaction redirection was the observed payload, npm removed the bad version, and users should purge caches / rebuild bundles. | 4.4.3 | [GitHub Advisory Database](https://github.com/advisories/GHSA-4x49-vf9v-38px) |
| GHSA-gxpj-cx7g-858c / CVE-2017-16137 | Low | Regular-expression denial of service when untrusted input reaches the `%o` formatter; public advisory history says the bug was fixed, later reintroduced in the 3.2.x line, and repatched. | 2.6.9 / 3.1.0 / 3.2.7 / 4.3.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-gxpj-cx7g-858c) |
| GHSA-9vvw-cc9w-f27h / CVE-2017-20165 | High | Publicly reviewed inefficient-regular-expression-complexity issue affecting `src/node.js` / `useColors`; GitHub Advisory Database points to the same general hardening lineage as the older ReDoS record, but tracks it separately and maps fixes to the 2.6.x and 3.0.x lines. | 2.6.9 / 3.1.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-9vvw-cc9w-f27h) |

## Security Posture Notes

- Maintenance status: actively maintained; latest npm dist-tag observed in this pass was `4.4.3`, published after the 2025 compromised-package incident to supersede the malicious `4.4.2` release.
- Known sensitive surfaces: browser-bundled consumption, any code path that passes attacker-controlled strings into debug formatting, and dependency pipelines that mirror npm artifacts into private registries or caches.
- Disclosure maturity: GitHub security advisories exist, but the repository's security-policy page currently says no `SECURITY.md` / no security policy is configured.
- Notes: the 2025 incident is not a conventional code defect; it is a supply-chain compromise of a single published version and should be treated differently from the older regex-complexity issues.
- Notes: the two 2017 CVE / GHSA records appear closely related in public evidence and may reflect overlapping descriptions of regex-complexity flaws / patch lineage rather than fully separate bug classes; keep future updates conservative unless upstream clarifies the distinction.
- Notes: the maintainer advisory explicitly says local/server/CLI usage was not the primary observed target in the malware incident, but browser bundles built from the compromised artifact may need full rebuild and cache purge.

## Dependencies of Note

- None flagged yet from this package-advisory pass.

## Open Questions

- Did the project publish a post-incident maintainer writeup or release note beyond advisory / issue-thread material that is worth linking directly on a future pass?
- Can the older regex-complexity advisories be cleanly de-duplicated into one canonical root cause timeline without losing public-record fidelity?
- Which high-download downstream packages still transitively permit vulnerable `debug` ranges in long-lived enterprise support branches?

## Related Pages

- [[npm/index]]
- [[npm/semver]]
- [[npm/minimist]]

---
*Last updated: 2026-04-12 | Sources: 7 (GitHub Advisory Database, OSV.dev package query, NVD CVE record, upstream issue thread, GitHub security-policy page, npm registry metadata, npm downloads API)*
