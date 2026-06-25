# axum (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~7.0M est. (89.5M / 90 days, as of 2026-06-25)
**Repository:** https://github.com/tokio-rs/axum
**Security Contact:** https://github.com/tokio-rs/axum/security/advisories
**Disclosure Policy:** https://github.com/tokio-rs/axum/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-25 | OSS Security KB | advisory-db lookup | automated | 1 public advisory row mapped (RUSTSEC-2022-0055 / CVE-2022-3212) across axum-core and axum | [rustsec/advisory-db](https://github.com/rustsec/advisory-db/tree/main/crates/axum-core), [github/advisory-database](https://github.com/advisories?query=axum) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-3212 / RUSTSEC-2022-0055 / GHSA-m77f-652q-wwp4 | High (DoS) | axum-core: `<bytes::Bytes as FromRequest>::from_request` imposed no default limit on request body size; a malicious or misbehaving client could stream an unbounded (or infinite) request body causing server-side OOM crash. Propagates to `axum::extract::Form`, `axum::extract::Json`, and `String` extractors via their use of `Bytes::from_request` internally. Affected: axum-core ≤ 0.2.7 and 0.3.0-rc.1; axum ≤ 0.5.15 and 0.6.0-rc.1. Patched versions enforce a 2 MB default body limit; callers needing larger limits use `DefaultBodyLimit::max(n)` or `DefaultBodyLimit::disable()`. | axum-core ≥ 0.2.8 or ≥ 0.3.0-rc.2; axum ≥ 0.5.16 or ≥ 0.6.0-rc.2 | [RUSTSEC-2022-0055](https://rustsec.org/advisories/RUSTSEC-2022-0055.html) / [GHSA-m77f-652q-wwp4](https://github.com/advisories/GHSA-m77f-652q-wwp4) |

*OSV live record: https://osv.dev/list?ecosystem=crates.io&q=axum*

## Security Posture Notes

`axum` is a high-performance, ergonomic Rust web framework built on the `tokio` async runtime and `hyper` HTTP implementation. Current stable version is 0.8.9 (~361.7M total crates.io downloads; ~89.5M in the past 90 days). Maintained by the Tokio organization; coordinated disclosure goes through GitHub Security Advisories.

**RUSTSEC-2022-0055 (August 2022):** The only published RustSec advisory for the axum family targets `axum-core`, the internal trait-implementation crate that provides the `FromRequest` extractor infrastructure. Without a default body size cap in `Bytes::from_request`, any `Form`, `Json`, or `String` extractor was vulnerable to unbounded-memory-consumption DoS from crafted or misbehaving request bodies. The fix (axum-core 0.2.8 / 0.3.0-rc.2; axum 0.5.16 / 0.6.0-rc.2) introduces a configurable 2 MB default, well behind the current stable line (0.8.x). No additional RustSec or GHSA advisories for `axum` or `axum-core` were found in the advisory databases as of this pass.

**tower-http note:** Applications using `axum` with `tower_http::services::ServeDir` or `ServeFile` for static file serving are affected by `tower-http` advisories RUSTSEC-2021-0135 and RUSTSEC-2022-0043 (file-disclosure via path traversal, both fixed in tower-http ≥ 0.2.1). These are on the `tower-http` crate, not on `axum` directly.

## Dependencies of Note

- `axum-core` — carries RUSTSEC-2022-0055 body-limit history; ensure ≥ 0.2.8.
- `hyper` — HTTP/1 and HTTP/2 implementation; see [[rust/hyper]] for parser-boundary and request-smuggling history.
- `tokio` — async runtime; see [[rust/tokio]] for its own advisory history.
- `h2` — HTTP/2 (transitive via hyper); see [[rust/h2]] for resource-exhaustion DoS history.

## Open Questions

- Verify whether any `axum` 0.7.x / 0.8.x or `axum-core` 0.4.x+ advisories have been filed since the 2022 record.
- Check whether `axum-extra` (additional extractors crate) has its own advisory surface in rustsec/advisory-db.
- Determine whether the `tower-http` file-disclosure cluster (RUSTSEC-2021-0135 / RUSTSEC-2022-0043) warrants a dedicated `tower-http` KB page.

## Related Pages

- [[rust/tokio]]
- [[rust/hyper]]
- [[rust/h2]]
- [[rust/rustls]]
- [[rust/rustls-webpki]]
- [[rust/index]]

---
*Last updated: 2026-06-25 | Sources: 2 (rustsec/advisory-db, github/advisory-database)*
