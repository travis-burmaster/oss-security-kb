# elliptic (npm)

**Registry:** npm  
**Weekly Downloads:** ~13,944,874 (2026-04-27 to 2026-05-03)  
**Repository:** https://github.com/indutny/elliptic  
**Security Contact:** GitHub Security Advisories / repository maintainers  
**Disclosure Policy:** https://github.com/indutny/elliptic/security/advisories  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-04 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / repository advisories, public CVE records, upstream issues / PRs / commits, npm registry metadata, npm downloads API, local Claude-compatible proxy synthesis used as a drafting aid) | Added an advisory-mapped baseline for `elliptic`, covering the 2020 ECDSA / ECDH crypto flaws, the 2024 signature-malleability and verification-correctness cluster, the 2025 critical malformed-input ECDSA private-key extraction advisory fixed in `6.6.1`, and the still-unfixed public `CVE-2025-14505` deterministic-`k` issue affecting versions through `6.6.1`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-vjh7-7g9h-fjfh | Critical | Public repository advisory describes ECDSA private-key extraction when `elliptic` signs malformed inputs such as strings or numbers: different converted message values can produce equivalent nonce arrays, causing `k` reuse and allowing key extraction from a signature pair. | 6.6.1 | https://github.com/indutny/elliptic/security/advisories/GHSA-vjh7-7g9h-fjfh |
| CVE-2025-14505 / GHSA-848j-6mx2-7j84 | Low | Public OSV / GitHub advisory records say the ECDSA RFC 6979 deterministic-`k` computation can mishandle leading-zero interim `k` values, producing faulty signatures and, under stated conditions, possible secret-key exposure. The advisory states all known versions through `6.6.1` are affected and lists no fixed version. | No fixed version listed in OSV / GHSA as of this review | https://github.com/advisories/GHSA-848j-6mx2-7j84 |
| CVE-2024-48948 / GHSA-fc9h-whq2-v747 | Low | Valid ECDSA signatures could be incorrectly rejected when hashes contain at least four leading zero bytes and the curve order is smaller than the hash, due to `_truncateToN` handling. | 6.6.0 | https://github.com/advisories/GHSA-fc9h-whq2-v747 |
| CVE-2024-48949 / GHSA-434g-2637-qmqr | Low | EDDSA verification omitted an order-bound / non-negative validation for `S`, enabling signature malleability where an application relies on signature uniqueness. | 6.5.6 | https://github.com/advisories/GHSA-434g-2637-qmqr |
| CVE-2024-42459 / GHSA-f7q4-pwc6-w24p | Low | EDDSA signature malleability from a missing signature-length check, allowing zero-valued bytes to be removed or appended. | 6.5.7 | https://github.com/advisories/GHSA-f7q4-pwc6-w24p |
| CVE-2024-42460 / GHSA-977x-g7h5-7qgw | Low | ECDSA signature malleability from a missing check on whether the leading bit of `r` and `s` is zero. | 6.5.7 | https://github.com/advisories/GHSA-977x-g7h5-7qgw |
| CVE-2024-42461 / GHSA-49q7-c7j4-3p7m | Low | ECDSA signature malleability because BER-encoded signatures were accepted. | 6.5.7 | https://github.com/advisories/GHSA-49q7-c7j4-3p7m |
| CVE-2020-28498 / GHSA-r9p9-mrjm-926w | Moderate | `secp256k1` ECDH public-key derivation did not confirm that the supplied public key point was on the curve, creating private-key exposure risk after repeated ECDH operations. | 6.5.4 | https://github.com/advisories/GHSA-r9p9-mrjm-926w |
| CVE-2020-13822 / GHSA-vh7m-p724-62c2 | High | ECDSA signature malleability via encoding variations, leading zero bytes, or integer overflows, with impact when downstream systems require one canonical signature. | 6.5.3 | https://github.com/advisories/GHSA-vh7m-p724-62c2 |

## Security Posture Notes

- `elliptic` is a high-blast-radius cryptographic dependency (~13.9M weekly downloads in this review window) whose advisories often affect signature canonicality, signature verification correctness, ECDH validation, or private-key exposure boundaries.
- The package's modern public advisory history is unusually dense for a cryptographic primitive wrapper: several low-severity malleability records are operationally important when signatures are used as identifiers, authorization artifacts, blockchain transactions, or audit-log evidence.
- `6.6.1` is the minimum version supported by public fix data for all *patched* advisories in this page, but it does **not** close `CVE-2025-14505` according to the OSV / GitHub advisory data gathered on 2026-05-04.
- The unpatched `CVE-2025-14505` record should be interpreted conservatively: the published severity is Low, but the described failure mode involves faulty ECDSA signatures and possible secret-key exposure under stated conditions.
- Applications that sign attacker-influenced input should treat the 2025 malformed-input private-key extraction advisory as higher priority than its package-level version bump alone suggests.

## Recommendations for Developers

1. Upgrade to `elliptic@6.6.1` or newer to receive the latest published patched fixes, while tracking `CVE-2025-14505` for an upstream remediation.
2. Avoid signing raw attacker-controlled values; normalize inputs to the expected byte/hex representation before calling ECDSA signing APIs.
3. Treat signatures as non-canonical unless the application explicitly validates canonical form and is on a fixed release for the relevant malleability advisories.
4. For new cryptographic designs, prefer maintained platform crypto libraries or well-reviewed higher-level libraries rather than depending directly on low-level JavaScript ECC primitives.
5. Inventory transitive `elliptic` usage in wallet, blockchain, JWT/JWK, TLS, WebCrypto polyfill, and build-tool dependency trees.

## Dependencies of Note

- Frequently appears transitively through cryptography, blockchain, wallet, signing, and legacy browser-crypto packages.
- Downstream risk is highest where applications perform ECDSA signing or verification over attacker-influenced messages, depend on signature uniqueness, or expose repeated signing operations with long-lived private keys.

## Open Questions

- Has upstream published or planned a fix for `CVE-2025-14505` after `6.6.1`?
- Which high-volume transitive packages still pin `elliptic` below `6.6.1`, and which expose signing operations to user-controlled inputs?
- Should this KB add a cross-package crypto-primitives page to compare `elliptic`, `node-forge`, `jsonwebtoken`, and platform crypto APIs?

## Related Pages

- [[npm/jsonwebtoken]]
- [[npm/nanoid]]
- [[npm/uuid]]
- [[npm/index]]

---
*Last updated: 2026-05-04 | Sources: 24 (OSV.dev package query for npm/elliptic, OSV vulnerability records for all GHSA IDs listed above, GitHub Advisory Database / upstream repository security advisory records, public CVE records, upstream issues / PRs / commits, npm registry metadata, npm downloads API, local Claude-compatible proxy synthesis used as drafting aid only)*
