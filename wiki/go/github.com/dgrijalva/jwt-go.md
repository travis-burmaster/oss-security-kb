# dgrijalva/jwt-go (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (archived; 29,217 packages import as of 2026-08-19)
**Repository:** https://github.com/dgrijalva/jwt-go
**Security Contact:** none listed (repository archived)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-26160 / GHSA-w73w-5m7g-f7qc / GO-2020-0017 | High (CVSS 3.1: 7.5 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N; CWE-287, CWE-755) | Audience (`aud`) claim bypass: when the token's `aud` field is a JSON array, `MapClaims`'s type assertion to `string` fails silently and the resulting value is `""`. Any service that relies on `VerifyAudience` alone to enforce a non-empty audience restriction can be bypassed by presenting a token with `"aud": []`. | No fix — package archived with no patch available. Migrate to github.com/golang-jwt/jwt ≥ 3.2.1 | [GHSA-w73w-5m7g-f7qc](https://github.com/advisories/GHSA-w73w-5m7g-f7qc) / [GO-2020-0017](https://pkg.go.dev/vuln/GO-2020-0017) |

## Security Posture Notes

`github.com/dgrijalva/jwt-go` is an **archived, unmaintained** JWT library. The repository was archived after the maintainer transferred active development to [golang-jwt/jwt](https://github.com/golang-jwt/jwt). No security patches will be released; the only remediation is migration.

CVE-2020-26160 is a design-level flaw in audience validation. The JWT specification allows `aud` to be either a JSON string or a JSON array of strings. The library's `MapClaims.VerifyAudience` performs a single type assertion to `string`; when the token contains an array (`[]string{}`), the assertion fails silently and the effective audience collapses to `""`. A service that calls `VerifyAudience(requiredAud, true)` but relies on jwt-go's result without its own secondary check is susceptible to an attacker-controlled token that specifies `"aud": []` — the empty-string audience passes `required == ""` comparisons.

Despite being archived, the package retains **29,217 direct importers** on pkg.go.dev (as of 2026-08-19), giving it very broad ecosystem exposure. The successor `github.com/golang-jwt/jwt` (already covered at `[[go/github.com/golang-jwt/jwt]]`) v4 and v5 address this and other issues.

## Dependencies of Note

None flagged (minimal dependency surface).

## Open Questions

- What fraction of the 29,217 importers have migrated to golang-jwt/jwt? No aggregate migration-tracking data found in this pass.
- Are there major infrastructure projects (CI runners, cloud SDKs, Kubernetes controllers) still pinned to dgrijalva/jwt-go that have not issued a migration?

## Related Pages

- [[go/github.com/golang-jwt/jwt]] — successor library; covers v4 ParseWithClaims error-handling boundary and ParseUnverified memory-allocation DoS history
- [[go/github.com/go-jose/go-jose]] — JOSE/JWE/JWS/JWT implementation (successor to square/go-jose)
- [[go/index]]

---
*Last updated: 2026-08-19 | Sources: 2 (GHSA-w73w-5m7g-f7qc, GO-2020-0017)*
