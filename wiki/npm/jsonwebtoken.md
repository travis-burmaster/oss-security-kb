# jsonwebtoken (npm)

**Registry:** npm
**Weekly Downloads:** ~14,000,000 (as of 2026-04-07)
**Repository:** https://github.com/auth0/node-jsonwebtoken
**Security Contact:** security@auth0.com
**Disclosure Policy:** https://auth0.com/responsible-disclosure-policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-11 | OpenClaw recurring review | package advisory history | manual | 4 public advisory records reviewed, including 3 package vulnerabilities fixed in 9.0.0 and 1 later-retracted claim that should not be treated as a valid library CVE | https://osv.dev/list?ecosystem=npm&q=jsonwebtoken |
| 2026-03-31 | travis-burmaster | `verify()` + `clockTolerance` option handling | manual | 1 bug found (filed) | [Issue #1021](https://github.com/auth0/node-jsonwebtoken/issues/1021) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2015-9235 / GHSA-c7hr-j4mj-j2w6 | Critical | Weak JWT algorithm validation allowed signature verification bypass when attackers could influence the token algorithm. | 4.2.2 | https://github.com/advisories/GHSA-c7hr-j4mj-j2w6 |
| CVE-2022-23539 / GHSA-8cf7-32gw-wr33 | High | Invalid asymmetric key type / algorithm combinations could be accepted, enabling insecure legacy key usage unless callers upgraded or explicitly opted into legacy behavior. | 9.0.0 | https://github.com/auth0/node-jsonwebtoken/security/advisories/GHSA-8cf7-32gw-wr33 |
| CVE-2022-23541 / GHSA-hjrf-2m68-5959 | Moderate | A poorly implemented key retrieval function could let applications verify forged tokens when they mixed symmetric and asymmetric verification through the same callback path. | 9.0.0 | https://github.com/auth0/node-jsonwebtoken/security/advisories/GHSA-hjrf-2m68-5959 |
| CVE-2022-23540 / GHSA-qwph-4952-7xr6 | Moderate | `jwt.verify()` could accept the `none` algorithm when no algorithms were specified and a falsy key/secret was supplied, producing signature-validation bypass in affected call patterns. | 9.0.0 | https://github.com/auth0/node-jsonwebtoken/security/advisories/GHSA-qwph-4952-7xr6 |
| CVE-2022-23529 / GHSA-27h2-hvpr-p74q | Rejected CVE | GitHub later clarified the reported RCE scenario depended on insecure calling code, and NVD marks CVE-2022-23529 as rejected. Track it as a cautionary ecosystem discussion, not a confirmed package vulnerability. | N/A | https://nvd.nist.gov/vuln/detail/CVE-2022-23529 |
| Issue #1021 | No assigned severity (public GitHub issue only; no CVE/GHSA issued as of 2026-04-27) | Reported behavior: `clockTolerance: Number.MAX_SAFE_INTEGER` can effectively disable expiration enforcement. This is a publicly filed issue, not a published advisory. | unfixed (as of 2026-04-07) | [auth0/node-jsonwebtoken#1021](https://github.com/auth0/node-jsonwebtoken/issues/1021) |

*Full CVE history: https://osv.dev/list?ecosystem=npm&q=jsonwebtoken*

## Security Posture Notes

- `jsonwebtoken` is a high-leverage authentication dependency, and its public advisory history clusters around verification semantics rather than parser memory safety: algorithm confusion, key-type validation, callback-driven key selection, and insecure defaults around unsigned tokens.
- The 9.0.0 release is the main security watershed for the package. Public release notes explicitly mention key validation work, algorithm/key-type checks for EC, RSA, and RSA-PSS, and the compatibility escape hatch `allowInvalidAsymmetricKeyTypes` for legacy deployments.
- The public record around CVE-2022-23529 is easy to misstate. GitHub's advisory now says the reported RCE scenario was not a library vulnerability after review, and NVD marks the CVE as rejected. That makes it useful context, but not something the KB should present as a confirmed package flaw on equal footing with the accepted advisories.
- Real-world exploitability still depends heavily on application design. Several advisories require callers to combine risky configuration choices, permissive algorithm handling, or weak key-selection callbacks.

## Dependencies of Note

- `jws` and `jwa` remain the most important adjacent packages because signing and verification behavior depends on the lower-level JOSE implementation stack.
- Application-level key retrieval callbacks are part of the practical threat surface even though they are not external package dependencies; future KB pages may need a pattern-focused note for callback-driven verification misuse.

## Open Questions

- Which currently popular packages or frameworks still bundle or document pre-9.x `jsonwebtoken` usage patterns?
- Is it worth separating package flaws from insecure integration patterns into different subsections so rejected or highly conditional claims stay easy to interpret?
- Are there additional public maintainer notes around migration from 8.x to 9.x that belong in a future hardening section?

## Related Pages

- [[npm/index]]
- [[npm/express]]

---
*Last updated: 2026-04-11 | Sources: 8 (OSV package query, GitHub Advisory Database, Auth0 GHSA advisory pages, 9.0.0 release notes, NVD rejected CVE record, public issue #1021)*
