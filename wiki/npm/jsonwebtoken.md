# jsonwebtoken (npm)

**Registry:** npm
**Weekly Downloads:** ~14,000,000 (as of 2026-04-07)
**Repository:** https://github.com/auth0/node-jsonwebtoken
**Security Contact:** security@auth0.com
**Disclosure Policy:** https://auth0.com/responsible-disclosure-policy

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2022-12-21 | Unit 42 (Palo Alto) | Full verify() logic | manual | 3 CVEs (CVE-2022-23529, -23539, -23540) | [Blog post](https://unit42.paloaltonetworks.com/jsonwebtoken-vulnerabilities/) |
| 2026-03-31 | travis-burmaster | `verify()` + `clockTolerance` option handling | manual | 1 bug found (filed) | [Issue #1021](https://github.com/auth0/node-jsonwebtoken/issues/1021) |

### Audit Notes (2022-12-21 — Unit 42)
Three vulnerabilities found in the `verify()` function, all fixed in v9.0.0:
- CVE-2022-23529: Remote code execution via malicious `secretOrPublicKey` passed as an object
- CVE-2022-23539: Weak key confusion — RS256 public key accepted for HS256 algorithm
- CVE-2022-23540: `none` algorithm accepted even when algorithm list specified

### Audit Notes (2026-03-31 — travis-burmaster)
Scope: the `clockTolerance` option in `verify()`. This option is intended to allow a small time window (e.g., 5 seconds) to account for clock skew between issuer and verifier. 

**Bug found:** Setting `clockTolerance: Number.MAX_SAFE_INTEGER` (9,007,199,254,740,991) bypasses the `exp` (expiration) claim verification entirely — expired tokens are accepted indefinitely. While a deliberately misconfigured value, the library performs no bounds checking or warning. Any application where user-controlled config flows into JWT verification options is potentially exposed.

This is a defense-in-depth / misconfiguration issue rather than a direct exploit, but represents a silent failure mode in security-critical code. Filed as Issue #1021.

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-23529 | Critical (9.8) | RCE via malicious secretOrPublicKey object | 9.0.0 | [Advisory](https://github.com/auth0/node-jsonwebtoken/security/advisories/GHSA-27h2-hvpr-p74q) |
| CVE-2022-23539 | Medium (6.8) | Weak key confusion (RS256 public key → HS256) | 9.0.0 | [Advisory](https://github.com/auth0/node-jsonwebtoken/security/advisories/GHSA-8cf7-32gw-wr33) |
| CVE-2022-23540 | Medium (6.4) | `none` algorithm accepted incorrectly | 9.0.0 | [Advisory](https://github.com/auth0/node-jsonwebtoken/security/advisories/GHSA-qwph-4952-7lwq) |
| Issue #1021 | Low–Medium (TBD) | `clockTolerance: MAX_SAFE_INTEGER` bypasses exp verification | unfixed (as of 2026-04-07) | [Issue #1021](https://github.com/auth0/node-jsonwebtoken/issues/1021) |

*Full CVE history: https://osv.dev/list?ecosystem=npm&q=jsonwebtoken*

## Security Posture Notes

Maintained by Auth0 (Okta). ~14M weekly downloads — extremely widely used for JWT signing/verification in Node.js applications. Has a formal security disclosure policy and dedicated security team at Auth0. Last major security overhaul in v9.0.0 (Dec 2022) following Unit 42 research.

**Note:** Many applications remain on v8.x despite the 2022 CVEs. The `npm audit` ecosystem flags these, but migration to v9 requires API changes.

## Dependencies of Note

- `jws` — JWT signing (check for algorithm confusion bugs)
- `jws` → `jwa` — HMAC/RSA/ECDSA implementations
- `ms` — time string parsing (has had ReDoS history; check version pinned)

## Related Pages

- [[npm/express-jwt]]
- [[npm/jose]]
- [[npm/passport-jwt]]

---
*Last updated: 2026-04-07 | Sources: 2 (Unit 42 blog 2022, GitHub Issue #1021 2026)*
