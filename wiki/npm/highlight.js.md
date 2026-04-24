# highlight.js (npm)

**Registry:** npm
**Weekly Downloads:** ~20,598,521 (last week, fetched 2026-04-24)
**Repository:** https://github.com/highlightjs/highlight.js
**Security Contact:** security@highlightjs.com
**Disclosure Policy:** public GitHub security advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-24 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream release notes / fix commits, npm registry metadata, npm downloads API, local Claude-compatible proxy used only as a drafting aid) | Added a new advisory-mapped page for `highlight.js` after confirming two public package advisories: a prototype-pollution issue fixed across the 9.x and 10.x lines, plus a later grammar-driven ReDoS / freeze issue fixed in `10.4.1`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-26237 / GHSA-vfrc-7r7c-w9mx | Moderate | Prototype pollution from crafted language names during highlighting of attacker-controlled HTML / Markdown code blocks; public advisory text stresses that applications not rendering untrusted user content are unaffected. | 9.18.2, 10.1.2 | https://github.com/advisories/GHSA-vfrc-7r7c-w9mx |
| GHSA-7wwv-vh3v-89cq | Moderate | Multiple shipped grammars had exponential or polynomial regex backtracking that could freeze browsers or block server-side event loops when highlighting untrusted content or using `highlightAuto` with affected grammars enabled. | 10.4.1 | https://github.com/advisories/GHSA-7wwv-vh3v-89cq |

*Full CVE / GHSA history: https://osv.dev/list?ecosystem=npm&q=highlight.js*

## Security Posture Notes

- `highlight.js` has a **small but real published package-level advisory history** in this review pass: one prototype-pollution issue and one later grammar-driven ReDoS / freeze issue.
- Scope matters. Both public advisories are **content-handling issues**, not arbitrary code execution in the highlighter itself. Practical risk depends heavily on whether an application feeds **attacker-controlled code blocks or language names** into the library.
- The 2020 prototype-pollution advisory is narrower than a generic “highlighting is unsafe” claim. Public advisory text says the main trigger is **user-controlled language names** in HTML / Markdown contexts, and explicitly notes that deployments not rendering user-provided data are unaffected.
- The ReDoS advisory is also grammar-specific rather than parser-wide. Public advisory text names the affected grammars and explains that the worst cases appear when applications highlight untrusted content or rely on `highlightAuto` with vulnerable grammars registered.
- Upstream release notes for `10.4.1` make the remediation path unusually clear by calling out broad regex-backtracking fixes across many bundled grammars, while the older prototype-pollution advisory links the fix to PR `#2636` and commit `7241013`.
- Current npm metadata in this pass shows `11.11.1` as latest, which is beyond both public fix points. The larger operational risk is older pinned installs, CMS / Markdown stacks that still bundle outdated versions, or server-side rendering paths that highlight untrusted content.
- Public disclosure posture is reasonable: upstream has published GitHub security advisories and provides a dedicated security contact at `security@highlightjs.com`.

## Dependencies of Note

- `highlight.js` is commonly pulled in through Markdown renderers, documentation generators, CMS platforms, and static-site tooling rather than being used directly.
- Risk increases when downstream applications expose raw language-name selection to end users or call `highlightAuto` on attacker-controlled content.
- The GHSA-7wwv-vh3v-89cq advisory also covers the separate npm package `@highlightjs/cdn-assets`, but this page focuses only on the direct `highlight.js` package.

## Open Questions

- Which widely used Markdown / CMS stacks still pin `highlight.js` below the modern fixed lines?
- Are there strong downstream release notes worth cross-linking for server-side Markdown renderers that bundle vulnerable `highlight.js` versions?
- Would a future KB pass benefit from grouping `highlight.js`, `marked`, and `markdown-it` into a cross-page note about rendering untrusted content safely?

## Related Pages

- [[npm/marked]]
- [[npm/markdown-it]]
- [[npm/sanitize-html]]
- [[npm/index]]

---
*Last updated: 2026-04-24 | Sources: 8 (OSV.dev package query and vulnerability records, GitHub Advisory Database, public CVE records, upstream GitHub security advisories, upstream fix PR / commit references, upstream `10.4.1` release notes, npm registry metadata, npm downloads API)*
