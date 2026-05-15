# bleach (python)

**Registry:** PyPI  
**Weekly Downloads:** unknown in this pass (PyPIStats returned HTTP 429 on 2026-05-15)  
**Repository:** https://github.com/mozilla/bleach  
**Security Contact:** Mozilla secure bug tracker / security@mozilla.org  
**Disclosure Policy:** https://github.com/mozilla/bleach/security/policy and https://www.mozilla.org/en-US/security/#For_Developers  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-15 | OpenClaw recurring review | package-level public advisory mapping for PyPI `bleach` | public-source curation from OSV.dev package and vulnerability records, GitHub Advisory Database / upstream GHSA records, public CVE / NVD records, PyPA advisory aliases, upstream README / security policy / release references, PyPI metadata, and local proxy-assisted drafting | Added initial advisory-mapped page for Bleach's published sanitizer-bypass and parser-boundary vulnerability history: URI-scheme filtering bypass, repeated mutation-XSS conditions around allowlisted raw / SVG / MathML tags, and a style-attribute ReDoS issue. | https://osv.dev/list?ecosystem=PyPI&q=bleach |

## Known Vulnerabilities

OSV returns both canonical GHSA records and PYSEC aliases for the same underlying issues. This page counts the five GHSA / CVE-backed vulnerability records once each and keeps fixed-version boundaries tied to public advisory metadata.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2018-7753 / GHSA-m9mq-p2f9-cfqv / PYSEC-2018-51 | Critical | URI-valued attributes were not properly sanitized when the value used character entities, allowing an otherwise disallowed URI scheme to pass through sanitization. | 2.1.3 | https://github.com/advisories/GHSA-m9mq-p2f9-cfqv ; https://nvd.nist.gov/vuln/detail/CVE-2018-7753 ; https://github.com/mozilla/bleach/releases/tag/v2.1.3 |
| CVE-2020-6802 / GHSA-q65m-pv3f-wr5r / PYSEC-2020-27 | Moderate | Mutation XSS affected `bleach.clean()` calls that allowed `noscript` together with raw-text tags such as `script`, `style`, `iframe`, `xmp`, and related tags. | 3.1.1 | https://github.com/mozilla/bleach/security/advisories/GHSA-q65m-pv3f-wr5r ; https://nvd.nist.gov/vuln/detail/CVE-2020-6802 ; https://github.com/mozilla/bleach/commit/f77e0f6392177a06e46a49abd61a4d9f035e57fd |
| CVE-2020-6816 / GHSA-m6xf-fq7q-8743 / PYSEC-2020-28 | Moderate | Mutation XSS affected `bleach.clean()` when `svg` or `math`, an RCDATA tag, and `strip=False` were combined in the allowlist / options. | 3.1.2 | https://github.com/mozilla/bleach/security/advisories/GHSA-m6xf-fq7q-8743 ; https://nvd.nist.gov/vuln/detail/CVE-2020-6816 ; https://github.com/mozilla/bleach/releases/tag/v3.1.2 |
| CVE-2020-6817 / GHSA-vqhp-cxgc-6wmm / PYSEC-2020-340 | High | `bleach.clean()` style-attribute parsing could trigger regular-expression denial of service when callers allowed a `style` attribute on cleaned tags. | 3.1.4 | https://github.com/mozilla/bleach/security/advisories/GHSA-vqhp-cxgc-6wmm ; https://nvd.nist.gov/vuln/detail/CVE-2020-6817 ; https://github.com/mozilla/bleach/releases/tag/v3.1.4 |
| CVE-2021-23980 / GHSA-vv2x-vrpj-qqpq / PYSEC-2021-865 | Moderate | Mutation XSS affected `bleach.clean()` when SVG / MathML tags, paragraph or break tags, raw-text / RCDATA tags, and `strip_comments=False` were combined; upstream noted these tags and options were not all defaults. | 3.3.0 | https://github.com/mozilla/bleach/security/advisories/GHSA-vv2x-vrpj-qqpq ; https://nvd.nist.gov/vuln/detail/CVE-2021-23980 ; https://github.com/mozilla/bleach/commit/79b7a3c5e56a09d1d323a5006afa59b56162eb13 |

*Full OSV package listing: https://osv.dev/list?ecosystem=PyPI&q=bleach*

## Security Posture Notes

- Bleach is an HTML sanitization library, so its core security boundary is application-dependent allowlist construction. The public advisory history is concentrated around sanitizer bypasses and resource-exhaustion behavior in specific parser / allowlist combinations.
- Several records are mutation-XSS issues involving rarely safe tag families such as SVG, MathML, `noscript`, or raw-text / RCDATA tags. Applications should treat non-default allowlists as security-sensitive configuration and pair sanitization with context-aware output handling and browser defenses such as a restrictive CSP.
- Upstream README text fetched in this pass says, "2023-01-23: Bleach is deprecated," while the PyPI package still showed latest release `6.3.0`. The security policy page provides a Mozilla secure bug-report path and security email, but its supported-version table appeared stale relative to current PyPI metadata.
- Current public records found in this pass are fixed by versions at or before `3.3.0`; this page did not identify an unfixed Bleach package advisory in OSV / GHSA.
- This review did not perform active vulnerability hunting, exploit validation, or live target testing. It only normalized already-public advisory, CVE, upstream release / policy, and package metadata.

## Dependencies of Note

- Bleach's sanitizer behavior depends on HTML parser behavior and consumer-provided tag / attribute / protocol allowlists.
- Consumers that expose rich-text editing, Markdown-to-HTML pipelines, issue trackers, comments, CMS content, or email rendering should verify how Bleach is configured rather than treating the package name alone as a complete mitigation.

## Open Questions

- Should future KB maintenance add a shared sanitizer comparison page for `bleach`, `nh3`, `dompurify`, `sanitize-html`, and `lxml.html.clean`?
- Are there public migration notes from Bleach to maintained alternatives that should be captured for downstream projects relying on long-term sanitizer support?
- Should the KB separately track application frameworks that inherit Bleach risk through optional rich-text or Markdown rendering features?

## Related Pages

- [[python/lxml]]
- [[npm/dompurify]]
- [[npm/sanitize-html]]
- [[python/index]]

---
*Last updated: 2026-05-15 | Sources: OSV package query and individual vulnerability records for PyPI `bleach`; GitHub Advisory Database / upstream GHSA entries for GHSA-m9mq-p2f9-cfqv, GHSA-q65m-pv3f-wr5r, GHSA-m6xf-fq7q-8743, GHSA-vqhp-cxgc-6wmm, and GHSA-vv2x-vrpj-qqpq; public CVE / NVD records for CVE-2018-7753, CVE-2020-6802, CVE-2020-6816, CVE-2020-6817, and CVE-2021-23980; PyPA advisory aliases; upstream README, security policy, commits, and release references; PyPI metadata; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid.*
