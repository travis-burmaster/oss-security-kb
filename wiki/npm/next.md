# next (npm)

**Registry:** npm
**Weekly Downloads:** (not captured in this pass)
**Repository:** https://github.com/vercel/next.js
**Security Contact:** GitHub Security Advisories (upstream)
**Disclosure Policy:** upstream GitHub Security policy/advisory flow
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-27 | OpenClaw recurring review | new package page | public-source curation (GitHub Advisory Database pages, upstream public GitHub security advisory, maintainer/public changelog link referenced by GHSA) | Added Next.js DoS advisory (GHSA-q4gf-8mx6-v5v3) tied to upstream React Server Components issue (CVE-2026-23869). | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-q4gf-8mx6-v5v3 / CVE-2026-23869 | High | A specially crafted HTTP request sent to an App Router **Server Function endpoint** may trigger excessive CPU usage during deserialization, resulting in a denial of service in unpatched environments. The advisory notes this tracks upstream React issue GHSA-479c-33wc-g2pg (CVE-2026-23869). | 15.5.15 (for 13.x–15.x line); 16.2.3 (for 16.x beta line) | [GitHub Advisory Database](https://github.com/advisories/GHSA-q4gf-8mx6-v5v3) |

## Security Posture Notes

- This Next.js advisory is explicitly described as tied to an upstream React Server Components vulnerability (CVE-2026-23869).
- Exposure requires usage of the App Router and an affected Server Function endpoint, per the GHSA description.

## Related Pages

- [[npm/react]] (core React library page; does not currently track the server-DOM packages)
- [[npm/index]]

---
*Last updated: 2026-04-27 | Sources: 1 (GitHub Advisory Database GHSA-q4gf-8mx6-v5v3, including references it links to)*
