# jsonwebtoken (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~16.4M est. (49,320,753 / 90 days as of 2026-09-21)
**Repository:** https://github.com/Keats/jsonwebtoken
**Security Contact:** none listed (no SECURITY.md found in repository)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No formal third-party audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-25537 / GHSA-h395-gr6q-cpjc | Moderate (CVSS 4.0 AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:L/VA:N/SC:N/SI:N/SA:N) | JWT claim type confusion → authorization bypass — standard time-based claims (`nbf`, `exp`) that receive incorrect JSON types (e.g. a string instead of a number) are parsed as `FailedToParse`. The validation logic treats `FailedToParse` identically to `NotPresent`. Consequently, if validation of a claim is enabled (e.g. `validate_nbf = true`) but the claim is not explicitly marked as required, validation is skipped entirely for malformed claims. Attackers can exploit this by sending time-based claims as strings to bypass "Not Before" or expiration checks, potentially gaining unauthorized access or extending token validity indefinitely. Affects all versions ≤ 10.2.0; fixed in 10.3.0 (February 2026). | 10.3.0 | [GHSA-h395-gr6q-cpjc](https://github.com/advisories/GHSA-h395-gr6q-cpjc) |

## Security Posture Notes

jsonwebtoken is the dominant Rust JWT library, providing `encode`/`decode` functions with algorithm selection (HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384, PS256, PS384, PS512, EdDSA). It supports `aws_lc_rs` and `rust_crypto` backends.

**Claim validation gap (CVE-2026-25537):** The validated claim parsing model has a subtle API design risk: callers who enable validation for a claim but do not set that claim as required will silently receive no validation if the claim arrives in a non-number JSON type. This is an authorization bypass risk for applications that rely on `validate_nbf` or expiration checks against externally supplied tokens. The fix in 10.3.0 ensures `FailedToParse` is treated as a hard validation failure when that claim's validation is enabled.

**ES512 limitation (downstream, not a jsonwebtoken CVE):** SurrealDB filed CVE-2026-63761 / GHSA-fwg2-gr34-q3w8 against itself (not against jsonwebtoken) documenting that jsonwebtoken 10.x does not implement ES512 (P-521) — the library silently downgrades `ES512` configurations to `ES384`. This is a limitation of the library's algorithm support, not a security vulnerability in jsonwebtoken itself. Callers requiring genuine ES512 signatures should be aware this is not supported in the 10.x line; jsonwebtoken 11.x added P-521 support via the `aws_lc_rs` backend.

Total crates.io downloads: ~192.6M; current stable: 11.1.0.

## Dependencies of Note

- `aws_lc_rs` or `ring` / `rust_crypto` — cryptographic backends; see [[rust/ring]] for ring's advisory history.

## Open Questions

- Confirm whether jsonwebtoken 11.x (ES512 via aws_lc_rs) has a SECURITY.md or responsible-disclosure contact.
- Check for any RustSec advisories filed against jsonwebtoken post-10.3.0 (none found in this pass).
- Evaluate whether the `FailedToParse == NotPresent` design pattern affects any other claim types beyond `nbf`/`exp`.

## Related Pages

- [[rust/ring]]
- [[rust/rustls]]
- [[rust/index]]

---
*Last updated: 2026-09-21 | Sources: 1 direct GHSA advisory (github/advisory-database); 2 downstream SurrealDB GHSA entries excluded*
