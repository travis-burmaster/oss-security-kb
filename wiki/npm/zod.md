# zod (npm)

**Registry:** npm
**Weekly Downloads:** ~160,000,000 (as of 2026-04-23)
**Repository:** https://github.com/colinhacks/zod
**Security Contact:** GitHub Security Advisories / private reporting enabled
**Disclosure Policy:** https://github.com/colinhacks/zod/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No audits on record.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-4316 / GHSA-m95q-7qp3-xv42 | Moderate | Denial of service in email validation from inefficient regular-expression handling; the public record says versions through `3.22.2` were affected. | 3.22.3 | [GHSA](https://github.com/advisories/GHSA-m95q-7qp3-xv42), [OSV.dev](https://osv.dev/vulnerability/GHSA-m95q-7qp3-xv42), [v3.22.3 release](https://github.com/colinhacks/zod/releases/tag/v3.22.3) |

## Security Posture Notes

- Public package-scoped OSV / GitHub Advisory Database evidence gathered in this pass showed one direct published `zod` advisory: the 2023 email-validation ReDoS / denial-of-service issue fixed in `3.22.3`.
- The upstream fix trail is unusually clean for a small page: the advisory links directly to the public issue, fix PR, fix commit, and the `v3.22.3` release containing the regex hardening.
- Current npm metadata shows the package is now well beyond the fix point on the modern line, but the public record still matters because `zod` has massive downstream usage and older `3.x` pins remain common.
- No additional direct package-level GHSA / OSV records were surfaced in this pass, so this page intentionally stays narrow rather than speculating about broader validation-library risk.

## Dependencies of Note

- None flagged from this compact public-advisory pass.

## Open Questions

- Has any broader public security review of Zod's validator surface been published beyond the single advisory presently visible in OSV / GHSA?
- Are there other validator-specific performance or parser-boundary bugs in issue trackers that later matured into advisories and should be normalized here if published?

## Related Pages

- [[npm/validator]]
- [[npm/index]]

---
*Last updated: 2026-04-24 | Sources: 8 (OSV.dev package query and vulnerability record, GitHub Advisory Database, public CVE / NVD alias for CVE-2023-4316, upstream issue #2609, upstream PR #2824, upstream fix commit 2ba00fe, v3.22.3 release notes, npm registry metadata, npm downloads API)*
