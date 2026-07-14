# quinn (Rust / crates.io)

**Registry:** crates.io
**Stable Version:** 0.11.11 (as of 2026-06-22)
**Weekly Downloads:** ~5.7M/week est. (quinn), ~5.8M/week est. (quinn-proto); ~225M / ~231M total downloads respectively (as of 2026-07-14)
**Repository:** https://github.com/quinn-rs/quinn
**Security Contact:** GitHub security advisories (https://github.com/quinn-rs/quinn/security)
**Disclosure Policy:** https://github.com/quinn-rs/quinn/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No public proactive audits on record.*

## Known Vulnerabilities

`quinn` is the user-facing QUIC crate; `quinn-proto` is the underlying protocol state machine. Advisories in either crate affect quinn users transitively. All five advisories below are network-reachable denial-of-service or soundness issues.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-28036 / RUSTSEC-2021-0035 / GHSA-fhv4-fx3v-77w6 | **High** (CVSS 7.5) | `quinn` crate makes unfounded assumptions about the memory layout of `std::net::SocketAddrV4` and `SocketAddrV6`, performing direct pointer casts to OS `sockaddr` structs without any standard-library layout guarantee. A future stdlib layout change would cause undefined behavior in all affected versions. Network-reachable vectors via connection establishment elevate practical severity. Affects quinn < 0.5.4, < 0.6.2. | quinn ≥ 0.5.4, ≥ 0.6.2, ≥ 0.7.0 | [RUSTSEC-2021-0035](https://rustsec.org/advisories/RUSTSEC-2021-0035.html) · [GHSA-fhv4-fx3v-77w6](https://github.com/advisories/GHSA-fhv4-fx3v-77w6) |
| CVE-2023-42805 / RUSTSEC-2023-0063 | **High** (DoS, AV:N) | `quinn-proto`: receiving a QUIC packet containing an unknown frame type causes a panic, crashing the server endpoint. No authentication is required; any network peer can send a single crafted packet to trigger the crash. Affects quinn-proto < 0.9.5 (0.9.x branch) and < 0.10.5 (0.10.x branch). | quinn-proto ≥ 0.9.5, ≥ 0.10.5 | [RUSTSEC-2023-0063](https://rustsec.org/advisories/RUSTSEC-2023-0063.html) |
| CVE-2024-45311 / RUSTSEC-2024-0373 / GHSA-vr26-jcq5-fjj8 | **High** (CVSS:3.1 7.5 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) | `quinn-proto` 0.11.0 overhauled server-side `Endpoint` handling; some post-connection-attempt cleanup paths confused the initial destination connection ID with the DCID of a subsequent packet, producing inconsistent internal state that later panics on `Endpoint::retry()` calls. Affects quinn-proto 0.11.0–0.11.6 only; versions < 0.11.0 are unaffected. | quinn-proto ≥ 0.11.7 | [RUSTSEC-2024-0373](https://rustsec.org/advisories/RUSTSEC-2024-0373.html) · [GHSA-vr26-jcq5-fjj8](https://github.com/advisories/GHSA-vr26-jcq5-fjj8) |
| CVE-2026-31812 / RUSTSEC-2026-0037 / GHSA-6xvm-j4wr-6v98 | **High** (CVSS 4.0 AV:N/AC:L/AT:N/PR:N/UI:N/VA:H) | `quinn-proto`: receiving QUIC transport parameters containing invalid values causes a panic due to unchecked `unwrap()` calls in the parameter-parsing code path. Insufficient fuzzing coverage allowed this to reach production; the fix added a dedicated fuzzing target for transport-parameter parsing. Affects quinn-proto ≥ 0.5.0, < 0.11.14; versions < 0.5.0 unaffected. | quinn-proto ≥ 0.11.14 | [RUSTSEC-2026-0037](https://rustsec.org/advisories/RUSTSEC-2026-0037.html) · [GHSA-6xvm-j4wr-6v98](https://github.com/advisories/GHSA-6xvm-j4wr-6v98) |
| RUSTSEC-2026-0185 / GHSA-4w2j-m93h-cj5j | **High** (CVSS:3.1 7.5 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) | `quinn-proto`: the `Assembler` stream-reassembly component accumulates unbounded overhead when a peer sends non-contiguous stream fragments while deliberately withholding early stream data (leaving many gaps). Callers consuming via `AsyncRead` — the common path — are fully exposed: an adversary with enough bandwidth can exhaust server memory (OOM). Disclosed 2026-06-22. Affects all quinn-proto < 0.11.15. | quinn-proto ≥ 0.11.15 | [RUSTSEC-2026-0185](https://rustsec.org/advisories/RUSTSEC-2026-0185.html) · [GHSA-4w2j-m93h-cj5j](https://github.com/advisories/GHSA-4w2j-m93h-cj5j) |

## Security Posture Notes

- **quinn** is the dominant Rust QUIC implementation, widely deployed in cloud infrastructure, CDN edge stacks, and HTTP/3 servers. The `quinn` crate wraps `quinn-proto` (the QUIC state machine) and `quinn-udp` (the platform UDP layer). Download-volume context: ~225M total (quinn) and ~231M total (quinn-proto) crates.io downloads; ~5.7M/week recent pace (90-day rolling, as of 2026-07-14).
- **DoS pattern across all five advisories:** Four of five advisories are network-reachable DoS vulnerabilities triggered by malformed or adversarial QUIC input — unknown frame types, invalid transport parameters, malformed `Endpoint` state, and unbounded reassembly. The QUIC protocol's framing flexibility creates an ongoing parser-hardening surface.
- **RUSTSEC-2026-0185 (OOM, June 2026):** Most operationally significant recent advisory. Stream reassembly has no per-connection memory cap before 0.11.15 for the described gap pattern. Deployments on quinn 0.11.14 or earlier that accept connections from untrusted peers should upgrade to ≥ 0.11.15 promptly.
- **Current stable 0.11.11 (2026-06-22)** is vulnerable to RUSTSEC-2026-0185. **quinn-proto ≥ 0.11.15** is the first fully-patched version covering all active advisories.
- **RUSTSEC-2021-0035 (soundness):** Same class as [[rust/mio]] RUSTSEC-2020-0081 — an unfounded memory-layout assumption. All affected versions predate quinn 0.7.0 and are well past end-of-life.
- **Disclosure policy:** https://github.com/quinn-rs/quinn/security/policy; private reports accepted via GitHub security advisories.

## Dependencies of Note

- **[[rust/rustls]]** — quinn relies on rustls for TLS 1.3; see [[rust/rustls]] for RUSTSEC-2024-0336 and RUSTSEC-2024-0399.
- **[[rust/ring]]** — underlying cryptographic primitive for TLS operations; see [[rust/ring]] for RUSTSEC-2025-0009.
- **[[rust/tokio]]** — quinn's async runtime dependency.

## Open Questions

- Is RUSTSEC-2026-0185 (OOM) back-patched to the 0.10.x or 0.9.x branches used in long-lived deployments?
- Are there additional unchecked `unwrap()` or fuzzing-coverage gaps in the `quinn-proto` frame decoder beyond those covered by RUSTSEC-2026-0037?
- What downstream Rust crates (HTTP/3 servers, QUIC-based messaging) carry a direct dependency on quinn and have not yet been updated past 0.11.15?

## Related Pages

- [[rust/rustls]]
- [[rust/ring]]
- [[rust/tokio]]
- [[rust/hyper]]
- [[rust/index]]

---
*Last updated: 2026-07-14 | Sources: 5 (RUSTSEC-2021-0035 / GHSA-fhv4-fx3v-77w6, RUSTSEC-2023-0063 / CVE-2023-42805, RUSTSEC-2024-0373 / GHSA-vr26-jcq5-fjj8, RUSTSEC-2026-0037 / GHSA-6xvm-j4wr-6v98, RUSTSEC-2026-0185 / GHSA-4w2j-m93h-cj5j)*
