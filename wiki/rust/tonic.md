# tonic (crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~6.3M/week est. (as of 2026-08-05)
**Repository:** https://github.com/hyperium/tonic
**Security Contact:** GitHub security advisories (https://github.com/hyperium/tonic/security)
**Disclosure Policy:** GitHub security advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2024-0376 / CVE-2024-47609 / GHSA-4jwc-w2hc-78qv | Moderate (CVSS 3.1: 5.3 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L; CWE-755) | Remotely exploitable denial-of-service in `tonic::transport::Server`: certain uncovered error conditions in the TCP/TLS stream acceptance loop cause the accept loop to exit, forcing the server to terminate cleanly rather than log the error and continue. An attacker can trigger these conditions by initiating a TCP/TLS connection that produces an uncovered error state. Affects exactly tonic 0.12.2; versions below 0.12.2 are unaffected. Workaround: implement a custom accept loop. | tonic ≥ 0.12.3 | [GHSA-4jwc-w2hc-78qv](https://github.com/advisories/GHSA-4jwc-w2hc-78qv) / [RUSTSEC-2024-0376](https://rustsec.org/advisories/RUSTSEC-2024-0376.html) |

## Security Posture Notes

`tonic` is the dominant gRPC-over-HTTP/2 framework for Rust, widely used in both internal microservice infrastructure and public-facing gRPC API servers. With ~347M total crates.io downloads and ~6.3M/week (as of 2026-08-05), it is one of the most widely deployed Rust network libraries. Current stable version is 0.14.6, released well past the October 2024 fix.

RUSTSEC-2024-0376 affects only the exact version 0.12.2 — a narrow but real exposure window. The vulnerability is network-reachable without authentication, requiring only that an attacker can reach the gRPC port. The CVSS 3.1 score is 5.3 (Moderate) because impact is limited to availability (server shutdown rather than data exfiltration or privilege escalation), but an unauthenticated server shutdown is a significant operational risk for production gRPC services. The fix was published alongside the advisory in October 2024.

The root cause is missing error-type handling in the TCP/TLS accept loop: certain error variants that should be logged-and-retried instead fell through to a path that terminated the loop. The fix added exhaustive matching on the error conditions so uncovered states are handled gracefully.

The project discloses via GitHub security advisories. The hyperium/tonic monorepo also contains `tonic-health`, `tonic-reflection`, `tonic-web`, and `tonic-build`; the advisory applies specifically to the runtime transport layer in the `tonic` crate.

## Dependencies of Note

- `tonic-health`, `tonic-reflection`, `tonic-web`: workspace crates within the hyperium/tonic monorepo that depend on `tonic::transport::Server` and are thus exposed to the same accept-loop vulnerability when using 0.12.2.
- `bytes`: tonic depends on `bytes` for zero-copy buffer handling; see [[rust/bytes]] for its own advisory history (integer overflow in `BytesMut::reserve`).
- `hyper`, `h2`: tonic's underlying HTTP/2 transport layer; see [[rust/hyper]] and [[rust/h2]] for their advisory histories.
- Services pinning `tonic = "0.12.2"` exactly in `Cargo.lock` are affected; a `tonic = "0.12"` version requirement with `cargo update` would have resolved to 0.12.3+.

## Open Questions

- Confirm whether `tonic-build` (codegen crate for gRPC service stubs) carries any advisories independent of the runtime `tonic` crate.
- Review the 2025–2026 advisory landscape for 0.13.x and 0.14.x releases — the current pass confirms no advisories for those versions as of 2026-08-05.
- Assess whether deployments using `tonic` with TLS termination at a sidecar (Envoy/Istio) are shielded from the accept-loop condition versus deployments using native `tonic` TLS.

## Related Pages

- [[rust/hyper]]
- [[rust/h2]]
- [[rust/bytes]]
- [[rust/tower-http]]
- [[rust/axum]]
- [[rust/index]]

---
*Last updated: 2026-08-05 | Sources: 2*
