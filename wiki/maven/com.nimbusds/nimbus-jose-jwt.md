# nimbus-jose-jwt (Maven)

**Registry:** Maven Central
**Weekly Downloads:** unknown (very high; backbone of Spring Security OAuth2 JWT, Keycloak, Quarkus, Micronaut)
**Repository:** https://bitbucket.org/connect2id/nimbus-jose-jwt
**Security Contact:** https://connect2id.com/products/nimbus-jose-jwt (commercial maintainer: Connect2id)
**Disclosure Policy:** https://connect2id.com/products/nimbus-jose-jwt/security
**Current Status:** advisory-mapped

## Audit History

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-53864 / GHSA-xwmg-2g98-w7v9 | Moderate CVSS 7.5 | DoS via deeply nested JSON in JWT claim set. Uncontrolled recursion when processing JWTs containing claim values with deeply nested JSON objects causes CPU exhaustion. Independent of underlying JSON library depth limits. | 9.37.4; 10.0.2 | [GHSA-xwmg-2g98-w7v9](https://github.com/advisories/GHSA-xwmg-2g98-w7v9) |
| CVE-2023-52428 / GHSA-gvpg-vgmx-xg6w | High CVSS 7.5 | JWE p2c header PBKDF2 iteration-count DoS. The `PasswordBasedDecrypter` (PBES2 algorithms) does not validate the `p2c` (iteration count) JWE header, allowing a crafted JWE with an extremely large `p2c` value to exhaust CPU/memory on decryption. | 9.37.2 | [GHSA-gvpg-vgmx-xg6w](https://github.com/advisories/GHSA-gvpg-vgmx-xg6w) |
| CVE-2019-17195 / GHSA-f6vf-pq8c-69m4 | Critical CVSS 9.8 | Insufficient exception handling during JWT parsing. Uncaught exceptions during token processing can crash the application or allow authentication bypass when JWT validation logic is wrapped in broad catch blocks that treat parse exceptions as valid empty results. | 7.9 | [GHSA-f6vf-pq8c-69m4](https://github.com/advisories/GHSA-f6vf-pq8c-69m4) |
| CVE-2017-12973 / GHSA-jfmq-4g4m-99rh | Low CVSS 3.1 | AES-CBC HMAC padding oracle. After detecting an invalid HMAC on an AES-CBC JWE, the library continues decryption instead of aborting, enabling classic CBC padding oracle attacks for JWE plaintexts. | 4.39 | [GHSA-jfmq-4g4m-99rh](https://github.com/advisories/GHSA-jfmq-4g4m-99rh) |
| CVE-2017-12972 / GHSA-2qp9-wg27-9pcv | High | HMAC bypass via integer overflow in length conversion. Integer overflow when converting Additional Authenticated Data (AAD) and ciphertext lengths from bytes to bits allows an attacker to shift AAD/ciphertext to obtain a different plaintext that verifies under the same HMAC. | 4.39 | [GHSA-2qp9-wg27-9pcv](https://github.com/advisories/GHSA-2qp9-wg27-9pcv) |
| CVE-2017-12974 / GHSA-pfv2-37f7-9m6w | High CVSS 7.5 | EC key curve validation bypass (Invalid Curve Attack). `ECKey` construction does not verify that supplied public point coordinates lie on the specified named curve. When a JCE provider lacks native curve validation, an attacker can supply an off-curve public key point to extract the private key via differential side-channel. | 4.36 | [GHSA-pfv2-37f7-9m6w](https://github.com/advisories/GHSA-pfv2-37f7-9m6w) |

## Security Posture Notes

Connect2id Nimbus JOSE+JWT is the dominant JOSE (JSON Object Signing and Encryption) implementation on the JVM. It is the backend for Spring Security's OAuth 2.0 / OIDC resource-server JWT support, used directly by Keycloak, Red Hat SSO, Micronaut Security, and Quarkus OidcExtension. Its wide adoption in identity-critical paths makes any cryptographic vulnerability particularly high-impact.

Historical vulnerability patterns:
- **Cryptographic implementation flaws (2017)**: Three related advisories (CVE-2017-12972/12973/12974) in version 4.x revealed failures in AES-CBC HMAC verification — the library processed beyond an authentication failure (padding oracle), had an integer overflow in length conversion that could bypass HMAC entirely, and failed to validate EC point coordinates. These are classic pitfalls of building AES-CBC-HMAC-SHA2 from primitives rather than using an AEAD mode.
- **EC key validation (2017)**: The Invalid Curve Attack (CVE-2017-12974) is a well-known pitfall for EC implementations that trust the public key's claimed curve without validating point coordinates. Fixed in 4.36.
- **Exception handling (2019)**: CVE-2019-17195 reflects a hardening gap — parse exceptions were not propagated clearly, risking confused-deputy authentication bypass patterns downstream. Fixed in 7.9.
- **p2c DoS (2023)**: CVE-2023-52428 matches a known JOSE attack pattern (also present in python-jose, go-jose/go-jose) where the PBKDF2 iteration count is attacker-controlled without an upper bound. Fixed in 9.37.2 by capping p2c.
- **Nested JSON DoS (2025)**: CVE-2025-53864 is a recursive-JSON DoS; the library added its own depth limit rather than relying on the upstream JSON library. Fixed in 9.37.4 / 10.0.2.

**Current stable:** 9.37.4 (security-patch line for 9.x) and 10.0.2 (current major with breaking API changes). Both lines receive security patches.

**Security disclosure:** Connect2id operates a commercial business around Nimbus JOSE+JWT and maintains a security advisories page at connect2id.com.

## Dependencies of Note

- **Gson / Jackson**: The nested-JSON DoS (CVE-2025-53864) is independent of Gson's own depth limits; the library must enforce its own claim-level recursion bounds.
- **JCE provider**: EC curve validation behavior depends on the JCE provider in use. The JDK's built-in provider validates curve coordinates; third-party providers (e.g., older BouncyCastle versions) may not, making CVE-2017-12974 exploitable even on patched versions of this library if the JCE provider does not validate.

## Open Questions

- Complete GHSA record count beyond the 6 mapped here not yet confirmed.
- Interaction with Spring Security's `NimbusJwtDecoder` default configuration and which CVEs are mitigated at the framework level vs. library level.
- nimbus-jose-jwt 10.x API migration guide for p2c limit configuration not reviewed.

## Related Pages

- [[maven/org.springframework.security/spring-security-core]]
- [[maven/org.bouncycastle/bcprov-jdk18on]] — Bouncy Castle used as JCE provider alongside Nimbus
- [[maven/index]]

---
*Last updated: 2026-09-08 | Sources: 6*
