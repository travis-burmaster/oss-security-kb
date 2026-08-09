# prost (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** 121,999,779 (as of 2026-08-09)
**Repository:** https://github.com/tokio-rs/prost
**Security Contact:** https://github.com/tokio-rs/prost/security
**Disclosure Policy:** GitHub private vulnerability reporting (tokio-rs org standard)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-08-09 | oss-security-kb | advisory-db sweep | automated (RustSec + GHSA search) | 1 confirmed advisory | [RUSTSEC-2020-0002](https://rustsec.org/advisories/RUSTSEC-2020-0002.html) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-35858 / RUSTSEC-2020-0002 / GHSA-gv73-9mwv-fwgq | **Critical** CVSS 9.8 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | Stack overflow via deeply nested / recursive protobuf message decoding from untrusted input. On x86 (stack probes present), results in controlled DoS. On ARM and other architectures without stack probes, stack overflow is unsound: adjacent memory can be corrupted, enabling potential memory corruption or remote code execution. CWE-787. | ≥ 0.6.1 | [RUSTSEC-2020-0002](https://rustsec.org/advisories/RUSTSEC-2020-0002.html) / [GHSA-gv73-9mwv-fwgq](https://github.com/advisories/GHSA-gv73-9mwv-fwgq) |

## Security Posture Notes

prost is the dominant Protocol Buffers implementation for Rust, maintained under the tokio-rs GitHub organization (Tokio async runtime umbrella). It is a foundational dependency for tonic (gRPC), and is widely used in cloud-native, data-pipeline, and networking applications; ~524M total crates.io downloads and ~122M/week (2026-08-09).

The single confirmed advisory (RUSTSEC-2020-0002, disclosed 2020-01-16) was introduced at project inception and fixed in 0.6.1. The root cause is unbounded recursion in the protobuf wire-format decoder: message fields whose types are themselves messages are decoded recursively, and an attacker-controlled protobuf message with sufficient nesting depth will exhaust the stack. On x86 this causes a controlled stack overflow (SIGSEGV / SEH exception — DoS). On ARM and architectures without hardware stack-guard pages the overflow is unsound and can overwrite adjacent stack frames or heap metadata, enabling memory corruption with potential for arbitrary code execution.

The current stable release (0.14.4) is not affected. All users should confirm they are on ≥ 0.6.1; most applications running modern Rust toolchains will be on a much newer release.

Downstream blast radius is high because protobuf is frequently used to deserialize data arriving from the network or from untrusted third parties. Any application using prost to decode externally sourced protobuf messages while running a version < 0.6.1 is vulnerable.

## Dependencies of Note

- **bytes** — used for zero-copy buffer management; covered at [[rust/bytes]]
- **tonic** — gRPC framework built on prost; covered at [[rust/tonic]]

## Open Questions

- No advisories on record for prost ≥ 0.6.1. Monitor for new disclosures as the protobuf schema / custom `Message` derive macros evolve.
- Check whether any downstream tonic / gRPC consumers pin an old prost version that could re-introduce the stack-overflow exposure.

## Related Pages

- [[rust/tonic]]
- [[rust/bytes]]
- [[rust/index]]

---
*Last updated: 2026-08-09 | Sources: 2 (RUSTSEC advisory DB, GitHub Advisory Database)*
