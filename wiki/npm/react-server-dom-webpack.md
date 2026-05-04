# react-server-dom-webpack (npm)

**Registry:** npm
**Weekly Downloads:** ~799,789 (2026-04-27 through 2026-05-03)
**Repository:** https://github.com/facebook/react
**Security Contact:** Meta / React GitHub Security Advisories
**Disclosure Policy:** https://github.com/facebook/react/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-04 | OpenClaw recurring review | new package page | public-source curation (OSV.dev package query, GitHub Advisory Database records, public CVE / NVD aliases, React security advisories, and React release / disclosure blog references) | Added a dedicated React Server Components package page covering the six currently published `react-server-dom-webpack` advisories across RCE, source-code exposure, and repeated DoS fix trains through 19.0.5 / 19.1.6 / 19.2.5. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-55182 / GHSA-fv66-9v8q-g76r | Critical | React Server Components unauthenticated remote-code-execution advisory affecting `react-server-dom-webpack`, `react-server-dom-parcel`, and `react-server-dom-turbopack` release lines. | 19.0.1, 19.1.2, 19.2.1 | [GHSA](https://github.com/advisories/GHSA-fv66-9v8q-g76r), [OSV.dev](https://osv.dev/vulnerability/GHSA-fv66-9v8q-g76r), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-55182), [React release refs](https://github.com/facebook/react/security/advisories/GHSA-fv66-9v8q-g76r) |
| CVE-2025-55183 / GHSA-925w-6v3x-g4j4 | Moderate | Source-code exposure vulnerability in React Server Components affecting the webpack, parcel, and turbopack server-dom packages. | 19.0.2, 19.1.3, 19.2.2 | [GHSA](https://github.com/advisories/GHSA-925w-6v3x-g4j4), [OSV.dev](https://osv.dev/vulnerability/GHSA-925w-6v3x-g4j4), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-55183), [React disclosure blog](https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components) |
| CVE-2025-55184 / GHSA-2m3v-v2m8-q956 | High | Denial-of-service vulnerability in React Server Components affecting the same server-dom package family. | 19.0.2, 19.1.3, 19.2.2 | [GHSA](https://github.com/advisories/GHSA-2m3v-v2m8-q956), [OSV.dev](https://osv.dev/vulnerability/GHSA-2m3v-v2m8-q956), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-55184), [React disclosure blog](https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components) |
| CVE-2025-67779 / GHSA-7gmr-mq3h-m5h9 | High | Follow-up denial-of-service advisory after the public record described the CVE-2025-55184 fix as incomplete in a specific case. | 19.0.3, 19.1.4, 19.2.3 | [GHSA](https://github.com/advisories/GHSA-7gmr-mq3h-m5h9), [OSV.dev](https://osv.dev/vulnerability/GHSA-7gmr-mq3h-m5h9), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-67779) |
| CVE-2026-23864 / GHSA-83fc-fqcc-2hmg | High | Multiple denial-of-service vulnerabilities remained after earlier RSC DoS fixes, according to the React advisory. | 19.0.4, 19.1.5, 19.2.4 | [GHSA](https://github.com/advisories/GHSA-83fc-fqcc-2hmg), [OSV.dev](https://osv.dev/vulnerability/GHSA-83fc-fqcc-2hmg), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-23864), [React disclosure blog](https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components) |
| CVE-2026-23869 / GHSA-479c-33wc-g2pg | High | Denial-of-service vulnerability triggered by specially crafted requests to Server Function endpoints in affected React Server Components versions. | 19.0.5, 19.1.6, 19.2.5 | [GHSA](https://github.com/advisories/GHSA-479c-33wc-g2pg), [OSV.dev](https://osv.dev/vulnerability/GHSA-479c-33wc-g2pg), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-23869), [Next.js related GHSA](https://github.com/advisories/GHSA-q4gf-8mx6-v5v3) |

## Security Posture Notes

- This page is intentionally separate from [[npm/react]]: the public advisories are package-scoped to the React Server Components transport / server-dom package family, not the legacy core `react` XSS records tracked on the core page.
- The safest version floor across the published 19.x RSC advisory train is `19.0.5`, `19.1.6`, or `19.2.5`, depending on the consumer's selected React release line.
- The same public advisory records repeatedly name sibling packages `react-server-dom-parcel` and `react-server-dom-turbopack`; this page tracks only the webpack package and should be cross-linked if sibling pages are added later.
- The Next.js page already tracks `GHSA-q4gf-8mx6-v5v3` / `CVE-2026-23869` as a framework-level downstream advisory tied to the upstream RSC issue; keep framework exposure notes separate from package-level React records.
- This KB entry avoids exploit steps or proof-of-concept material and records only public advisory, CVE, release, and maintainer disclosure evidence.

## Dependencies of Note

- `react` / `react-dom` release alignment matters operationally, but the public advisories here are scoped to `react-server-dom-webpack` and sibling server-dom packages.

## Open Questions

- Should sibling package pages be created for `react-server-dom-parcel` and `react-server-dom-turbopack`, or should their shared advisory history remain referenced from this webpack-focused page?
- Should the broader `react-dom` package receive a small separate page for its legacy `CVE-2018-6341` XSS advisory, or is the React Server Components cluster the higher-value React ecosystem gap for now?
- Next.js has a much larger direct package-level OSV surface than its current compact page captures; a future dedicated normalization pass should reconcile those records instead of forcing a partial update here.

## Related Pages

- [[npm/react]]
- [[npm/next]]
- [[npm/index]]

---
*Last updated: 2026-05-04 | Sources: 20 (OSV.dev package query and six vulnerability records, GitHub Advisory Database / React Security Advisory records, public CVE / NVD aliases for CVE-2025-55182, CVE-2025-55183, CVE-2025-55184, CVE-2025-67779, CVE-2026-23864, and CVE-2026-23869, React RSC disclosure blog, npm downloads API, and related Next.js GHSA-q4gf-8mx6-v5v3)*
