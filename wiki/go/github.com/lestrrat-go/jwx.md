# lestrrat-go/jwx (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-08-14); 2,414 GitHub stars; v2 module listed on pkg.go.dev with importers in hundreds of projects
**Repository:** https://github.com/lestrrat-go/jwx
**Security Contact:** GitHub private vulnerability reporting (https://github.com/lestrrat-go/jwx/security/advisories)
**Disclosure Policy:** https://go.dev/security/policy (Go vulnerability database)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-08-14 | OSS Security KB | GHSA database lookup across v1/v2 module lineage | automated | 4 public advisory rows mapped (GHSA-rm8v through GHSA-hj3v) | [github/advisory-database](https://github.com/github/advisory-database) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-rm8v-mxj3-5rmq (no CVE) | Moderate | AES-CBC JWE padding oracle / timing attack: `jwe.Decrypt` with AES-CBC encryption returns a distinguishable error message ("failed to generate plaintext from decrypted blocks: invalid padding") and performs non-constant-time padding removal, violating RFC 7516 §11.5 requirements. The authentication tag is verified first, so this is not an immediately exploitable oracle in most deployments, but the error distinction may leak plaintext length under network timing conditions. Affects `github.com/lestrrat-go/jwx/v2` ≤ 2.0.10 and `github.com/lestrrat-go/jwx` ≤ 1.2.25. | v2.0.11 / v1.2.26 | [GHSA-rm8v-mxj3-5rmq](https://github.com/advisories/GHSA-rm8v-mxj3-5rmq) |
| CVE-2023-49290 / GHSA-7f9x-gw85-8grf | Moderate (CVSS 5.3 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L) | PBES2 JWE p2c parameter CPU exhaustion DoS: JWE key management algorithms based on PBKDF2 (`PBES2-HS256+A128KW`, etc.) use the `p2c` header parameter to control iteration count. An unauthenticated attacker can send a JWE with an arbitrarily large `p2c` value (e.g. 2,000,000,000), causing the decrypting party to expend unbounded CPU time on key derivation and resulting in a denial-of-service condition. Affects both v1 and v2 module lines. | v2.0.18 / v1.2.27 | [GHSA-7f9x-gw85-8grf](https://github.com/advisories/GHSA-7f9x-gw85-8grf) |
| CVE-2024-21664 / GHSA-pvcr-v8j8-j5q3 | Moderate (AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L) | JWS Parse nil pointer dereference DoS: `jws.Parse()` and `jws.Verify()` panic with a nil pointer dereference when processing a JSON-serialized JWS payload that contains a `signature` field but is missing the `protected` field. The code in `jws/message.go:UnmarshalJSON()` assumes both fields are present; feeding it `{"signature": ""}` causes a nil dereference in `getB64Value(sig.protected)`. Any system performing JWS verification on user-supplied input is vulnerable. | v2.0.19 / v1.2.28 | [GHSA-pvcr-v8j8-j5q3](https://github.com/advisories/GHSA-pvcr-v8j8-j5q3) |
| CVE-2024-28122 / GHSA-hj3v-m684-v259 | Moderate (CVSS 7.5 AV:N/AC:L/PR:H/UI:N/S:C/C:N/I:N/A:H) | JWE decompression bomb (data amplification) DoS: `jwe.Decrypt` will decompress the JWE payload if the algorithm is configured to use compression. An attacker with a trusted public key (PR:H) can craft a JWE token with a very high compression ratio, causing the decrypting party to allocate excessive memory and consume significant CPU time during decompression, effectively denying service. Affects `github.com/lestrrat-go/jwx/v2` ≤ 2.0.20 and `github.com/lestrrat-go/jwx` ≤ 1.2.28. | v2.0.21 / v1.2.29 | [GHSA-hj3v-m684-v259](https://github.com/advisories/GHSA-hj3v-m684-v259) |

*OSV live record: https://osv.dev/list?ecosystem=Go&q=github.com%2Flestrrat-go%2Fjwx*

## Security Posture Notes

`github.com/lestrrat-go/jwx` is a complete Go implementation of the JOSE (JSON Object Signing and Encryption) standard family — JWT (RFC 7519), JWS (RFC 7515/7797), JWE (RFC 7516), JWK (RFC 7517/7638), and JWA (RFC 7518). The library is maintained by @lestrrat under the `lestrrat-go` GitHub organization.

**Version history and current stable lines:**
- `github.com/lestrrat-go/jwx` — v1.x line; latest patched v1 is ≥ 1.2.29
- `github.com/lestrrat-go/jwx/v2` — v2.x line; latest stable v2.1.7 (current as of pkg.go.dev); all 4 advisories patched as of v2.0.21
- `github.com/lestrrat-go/jwx/v3` — v3.x line; new major version released in 2025/2026
- `github.com/lestrrat-go/jwx/v4` — v4.x in active development (default branch `develop/v4` as of 2026-08-14)

The repository has 2,414 GitHub stars and 0 open issues as of 2026-08-14, indicating active maintenance. GitHub private vulnerability reporting is enabled.

**Recurring security pattern — JWE decryption path:** Three of the four advisories exploit the JWE decryption code path: the padding oracle (GHSA-rm8v), the p2c DoS (GHSA-7f9x), and the decompression bomb (GHSA-hj3v). This pattern parallels issues seen in `go-jose/go-jose` (GHSA-2c7c and GHSA-c5q2), suggesting that JWE decryption of untrusted tokens is the highest-risk surface in JOSE libraries generally. Callers that do not use JWE can reduce exposure by restricting accepted key algorithms.

**Migration guidance:** Projects currently on v1 or v2 should ensure they are on v1.2.29+ or v2.0.21+ to have all four advisories resolved. Migration to v3 or v4 is recommended for long-term support; note that v3/v4 have breaking API changes relative to v2.

**No advisories confirmed on v3/v4:** The four GHSA advisories in this pass all list v1 and v2 as affected. The github/advisory-database search returned exactly 4 records for `lestrrat-go/jwx`; no additional advisories were found for v3 or v4.

## Dependencies of Note

lestrrat-go/jwx has a small set of Go standard library dependencies plus `github.com/lestrrat-go/httprc` for JWK auto-refresh. No known CVEs in direct dependencies flagged.

## Open Questions

- Confirm whether v3 and v4 module lines are entirely unaffected by the four mapped advisories, or whether similar code paths exist and have been separately addressed without formal GHSA disclosure.
- Assess whether JWK key caching (`jwk.Cache`) introduces any TOCTOU or cache-poisoning attack surface.
- Check whether the padding oracle fix (GHSA-rm8v) uses constant-time comparison throughout the AES-CBC path — the advisory notes authentication is verified first, but the timing leak in padding removal should be independently verified in the fix commit.

## Related Pages

- [[go/github.com/go-jose/go-jose]]
- [[go/github.com/golang-jwt/jwt]]
- [[go/golang.org-x-crypto]]
- [[go/index]]

---
*Last updated: 2026-08-14 | Sources: 4 (github/advisory-database: 4 GHSA records; pkg.go.dev; github.com/lestrrat-go/jwx)*
