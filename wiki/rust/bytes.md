# bytes (crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~14.5M/week est. (as of 2026-07-08)
**Repository:** https://github.com/tokio-rs/bytes
**Security Contact:** GitHub security advisories (https://github.com/tokio-rs/bytes/security)
**Disclosure Policy:** GitHub security advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2026-0007 / CVE-2026-25541 / GHSA-434x-w66g-qw3r | Moderate (CVSS 4.0 AV:L/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:H/SC:N/SI:N/SA:N / E:P) | `BytesMut::reserve` integer overflow in the unique-reclaim path: the condition `if v_capacity >= new_cap + offset` uses an unchecked addition; when `new_cap + offset` overflows `usize` in release builds (wrapping arithmetic), the condition may incorrectly evaluate to true, corrupting `self.cap` to a value that exceeds actual allocated capacity. Subsequent APIs such as `spare_capacity_mut()` trust the corrupted cap and may return out-of-bounds slices, leading to undefined behavior. PoC: call `reserve(usize::MAX - 6)` after a split-and-drop sequence. Debug builds are protected by Rust's overflow-check panics; only release builds are affected. The vulnerable path was introduced in 1.2.1 when the unique-reclaim optimization was added. | bytes ≥ 1.11.1 (versions < 1.2.1 unaffected, as the reclaim path did not yet exist) | [GHSA-434x-w66g-qw3r](https://github.com/advisories/GHSA-434x-w66g-qw3r) / [RUSTSEC-2026-0007](https://rustsec.org/advisories/RUSTSEC-2026-0007.html) |

## Security Posture Notes

The `bytes` crate is the zero-copy byte-buffer foundation for the Tokio async ecosystem. `BytesMut` and `Bytes` are used directly by `hyper`, `h2`, `axum`, `tonic`, and most Tokio-based network services. With ~836M all-time crates.io downloads and ~14.5M/week (as of 2026-07-08), it is one of the most widely depended-upon Rust crates.

The sole published advisory, RUSTSEC-2026-0007, is rated Moderate because exploitation requires the caller to pass a near-`usize::MAX` reserve argument, which is an unusual pattern in practice. In release builds, Rust's wrapping integer arithmetic turns the overflow silently instead of panicking, making this a realistic — if unlikely — code path in programs that set the reserve size based on external input without bounds-checking.

The project uses GitHub security advisories for disclosure. Current stable version: 1.12.0.

## Dependencies of Note

- Downstream crates pinning `bytes < 1.11.1` inherit the integer overflow in any code path calling `BytesMut::reserve` with a very large argument.
- `h2`, `hyper`, `axum`, and `tonic` all depend on `bytes::BytesMut` directly; consumers that pin old versions of these crates may transitively pull in the vulnerable `bytes`.

## Open Questions

- Audit analogous unchecked arithmetic paths in `BytesMut::extend_from_slice`, `split_to`, and `freeze` — no RustSec advisories filed for these, but the overflow pattern may recur.
- Confirm whether `hyper`, `h2`, and `tonic` have updated their `Cargo.toml` minimum `bytes` constraint to `≥ 1.11.1`.

## Related Pages

- [[rust/tokio]]
- [[rust/hyper]]
- [[rust/axum]]
- [[rust/h2]]
- [[rust/index]]

---
*Last updated: 2026-07-08 | Sources: 2*
