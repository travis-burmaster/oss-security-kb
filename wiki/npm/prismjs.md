# prismjs (npm)

**Registry:** npm  
**Weekly Downloads:** ~20,751,063 (2026-04-27 to 2026-05-03)  
**Repository:** https://github.com/PrismJS/prism  
**Security Contact:** GitHub Security Advisories / repository maintainers  
**Disclosure Policy:** https://github.com/PrismJS/prism/security/advisories  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-04 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / repository advisories, public CVE records, upstream PRs / commits, npm registry metadata, npm downloads API, local Claude-compatible proxy synthesis used as a drafting aid) | Added an advisory-mapped baseline for PrismJS' published package history, covering plugin-specific XSS, grammar / comment ReDoS, and the 2024 DOM-clobbering issue fixed in `1.30.0`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-53382 / GHSA-x7hr-w5r2-h6wg | Moderate | PrismJS through `1.29.0` allowed DOM clobbering because `document.currentScript` lookup could be shadowed by attacker-injected HTML elements, producing XSS when untrusted input contains HTML. | 1.30.0 | https://github.com/advisories/GHSA-x7hr-w5r2-h6wg |
| CVE-2022-23647 / GHSA-3949-f494-cm99 | High | The Command Line plugin did not properly escape output, causing input text to be inserted into the DOM as HTML. Public advisory notes server-side Prism usage and sites not using the plugin were not affected. | 1.27.0 | https://github.com/advisories/GHSA-3949-f494-cm99 |
| CVE-2021-3801 / GHSA-hqhp-5p83-hx96 | Moderate | Crafted HTML comments could trigger excessive CPU consumption through a ReDoS vulnerability. | 1.25.0 | https://github.com/advisories/GHSA-hqhp-5p83-hx96 |
| CVE-2021-32723 / GHSA-gj77-59wh-66hg | High | ReDoS in selected language grammars when highlighting untrusted text; advisory specifically called out ASCIIDoc and ERB before `1.24.0`. | 1.24.0 | https://github.com/advisories/GHSA-gj77-59wh-66hg |
| CVE-2021-23341 / GHSA-h4hr-7fg3-h35w | High | ReDoS in `prism-asciidoc`, `prism-rest`, `prism-tap`, and `prism-eiffel` components before `1.23.0`. | 1.23.0 | https://github.com/advisories/GHSA-h4hr-7fg3-h35w |
| CVE-2020-15138 / GHSA-wvhm-4hhf-97x9 | High | Previewers / Easing preview plugin XSS affected Safari and Internet Explorer users of vulnerable Prism plugin combinations. | 1.21.0 | https://github.com/advisories/GHSA-wvhm-4hhf-97x9 |

## Security Posture Notes

- PrismJS is a very high-usage syntax highlighter (~20.8M weekly downloads in this review window), and most of its published security history is context-sensitive: risk depends heavily on whether untrusted content is highlighted, whether HTML is allowed, and which plugins or language grammars are enabled.
- The advisory pattern is split between **browser-side XSS / DOM trust boundaries** and **regex-complexity DoS** in language grammars or comment parsing.
- `1.30.0` is the clean public minimum for the currently mapped advisory set because it includes the DOM-clobbering fix after the earlier `1.21.0`-`1.27.0` plugin / ReDoS fixes.
- Server-side highlighting is not automatically safe if attacker-controlled input can trigger expensive grammars at scale; it just changes the failure mode from browser XSS to CPU exhaustion.
- Plugin and grammar selection is part of the security boundary. Several advisories did not apply to all Prism users, but package-version scanners will still flag broad version ranges.

## Recommendations for Developers

1. Upgrade to `prismjs@1.30.0` or newer.
2. Do not highlight untrusted HTML as trusted DOM; sanitize before insertion and prefer text-only code blocks where possible.
3. Disable unused plugins and languages, especially when highlighting user-generated content.
4. Rate-limit or sandbox server-side highlighting of untrusted input to reduce ReDoS blast radius.
5. Treat browser plugin usage as security-sensitive UI code, not just presentation styling.

## Dependencies of Note

- Commonly used by documentation sites, static-site generators, Markdown renderers, CMS plugins, browser demos, and build-time documentation pipelines.
- Highest-risk deployments combine user-generated Markdown / HTML with client-side Prism plugins that insert rendered output into the DOM.

## Open Questions

- Which popular static-site generators or Markdown renderers still bundle PrismJS below `1.30.0`?
- Are there public downstream incidents where Prism grammar ReDoS caused production outages?
- Should the KB cross-link PrismJS with `highlight.js`, `markdown-it`, `marked`, `dompurify`, and `sanitize-html` as a shared untrusted-content rendering surface?

## Related Pages

- [[npm/highlight.js]]
- [[npm/markdown-it]]
- [[npm/marked]]
- [[npm/dompurify]]
- [[npm/sanitize-html]]
- [[npm/index]]

---
*Last updated: 2026-05-04 | Sources: 18 (OSV.dev package query for npm/prismjs, OSV vulnerability records for all GHSA IDs listed above, GitHub Advisory Database / repository security advisories, public CVE records, upstream PRs / commits, npm registry metadata, npm downloads API, local Claude-compatible proxy synthesis used as drafting aid only)*
