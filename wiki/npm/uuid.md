# uuid (npm)

**Registry:** npm
**Weekly Downloads:** ~244,292,294 (2026-04-17 to 2026-04-23)
**Repository:** https://github.com/uuidjs/uuid
**Security Contact:** project maintainers via `npm owner ls uuid`
**Disclosure Policy:** https://github.com/uuidjs/uuid/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-25 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev package query and vuln record, GitHub Advisory Database page, upstream security policy, upstream changelog, upstream fix commit, npm registry metadata, npm downloads API, local Claude-compatible proxy used as drafting aid only) | Added a new advisory-mapped page for `uuid` after confirming one direct npm package advisory: the 2026 bounds-checking flaw in caller-supplied buffer writes for `v3()`, `v5()`, and `v6()`, fixed in `14.0.0`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-w5hq-g745-h8pq | Severity not relied on in this pass | Public advisory records describe missing bounds validation when `v3()`, `v5()`, or `v6()` wrote into a caller-supplied output buffer. With an invalid `offset` or undersized `buf`, affected versions could perform silent partial / out-of-range writes instead of throwing like `v1()`, `v4()`, and `v7()` already did. | 14.0.0 | https://github.com/advisories/GHSA-w5hq-g745-h8pq |

*Full package history: https://osv.dev/list?ecosystem=npm&q=uuid*

## Security Posture Notes

- `uuid` has an unusually large operational blast radius because it is one of npm's most widely deployed utility packages; this review window saw roughly **244.3M weekly downloads**.
- The currently published direct package-level advisory surface is **small but real**: OSV returned one package-scoped vulnerability for `pkg:npm/uuid` in this pass rather than a long chain of historical GHSA records.
- The affected path is narrower than many package bugs. The 2026 issue only applies when applications call `v3()`, `v5()`, or `v6()` with an explicit output `buf` and a bad `offset`; default string-returning usage is not the advisory's main risk path.
- Public upstream evidence is clean and internally consistent here: the GHSA summary, OSV record, `14.0.0` changelog entry, and fix commit all describe the same missing bounds checks and the same remediation behavior (`RangeError` when `offset < 0` or `offset + 16 > buf.length`).
- The fix also matters as an API-consistency hardening step: prior to `14.0.0`, `v1()`, `v4()`, and `v7()` already rejected invalid bounds while `v3()`, `v5()`, and `v6()` did not.
- The repository does publish a security policy, but the reporting path is still lightweight: reporters are directed to email the maintainers listed by `npm owner ls uuid` rather than using a richer public disclosure workflow.

## Recommendations for Developers

1. **Upgrade to `14.0.0` or newer** if you use `uuid` buffer-output APIs directly.
2. **Audit any code that passes caller-controlled or loosely validated `buf` / `offset` arguments** into `v3()`, `v5()`, or `v6()`.
3. **Prefer simple string-returning UUID generation paths** unless you specifically need buffer-output behavior.
4. **Treat older helper wrappers carefully**: application code may assume all UUID generation variants reject invalid offsets uniformly, but that was only made consistent in `14.0.0`.

## Dependencies of Note

- Security-sensitive usage tends to cluster around session identifiers, invitation links, object handles, request correlation IDs, and storage keys.
- Wrapper utilities that expose `buf` / `offset` arguments indirectly are the most relevant downstream review target for this advisory.
- Adjacent identifier-generation packages such as [[npm/nanoid]] remain useful comparison points because practical downstream risk often depends on developer assumptions about identifier correctness, uniqueness, and misuse resistance rather than classic parser exploit chains.

## Open Questions

- Did maintainers backport the `GHSA-w5hq-g745-h8pq` bounds-check fix to any older major lines, or is `14.0.0+` the only published remediation path?
- Are there strong public examples of downstream wrappers exposing user-influenced `buf` / `offset` values in practice, or is exploitability mostly limited to local misuse and robustness failures?
- Should the KB eventually capture predecessor-package lineage such as older `node-uuid` disclosures on a separate note, rather than mixing them directly into the modern `uuid` package table?

## Related Pages

- [[npm/nanoid]]
- [[npm/jsonwebtoken]]
- [[npm/validator]]
- [[npm/index]]

---
*Last updated: 2026-04-25 | Sources: 8 (OSV.dev package query for npm/uuid, OSV vuln record for GHSA-w5hq-g745-h8pq, GitHub Advisory Database entry for the same GHSA ID, upstream `CHANGELOG.md`, upstream fix commit `3d2c5b0`, repository security policy, npm registry metadata, npm downloads API)*
