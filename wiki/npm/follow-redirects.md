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
| 2026-04-15 | OpenClaw recurring review | package advisory curation | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream SECURITY.md, npm registry metadata) | 5 published records mapped; redirect-boundary credential leakage is the recurring pattern | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-74fj-2j2h-c42q / CVE-2022-0155 | High | Older releases could leak sensitive information during redirects; OSV links the public fix to commit `8b347cb` and maps the first patched release to `1.14.7`. | 1.14.7 | [GitHub Advisory Database](https://github.com/advisories/GHSA-74fj-2j2h-c42q) |
| GHSA-pw2r-vq6v-hr8c / CVE-2022-0536 | Moderate | Older releases exposed sensitive information to an unauthorized actor during redirect handling; public records map the first patched release to `1.14.8`. | 1.14.8 | [GitHub Advisory Database](https://github.com/advisories/GHSA-pw2r-vq6v-hr8c) |
| GHSA-jchw-25xp-jwwc / CVE-2023-26159 | Moderate | Improper handling of URLs through the legacy `url.parse()` path could misinterpret a hostname and enable redirect abuse until `1.15.4`. | 1.15.4 | [GitHub Advisory Database](https://github.com/advisories/GHSA-jchw-25xp-jwwc) |
| GHSA-cxjh-pqwp-8mfp / CVE-2024-28849 | Moderate | Cross-domain redirects cleared `authorization` and `cookie` headers but kept `proxy-authorization`, allowing credential leakage until `1.15.6`. | 1.15.6 | [GitHub Advisory Database](https://github.com/advisories/GHSA-cxjh-pqwp-8mfp) |
| GHSA-r4q5-vmmm-2653 | Moderate | GitHub's public advisory records that custom authentication headers could leak to cross-domain redirect targets; OSV maps the first patched release to `1.16.0`. No CVE alias was present in the public records gathered for this pass. | 1.16.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-r4q5-vmmm-2653) |

## Security Posture Notes

- The public advisory history is unusually concentrated around one trust boundary: redirect handling. Four of the five published records in this pass describe some form of credential, header, or destination-handling mistake during redirect processing.
- That pattern matters because `follow-redirects` is frequently consumed transitively through higher-level HTTP clients such as `axios`, so a small package bug can have wide downstream exposure.
- npm download data gathered in this pass was ~85.8M per week, which makes even moderate-severity redirect bugs operationally important.
- Upstream does publish a `SECURITY.md`, and it points reporters to GitHub Security Advisories rather than ad hoc issue disclosure.
- npm registry metadata in this pass showed `latest=1.16.0`, which sits at or above every fixed version in the currently published OSV/GHSA set captured here.

## Recommendations for Developers

1. **Run `1.16.0` or newer** so all currently published advisories in this review are covered.
2. **Audit redirect behavior in transitive clients** such as `axios`, not just direct `follow-redirects` consumers.
3. **Treat custom authentication headers as sensitive** during cross-domain redirects; the newest published GHSA shows that stripping only standard auth headers was not sufficient.
4. **Be careful with legacy compatibility paths** around URL parsing, especially if your application accepts redirect targets or proxy-like destinations from untrusted input.
5. **Watch GitHub advisories as well as npm updates** because the package's public security trail is concentrated there.

## Dependencies of Note

- `follow-redirects` is a tiny package with limited internal complexity, but its real blast radius comes from reverse-transitive use across HTTP stacks and developer tooling.
- Consumers may never notice it directly in `package.json`, so lockfile and SBOM review matters here more than usual.

## Open Questions

- Which major downstream packages besides `axios` still pin older vulnerable `1.14.x` or `1.15.x` lines?
- Does upstream plan any broader policy for stripping or allowlisting custom sensitive headers across redirects beyond the current targeted fixes?
- Should the KB eventually group `follow-redirects`, `axios`, `requests`, and similar libraries under a shared redirect-credential-leak pattern note?

## Related Pages

- [[npm/axios]]
- [[python/requests]]
- [[python/urllib3]]
- [[npm/index]]

---
*Last updated: 2026-04-15 | Sources: 6 (OSV.dev package query for npm/follow-redirects, GitHub Advisory Database entries for the five published GHSA records, public CVE records for CVE-2022-0155 / CVE-2022-0536 / CVE-2023-26159 / CVE-2024-28849, upstream SECURITY.md, npm registry metadata, npm downloads API)*
