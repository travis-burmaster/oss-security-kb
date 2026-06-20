# ring (crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~134,594,184 (as of 2026-06-20)
**Repository:** https://github.com/briansmith/ring
**Security Contact:** https://github.com/briansmith/ring/security (GitHub private vulnerability reporting)
**Disclosure Policy:** https://github.com/briansmith/ring/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-20 | OSS Security KB | advisory-db lookup | automated | 2 active advisories mapped (1 DoS, 1 unmaintained notice); 1 withdrawn advisory noted | [rustsec/advisory-db](https://github.com/rustsec/advisory-db/tree/main/crates/ring) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-4432 / RUSTSEC-2025-0009 / GHSA-4p46-pwfr-66x6 | Medium — DoS | Two panic-on-integer-overflow conditions when Rust overflow checking is enabled at runtime: (1) `ring::aead::quic::HeaderProtectionKey::new_mask()` may panic on specially crafted QUIC packets (~1-in-2³² probability per packet); (2) AES-128-GCM and AES-256-GCM may panic when encrypting or decrypting a single chunk of ~64 GiB on 64-bit systems. Overflow checking is disabled by default in release builds; exploitable only in debug builds or `RUSTFLAGS="-C overflow-checks"` release builds. Standard TLS and SSH deployments are unaffected because they chunk data below the 64 GiB threshold. | 0.17.12 | [RUSTSEC-2025-0009](https://rustsec.org/advisories/RUSTSEC-2025-0009.html) |
| RUSTSEC-2025-0010 (informational — unmaintained) | — | All `ring` versions < 0.17 are unmaintained; 0.16.20 is the final 0.16.x release (over 4 years old). The project patches only the latest 0.17.x line; backporting to < 0.17.10 is impractical due to license changes introduced in the 0.17.x development cycle. | Upgrade to ≥ 0.17 | [RUSTSEC-2025-0010](https://rustsec.org/advisories/RUSTSEC-2025-0010.html) |

*Note: RUSTSEC-2025-0007 (maintenance hiatus) was published 2025-02-20 and withdrawn 2025-02-22 after the Rustls team was granted repository access and committed to security maintenance; standard development resumed and the advisory was retracted.*

## Security Posture Notes

`ring` is a widely used cryptographic library combining Rust, C, and assembly (~110,000 lines total). It provides AES-GCM, ChaCha20-Poly1305, ECDH, ECDSA, Ed25519, RSA, and QUIC header-protection primitives. With ~582M total downloads and ~135M recent weekly downloads it is among the most downloaded security-critical crates in the Rust ecosystem.

The single active vulnerability (RUSTSEC-2025-0009 / CVE-2025-4432) affects only deployments where Rust overflow checking is active at runtime — not the default for `--release` builds. QUIC-based deployments (e.g. using `quinn`) face a higher exposure profile due to the network-reachable QUIC panic path. Current version 0.17.14 (March 2025) addresses the issue.

Users pinned to 0.16.x should upgrade to the 0.17.x line; that branch carries the unmaintained advisory (RUSTSEC-2025-0010) with no further security patches planned.

## Dependencies of Note

- Embeds vendored C and assembly code; the C layer is not independently versioned as a third-party crate.
- Build system uses Perl scripts to generate assembly at compile time; supply-chain exposure is confined to build time.

## Open Questions

- Confirm scope of GHSA-c86p-w88r-qvqr (filed 2025-05), which also aliases CVE-2025-4432; may be a downstream artifact from a package depending on `ring`.
- Monitor whether QUIC-path exposure triggers additional advisories as QUIC adoption in Rust grows.
- Track whether ongoing Rustls co-maintenance results in any additional advisory filings or disclosure process changes.

## Related Pages

- [[rust/hyper]]
- [[rust/h2]]
- [[rust/reqwest]]
- [[rust/openssl]]
- [[rust/index]]

---
*Last updated: 2026-06-20 | Sources: 3 (rustsec/advisory-db, github/advisory-database, crates.io API)*
