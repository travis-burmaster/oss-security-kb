# github.com/golang-jwt/jwt (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-05-10)
**Repository:** https://github.com/golang-jwt/jwt
**Security Contact:** GitHub private vulnerability reporting / security advisory workflow
**Disclosure Policy:** https://github.com/golang-jwt/jwt/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-10 | OpenClaw recurring review | package advisory normalization across `github.com/golang-jwt/jwt`, `/v4`, and `/v5` module paths | public-source curation (OSV package and vulnerability records, GitHub Advisory Database records, Go vulnerability database, public CVE records, upstream release notes / version history, upstream security policy, fix commits, local proxy draft assist) | Added a new advisory-mapped page after normalizing the v4-only `ParseWithClaims` error-handling advisory and the cross-version `ParseUnverified` allocation-amplification DoS advisory. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-51744 / GHSA-29wx-vh33-7x7r / GO-2024-3250 | Medium | In `github.com/golang-jwt/jwt/v4`, unclear `ParseWithClaims` error behavior could lead callers to accept an invalid-signature token if they only checked for a less-dangerous combined validation error such as expiration. The v4.5.1 fix backported the v5 behavior so parsing returns immediately on dangerous errors such as invalid signatures. | 4.5.1 for `/v4`; `/v5` already had the corrected behavior | https://github.com/advisories/GHSA-29wx-vh33-7x7r |
| CVE-2025-30204 / GHSA-mh63-6h87-95cp / GO-2025-3553 | High | `Parser.ParseUnverified` split attacker-controlled token input on every period, so a token with many period characters could force excessive memory allocation and denial of service. Public records mark the affected paths as `/v5` from 5.0.0-rc.1 before 5.2.2, `/v4` before 4.5.2, and the unversioned v3 path from 3.2.0 through 3.2.2 with no v3 fix published. | 5.2.2 for `/v5`; 4.5.2 for `/v4`; no fixed v3 release listed | https://github.com/advisories/GHSA-mh63-6h87-95cp |

*Full CVE history: https://osv.dev/list?ecosystem=Go&q=github.com/golang-jwt/jwt*

## Security Posture Notes

- The package spans three Go module paths in public advisory data: the unversioned `github.com/golang-jwt/jwt` v3 line, `github.com/golang-jwt/jwt/v4`, and `github.com/golang-jwt/jwt/v5`. Consumers need to check the actual import path, not only the repository name.
- The current security policy says the latest `v5` line is supported, with `v4` backports possible only in critical cases. That makes `v5` the preferred target for new remediation work even though the two normalized advisories in this pass also have v4 backports.
- `CVE-2024-51744` is a JWT validation-boundary issue rather than a parser crash: it depends on application error handling around combined errors. The public advisory's workaround is to audit error checks carefully, especially where code tests only for `ErrTokenExpired` and ignores signature-invalid errors.
- `CVE-2025-30204` is a resource-exhaustion issue on untrusted token strings. Public Go vulnerability data identifies `Parser.ParseUnverified` as the affected symbol for `/v4` and `/v5`, while the GitHub advisory also records the unfixed v3 range.
- The upstream release evidence aligns with the advisory fixed versions: `v4.5.1` was published with a security note for the `ParseWithClaims` behavior, and `v4.5.2` / `v5.2.2` were published on 2025-03-21 for `GHSA-mh63-6h87-95cp`.
- The fork's historical version notes say `3.2.1` fixed the earlier `CVE-2020-26160` `VerifyAudience` string-vs-`[]string` issue from the jwt-go lineage. This pass kept that as lineage context rather than a separate current golang-jwt advisory row because the normalized OSV/GHSA records gathered for this package focus on the 2024 and 2025 advisories above.
- Repository metadata gathered in this pass showed active maintenance signals: public repository `golang-jwt/jwt`, default branch `main`, last pushed 2026-05-01, and latest release `v5.3.1` published 2026-01-28.

## Dependencies of Note

- JWT parser and validation behavior is usually on an authentication / authorization boundary, so downstream impact is highly dependent on how services handle parse errors, token expiration, key selection, and accepted algorithms.
- Services that use `ParseUnverified` as part of pre-validation routing, key discovery, or logging should treat untrusted token size and structure as part of their DoS threat model.
- The unversioned v3 import path is especially important for transitive inventory because public data lists no fixed v3 release for `CVE-2025-30204`.

## Open Questions

- Are there still widely used downstream projects pinned to the unversioned v3 module path despite the security policy's focus on v5 and critical-only v4 backports?
- Do any public framework integrations call `ParseUnverified` on request headers before enforcing request-size or header-size limits?
- Should future KB work split Go JWT libraries into a comparison page covering `golang-jwt/jwt`, `lestrrat-go/jwx`, and `go-jose` advisory histories?

## Related Pages

- [[go/golang.org-x-crypto]]
- [[go/index]]

---
*Last updated: 2026-05-10 | Sources: 17 (OSV package queries for Go/github.com/golang-jwt/jwt, /v4, and /v5; normalized OSV vulnerability records for GHSA-29wx-vh33-7x7r, GO-2024-3250, GHSA-mh63-6h87-95cp, and GO-2025-3553; GitHub Advisory Database entries; Go vulnerability database pages; public CVE records for CVE-2024-51744 and CVE-2025-30204; upstream releases v4.5.1, v4.5.2, v5.2.2, and v5.3.1; upstream SECURITY.md; upstream VERSION_HISTORY.md; upstream fix commits 7b1c1c0 and 0951d18; public repository metadata; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid)*
