# tower-http (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~7.5M/week estimated (as of 2026-07-06); 331,097,666 total downloads; ~98.3M recent (last ~90 days)
**Repository:** https://github.com/tower-rs/tower-http
**Security Contact:** GitHub Security Advisories — https://github.com/tower-rs/tower-http/security
**Disclosure Policy:** https://github.com/tower-rs/tower-http/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-07-06 | OSS Security KB | RustSec advisory-db lookup | automated | 2 RustSec advisory rows mapped (RUSTSEC-2021-0135, RUSTSEC-2022-0043; same underlying vulnerability) | [rustsec/advisory-db](https://github.com/rustsec/advisory-db) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2022-0043 / GHSA-qrqq-9c63-xfrg | Moderate (file-disclosure) | `tower_http::services::fs::ServeDir` on Windows accepts absolute Windows-style paths embedded in URL segments (e.g. `/foo/bar/c:/windows/web/screen/img101.png`), bypassing the configured serve directory and returning files from arbitrary filesystem locations. Windows deployments only; Linux/macOS unaffected. | ≥ 0.2.1 (main), ≥ 0.1.3 (legacy 0.1.x) | [RUSTSEC-2022-0043](https://rustsec.org/advisories/RUSTSEC-2022-0043.html) |
| RUSTSEC-2021-0135 | Moderate (file-disclosure) | Predecessor / duplicate record for the same `ServeDir` Windows absolute-path traversal as RUSTSEC-2022-0043; both IDs reference the same upstream fix (tower-rs/tower-http#204) and the same fixed versions. RUSTSEC-2022-0043 / GHSA-qrqq-9c63-xfrg is the canonical GHSA-aliased record. | ≥ 0.2.1 (main), ≥ 0.1.3 (legacy 0.1.x) | [RUSTSEC-2021-0135](https://rustsec.org/advisories/RUSTSEC-2021-0135.html) |

*OSV live record: https://osv.dev/list?ecosystem=crates.io&q=tower-http*

## Security Posture Notes

`tower-http` provides HTTP-specific Tower middleware and utilities (compression, tracing, auth, CORS, static-file serving, request/response logging) and is the de facto middleware layer for the axum web framework. It runs on the Tokio async runtime and is built on top of `hyper`. With 331M total downloads and approximately 7.5M weekly downloads driven by axum's rapid adoption, its blast radius spans a large proportion of the Rust async web ecosystem. Latest stable version: **0.7.0** (released June 15, 2026).

**The single recorded vulnerability class** (RUSTSEC-2022-0043 / RUSTSEC-2021-0135) is a Windows-only path traversal in the `ServeDir` static-file service. The flaw permits absolute Windows-style drive paths embedded in URL segments (e.g., `c:/windows/...`) to escape the configured serve-directory root and retrieve arbitrary files. It was introduced with the `ServeDir` service and fixed in PR #204, shipped in ≥ 0.2.1 (0.2.x branch) and ≥ 0.1.3 (legacy 0.1.x branch). Linux, macOS, and other Unix-like platforms are unaffected.

**Two RustSec IDs, one vulnerability:** The RustSec advisory database carries RUSTSEC-2021-0135 (filed in the 2021 ID batch) and RUSTSEC-2022-0043 (filed January 2022 with the GHSA alias GHSA-qrqq-9c63-xfrg) for the same underlying `ServeDir` flaw and the same fix. They reference the same upstream pull request (#204). Consumers tracking RustSec IDs should treat both as referring to the same issue; RUSTSEC-2022-0043 / GHSA-qrqq-9c63-xfrg is the authoritative record.

**GitHub advisory page** for tower-rs/tower-http shows "no published security advisories," confirming the two RUSTSEC records were filed directly through the RustSec advisory database rather than via GitHub's advisory flow.

**Current safe version:** ≥ 0.7.0 (latest stable). Any version ≥ 0.2.1 resolves the ServeDir traversal on Windows.

## Dependencies of Note

- `tower` — core service abstraction; no direct advisories on record (see RustSec advisory-db for `tower`)
- `hyper` — HTTP client/server foundation; see [[rust/hyper]] for its own advisory history (HTTP/1 request-smuggling, header-injection, TLS hostname-verification history)

## Open Questions

- Verify whether `tower_http::services::fs::ServeDir`'s path handling on Windows with case-insensitive filesystems or UNC paths (e.g. `\\server\share\`) could introduce additional escape conditions beyond what RUSTSEC-2022-0043 addresses.
- Monitor `ServeDir` security surface as tower-http gains new middleware features in the 0.7.x line (HTTP/2, enhanced tracing).

## Related Pages

- [[rust/axum]]
- [[rust/hyper]]
- [[rust/tokio]]
- [[rust/index]]

---
*Last updated: 2026-07-06 | Sources: 2*
