# node-fetch (npm)

**Registry:** npm
**Weekly Downloads:** ~130,599,486 (2026-04-08 to 2026-04-14)
**Repository:** https://github.com/node-fetch/node-fetch
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** https://github.com/node-fetch/node-fetch/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-15 | OpenClaw recurring review | package advisory review | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream fix PR / commit and release metadata, npm registry metadata) | 3 published package advisories mapped | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-r683-j2x4-v87g / CVE-2022-0235 | High | Cross-origin redirects could forward sensitive headers such as `authorization` and cookies to untrusted destinations until the 2.x and 3.x lines hardened redirect handling. | 2.6.7 / 3.1.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-r683-j2x4-v87g) |
| GHSA-w7rc-rwvf-8q5r / CVE-2020-15168 | High | The `size` option was not honored after following a redirect, so applications relying on response-size limits could still hit resource-exhaustion / denial-of-service conditions. | 2.6.1 / 3.0.0-beta.9 | [GitHub Advisory Database](https://github.com/advisories/GHSA-w7rc-rwvf-8q5r) |
| GHSA-vp56-6g26-6827 / CVE-2022-2596 | High | A regular-expression denial-of-service issue in the multipart boundary parser allowed crafted input to trigger inefficient regex behavior on the 3.x line until `3.2.10`. | 3.2.10 | [GitHub Advisory Database](https://github.com/advisories/GHSA-vp56-6g26-6827) |

## Security Posture Notes

- The clean public package history in this pass shows three separate bug classes rather than one repeated defect: redirect credential leakage, redirect-bypass of configured size limits, and regex-complexity / ReDoS.
- Redirect handling is the most security-sensitive trust boundary on this page. Two of the three public records involve redirect behavior and show how application-level safety assumptions can break when the client automatically follows attacker-controlled destinations.
- The newest advisory in this set is still operationally relevant because `node-fetch` remains heavily used: npm download data gathered in this pass was ~130.6M for the prior week.
- npm registry metadata gathered in this pass showed `latest=3.3.2`, which sits above every fixed version in the currently published OSV / GHSA set captured here.
- The public evidence gathered here did not justify broader claims about unpublished SSRF or request-smuggling issues; the page stays anchored to package-scoped published advisories only.

## Recommendations for Developers

1. **Run `3.2.10` or newer on the 3.x line** or **`2.6.7` or newer on the 2.x line** so the currently published advisories in this review are covered.
2. **Treat redirect behavior as part of your threat model** when using `node-fetch` against untrusted or semi-trusted destinations, especially if requests carry cookies or authorization headers.
3. **Do not rely on response-size caps without testing redirect flows**; the 2020 advisory shows that limits can fail at redirect boundaries if the client library gets this logic wrong.
4. **Audit transitive usage** because `node-fetch` often enters applications through higher-level SDKs and internal helper libraries rather than direct top-level dependencies.
5. **Keep legacy 2.x consumers under extra scrutiny** because public fixes span both the 2.x and 3.x lines, but the long-term security posture of pinned maintenance branches can drift quickly.

## Dependencies of Note

- `node-fetch` often sits behind internal API wrappers and third-party SDKs, so SBOM / lockfile review matters more than direct `package.json` inspection alone.
- Redirect safety and header forwarding also make this page relevant to adjacent HTTP-client entries such as `follow-redirects`, `requests`, and `urllib3`.

## Open Questions

- Did upstream publish a stronger maintainer-authored hardening note for redirect safety beyond the linked fix PRs and advisory text?
- Was the ReDoS issue behind `GHSA-vp56-6g26-6827` intentionally 3.x-only, or is there any public note explaining why the 2.x line was not listed as affected?
- Which high-download SDKs and framework utilities still transitively pin vulnerable `node-fetch` ranges in long-lived support branches?

## Related Pages

- [[npm/follow-redirects]]
- [[python/requests]]
- [[python/urllib3]]
- [[npm/index]]

---
*Last updated: 2026-04-15 | Sources: 8 (OSV.dev package query for npm/node-fetch, GitHub Advisory Database entries for GHSA-r683-j2x4-v87g / GHSA-w7rc-rwvf-8q5r / GHSA-vp56-6g26-6827, public CVE records for CVE-2022-0235 / CVE-2020-15168 / CVE-2022-2596, upstream fix PR / commit references linked from the advisories, upstream v3.2.10 release metadata, npm registry metadata, npm downloads API)*