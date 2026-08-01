# ed25519-dalek (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** unknown (crates.io API rate-limited; ~179M total all-time downloads as of 2026-08-01)
**Repository:** https://github.com/dalek-cryptography/curve25519-dalek/tree/main/ed25519-dalek
**Security Contact:** security@dalek.rs (SECURITY.md at dalek-cryptography/curve25519-dalek)
**Disclosure Policy:** https://github.com/dalek-cryptography/curve25519-dalek/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No public proactive source-code audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-50237 / RUSTSEC-2022-0093 / GHSA-w5vr-6qhr-36cc | High (crypto-failure) | Double public key signing oracle attack enabling private key extraction — pre-2.0 versions model private and public keys as separate types that can be assembled into a `Keypair`, and APIs exist to serialize/deserialize the combined 64-byte blob. An adversary who can supply arbitrary public keys to the signing function obtains two signatures for the same message sharing the same `R` value but differing in `S`; this pair immediately enables extraction of the private key. The v2.0 rewrite removed decoupled keypair APIs from the public interface, keeping them only in clearly-labeled `hazmat` modules. | ≥ 2.0.0 | [RUSTSEC-2022-0093](https://rustsec.org/advisories/RUSTSEC-2022-0093.html) · [GHSA-w5vr-6qhr-36cc](https://github.com/advisories/GHSA-w5vr-6qhr-36cc) · [MystenLabs write-up](https://github.com/MystenLabs/ed25519-unsafe-libs) |

*OSV link: https://osv.dev/list?ecosystem=crates.io&q=ed25519-dalek*

## Security Posture Notes

`ed25519-dalek` is the canonical Rust implementation of Ed25519 (Edwards-curve Digital Signature Algorithm over Curve25519), part of the `dalek-cryptography` monorepo. With ~179M total crates.io downloads and current version 3.0.0, it is the dominant Ed25519 implementation in the Rust ecosystem and a transitive dependency of a large proportion of Rust applications that perform digital signatures, TLS certificate verification, or key-based authentication.

**RUSTSEC-2022-0093 — Double Public Key Signing Oracle Attack (disclosed 2022-06-11).**
The root cause is an API design flaw, not a mathematical error in Ed25519 itself. In versions < 2.0:

- The `Keypair` type wraps a `SecretKey` and a `PublicKey` as separate fields.
- The `sign()` method accepts both as inputs. The `S` scalar in an Ed25519 signature is computed deterministically from the secret key and the message; the `R` value is computed from the secret key and a nonce.
- Crucially, the `R` value does NOT depend on the public key — so if an adversary can substitute an arbitrary public key while keeping the secret key fixed, two calls with the same message but different public keys produce signatures with the same `R` and different `S` values. From these two `(R, S₁)` and `(R, S₂)` pairs the private scalar can be algebraically recovered.

The practical prerequisite is that the calling application exposes a signing oracle where the public key is attacker-supplied (e.g., a key rotation flow that signs with the new public key before verifying ownership of the corresponding private key). The fix in 2.0 removes this API pattern; the `hazmat` module retains low-level access for implementors who explicitly opt in.

A detailed write-up with exploit analysis was published by MystenLabs: https://github.com/MystenLabs/ed25519-unsafe-libs

**Interaction with RUSTSEC-2024-0344 (curve25519-dalek timing side-channel).**
`ed25519-dalek` uses `curve25519-dalek` for scalar arithmetic. RUSTSEC-2024-0344 (see [[rust/curve25519-dalek]]) documents a timing variability in `Scalar::sub` introduced by LLVM's optimizer. Applications using `ed25519-dalek` versions that pin to `curve25519-dalek` < 4.1.3 are indirectly exposed. The two advisories are independent issues but both affect the same cryptographic signing path.

**Version matrix:**
- `ed25519-dalek` < 2.0.0: RUSTSEC-2022-0093 directly applies.
- `ed25519-dalek` 2.x+: RUSTSEC-2022-0093 resolved; check `curve25519-dalek` pinned version for RUSTSEC-2024-0344 exposure.
- `ed25519-dalek` 3.0.0 (current max): Review changelog for any API changes; verify `curve25519-dalek` ≥ 4.1.3.

**Downstream blast radius:** The advisory applies to any library or application that:
1. Uses `ed25519-dalek` < 2.0.0 directly, or
2. Depends on a library that re-exports the pre-2.0 signing API without enforcing keypair coupling.

The MystenLabs write-up identifies several widely-deployed Rust cryptographic libraries that were affected at the time of disclosure. Applications should audit indirect dependencies and verify no pre-2.0 usage remains.

**Security contact:** Reports to security@dalek.rs; the project uses GitHub security advisories for public disclosure.

## Dependencies of Note

- **`curve25519-dalek`** — foundational elliptic curve arithmetic library; see [[rust/curve25519-dalek]] for its own advisory (RUSTSEC-2024-0344 timing side-channel). Ensure `curve25519-dalek` ≥ 4.1.3.
- **`signature` crate** — trait interface for signing; no known advisories but should be kept current.
- **`sha2`** — SHA-512 hashing used in Ed25519 nonce derivation; no known relevant advisories.

## Open Questions

- Confirm weekly download count via crates.io API when available (total ~179M as of 2026-08-01; current version 3.0.0).
- Verify the minimum `curve25519-dalek` version pinned by `ed25519-dalek` 2.x and 3.x to determine whether the RUSTSEC-2024-0344 timing issue is transitively resolved in the current release.
- Determine whether any additional advisories have been published against the 2.x or 3.x API since the 2022 disclosure.
- Assess `x25519-dalek` (the companion key-exchange crate) for similar API design issues; it shares the same monorepo and historical code patterns.

## Related Pages

- [[rust/curve25519-dalek]]
- [[rust/ring]]
- [[rust/rustls]]
- [[rust/index]]

---
*Last updated: 2026-08-01 | Sources: RUSTSEC-2022-0093 (raw.githubusercontent.com/rustsec/advisory-db); crates.io API (download stats); MystenLabs write-up (github.com/MystenLabs/ed25519-unsafe-libs)*
