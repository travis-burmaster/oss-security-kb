# reqwest (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~126,450,950 (as of 2026-06-15)
**Repository:** https://github.com/seanmonstar/reqwest
**Security Contact:** none listed (no SECURITY.md confirmed in this pass)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| (none on record) | — | — | — | — |

*No package-scoped RustSec or GHSA advisory was found for `reqwest` in this pass. OSV live record: https://osv.dev/list?ecosystem=crates.io&q=reqwest*

## Security Posture Notes

`reqwest` is the dominant ergonomic HTTP client crate for Rust, providing both synchronous and async (Tokio-backed) interfaces, TLS via `rustls` or the system-native `native-tls` backend, and automatic redirect/cookie/proxy handling. Crates.io reports ~528M total downloads and ~126M recent downloads, making it one of the most widely deployed networking libraries in the Rust ecosystem.

**No direct RustSec or GHSA advisories were confirmed for `reqwest` in this advisory-review pass.** The search of the `rustsec/advisory-db` repository and the GitHub Advisory Database (code-searched for `package = "reqwest"`) returned no results scoped to this crate.

**Trust-boundary notes for downstream consumers:**
- reqwest's cross-domain redirect policy (`prev_url.host_str()` vs `curr_url.host_str()`) strips `Authorization` headers on host change. This has been cited explicitly in the 2026 GHSA-9857-6mw7-fq2m advisory for `gix-transport` as the _correct_ behavior that the curl backend lacked. Consumers relying on reqwest for authenticated cross-service HTTP should verify that their custom redirect policies preserve this stripping.
- Applications that build redirect policies on top of `reqwest::redirect::Policy` (e.g., `Policy::limited(N)`) without re-validating redirect targets against SSRF allowlists introduce SSRF bypass risk; this pattern was cited in GHSA-96ff-gc8g-wpvg for a downstream consumer. The issue is in application logic, not in reqwest itself.
- reqwest bundles or proxies to `hyper` (see [[rust/hyper]]) and optionally `rustls` or `native-tls`; consumers should track vulnerabilities in those transitive dependencies independently.

**Maintenance:** The crate is maintained by Sean McArthur (seanmonstar) under active development; no archived/unmaintained RustSec notice was found. The project does not have a published `SECURITY.md` as of this pass — private disclosure should be directed to the GitHub repository security tab.

## Dependencies of Note

- [[rust/hyper]] — used as the underlying HTTP/1 and HTTP/2 transport; see that page for its advisory history.
- `rustls` / `native-tls` — TLS backends; `native-tls` delegates to the system OpenSSL/SChannel/Secure Transport.
- [[rust/tokio]] — async runtime dependency for the async interface.

## Open Questions

- Does reqwest have a private security contact or HackerOne program? The absence of a `SECURITY.md` is a gap; a future pass should file a documentation note if nothing surfaces.
- Are there any unpublished or embargoed advisories for the `native-tls` TLS-backend path that could affect reqwest consumers?
- Track RustSec advisory-db for new `reqwest` entries — the high download volume makes it a likely target for future research.

## Related Pages

- [[rust/hyper]]
- [[rust/tokio]]
- [[rust/index]]

---
*Last updated: 2026-06-15 | Sources: 2 (rustsec/advisory-db code search, crates.io API)*
