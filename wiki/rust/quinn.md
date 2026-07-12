# quinn (crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~9M/week est. (as of 2026-07-12)
**Repository:** https://github.com/quinn-rs/quinn
**Security Contact:** none listed (GitHub security advisories)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-28036 / RUSTSEC-2021-0035 / GHSA-fhv4-fx3v-77w6 | High (CVSS 3.1 7.5 — AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N; informational unsound) | Invalid memory layout assumption for `std::net::SocketAddr`: quinn cast `SocketAddrV4` and `SocketAddrV6` pointers directly to the C `sockaddr` representation without any layout guarantee from the Rust standard library. If the stdlib internal layout were to diverge in a future update, the cast produces undefined behavior (invalid memory access, potential information disclosure). Marked `informational = "unsound"` in RustSec; no confirmed in-the-wild exploitation because the stdlib layout has not changed. | 0.5.4, 0.6.2, or ≥ 0.7.0 | [RUSTSEC-2021-0035](https://rustsec.org/advisories/RUSTSEC-2021-0035.html); [GHSA-fhv4-fx3v-77w6](https://github.com/advisories/GHSA-fhv4-fx3v-77w6) |

## Security Posture Notes

`quinn` is a pure-Rust implementation of the QUIC transport protocol (RFC 9000), providing a foundation for HTTP/3 and other QUIC-based applications. It is used by CDN edge clients, cloud-infrastructure tooling, and the `h3` crate. The crate is actively maintained by the quinn-rs organization.

The RUSTSEC-2021-0035 advisory (published 2021-03-04) flags an unsound memory cast in network address conversion code. The `informational` classification in RustSec indicates a soundness violation that has not caused confirmed exploitation, rather than an actively triggerable vulnerability. The fix in 0.5.4 / 0.6.2 / ≥ 0.7.0 replaces the direct pointer cast with a properly guaranteed conversion via `socket2` or libc bindings.

Current stable: **0.11.11** (released 2026-06). No further open RustSec advisories.

**Total crates.io downloads:** ~223M (as of 2026-07-12).

## Dependencies of Note

- Depends on `rustls` (or optionally `aws-lc-rs` / `ring`) for TLS — see [[rust/rustls]] and [[rust/ring]] for those advisory histories.
- The `h3` crate builds atop `quinn`; any quinn vulnerability has direct HTTP/3 impact.

## Open Questions

- Track whether QUIC-protocol-level vulnerabilities (amplification attacks, version-negotiation downgrade) surface in quinn specifically.
- Audit the current `unsafe` surface in quinn's socket abstraction layer in the 0.7.x+ rewrite.

## Related Pages

- [[rust/rustls]]
- [[rust/ring]]
- [[rust/h2]]
- [[rust/index]]

---
*Last updated: 2026-07-12 | Sources: 2*
