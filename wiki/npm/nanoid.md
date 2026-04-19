# nanoid (npm)

**Registry:** npm
**Weekly Downloads:** ~153,079,501 (2026-04-12 to 2026-04-18)
**Repository:** https://github.com/ai/nanoid
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** https://github.com/ai/nanoid/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-19 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / GitHub security advisories, public CVE records, upstream changelog, upstream PR / commit / compare references, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for Nano ID's published package security history, covering the 2021 object-coercion collision issue fixed in `3.1.31` and the 2024 non-integer size predictability flaw fixed in `3.3.8` and `5.0.9`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-23566 / GHSA-qrpm-p2h7-hrv2 | Moderate | Public advisory records describe a collision / sensitive-information exposure issue when an object was passed in the `size` position; the upstream changelog for `3.1.31` explicitly says it fixed a collision vulnerability on object input in `size`. | 3.1.31 | https://github.com/advisories/GHSA-qrpm-p2h7-hrv2 |
| CVE-2024-55565 / GHSA-mwcw-c2x4-8c55 | Moderate | Passing a non-integer size could produce predictable or otherwise broken Nano ID generation. Public records and upstream changelog entries align on fixes landing in both the maintained `3.x` and `5.x` lines. | 3.3.8, 5.0.9 | https://github.com/advisories/GHSA-mwcw-c2x4-8c55 |

## Security Posture Notes

- Nano ID's published package-advisory history is **small but meaningful**: two input-validation flaws that undermine assumptions about identifier uniqueness or unpredictability rather than classic parser crashes or direct remote code execution.
- The package's role matters here. Nano ID is often used at authentication, correlation, invite-link, resource-label, or public-identifier boundaries, so even moderate-severity generation flaws can have outsized downstream impact when developers rely on uniqueness or entropy properties.
- Public evidence is unusually clean in this pass: OSV, GitHub Advisory Database, CVE aliases, upstream PR / commit / compare links, and the changelog all point at the same two fix windows.
- The 2024 advisory is especially operationally relevant because fixes landed on **two maintained branches at once** (`3.3.8` and `5.0.9`), which means version-family alone was not enough to infer safety.
- Nano ID remains extremely widely used (~153.1M weekly downloads in this review window), so even a narrow advisory set is worth normalizing in the KB.
- Public evidence gathered here supports **`5.0.9+` as the cleanest modern floor**, while older `3.x` consumers should use at least `3.3.8`; `3.1.31` only addresses the earlier 2021 issue.

## Recommendations for Developers

1. **Upgrade to `5.0.9` or newer**; if you are pinned to `3.x`, use at least `3.3.8`.
2. **Audit wrapper functions and helper utilities** that pass user-controlled or loosely typed values into Nano ID size parameters.
3. **Revisit any security assumptions tied to token unpredictability or ID uniqueness** if your deployment previously allowed non-integer or object-shaped inputs.
4. **Check transitive usage in frontend and backend frameworks** because Nano ID is often bundled indirectly rather than declared only at the top level.

## Dependencies of Note

- Frequently embedded in frontend frameworks, API SDKs, ORMs, state-management tooling, and custom helper libraries that need short identifiers.
- Security-sensitive usage includes invitation links, password-reset tokens, public object IDs, correlation IDs, and any context where developers assume generated IDs are uniformly random and collision-resistant.

## Open Questions

- Are there strong public downstream writeups that explain realistic exploitation boundaries for the 2021 object-coercion issue in production applications?
- Which popular packages still pin Nano ID below `3.3.8` or `5.0.9` transitively?
- Should the KB eventually cross-link Nano ID with other identifier-generation libraries so developers can compare bug classes around entropy, type coercion, and input validation?

## Related Pages

- [[npm/jsonwebtoken]]
- [[npm/validator]]
- [[npm/minimist]]
- [[npm/index]]

---
*Last updated: 2026-04-19 | Sources: 9 (OSV.dev package query for npm/nanoid, OSV vulnerability records for the two GHSA IDs listed above, GitHub Advisory Database / upstream GitHub security advisories, public CVE records, upstream changelog, upstream PR / commit / compare references, npm registry metadata, npm downloads API)*