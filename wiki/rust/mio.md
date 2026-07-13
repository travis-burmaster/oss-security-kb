# mio (Rust / crates.io)

**Registry:** crates.io
**Stable Version:** 1.2.1 (as of 2026-07-13)
**Repository:** https://github.com/tokio-rs/mio
**Security Contact:** security@tokio.rs (Tokio project security reports)
**Disclosure Policy:** https://github.com/tokio-rs/tokio/blob/master/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No public proactive audits on record.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-35922 / RUSTSEC-2020-0081 / GHSA-pf3p-x6qj-6j7q | **High** (local, unsound) | mio 0.7.x makes unfounded assumptions about the memory layout of `std::net::SocketAddrV4` and `SocketAddrV6`, performing direct pointer casts to OS `sockaddr` structs without any standard-library layout guarantee. If the stdlib representation changes, this triggers undefined behavior. Affects mio 0.7.0–0.7.5 only (< 0.7.0 unaffected). | 0.7.6 | [RUSTSEC-2020-0081](https://rustsec.org/advisories/RUSTSEC-2020-0081.html) · [GHSA-pf3p-x6qj-6j7q](https://github.com/advisories/GHSA-pf3p-x6qj-6j7q) |
| CVE-2024-27308 / RUSTSEC-2024-0019 / GHSA-r8w9-5wcg-vfj7 | **High** (Windows only) | Windows named-pipe implementation delivers invalidated tokens — corresponding to already-deregistered pipes — back to callers. Applications that store raw pointers inside mio tokens can encounter use-after-free conditions. Tokio ≥ 1.30.0 using an affected mio version is also vulnerable. Affects mio ≥ 0.7.2, ≤ 0.8.10 on Windows only; non-Windows platforms unaffected. | 0.8.11 | [RUSTSEC-2024-0019](https://rustsec.org/advisories/RUSTSEC-2024-0019.html) · [GHSA-r8w9-5wcg-vfj7](https://github.com/advisories/GHSA-r8w9-5wcg-vfj7) |

## Security Posture Notes

- **mio** is the foundational non-blocking I/O event loop beneath the Tokio async runtime — the dominant Rust async framework. With ~846M total crates.io downloads and ~196M recent downloads (est. ~13–15M/week), its indirect blast radius spans the overwhelming majority of production async Rust deployments.
- **RUSTSEC-2020-0081 (unsoundness):** Classified as an "unsound" Rust safety violation rather than an actively exploitable vulnerability — the assumed memory layout for `SocketAddr` held on all shipping stdlib implementations at the time of the advisory. No exploit path was demonstrated; the advisory recommends upgrading as a correctness precaution. Affects only the 0.7.0–0.7.5 range.
- **RUSTSEC-2024-0019 / CVE-2024-27308 (Windows named pipes):** More operationally significant on Windows deployments. The unsafe token-reuse path applies specifically to `mio::windows::NamedPipe::new` callers that maintain raw pointers in event tokens — a usage pattern relevant to Tokio's Windows async I/O implementation (see [[rust/tokio]]). Tokio ≥ 1.30.0 is explicitly listed as downstream-vulnerable when paired with mio ≤ 0.8.10.
- **Current stable 1.2.1 is unaffected by both advisories.** Deployments on mio 0.8.11+ and the 1.x series are clean.
- **Security policy:** Tokio project maintains a SECURITY.md and accepts private reports at security@tokio.rs; mio shares this disclosure path.

## Dependencies of Note

- **[[rust/tokio]]** — mio is tokio's primary I/O event-loop dependency. CVE-2024-27308 has explicit downstream impact on Tokio ≥ 1.30.0 paired with mio ≤ 0.8.10.
- **[[rust/hyper]]**, **[[rust/axum]]** — both rely on Tokio and therefore transitively on mio.

## Open Questions

- Are there additional unsoundness or memory-layout issues in the Linux (epoll) or macOS (kqueue) backend code paths?
- Does the upcoming mio 2.x series introduce a safer platform-abstraction layer that avoids unsafe `sockaddr` casting?

## Related Pages

- [[rust/tokio]]
- [[rust/axum]]
- [[rust/hyper]]
- [[rust/index]]

---
*Last updated: 2026-07-13 | Sources: 2 (RUSTSEC-2020-0081 / GHSA-pf3p-x6qj-6j7q, RUSTSEC-2024-0019 / GHSA-r8w9-5wcg-vfj7)*
