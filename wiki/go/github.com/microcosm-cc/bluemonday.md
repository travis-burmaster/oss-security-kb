# bluemonday (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** 2,680 known importers (pkg.go.dev; as of 2026-08-28)
**Repository:** https://github.com/microcosm-cc/bluemonday
**Security Contact:** none listed (no formal SECURITY.md; advisories filed via GitHub Security Advisories)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-08-28 | OSS Security KB (nightly pass) | public advisory database mapping | automated lookup (github/advisory-database) | 2 direct package advisories mapped | [GHSA search: bluemonday](https://github.com/advisories?query=bluemonday) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-3x58-xr87-2fcj / CVE-2021-29272 | Moderate (CVSS:3.1 6.1 AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N) | Cross-site scripting via Cyrillic uppercase-to-lowercase script tag bypass. Go's `strings.ToLower` canonicalizes Cyrillic uppercase characters, allowing `ЅCRIPT` (Cyrillic Dze) to match as `script` and evade the element-block list. An attacker can inject unsanitized JavaScript through carefully crafted Cyrillic lookalike content. | ≥ 1.0.5 | [GHSA-3x58-xr87-2fcj](https://github.com/advisories/GHSA-3x58-xr87-2fcj) |
| GHSA-x95h-979x-cf3j / CVE-2021-42576 | High (NVD CVSS:3.1 9.8 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N) | Sanitization policy not properly enforced for SELECT, STYLE, and OPTION HTML elements. These elements bypass the sanitization policy entirely when present in input, allowing injection of arbitrary CSS (via STYLE) and form-control hijacking or data exfiltration (via SELECT/OPTION) in applications using the UGC or StrictPolicy. Also affects the Python `pybluemonday` binding (< 0.0.8). NVD rates this Critical (9.8) though the GHSA database label is High. | ≥ 1.0.16 | [GHSA-x95h-979x-cf3j](https://github.com/advisories/GHSA-x95h-979x-cf3j) |

## Security Posture Notes

`bluemonday` is a whitelist-based HTML sanitizer written in Go, designed to filter user-generated content before it is rendered in a browser. It is used in a broad range of Go web applications and CMS platforms as the primary HTML-sanitization layer. The library has 2,680+ known importers on pkg.go.dev and v1.0.27 is the current stable release (2024-07-04).

**Vulnerability pattern:** Both confirmed advisories are XSS-class sanitization bypasses. The first (CVE-2021-29272) exploits Go's Unicode case-folding behavior to smuggle a `<script>` tag through a case-insensitive block check using visually similar Cyrillic characters. The second (CVE-2021-42576) represents a more fundamental policy-enforcement gap: the SELECT, STYLE, and OPTION elements were entirely absent from the allowlist enforcement logic in versions prior to 1.0.16, meaning any input containing these tags was passed through unsanitized regardless of the configured policy.

**Downstream impact:** Several additional GHSA advisories in the GitHub advisory database name `bluemonday` in their context (notably `gogs.io/gogs` CVE-2026-26022 and CVE-2026-52816), but those advisories represent misconfigurations or missing sanitization in consuming applications (Gogs explicitly allowing `data:` URIs in its bluemonday policy, or using Semantic UI HTML re-parsing that bypasses the sanitizer entirely) rather than flaws in `bluemonday` itself.

**Policy configuration risk:** The most common real-world risk with bluemonday is misconfiguration — callers who use `UGCPolicy()` as a baseline and then add permissive allowances (e.g., allowing `data:` URI schemes for anchor `href` attributes, or allowing `style` attributes with broad `regexp` matchers) substantially widen the XSS attack surface beyond what the default UGC policy intends.

**Current status:** All two confirmed direct advisories are patched in v1.0.16 and later. The latest release v1.0.27 is unaffected by both. The project is maintained by the `microcosm-cc` GitHub organization; issues and PRs are active as of 2024.

## Dependencies of Note

- `golang.org/x/net` — used for HTML parsing (the `html.Tokenizer`); carries its own advisory history (see [[go/golang.org-x-net]]). A tokenizer-level parsing inconsistency in `x/net/html` could theoretically affect sanitization correctness, though no such chain has been published for bluemonday.

## Open Questions

- Confirm whether bluemonday 1.0.27 is comprehensively resistant to mutation-XSS vectors (HTML re-serialization after sanitization can re-introduce injection opportunities in some sanitizers).
- Assess whether the `AllowDataURIImages()` helper, which adds `data:image/*` to the allowed URI schemes for image `src` attributes, creates a practical XSS risk for browsers that process `data:image/svg+xml` with active content.
- Monitor for additional bypass advisories given the general track record of HTML sanitizers (see [[npm/dompurify]], [[python/bleach]]) requiring ongoing maintenance to handle new HTML5 features and browser quirks.

## Related Pages

- [[python/bleach]]
- [[npm/dompurify]]
- [[npm/sanitize-html]]
- [[go/golang.org-x-net]]
- [[go/index]]

---
*Last updated: 2026-08-28 | Sources: github/advisory-database (2 direct advisories: GHSA-3x58-xr87-2fcj CVE-2021-29272, GHSA-x95h-979x-cf3j CVE-2021-42576), pkg.go.dev metadata*
