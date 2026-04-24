# vue (npm)

**Registry:** npm
**Weekly Downloads:** ~11,183,900 (2026-04-17 to 2026-04-23)
**Repository:** https://github.com/vuejs/core
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** https://github.com/vuejs/core/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-24 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / public GitHub security advisories, public CVE records, npm registry metadata, npm downloads API) | Added a conservative advisory-mapped page for `vue` based on the currently published package-level public advisory set surfaced in this pass. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-9506 / GHSA-5j4c-8p2g-v4jx | Low | Public advisory records describe a ReDoS condition in `parseHTML` that can be triggered by crafted template input causing inefficient regex evaluation. The affected range recorded in OSV / GHSA is `>=2.0.0-alpha.1` and `<3.0.0-alpha.0`, which confines the issue to the Vue 2 line rather than modern Vue 3 releases. | Vue 3 line (`3.0.0-alpha.0` and later are outside the affected range) | https://github.com/advisories/GHSA-5j4c-8p2g-v4jx |

## Security Posture Notes

- The public package-level advisory set gathered in this pass for `vue` is **small but not empty**: OSV returned one GitHub-reviewed advisory affecting the Vue 2 line.
- The recorded bug class is **regex-complexity / ReDoS** in HTML parsing, which matters most when applications or tooling accept attacker-influenced template content rather than only shipping static trusted templates.
- The public affected range in the advisory ends before `3.0.0-alpha.0`, so this record should be read primarily as a **Vue 2 legacy-line concern**, not as a statement about current Vue 3 releases.
- Current npm metadata gathered here shows **`3.5.33` as latest**, which is well outside the affected range, but the package still has very high usage (~11.2M weekly downloads), so legacy 2.x deployments remain relevant.
- This page intentionally stays conservative: this review pass surfaced one clear package-level advisory and does not generalize unrelated ecosystem issues into direct `vue` package findings without package-scoped public records.

## Recommendations for Developers

1. If you still run **Vue 2.x**, review whether any attacker-controlled or semi-trusted input can influence template parsing or compilation paths.
2. Prefer **supported Vue 3 releases** for long-term maintenance, since the currently gathered public advisory record does not affect the 3.x line.
3. Treat dynamic template construction as a **security-sensitive boundary** even when the published advisory severity is low.
4. Add regression tests for parser performance on malformed or adversarial template fragments if your product compiles or transforms user-influenced template content.

## Dependencies of Note

- `vue` is often consumed both directly by applications and indirectly through surrounding build / dev / SSR tooling, but the advisory gathered here maps to the core package itself.
- Template parsing and compilation behavior, not package installation or dependency resolution, is the main surface visible in the current public record set.

## Open Questions

- Are there maintainer-authored release notes or backport statements that would make the Vue 2 remediation path easier to document more precisely?
- Which major downstream frameworks or enterprise support distributions still ship Vue 2 with compensating controls for parser-related issues?
- Would a future KB pass benefit from comparing direct `vue` package advisories with adjacent Vue-ecosystem packages where the more active security history may actually live?

## Related Pages

- [[npm/react]]
- [[npm/vite]]
- [[npm/webpack-dev-server]]
- [[npm/index]]

---
*Last updated: 2026-04-24 | Sources: 6 (OSV.dev package query for npm/vue, OSV vulnerability record for GHSA-5j4c-8p2g-v4jx, GitHub Advisory Database / public GitHub security advisory for the same GHSA ID, public CVE / NVD record via advisory alias, npm registry metadata, npm downloads API)*