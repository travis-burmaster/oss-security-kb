# send (npm)

**Registry:** npm
**Weekly Downloads:** ~98,569,751 (2026-04-12 to 2026-04-18)
**Repository:** https://github.com/pillarjs/send
**Security Contact:** GitHub Security Advisory
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-19 | OpenClaw recurring review | public advisory refresh | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream HISTORY.md / README, npm registry metadata, npm downloads API) | Reconciled the page against the full public advisory set, confirmed three published package records, and promoted the page from audit-ingested to advisory-mapped while preserving a clearly labeled operational audit note. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| 2026-04-10 | [@travis-burmaster](https://github.com/travis-burmaster) | full-source (as part of Express 5.2.1 audit) | manual review | 1 finding (medium) + 6 areas confirmed safe | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-xwg4-93c6-3h42 / CVE-2014-6394 | Moderate | Versions `0.8.3` and earlier had a directory-traversal flaw when applications relied on the `root` option for confinement and similarly named directories outside the intended root were reachable. | 0.8.4 | https://osv.dev/vulnerability/GHSA-xwg4-93c6-3h42 |
| GHSA-jgqf-hwc5-hh37 / CVE-2015-8859 | Low | Versions before `0.11.1` could leak the configured absolute `root` path during error handling, creating filesystem-path disclosure. | 0.11.1 | https://osv.dev/vulnerability/GHSA-jgqf-hwc5-hh37 |
| GHSA-m6fv-jmcg-4jfg / CVE-2024-43799 | Medium | Passing untrusted input into `SendStream.redirect()` could trigger template injection that led to XSS in the generated redirect HTML. Public advisory text notes exploitation also required attacker control of redirect input plus user / browser preconditions. | 0.19.0 | https://osv.dev/vulnerability/GHSA-m6fv-jmcg-4jfg |

## Security Posture Notes

- Public package-advisory history for `send` is currently **small but real**: three published records spanning path confinement, error-surface information disclosure, and redirect-template injection.
- The package's blast radius is very large because `send` remains heavily deployed under Express and related static-file serving stacks, with roughly **98.6 million weekly downloads** in this review pass.
- The 2024 advisory is the clearest modern security inflection point. Upstream `HISTORY.md` ties `0.19.0` directly to "Remove link renderization in html while redirecting," which lines up with the public GHSA / CVE record for redirect-template injection.
- Upstream release history also matters for version interpretation: `1.1.0` is explicitly described as "Changes from 0.19.0," so the modern 1.x line carries forward the latest published security fix rather than reopening that issue on a separate major branch.
- Across the public record, `send`'s recurring risk surfaces are narrow and unsurprising for a static-file transport helper: path normalization / root-boundary handling, error-message exposure, and HTML generation around redirects.
- Public evidence from this pass points to **current maintained releases such as `1.2.1`** as clear of the published package-advisory set reviewed here.

## Recommendations for Developers

1. **Prefer current maintained releases** (`1.2.1` at review time) rather than older 0.x lines.
2. **Treat redirect targets as untrusted input** and validate or allowlist them before they reach `response.redirect()` / `SendStream.redirect()` paths.
3. **Keep `root`-confinement assumptions conservative** when reviewing older Express or middleware stacks that may still vendor or pin pre-`0.11.1` copies.
4. **Audit transitive dependencies in long-lived lockfiles** because `send` is commonly inherited through higher-level web frameworks rather than pinned directly.

## Dependencies of Note

- Commonly used underneath Express's `res.sendFile()` and `serve-static`, so applications often inherit it transitively.
- Exposure increases anywhere untrusted input influences redirect destinations or file-serving roots.

## Supplemental Public Audit Note

The repository also contains a public source-audit note from the April 2026 Express review saying current traversal defenses are layered and that symlink following is a deployment / filesystem-risk consideration rather than a published package advisory. This recurring review did not find new public advisories that would justify reclassifying that note as a package vulnerability.

## Open Questions

- Has the PillarJS / Express ecosystem published any broader guidance on safely handling redirect destinations after `CVE-2024-43799`, beyond the advisory text and patch itself?
- Which still-common long-term-support framework bundles most often retain pre-`0.19.0` copies of `send` in practice?
- Should a future KB pass map `send`, `serve-static`, and Express redirect behavior more explicitly as one operational cluster for static-file and redirect safety?

## Related Pages

- [[npm/express]]
- [[npm/serve-static]]
- [[npm/index]]

---
*Last updated: 2026-04-19 | Sources: 7 (OSV.dev package query for npm/send, OSV vulnerability records for the three published GHSA IDs, GitHub Advisory Database entries, public CVE records, upstream HISTORY.md / README, npm registry metadata, npm downloads API)*
*Auditor contact: [@travis-burmaster](https://github.com/travis-burmaster)*
