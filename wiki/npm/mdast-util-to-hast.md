# mdast-util-to-hast (npm)

**Registry:** npm
**Repository:** https://github.com/syntax-tree/mdast-util-to-hast
**Security Contact:** none listed
**Disclosure Policy:** public GitHub security advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-02 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / upstream GitHub security advisory, public CVE records, upstream fix commits referenced by the advisory) | Added a new advisory-mapped page for `mdast-util-to-hast` after confirming a public class-injection / markup-sanitization-boundary issue affecting 13.0.0 through 13.2.0 and fixed in 13.2.1. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-66400 / GHSA-4fh9-h7wg-q85m | Moderate | Public advisory records describe a class injection / sanitization-boundary flaw: multiple unprefixed classnames could be added in Markdown source by using character references in fenced code-block info strings, causing rendered user-supplied `<code>` elements to gain additional classes beyond the intended `language-*` prefix (e.g., ```js&#x20;xss → `<code class="language-js xss">`). Practical impact depends on downstream CSS/JS that matches on classes. | 13.2.1 | https://github.com/syntax-tree/mdast-util-to-hast/security/advisories/GHSA-4fh9-h7wg-q85m |

*Full CVE / GHSA history: https://osv.dev/list?ecosystem=npm&q=mdast-util-to-hast*

## Security Posture Notes

- This is a **class injection / markup sanitization boundary** issue in the fenced-code-block info-string handling path, not remote code execution.
- Public OSV data maps the affected SemVer range to **`>= 13.0.0, < 13.2.1`** with the fix in **`13.2.1`**.
- The advisory’s example shows the mechanism clearly: character references in the info string can turn what should be a single `language-*` class into multiple classes, which can matter if downstream applications apply CSS rules or JavaScript listeners keyed on class names.
- The public advisory links directly to the introducing and fixing commits, making it straightforward to validate remediation at the source level.

## Recommendations for Developers

1. **Upgrade to `13.2.1` or newer** if you depend on `mdast-util-to-hast` 13.x.
2. **Treat Markdown→HTML conversion as a trust boundary** when rendering untrusted content. Even issues that “only” influence classes can become security-relevant in real apps due to CSS selectors or JS event binding patterns.
3. If you must render untrusted Markdown, consider **defense-in-depth sanitization** of the resulting HTML/AST (e.g., allowlisting attributes/classes) even after upgrading.

## Related Pages

- [[npm/marked]]
- [[npm/markdown-it]]
- [[npm/highlight.js]]
- [[npm/dompurify]]
- [[npm/sanitize-html]]
- [[npm/index]]

---
*Last updated: 2026-05-02 | Sources: 4 (OSV.dev vulnerability record for GHSA-4fh9-h7wg-q85m / CVE-2025-66400, upstream GitHub security advisory, upstream fix commit references linked from the advisory, public CVE record as mapped by OSV)*
