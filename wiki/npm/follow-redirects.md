# follow-redirects (npm)

**Registry:** npm
**Weekly Downloads:** ~85,838,000 (2026-04-08 to 2026-04-14)
**Repository:** https://github.com/follow-redirects/follow-redirects
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** https://github.com/follow-redirects/follow-redirects/security/advisories
**Current Status:** advisory mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-16 | OpenClaw recurring review | package advisory curation | public-source curation (OSV.dev, GitHub Advisory Database, upstream repository security-policy text, upstream source / fix inspection, npm registry metadata) | 5 published records mapped; redirect-boundary credential leakage is the dominant long-term risk theme | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-74fj-2j2h-c42q / CVE-2022-0155 | High | Older releases exposed sensitive information during redirect handling. Public OSV / advisory metadata confirms a fix landed in the 1.14.7 line. | 1.14.7 | [GitHub Advisory Database](https://github.com/advisories/GHSA-74fj-2j2h-c42q), [OSV](https://osv.dev/vulnerability/GHSA-74fj-2j2h-c42q) |
| GHSA-pw2r-vq6v-hr8c / CVE-2022-0536 | Moderate | Another redirect-related sensitive-information exposure issue followed immediately after the 1.14.7 fix, indicating the original remediation was incomplete. | 1.14.8 | [GitHub Advisory Database](https://github.com/advisories/GHSA-pw2r-vq6v-hr8c), [OSV](https://osv.dev/vulnerability/GHSA-pw2r-vq6v-hr8c) |
| GHSA-jchw-25xp-jwwc / CVE-2023-26159 | Moderate | Improper handling of malformed URLs in the `url.parse()` fallback path could misinterpret the hostname and misdirect traffic during redirect processing. | 1.15.4 | [GitHub Advisory Database](https://github.com/advisories/GHSA-jchw-25xp-jwwc), [OSV](https://osv.dev/vulnerability/GHSA-jchw-25xp-jwwc) |
| GHSA-cxjh-pqwp-8mfp / CVE-2024-28849 | Moderate | Cross-domain redirects cleared `Authorization` and `Cookie` headers but failed to clear `Proxy-Authorization`, allowing proxy credentials to leak to a different host. | 1.15.6 | [GitHub repository advisory](https://github.com/follow-redirects/follow-redirects/security/advisories/GHSA-cxjh-pqwp-8mfp), [OSV](https://osv.dev/vulnerability/GHSA-cxjh-pqwp-8mfp) |
| GHSA-r4q5-vmmm-2653 | Moderate | Cross-domain redirects could still forward custom authentication headers such as `X-API-Key` or `X-Auth-Token` to the redirect target; the latest public fix generalized header stripping with a configurable sensitive-header list. | 1.16.0 | [GitHub repository advisory](https://github.com/follow-redirects/follow-redirects/security/advisories/GHSA-r4q5-vmmm-2653), [OSV](https://osv.dev/vulnerability/GHSA-r4q5-vmmm-2653) |

## Security Posture Notes

- The public advisory history is compact but thematically consistent: four of the five published records center on redirect-boundary handling of credentials or destination selection, not on a scattered mix of unrelated bug classes.
- The 2022 pair (`CVE-2022-0155` and `CVE-2022-0536`) looks like an incomplete-fix chain from public records alone: both were sensitive-information exposure flaws in redirect handling, fixed one patch release apart (`1.14.7` then `1.14.8`).
- The 2023 advisory (`CVE-2023-26159`) broadened the theme from header leakage to redirect-target interpretation: malformed URL handling in the `url.parse()` fallback could misread the hostname and redirect traffic incorrectly.
- The 2024 advisory (`CVE-2024-28849`) made the gap more specific: upstream's advisory text says `Proxy-Authorization` remained on cross-host redirects even though `Authorization` and `Cookie` were already being stripped.
- The 2026 advisory extended that same boundary again, this time to non-standard secrets such as `X-API-Key` and `X-Auth-Token`. Public upstream text explicitly frames the risk as custom authentication headers being forwarded verbatim to a different domain after redirect.
- Current upstream source code now defines a built-in `sensitiveHeaders` list (`Authorization`, `Proxy-Authorization`, `Cookie`) and constructs the stripping regex from that list plus `options.sensitiveHeaders`, which is consistent with the public 2026 mitigation description.
- The package's blast radius is disproportionately large for such a small library because it sits underneath other high-volume HTTP clients such as axios; npm download data in this pass was ~85.8M per week.
- Upstream at least publishes a minimal `SECURITY.md` pointing reporters to GitHub Security Advisories, which is better disclosure posture than many tiny transitives, but the public record still suggests redirect header-handling deserves continued scrutiny.

## Recommendations for Developers

1. **Run at least `1.16.0`** if you rely on automatic redirects, since that is the first public release that clears the full currently known published advisory set.
2. **Treat custom auth headers as sensitive configuration**, not just standard ones — populate `sensitiveHeaders` with every non-standard secret-bearing header your application sends.
3. **Check transitive trees**, not only direct dependencies, because many applications inherit `follow-redirects` through `axios` or other HTTP-client wrappers.
4. **Review redirect expectations in SSRF-sensitive code paths**; several public issues here become relevant specifically when user influence exists over redirect targets or redirect-triggering URLs.
5. **Watch upstream security advisories** for further redirect-boundary fixes, because the public history shows repeated extension of what counts as a sensitive header.

## Dependencies of Note

- `follow-redirects` is primarily a transitive dependency risk rather than a package most applications interact with directly.
- Public evidence in this pass points to redirect logic itself as the core sensitive surface: header propagation, host interpretation, and cross-domain redirect handling.

## Open Questions

- Are there additional widely used auth-header conventions that still require explicit `sensitiveHeaders` configuration in real deployments?
- Which major downstream packages besides axios still pin older `1.14.x` or `1.15.x` ranges in practice?
- Has upstream published any broader redirect-hardening guidance beyond the advisory text and the current `sensitiveHeaders` implementation?

## Related Pages

- [[npm/axios]]
- [[python/requests]]
- [[python/urllib3]]
- [[npm/index]]

---
*Last updated: 2026-04-16 | Sources: 8 (OSV.dev package query for npm/follow-redirects, GitHub Advisory Database entries for the published GHSA/CVE set, public GitHub repository advisories for the 2024 and 2026 records, upstream SECURITY.md, current upstream `index.js`, npm registry metadata, npm downloads API)*
