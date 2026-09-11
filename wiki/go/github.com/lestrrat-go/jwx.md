# lestrrat-go/jwx (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (pkg.go.dev crawl-based; v2 deprecated; current maintained line is v4)
**Repository:** https://github.com/lestrrat-go/jwx
**Security Contact:** GitHub Security Advisories (https://github.com/lestrrat-go/jwx/security/advisories)
**Disclosure Policy:** https://github.com/lestrrat-go/jwx/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-rm8v-mxj3-5rmq (no CVE assigned) | Moderate | AES-CBC JWE padding oracle — decryption failure paths return distinct error messages that leak padding validity, and the padding removal implementation does not use constant-time execution; violates RFC 7516 §B.3 and enables classical padding oracle attacks and timing side-channel attacks against JOSE endpoints using AES-CBC + HMAC key encryption; all JWE algorithms that use AES-CBC encryption mode are affected (A128CBC-HS256, A192CBC-HS384, A256CBC-HS512); authentication tags are verified before decryption reducing immediate exploit risk, but timing channels remain | v1 1.2.26, v2 2.0.11 | [GHSA-rm8v-mxj3-5rmq](https://github.com/advisories/GHSA-rm8v-mxj3-5rmq) |
| CVE-2023-49290 / GHSA-7f9x-gw85-8grf | Moderate (CVSS 3.1 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L) | PBES2 p2c iteration-count DoS — the `p2c` parameter in PBES2-* JWE key encryption algorithms controls the PBKDF2 iteration count and is accepted without an upper-bound limit; an attacker supplying a malicious JWE with a very large p2c value causes unbounded CPU consumption, enabling unauthenticated denial-of-service against any service that decrypts JWE tokens using PBES2 key wrapping | v1 1.2.27, v2 2.0.18 | [GHSA-7f9x-gw85-8grf](https://github.com/advisories/GHSA-7f9x-gw85-8grf) |
| CVE-2024-21664 / GHSA-pvcr-v8j8-j5q3 | Moderate (CVSS 3.1 AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L) | JWS nil pointer dereference DoS — `jws.Parse` (and any function that calls it, including `jws.Verify`) crashes with a nil dereference when processing a JSON-serialized JWS payload containing a `signature` field without a corresponding `protected` field; the bug is in `message.go:UnmarshalJSON()` which assumes both fields are always present together; exploitable by supplying any crafted JWS value to an affected endpoint | v1 1.2.28, v2 2.0.19 | [GHSA-pvcr-v8j8-j5q3](https://github.com/advisories/GHSA-pvcr-v8j8-j5q3) |
| CVE-2024-28122 / GHSA-hj3v-m684-v259 | Moderate (CVSS 3.1 AV:N/AC:L/PR:H/UI:N/S:C/C:N/I:N/A:H) | JWE decompression bomb — crafting a malicious JWE token with an extremely high compression ratio causes uncontrolled memory allocation and CPU exhaustion when the payload is decompressed; requires the attacker to encrypt the payload with a trusted public key, making the practical exploitability surface limited to scenarios where attacker-controlled data is encrypted under a server key before being processed by the same server | v2 2.0.21, v1 1.2.29 | [GHSA-hj3v-m684-v259](https://github.com/advisories/GHSA-hj3v-m684-v259) |

*OSV live record: https://osv.dev/list?ecosystem=Go&q=github.com%2Flestrrat-go%2Fjwx*

## Security Posture Notes

`github.com/lestrrat-go/jwx` is a Go implementation of the JOSE (JSON Object Signing and Encryption) suite of specifications — JWA, JWE, JWK, JWS, and JWT (RFC 7515–7519, 7797, 8037, 8812). It is developed and maintained by Taro Minowa (lestrrat) and used in security-sensitive applications as a JOSE primitive library, typically wrapping or replacing standard library JWT implementations.

**Versioning and maintenance status (September 2026):** The package has gone through four major versions:
- **v1** (`github.com/lestrrat-go/jwx`): maintenance-only; latest 1.2.29; carries all four advisories above.
- **v2** (`github.com/lestrrat-go/jwx/v2`): deprecated as of 2026; no longer maintained; carries advisories GHSA-rm8v-mxj3-5rmq, CVE-2023-49290, CVE-2024-21664, CVE-2024-28122.
- **v3** (`github.com/lestrrat-go/jwx/v3`): intermediate release; check for independent advisory history.
- **v4** (`github.com/lestrrat-go/jwx/v4`): current actively maintained line; v4.5.0 as of September 2026; requires Go ≥ 1.26. No separate v4 advisory found in this pass.

Users on v1 or v2 should migrate to v4. Both v1 and v2 carry unresolved exposure to the four advisories above if not patched to the minimum fixed versions.

**Advisory pattern analysis:** Three of four advisories are denial-of-service flaws triggered at the parsing or key-derivation layer — a common pattern in JOSE implementations. The PBES2 p2c DoS (CVE-2023-49290) is the same class of vulnerability that affected go-jose (GHSA-2q45-4gfh-8j89), Nimbus JOSE+JWT (CVE-2023-52428), and other JOSE libraries simultaneously. The padding oracle advisory (GHSA-rm8v-mxj3-5rmq) is cryptographically more severe in principle but mitigated in practice because authentication tags are verified first under the default AES-CBC-HMAC construction. The decompression bomb (CVE-2024-28122) requires attacker-controlled data encrypted under a server key — a narrow but realistic scenario in some token relay or JWT-inspection architectures.

**Recommended configuration hardening:** Operators using lestrrat-go/jwx for JWE decryption should:
1. Migrate to v4 (current maintained line).
2. Restrict accepted key algorithms — avoid PBES2-* algorithms unless explicitly required; prefer ECDH-ES or RSA-OAEP key wrapping, which are unaffected by the p2c DoS.
3. Restrict accepted content encryption algorithms — prefer AES-GCM (A128GCM, A192GCM, A256GCM) over AES-CBC to sidestep the padding oracle class of vulnerability.
4. Apply JWE payload decompression limits or disable payload compression at the application level where not needed.

## Dependencies of Note

- `github.com/lestrrat-go/blackmagic` — internal reflection utility; no separate advisory history found.
- `github.com/lestrrat-go/httpcc` — HTTP content-type parser; no separate advisory history found.
- `github.com/lestrrat-go/iter` — iterator utilities; no separate advisory history found.
- Standard library `crypto/subtle`, `crypto/sha256`, etc. — cryptographic primitives; correctness depends on Go stdlib guarantees.

## Open Questions

- v3 and v4 advisory coverage: no GHSA advisories for `github.com/lestrrat-go/jwx/v3` or `/v4` found in this pass; verify against current GHSA database in a future pass.
- ECDH-ES invalid curve attack: not found in the current advisory set; the library's EC key validation path warrants verification against known JOSE invalid-curve patterns.
- Algorithm negotiation: whether the library enforces strict algorithm allow-listing by default (opt-in safe set vs. opt-out unsafe set) — the advisory history suggests the default configuration accepted unbounded p2c and compression, implying users bear algorithm-restriction responsibility.

## Related Pages

- [[go/github.com/go-jose/go-jose]] — alternative Go JOSE library with overlapping advisory pattern (PBES2 DoS, decompression bomb, AES-CBC padding oracle)
- [[go/github.com/golang-jwt/jwt]] — Go JWT-specific library (narrower scope, no JWE)
- [[go/github.com/dgrijalva/jwt-go]] — archived predecessor Go JWT library
- [[dotnet/Microsoft.IdentityModel.JsonWebTokens]] — .NET JOSE/JWT with overlapping JWE compression bomb pattern
- [[maven/com.nimbusds/nimbus-jose-jwt]] — JVM JOSE with same PBES2 DoS and AES-CBC padding oracle class
- [[go/index]]

---
*Last updated: 2026-09-11 | Sources: 4 (GHSA-rm8v-mxj3-5rmq, GHSA-7f9x-gw85-8grf, GHSA-pvcr-v8j8-j5q3, GHSA-hj3v-m684-v259)*
