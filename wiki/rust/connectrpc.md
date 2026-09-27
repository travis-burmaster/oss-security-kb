# connectrpc (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~323K/week est. (as of 2026-09-27)
**Repository:** https://github.com/connectrpc/connect-rust
**Security Contact:** https://github.com/connectrpc/connect-rust/security
**Disclosure Policy:** https://github.com/connectrpc/connect-rust/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2026-0304 | Moderate | **DoS via indefinite streaming request body reading** — when a streaming call terminates early (handler completion, interceptor rejection, timeout), a background task that was already reading the request body continues indefinitely; one HTTP/2 connection can hold 200 stalled streams (~800 MiB at default message size) with no server-side connection limit, allowing a single client to exhaust server capacity | 0.8.2, 0.9.1 | [RUSTSEC-2026-0304](https://rustsec.org/advisories/RUSTSEC-2026-0304.html) |

## Security Posture Notes

`connectrpc` is a Tower-based Rust implementation of the Connect RPC protocol, maintained by the ConnectRPC organization (GitHub: connectrpc/connect-rust). It supports HTTP/1.1, HTTP/2, gRPC, and gRPC-Web transports and is the reference library for building Connect-protocol services in Rust. Total crates.io downloads: ~7.25M; latest stable: 0.9.1.

RUSTSEC-2026-0304 (published 2026-09-21, fixed in 0.8.2/0.9.1 via [PR #313](https://github.com/connectrpc/connect-rust/pull/313)) describes a resource-exhaustion class: the library spawns background tasks to read request bodies for streaming calls before handler execution. When calls terminate prematurely — due to handler completion, interceptor rejection, or timeout — these background tasks continue reading with no time or size bound. The HTTP/2 protocol permits up to 200 concurrent streams per connection by default; a single connection stalling 200 streams at the 4 MiB default message size can pin ~800 MiB of server memory.

**Exposure profile by authentication model:**
- *Tower middleware authentication (before routing):* lower risk — unauthorized connections are terminated before a background task is spawned.
- *Interceptor-based or no authentication:* fully exposed — any client (unauthenticated or authenticated) can trigger the stall.

**Mitigations (besides upgrading):** apply Tower middleware for authentication before the connectrpc service layer; configure HTTP/2 connection max-age limits; enforce per-message size limits via the connectrpc API.

The fixed versions (0.8.2, 0.9.1) apply a 5-second timeout and a 1 MiB size cap to post-handler body reading.

No CVE or GHSA has been assigned to RUSTSEC-2026-0304 as of this pass (2026-09-27).

## Dependencies of Note

The Tower + hyper + tokio stack underlies connectrpc; all are independently tracked in this KB. No additional direct dependency advisories flagged.

## Open Questions

- Has a CVE or GHSA been assigned to RUSTSEC-2026-0304? Monitor rustsec/advisory-db and GitHub advisory database.
- Are there pending undisclosed advisories for earlier 0.x releases?

## Related Pages

- [[rust/tonic]] — gRPC (not ConnectRPC) Rust framework, also Tower/hyper-based; has one historical DoS advisory
- [[rust/tower-http]] — Tower HTTP middleware layer (ServeDir path traversal advisory)
- [[rust/index]]

---
*Last updated: 2026-09-27 | Sources: 2*
