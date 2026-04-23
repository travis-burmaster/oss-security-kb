# dompurify (npm)

**Registry:** npm
**Weekly Downloads:** ~38,291,307 (2026-04-16 to 2026-04-22)
**Repository:** https://github.com/cure53/DOMPurify
**Security Contact:** https://github.com/cure53/DOMPurify/security/policy
**Disclosure Policy:** https://github.com/cure53/DOMPurify/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-23 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev package query, OSV vulnerability records, GitHub Advisory Database / public GitHub security advisories, public CVE records, upstream release notes, npm registry metadata, npm downloads API, local Claude-compatible proxy used only as a drafting aid) | Added a new advisory-mapped page for `dompurify` after public evidence showed a dense package-level history centered on mutation-XSS / sanitization-bypass fixes, newer prototype-pollution and configuration-bypass issues, and a recent `3.3.2` → `3.4.0` hardening train. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-8hgg-xxm5-3873 / CVE-2019-25155 | See source | Older demo / hook material allowed reverse tabnabbing because links opened with `_blank` lacked `rel="noopener noreferrer"`; public records map the fix to `1.0.11`. | 1.0.11 | https://github.com/advisories/GHSA-8hgg-xxm5-3873 |
| GHSA-chqj-j4fh-rw7m / CVE-2019-16728 | See source | Mutation-XSS bypass in releases before `2.0.3` using crafted `<svg>` / `<math>` content and parser recontextualization. | 2.0.3 | https://github.com/advisories/GHSA-chqj-j4fh-rw7m |
| GHSA-mjjq-c88q-qhr6 | See source | Follow-on mutation-XSS bypass in releases before `2.0.7`; public advisory history treats this as a separate sanitization-bypass fix from the earlier `2.0.3` issue. | 2.0.7 | https://github.com/advisories/GHSA-mjjq-c88q-qhr6 |
| GHSA-63q7-h895-m982 / CVE-2020-26870 | See source | Mutation-XSS issue in releases before `2.0.17`; public records describe namespace-changing / serialize-parse roundtrip behavior that could turn sanitized markup into executable content. | 2.0.17 | https://github.com/advisories/GHSA-63q7-h895-m982 |
| GHSA-gx9m-whjm-85jf / CVE-2024-47875 | See source | Nesting-based mutation-XSS affecting both `2.x` and `3.x` lines; OSV maps fixes to `2.5.0` and `3.1.3`. | 2.5.0 / 3.1.3 | https://github.com/advisories/GHSA-gx9m-whjm-85jf |
| GHSA-mmhx-hmjr-r674 / CVE-2024-45801 | See source | Public advisory describes bypassing recent depth checks via special nesting and prototype-pollution-assisted weakening, with fixes in `2.5.4` and `3.1.3`. | 2.5.4 / 3.1.3 | https://github.com/advisories/GHSA-mmhx-hmjr-r674 |
| GHSA-p3vf-v8qc-cwcr / CVE-2024-48910 | See source | Prototype-pollution issue in the `2.x` line; public records map the fix to `2.4.2`. | 2.4.2 | https://github.com/advisories/GHSA-p3vf-v8qc-cwcr |
| GHSA-vhxf-7vqr-mrjg / CVE-2025-26791 | See source | `SAFE_FOR_TEMPLATES` regex flaw leading to conditional mutation-XSS before `3.2.4`. | 3.2.4 | https://github.com/advisories/GHSA-vhxf-7vqr-mrjg |
| GHSA-v8jm-5vwx-cfxm / CVE-2025-15599 | See source | Attribute-sanitization bypass tied to missing `textarea` raw-text handling; public records map the fix to `3.2.7`. | 3.2.7 | https://github.com/advisories/GHSA-v8jm-5vwx-cfxm |
| GHSA-v2wj-7wpq-c8vv / CVE-2026-0540 | See source | Cross-site-scripting bypass due to missing raw-text element validation, affecting both `2.5.3`–`2.5.8` and `3.1.3`–`3.3.1`; fixed in `2.5.9` and `3.3.2`. | 2.5.9 / 3.3.2 | https://github.com/advisories/GHSA-v2wj-7wpq-c8vv |
| GHSA-cj63-jhhr-wcxv | See source | `USE_PROFILES` handling rebuilt `ALLOWED_ATTR` in a way that made prototype-polluted array properties security-relevant; fixed in `3.3.2`. | 3.3.2 | https://github.com/advisories/GHSA-cj63-jhhr-wcxv |
| GHSA-cjmm-f4jc-qw8r | See source | Function-based `ADD_ATTR` / `attributeCheck` path could skip URI-safe validation and re-allow dangerous values; fixed in `3.3.2`. | 3.3.2 | https://github.com/advisories/GHSA-cjmm-f4jc-qw8r |
| GHSA-h8r8-wccr-v5f2 | See source | Public advisory describes mutation-XSS via re-contextualization when sanitized HTML is reinserted into a new parsing context with raw-text wrappers; fixed in `3.3.2`. | 3.3.2 | https://github.com/advisories/GHSA-h8r8-wccr-v5f2 |
| GHSA-39q2-94rc-95cp | See source | `ADD_TAGS` function-form behavior could short-circuit `FORBID_TAGS`, letting custom tag checks bypass explicit forbid rules before `3.4.0`. | 3.4.0 | https://github.com/advisories/GHSA-39q2-94rc-95cp |
| GHSA-crv5-9vww-q3g8 / CVE-2026-41239 | See source | `SAFE_FOR_TEMPLATES` bypass in `RETURN_DOM` mode; public advisory maps the fix to `3.4.0`. | 3.4.0 | https://github.com/advisories/GHSA-crv5-9vww-q3g8 |
| GHSA-h7mw-gpvr-xq4m / CVE-2026-41240 | See source | Another `FORBID_TAGS` / function-based `ADD_TAGS` asymmetry let custom allow logic override explicit forbids before `3.4.0`. | 3.4.0 | https://github.com/advisories/GHSA-h7mw-gpvr-xq4m |
| GHSA-v9jr-rg53-9pgp / CVE-2026-41238 | See source | Prototype-pollution-assisted XSS bypass through `CUSTOM_ELEMENT_HANDLING` fallback behavior in `3.0.1` through `3.3.3`; fixed in `3.4.0`. | 3.4.0 | https://github.com/advisories/GHSA-v9jr-rg53-9pgp |

## Security Posture Notes

- `dompurify` is a **security-critical sanitizer**, so even "just XSS" advisories deserve more attention than they would in an ordinary utility package.
- The public package history collected in this pass is both real and dense: **17 published OSV / GHSA records** were returned by the package query, with the clearest recurring theme being **mutation-XSS / sanitization-bypass** behavior rather than memory corruption.
- The most important upgrade landmarks in the current public record are:
  - `2.0.3` → `2.0.17` for the older mutation-XSS cluster,
  - `2.4.2` / `2.5.0` / `2.5.4` / `2.5.9` for the later `2.x` hardening train,
  - `3.1.3`, `3.2.4`, `3.2.7`, `3.3.2`, and `3.4.0` for the modern `3.x` fix cadence.
- `3.3.2` and `3.4.0` stand out as especially important maintenance releases in the public record: upstream release notes explicitly call out multiple security-relevant fixes in each.
- The newer public issues are not all the same bug class. In addition to classic mXSS, the package record now includes **prototype-pollution-sensitive configuration paths**, **URI-validation bypasses**, and **custom-element / forbid-list interaction flaws**.
- Current npm metadata in this pass showed **`latest=3.4.1`**, which is newer than the current public advisory fix point (`3.4.0`) and therefore clears the published package advisory set gathered here.
- Public npm download data still shows a very large operational footprint (**~38.3M weekly downloads**), so small sanitizer regressions can have a wide downstream blast radius.
- Upstream has a real security-policy page, which is a stronger disclosure signal than many comparable packages expose publicly.

## Recommendations for Developers

1. **Upgrade to `3.4.1` or newer**; current npm metadata in this pass showed `3.4.1` as the latest release and the first tag newer than the current `3.4.0` public advisory fix point.
2. **Regression-test custom sanitizer options**, especially `SAFE_FOR_TEMPLATES`, `RETURN_DOM`, `ADD_ATTR`, `ADD_TAGS`, `USE_PROFILES`, and custom-element handling. Recent public advisories repeatedly hit option interaction surfaces rather than only default behavior.
3. **Treat DOMPurify as one layer of defense-in-depth**, not a sole application security control; pair it with contextual output encoding, framework-safe rendering patterns, and CSP where appropriate.
4. **Watch both major lines if you carry legacy `2.x`**. The public record includes repeated dual-line fixes where `2.x` and `3.x` each received separate remediation points.

## Dependencies of Note

- Commonly embedded in rich-text editors, Markdown / HTML rendering pipelines, CMS systems, comment systems, WYSIWYG editors, browser-side preview surfaces, and any application that accepts user-authored HTML.
- Security relevance increases when applications enable advanced configuration options or reinsert sanitized HTML into new parsing contexts.

## Open Questions

- Which popular downstream frameworks or editor bundles still pin vulnerable `2.x` or early `3.x` DOMPurify releases?
- Should the KB eventually add a comparison note across `dompurify`, `sanitize-html`, and framework-native sanitization paths, since their public records show recurring option-interaction failures rather than one-off bugs?
- Are there public maintainer or researcher writeups worth adding later to better cluster the repeated raw-text / namespace / re-contextualization bypass family?

## Related Pages

- [[npm/sanitize-html]]
- [[npm/marked]]
- [[npm/markdown-it]]
- [[npm/handlebars]]
- [[npm/index]]

---
*Last updated: 2026-04-23 | Sources: 12 (OSV.dev package query for npm/dompurify, OSV vulnerability records for the 17 published package entries surfaced in this pass, GitHub Advisory Database / public GitHub security advisories for the same records, public CVE / NVD records, upstream release notes for 3.3.2 / 3.4.0 / 3.4.1, upstream SECURITY.md / security policy, upstream README, npm registry metadata, npm downloads API, and public repository metadata)*