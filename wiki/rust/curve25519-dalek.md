# curve25519-dalek (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** unknown (crates.io API blocked in this environment; est. high-volume given ecosystem dependents)
**Repository:** https://github.com/dalek-cryptography/curve25519-dalek
**Security Contact:** security@dalek.rs (see SECURITY.md at dalek-cryptography/curve25519-dalek)
**Disclosure Policy:** https://github.com/dalek-cryptography/curve25519-dalek/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-58262 / RUSTSEC-2024-0344 / GHSA-x4gp-pqpj-f43q | High (crypto-failure) | Timing variability in `Scalar29::sub` and `Scalar52::sub` — LLVM inserts conditional branch instructions in the subtraction path, creating exploitable timing patterns that may enable private key extraction via timing side-channel analysis; fixed by using a `volatile` read as a compiler optimization barrier | ≥ 4.1.3 | [RUSTSEC-2024-0344](https://rustsec.org/advisories/RUSTSEC-2024-0344.html) · [GHSA-x4gp-pqpj-f43q](https://github.com/advisories/GHSA-x4gp-pqpj-f43q) · [PR #659](https://github.com/dalek-cryptography/curve25519-dalek/pull/659) |

*OSV link: https://osv.dev/list?ecosystem=crates.io&q=curve25519-dalek*

## Security Posture Notes

`curve25519-dalek` is a pure-Rust implementation of group operations on Ristretto and Curve25519, used as the foundational primitive for much of the Rust cryptography ecosystem. Key downstream consumers include:

- **`ed25519-dalek`** — EdDSA digital signatures over Curve25519
- **`x25519-dalek`** — X25519 ECDH key exchange
- **`snow`** — Noise protocol framework (used by WireGuard implementations)
- **`dalek-cryptography/*`** ecosystem (bulletproofs, zkp libraries)
- Various TLS and MLS implementations that depend on Ed25519 or X25519

The single known advisory (RUSTSEC-2024-0344) is a **compiler-induced timing variability** issue, not a logic bug in the mathematical implementation. The root cause is that LLVM's optimizer, when compiling the `sub` (subtraction) method on the internal `Scalar29` and `Scalar52` field-element representations, generates conditional branches that create timing differences observable by a co-located adversary. This class of flaw is particularly dangerous in cryptographic scalar operations because:

1. The Scalar type represents private keys and other secret values.
2. Elliptic curve scalar multiplication (`k * P`) calls `sub` repeatedly in the scalar recoding path.
3. An attacker who can measure execution timing (e.g., via cache timing, branch predictor state, or power analysis) may be able to recover the scalar (private key) bit by bit.

The fix employs a `volatile` read as a compiler optimization barrier (`black_box` equivalent) that prevents LLVM from optimizing the subtraction into a branch sequence. The issue was identified using the **DATA** (Differential Address Trace Analysis) tool developed by researchers at Fraunhofer AISEC and the Technical University of Munich.

**Researcher credit:** The vulnerability was discovered and reported by the DATA tool evaluation team at Fraunhofer AISEC / TU Munich; see [Pull #659](https://github.com/dalek-cryptography/curve25519-dalek/pull/659) for the full discussion and fix.

**Versions affected:** curve25519-dalek < 4.1.3. The 3.x line and earlier are in maintenance mode; check the advisory for their patch status. The `dalek-cryptography` team maintains active security contact at security@dalek.rs.

**Blast radius:** Any Rust application using `ed25519-dalek`, `x25519-dalek`, or direct `curve25519-dalek` scalar operations with a version < 4.1.3 should be treated as potentially vulnerable to timing-based private key extraction under adversarial co-location. The practical exploitability depends on the attacker's ability to collect sufficient timing observations.

## Dependencies of Note

- No direct runtime dependencies of security concern; the crate is intentionally minimal.
- `subtle` crate — constant-time helper library used in the same ecosystem; any advisories there would affect the broader dalek cryptography stack.

## Open Questions

- Confirm patch status for the 3.x maintenance branch (RUSTSEC-2024-0344 states patched ≥ 4.1.3; 3.x users should check the advisory for EOL/backport status).
- Assess whether downstream `ed25519-dalek` and `x25519-dalek` pinned their minimum `curve25519-dalek` version to 4.1.3 or later post-advisory.
- Verify download statistics via crates.io API when network access allows.

## Related Pages

- [[rust/ring]]
- [[rust/rustls]]
- [[rust/openssl]]
- [[rust/index]]

---
*Last updated: 2026-07-26 | Sources: RUSTSEC-2024-0344 (raw.githubusercontent.com/rustsec/advisory-db), GitHub advisory database (GHSA-x4gp-pqpj-f43q)*
