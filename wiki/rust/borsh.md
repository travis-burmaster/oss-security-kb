# borsh (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~16.5M est. (as of 2026-09-23)
**Repository:** https://github.com/near/borsh-rs
**Security Contact:** GitHub Security Advisories (https://github.com/near/borsh-rs/security/advisories)
**Disclosure Policy:** GitHub private vulnerability reporting
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2023-0033 / GHSA-fjx5-qpf4-xjf2 | Informational (unsound) | Zero-sized type (ZST) deserialization UB: if a type is a ZST that is neither Copy nor Clone (e.g., a singleton), deserializing it creates multiple instances; accessing or writing the deserialized data causes a segmentation fault. Affects only code that deserializes non-Copy ZSTs. No CVE assigned. | 0.10.4 / 1.0.0-alpha.1 | [RUSTSEC](https://rustsec.org/advisories/RUSTSEC-2023-0033) / [GHSA](https://github.com/advisories/GHSA-fjx5-qpf4-xjf2) |

## Security Posture Notes

`borsh` (Binary Object Representation Serializer for Hashing) is the canonical serialization format for the NEAR Protocol blockchain ecosystem and is also widely used in the Solana smart-contract ecosystem. Its design goal is deterministic, canonical binary encoding for content addressing and hashing, not arbitrary data exchange. This design limits some attack surface: no recursive pointer serialization, no arbitrary type instantiation, fixed-width integers, length-prefixed arrays.

The one confirmed advisory (RUSTSEC-2023-0033) is classified "informational/unsound" — it produces undefined behavior in otherwise-safe Rust when a non-Copy ZST is deserialized. In practice this pattern is unusual: most ZSTs implement `Copy`. The fix in 0.10.4 and 1.0.0-alpha.1 addresses the root cause.

Maintained by the NEAR Protocol team (NEAR Inc.) under the `near` GitHub organization. Active development: latest stable 1.8.1. crates.io: ~193.3M all-time downloads, ~49.6M/90 days (~16.5M/week est.).

## Dependencies of Note

The `borsh` crate has minimal runtime dependencies. The companion `borsh-derive` proc-macro depends on `syn`, `proc-macro2`, and `quote`; none of these have confirmed direct security advisories.

## Open Questions

- Are there advisories filed against `borsh-derive` related to macro expansion or code-generation hygiene?
- Monitor NEAR Protocol security disclosures (https://github.com/near/nearcore/security/advisories) for borsh-level protocol manipulation findings (e.g., malformed input triggering excessive allocation).
- Check whether the ZST UB pattern in RUSTSEC-2023-0033 is reachable in any NEAR or Solana contract verification paths.

## Related Pages

- [[rust/index]]

---
*Last updated: 2026-09-23 | Sources: 2*
