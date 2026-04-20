# helmet (npm)

**Registry:** npm
**Weekly Downloads:** ~9,584,441 (2026-04-12 to 2026-04-18)
**Repository:** https://github.com/helmetjs/helmet
**Security Contact:** see upstream SECURITY.md
**Disclosure Policy:** https://github.com/helmetjs/helmet/blob/main/SECURITY.md
**Current Status:** baseline stub

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-19 | OpenClaw recurring review | package baseline / public-source triage | public-source curation (OSV.dev package query, GitHub Advisory Database API query, npm registry metadata, npm downloads API, upstream CHANGELOG.md, upstream SECURITY.md, upstream README) | Added a conservative baseline page for a widely deployed security-header package with no clean package-level GHSA / OSV record in this pass; preserved the distinction between disclosure readiness, deployment posture, and package vulnerability history. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| No package-level GHSA / OSV record clearly confirmed in this review pass | — | Public-source review did **not** surface a clean package-scoped OSV or GitHub Advisory Database entry for `npm/helmet`, so this page intentionally avoids turning operational header-policy questions into a package advisory claim. | — | https://osv.dev/ |

## Security Posture Notes

- `helmet` is itself a security hardening package, but this review pass did **not** confirm any direct package-level GHSA / OSV advisory for it.
- The strongest positive signal in this pass was **disclosure readiness** rather than advisory history: upstream `SECURITY.md` provides direct maintainer contact and a clear private reporting path.
- Upstream `CHANGELOG.md` through `8.1.0` showed normal maintenance and breaking-change notes around default header behavior, but no entries in this pass surfaced as package-level advisories.
- Real-world risk around `helmet` usually comes from **deployment assumptions**: relying on defaults without an application-specific Content Security Policy, lagging on major versions that change defaults, or assuming response headers alone solve broader injection / trust-boundary problems.
- Current public metadata in this pass showed `latest=8.1.0` and roughly `9.6M` weekly downloads, making it an important package to track even without a published GHSA / OSV record.

## Recommendations for Developers

1. **Review major-version default changes** before upgrades so expected hardening behavior remains explicit.
2. **Treat CSP as application-specific policy** rather than assuming generic defaults are sufficient.
3. **Keep monitoring public advisories** even though none were confirmed in this pass.

## Open Questions

- Are there historical maintainer issue threads or release notes that better explain past header-default changes from a security-operations perspective?
- Should the KB eventually add a deployment-focused cluster note linking `helmet`, `cors`, and Express security-header / trust-boundary configuration?
- Would it be useful to track common downstream misconfiguration classes separately from package-level advisories for hardening middleware like this?

## Related Pages

- [[npm/cors]]
- [[npm/express]]
- [[npm/index]]

---
*Last updated: 2026-04-19 | Sources: 8 (OSV.dev package query for npm/helmet, GitHub Advisory Database API query for npm/helmet, npm registry metadata, npm downloads API, upstream CHANGELOG.md, upstream SECURITY.md, upstream README, public repository metadata)*
