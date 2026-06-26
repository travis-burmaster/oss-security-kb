# go-jose/go-jose (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-06-26); v4: 601 importers, v3: several thousand (estimated via transitive use)
**Repository:** https://github.com/go-jose/go-jose
**Security Contact:** https://github.com/go-jose/go-jose/security/advisories (GitHub private reporting)
**Disclosure Policy:** https://go.dev/security/policy (Go vulnerability database)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-26 | OSS Security KB | GHSA database lookup across v1/v2/v3/v4 module lineage | automated | 7 public advisory rows mapped (GHSA-86r9 through GHSA-78h2) | [github/advisory-database](https://github.com/github/advisory-database) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2016-9121 / GHSA-86r9-39j9-99wp | High (CVSS 7.5) | ECDH-ES invalid curve attack: go-jose failed to verify that the received public key lies on the same curve as the receiver's static private key, allowing a remote attacker to recover the static private key (full key disclosure). Affects `gopkg.in/square/go-jose.v1` and `github.com/square/go-jose`. | ≥ 1.0.4 (v1 / square) | [GHSA-86r9-39j9-99wp](https://github.com/advisories/GHSA-86r9-39j9-99wp) |
| CVE-2016-9123 / GHSA-3fx4-7f69-5mmg | High (CVSS 7.5) | CBC-HMAC integer overflow on 32-bit architectures: overflow in the length field could allow HMAC authentication bypass for CBC-HMAC encrypted messages. Affects `github.com/square/go-jose` < 1.0.5. | ≥ 1.0.5 (v1 / square) | [GHSA-3fx4-7f69-5mmg](https://github.com/advisories/GHSA-3fx4-7f69-5mmg) |
| GHSA-77gc-fj98-665h (no CVE) | Moderate | Signature validation bypass: go-jose supported messages with multiple signatures but did not indicate which signature was validated, allowing callers to read protected headers from an unvalidated signature. Affects `gopkg.in/square/go-jose.v1`. | ≥ 1.1.0 (v1 / square) | [GHSA-77gc-fj98-665h](https://github.com/advisories/GHSA-77gc-fj98-665h) |
| GHSA-2c7c-3mj9-8fqh (no CVE) | Moderate (CWE-400) | PBES2 "billion hashes" DoS: decrypting a PBES2-encrypted JWE with a maliciously large `p2c` (iteration count) causes unbounded CPU consumption. Affects `github.com/go-jose/go-jose/v3` < 3.0.1 and `gopkg.in/square/go-jose.v2` < 2.6.2. | ≥ 3.0.1 (v3) / ≥ 2.6.2 (v2 square) | [GHSA-2c7c-3mj9-8fqh](https://github.com/advisories/GHSA-2c7c-3mj9-8fqh) |
| CVE-2024-28180 / GHSA-c5q2-7r4c-mv6g | Moderate (CVSS 3.1) | JWE decompression bomb (data amplification): `Decrypt`/`DecryptMulti` can be fed JWE with highly compressed content, consuming excessive memory and CPU. Fixed by enforcing a 250 kB / 10× decompression limit. Archived `gopkg.in/square/go-jose.v2` will not receive a fix. | ≥ 4.0.1 (v4) / ≥ 3.0.3 (v3) / ≥ 2.6.3 (go-jose.v2) | [GHSA-c5q2-7r4c-mv6g](https://github.com/advisories/GHSA-c5q2-7r4c-mv6g) |
| CVE-2025-27144 / GHSA-c6gw-w398-hv78 | Moderate (CVSS v4.0: 4.0) | DoS in JWS/JWE token parsing: `strings.Split(token, ".")` on compact serialization is vulnerable to excessive memory consumption when processing tokens with a large number of `.` characters. Related to CVE-2025-22868 in `golang.org/x/oauth2/jws`. | ≥ 4.0.5 (v4) / ≥ 3.0.4 (v3) | [GHSA-c6gw-w398-hv78](https://github.com/advisories/GHSA-c6gw-w398-hv78) |
| CVE-2026-34986 / GHSA-78h2-9frx-2jm8 | High (CVSS 7.5) | JWE key-wrapping panic DoS: decrypting a JWE where the `alg` field specifies a key-wrapping algorithm (e.g. `A128KW`) but `encrypted_key` is empty causes a panic in `cipher.KeyUnwrap()` when it attempts to allocate a zero/negative-length slice. Reachable from `ParseEncrypted` + `Decrypt`. | ≥ 4.1.4 (v4) / ≥ 3.0.5 (v3) | [GHSA-78h2-9frx-2jm8](https://github.com/advisories/GHSA-78h2-9frx-2jm8) |

*OSV live record: https://osv.dev/list?ecosystem=Go&q=github.com%2Fgo-jose%2Fgo-jose*

## Security Posture Notes

`github.com/go-jose/go-jose` is the canonical Go implementation of the JOSE (JSON Object Signing and Encryption) standard family: JWS (JSON Web Signatures), JWE (JSON Web Encryption), JWK (JSON Web Keys), and JWT (JSON Web Tokens). The library originated at Square as `github.com/square/go-jose` / `gopkg.in/square/go-jose`, then transferred to the `go-jose` organization in 2022 as the community-governed replacement. The active module lines are:
- `github.com/go-jose/go-jose/v4` (v4.1.4, Apr 2026) — current stable release
- `github.com/go-jose/go-jose/v3` (v3.0.5, Apr 2026) — still receiving security fixes
- `gopkg.in/square/go-jose.v2` — **archived, receives no further fixes**; GHSA-c5q2-7r4c-mv6g explicitly notes it will not be patched

go-jose is a transitive dependency in many authentication, authorization, and token-handling libraries across the Go ecosystem. Notable adopters include ZITADEL identity platform, Dex OIDC provider, various OAuth2/OIDC middleware packages, and numerous microservices frameworks.

**2016 cryptographic vulnerabilities (v1 / square):** The original `square/go-jose` had two critical cryptographic issues: an ECDH-ES invalid-curve attack enabling private key recovery (CVE-2016-9121), and a 32-bit CBC-HMAC integer overflow enabling HMAC bypass (CVE-2016-9123). Both fixed in 1.0.4/1.0.5. Any caller still using pre-1.0.5 v1 code has an unfixable key-disclosure risk and should be treated as fully compromised.

**JWE decryption DoS pattern (2023–2026):** Four of the seven advisories exploit the JWE decryption path (PBES2 billion-hashes, decompression bomb, token-parsing memory, key-wrapping panic). This recurring pattern suggests that JWE decryption of untrusted inputs is the highest-risk code path. Callers that do not use JWE can filter their accepted algorithms list via `ParseEncrypted`'s `keyAlgorithms` parameter to avoid the key-wrapping panic even on unpatched versions (see GHSA-78h2-9frx-2jm8 workaround).

**Current safe versions:** v4 ≥ 4.1.4, v3 ≥ 3.0.5. Do not use `gopkg.in/square/go-jose.v2` for new code; it is archived and will not receive security patches.

## Dependencies of Note

The `gopkg.in/square/go-jose.v2` (archived) dependency in downstream libraries is a persistent concern; projects that declare a direct or transitive dependency on it are exposed to CVE-2024-28180 with no vendor fix available.

## Open Questions

- Verify whether `github.com/go-jose/go-jose` (unversioned base module, still present in the advisory for GHSA-c6gw-w398-hv78) is the same codebase as v3 or a legacy alias.
- Assess whether v2 (`gopkg.in/go-jose/go-jose.v2`) callers can feasibly migrate to v4 without breaking API changes.
- Monitor for any future advisories in the `cipher.Encrypt` / `cipher.Sign` paths, which have so far been less targeted than the decrypt path.

## Related Pages

- [[go/github.com/golang-jwt/jwt]]
- [[go/golang.org-x-crypto]]
- [[go/index]]

---
*Last updated: 2026-06-26 | Sources: 3 (github/advisory-database, pkg.go.dev, go.dev/security)*
