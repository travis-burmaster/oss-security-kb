# glob-parent (npm)

**Registry:** npm
**Weekly Downloads:** ~254,117,340 (2026-04-12 to 2026-04-18)
**Repository:** https://github.com/gulpjs/glob-parent
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-19 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / GitHub security advisories, public CVE records, upstream PR / commit / release references, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for glob-parent's published package security history, covering two separate ReDoS issues: the older enclosure-regex flaw fixed in `5.1.2` and the later 6.0.0-specific regression fixed in `6.0.1`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-28469 / GHSA-ww39-953v-wcq6 | High | Public advisory records describe a regular-expression denial-of-service issue in the enclosure regex used to check strings ending in enclosure containing a path separator. OSV tracks the fix in `5.1.2`. | 5.1.2 | https://github.com/advisories/GHSA-ww39-953v-wcq6 |
| CVE-2021-35065 / GHSA-cj88-88mr-972w | High | Public advisory records describe a separate ReDoS issue affecting `6.0.0` only. OSV and the linked upstream PR / commit / release references map the fix to `6.0.1`, and the advisory explicitly notes that this is separate from the older 2020 issue. | 6.0.1 | https://github.com/advisories/GHSA-cj88-88mr-972w |

## Security Posture Notes

- `glob-parent` has a **small but non-trivial published package-advisory history** with two distinct ReDoS records across adjacent major-version eras.
- The public record matters here because the fixes landed on different lines for different reasons: `CVE-2020-28469` was resolved in `5.1.2`, while `CVE-2021-35065` was a separate `6.0.0` regression fixed in `6.0.1`.
- OSV's reference set is especially useful for this page because it links the advisories directly to upstream PRs, commits, and release tags, reducing ambiguity around the remediation path.
- `glob-parent` is extraordinarily widespread (~254.1M weekly downloads in this review window), largely through transitive use in globbing, file-watching, bundling, and task-runner ecosystems.
- Even though the published issues are both denial-of-service class bugs, the package's transitive footprint makes version hygiene important in developer tooling, CI pipelines, and any service that parses attacker-influenced glob-like input.
- Public evidence gathered in this pass supports **`6.0.1+` as the clean current floor for the modern line** and **`5.1.2+` for older 5.x consumers**.

## Recommendations for Developers

1. **Upgrade to `6.0.1` or newer**; the current latest release at review time is `6.0.2`.
2. **If you remain pinned to 5.x, use at least `5.1.2`** to clear the older enclosure-regex issue.
3. **Audit transitive copies in build tooling, bundlers, and file-processing stacks** because `glob-parent` is usually inherited rather than declared directly.
4. **Treat glob-processing helpers as parser surfaces** when patterns or paths can be attacker-influenced.

## Dependencies of Note

- Commonly inherited through globbing stacks, file watchers, bundlers, task runners, lint/test tooling, and path-normalization helpers.
- Security-sensitive contexts include any workflow that derives glob-like patterns or enclosure-heavy path strings from untrusted input.

## Open Questions

- Which still-popular packages most often pin vulnerable `glob-parent` copies transitively below `5.1.2` or `6.0.1`?
- Are there strong public downstream writeups that explain realistic exploitability in production services versus developer-only tooling contexts?
- Should a future KB pass build a small cluster of cross-links around `glob-parent`, `micromatch`, and other glob-related parser utilities with recurring ReDoS history?

## Related Pages

- [[npm/micromatch]]
- [[npm/braces]]
- [[npm/path-to-regexp]]
- [[npm/index]]

---
*Last updated: 2026-04-19 | Sources: 10 (OSV.dev package query for npm/glob-parent, OSV vulnerability records for GHSA-ww39-953v-wcq6 and GHSA-cj88-88mr-972w, GitHub Advisory Database / upstream GitHub security advisories, public CVE records, upstream PR / commit references, upstream release references for 5.1.2 and 6.0.1, npm registry metadata, npm downloads API)*
