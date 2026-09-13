# github.com/lestrrat-go/jwx (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-09-13)
**Repository:** https://github.com/lestrrat-go/jwx
**Security Contact:** https://github.com/lestrrat-go/jwx/security (GitHub security advisories)
**Disclosure Policy:** https://github.com/lestrrat-go/jwx/security/policy
**Current Status:** advisory-mapped

## Audit History

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|
| GHSA-rm8v-mxj3-5rmq | Moderate | AES-CBC JWE decryption padding oracle: code returns distinguishable error messages for padding failures and executes non-constant-time padding removal in violation of RFC 7516 §11.5; enables timing side-channel attacks against ciphertext recovery | v1 ≥ 1.2.26 / v2 ≥ 2.0.11 | [GHSA-rm8v-mxj3-5rmq](https://github.com/advisories/GHSA-rm8v-mxj3-5rmq) |
| GHSA-7f9x-gw85-8grf / CVE-2023-49290 | Moderate (CVSS 5.3 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L) | JWE PBKDF2 `p2c` iteration-count DoS: attacker-controlled JWE token with an excessively large `p2c` value forces the server to perform unbounded PBKDF2 iterations → CPU exhaustion; the `p2c` parameter was not validated | v1 ≥ 1.2.27 / v2 ≥ 2.0.18 | [GHSA-7f9x-gw85-8grf](https://github.com/advisories/GHSA-7f9x-gw85-8grf) |
| GHSA-pvcr-v8j8-j5q3 / CVE-2024-21664 | Moderate (CVSS 7.5 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) | Nil-pointer dereference DoS in `jws.Parse()`: JSON-serialized JWS payload with a `signature` field but no `protected` field causes segmentation fault; also reachable indirectly via `jws.Verify()` | v1 ≥ 1.2.28 / v2 ≥ 2.0.19 | [GHSA-pvcr-v8j8-j5q3](https://github.com/advisories/GHSA-pvcr-v8j8-j5q3) |
| GHSA-hj3v-m684-v259 / CVE-2024-28122 | Moderate (CVSS 7.5 AV:N/AC:L/PR:H/UI:N/S:C/C:N/I:N/A:H) | JWE decompression bomb DoS: attacker with access to a valid public key crafts JWE token with extreme compression ratio; decompression at receipt exhausts memory → application freeze or OOM; fix enforces maximum decompressed data size limit | v1 ≥ 1.2.29 / v2 ≥ 2.0.21 | [GHSA-hj3v-m684-v259](https://github.com/advisories/GHSA-hj3v-m684-v259) |

## Security Posture Notes

`lestrrat-go/jwx` is the predominant Go implementation of the JOSE (JSON Object Signing and Encryption) family of standards: JWA, JWE, JWK, JWS, and JWT. It is used by authentication middleware, identity systems, service-mesh control planes, and API gateways that process externally-issued tokens.

The library ships as multiple Go module major versions:
- **v1** (`github.com/lestrrat-go/jwx`): legacy; last security fix at 1.2.29
- **v2** (`github.com/lestrrat-go/jwx/v2`): current LTS line; last security fix at 2.0.21
- **v3 / v4**: in active development as of mid-2026; no advisories published yet; migration docs available in the repository

All four confirmed advisories share a common pattern: attacker-controlled JWE or JWS tokens trigger CPU/memory exhaustion or nil-pointer crashes in parsing paths. The risk surface is primarily services that process tokens from untrusted parties (public API JWE decryption, multi-tenant JWS verification).

The maintainer (Daisuke Maki, `lestrrat-go`) uses GitHub Security Advisories for coordinated disclosure and has responded promptly to all four advisories — the 2023–2024 fix cluster moved from disclosure to patched release within weeks. All four advisories have fix versions; callers on v2 should be at ≥ 2.0.21 and on v1 ≥ 1.2.29. Migration to v2+ is recommended as v1 is no longer actively developed.

## Dependencies of Note

The library depends on cryptographic primitives for AES-CBC, ECDH-ES, RSA-OAEP, and PBKDF2. Algorithm agility remains a standing risk: GHSA-hj3v-m684-v259 required explicit decompression opt-in, but GHSA-7f9x-gw85-8grf shows that p2c was not bounded by default. Callers should verify that they restrict accepted JWE key management algorithms to the minimum necessary set.

## Open Questions

- Confirm whether v3/v4 carry forward all four fixes and address the p2c limit and decompression cap correctly.
- Assess whether other JOSE operations (ECDH key agreement, X.509 chain validation within JWK, key confusion between JWS and JWE) have been independently audited.
- Determine import count from pkg.go.dev for v2 (pkg.go.dev returned unreliable data for this module during this pass).

## Related Pages

- [[go/github.com/go-jose/go-jose]]
- [[go/github.com/golang-jwt/jwt]]
- [[go/golang.org-x-oauth2]]
- [[go/index]]

---
*Last updated: 2026-09-13 | Sources: 4*
