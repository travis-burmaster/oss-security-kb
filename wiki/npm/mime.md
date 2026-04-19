# mime (npm)

**Registry:** npm
**Weekly Downloads:** ~113,653,768 (2026-04-12 to 2026-04-18)
**Repository:** https://github.com/broofa/mime
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-19 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream issue / commit references, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for mime's published package security history, centered on the historical MIME-lookup ReDoS issue fixed in `1.4.1` and `2.0.3`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2017-16138 / GHSA-wrvr-8mpx-r7pp | High | Public advisory records describe a regular-expression denial-of-service issue when MIME lookup is performed on untrusted user input. OSV tracks coordinated fixes on both the older `1.x` line and the newer `2.x` line. | 1.4.1, 2.0.3 | https://github.com/advisories/GHSA-wrvr-8mpx-r7pp |

## Security Posture Notes

- `mime` has a **very small published package-advisory history** in this review pass: one older but still relevant ReDoS issue.
- The public evidence is consistent across OSV, GitHub Advisory Database, the CVE alias, and the linked upstream issue / commit trail: vulnerable ranges were fixed at `1.4.1` and `2.0.3`.
- This bug class is usage-dependent rather than automatic: exploitability depends on applications feeding attacker-controlled strings into MIME lookup helpers.
- The package remains widely deployed (~113.7M weekly downloads in this review window), so older transitive copies can still matter even though the advisory itself is historical.
- Public evidence gathered in this pass supports **`2.0.3+` as the minimum safe floor for the 2.x line**, while current consumers on modern releases are far beyond the fix point.

## Recommendations for Developers

1. **Upgrade to `2.0.3` or newer**; the current latest release at review time is `4.1.0`.
2. **Avoid passing untrusted raw filenames or extensions into MIME lookup helpers without validation** when legacy copies may still be present.
3. **Check older transitive dependencies and lockfiles** because small utility packages like `mime` often linger far below current versions.
4. **Prefer current maintained releases** rather than pinning just above the historical fix boundary.

## Dependencies of Note

- Often inherited through static-file serving, upload handling, HTTP middleware, bundlers, and older web stacks.
- Security relevance is highest in code paths that derive content types from attacker-controlled names, extensions, or path fragments.

## Open Questions

- Are there good public downstream writeups that characterize realistic exploit conditions for this MIME-lookup ReDoS beyond the advisory and patch trail?
- Which still-common server or middleware stacks most often pin pre-fix `mime` transitively?
- Should a future KB pass cross-link `mime` more explicitly with static-file and upload middleware pages that commonly depend on it?

## Related Pages

- [[npm/send]]
- [[npm/serve-static]]
- [[npm/multer]]
- [[npm/index]]

---
*Last updated: 2026-04-19 | Sources: 7 (OSV.dev package query for npm/mime, OSV vulnerability record for GHSA-wrvr-8mpx-r7pp, GitHub Advisory Database entry for the same GHSA ID, public CVE record, upstream issue / commit references, npm registry metadata, npm downloads API)*
