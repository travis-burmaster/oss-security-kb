# react-router (npm)

**Registry:** npm
**Weekly Downloads:** ~53,827,272 (last week, fetched 2026-04-23)
**Repository:** https://github.com/remix-run/react-router
**Security Contact:** GitHub Security Advisory "Report a Vulnerability" flow; hosting-provider contact also noted at hello@remix.run
**Disclosure Policy:** https://github.com/remix-run/react-router/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-23 | OpenClaw recurring review | package advisory normalization | public-source curation (GitHub Advisory Database / public GHSA pages, OSV.dev records, public CVE records, upstream SECURITY.md, upstream release notes / changelog, npm registry metadata, npm downloads API) | Added a dedicated package page covering seven published package advisories across the 6.x and 7.x lines, with mode scoping preserved so Framework/Data/Declarative differences are not flattened into misleading package-wide claims. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive full-source audit on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-43864 / GHSA-f46r-rw29-r322 | High | Framework Mode cache-poisoning / availability issue: attacker-controlled `X-React-Router-SPA-Mode` header could force SPA handling on SSR routes that use loaders, producing an error response that can become a cached DoS outcome. | 7.5.2 | https://github.com/advisories/GHSA-f46r-rw29-r322 |
| CVE-2025-43865 / GHSA-cpj6-fhp6-mr6j | High | Framework Mode prerender-data spoofing / cache-poisoning issue: attacker-controlled `X-React-Router-Prerender-Data` could overwrite prerendered loader data and potentially enable poisoned content or downstream stored-XSS-style outcomes if cached. | 7.5.2 | https://github.com/advisories/GHSA-cpj6-fhp6-mr6j |
| CVE-2025-59057 / GHSA-3cgp-3xvw-98x8 | High | SSR XSS in `meta()` / `<Meta>` when generating `script:ld+json` tags from untrusted content in Framework Mode; the advisory explicitly says Declarative and Data Mode are not affected. | 7.9.0 | https://github.com/advisories/GHSA-3cgp-3xvw-98x8 |
| CVE-2025-68470 / GHSA-9jcx-v3wj-wh4m | Moderate | Unexpected external redirect via untrusted paths passed to `navigate()`, `<Link>`, or `redirect()`; this one spans both supported major lines rather than only 7.x framework-only surfaces. | 6.30.2 / 7.9.6 | https://github.com/advisories/GHSA-9jcx-v3wj-wh4m |
| CVE-2026-21884 / GHSA-8v8x-cx79-35w7 | High | SSR XSS in `<ScrollRestoration>` when `getKey` / `storageKey` values are generated from untrusted content in Framework Mode SSR. | 7.12.0 | https://github.com/advisories/GHSA-8v8x-cx79-35w7 |
| CVE-2026-22029 / GHSA-2w69-qvjg-hvjx | High | Unsafe SPA open-navigation redirects from loaders/actions can produce unsafe URLs and client-side JavaScript execution; advisory scope includes Framework Mode, Data Mode, and unstable RSC modes, but not Declarative Mode. | 7.12.0 | https://github.com/advisories/GHSA-2w69-qvjg-hvjx |
| CVE-2026-22030 / GHSA-h5cw-625j-3rxh | Moderate | CSRF on document POST requests to UI routes when using server-side `action` handlers in Framework Mode or unstable RSC modes; advisory explicitly excludes Declarative and Data Mode. | 7.12.0 | https://github.com/advisories/GHSA-h5cw-625j-3rxh |

## Security Posture Notes

- Public advisory history is **mode-sensitive rather than uniform**: six currently published package advisories are concentrated in 7.x Framework Mode / SSR / unstable-RSC surfaces, while the untrusted-path external redirect issue (`GHSA-9jcx-v3wj-wh4m`) is the one clearly spanning both 6.x and 7.x lines.
- The upstream project publishes a meaningful security policy in `SECURITY.md`, explicitly marks both **6.x and 7.x** as supported for security updates, and routes vulnerability reports through GitHub Security Advisories rather than a vague issue-tracker process.
- Upstream release notes provide a clean public fix trail: `v7.5.2` says it fixed **two** cache-poisoning issues tied to build-time SPA / prerender headers; `v7.9.0` calls out the `meta()` / JSON-LD XSS fix; `v7.9.6` and `v6.30.2` both call out the untrusted-path redirect fix; and `v7.12.0` explicitly groups the later CSRF + open-redirect/XSS + `ScrollRestoration` XSS fixes.
- Current public package metadata shows `react-router` at `7.14.2`, beyond the latest published security fix point (`7.12.0`), while the security policy still says the maintained 6.x line also receives security updates.
- Because several advisories are framed as "only exploitable if developers pass untrusted content into routing / redirect / SSR metadata paths," this package should be read as a **security-boundary library** where misuse of framework features materially affects exploitability.
- No public proactive full-source audit was identified in this pass; current evidence is advisory- and release-driven rather than audit-report-driven.

## Dependencies of Note

- `@remix-run/router` appears directly in at least one published advisory chain (`GHSA-2w69-qvjg-hvjx`) as a separately affected package, so downstream triage should not assume the entire risk picture is isolated to the top-level `react-router` package name.
- Several advisories specifically concern Framework Mode server-runtime behavior, so deployments using broader Remix / server-runtime packages may need coordinated upgrades rather than a narrow client-package bump.

## Open Questions

- Has anyone published a dedicated full-source security review of the React Router 7 server/runtime surfaces beyond the individual advisory disclosures?
- Which widely deployed Framework Mode patterns still leave applications exposed even after upgrading, especially around untrusted redirect targets and SSR metadata generation?
- Should related packages such as `@remix-run/router` or other server-runtime components receive separate KB pages to avoid flattening package-boundary details into this page?

## Related Pages

- [[npm/index]]
- [[npm/next-intl]]
- [[npm/express]]

---
*Last updated: 2026-04-23 | Sources: 14 (GitHub Advisory Database / public GHSA pages, OSV.dev vulnerability records, public CVE records, upstream SECURITY.md, upstream changelog / release notes for v7.5.2, v7.9.0, v7.9.6, v6.30.2, and v7.12.0, npm registry metadata, npm downloads API, plus a successful local proxy drafting pass used only as a synthesis aid)*
