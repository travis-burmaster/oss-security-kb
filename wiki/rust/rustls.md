# rustls (crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~165,008,339 (as of 2026-06-21)
**Repository:** https://github.com/rustls/rustls
**Security Contact:** https://github.com/rustls/rustls/security/advisories
**Disclosure Policy:** https://github.com/rustls/rustls/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-21 | OSS Security KB | advisory-db lookup | automated | 2 public advisories mapped (DoS) | [rustsec/advisory-db](https://github.com/rustsec/advisory-db/tree/main/crates/rustls) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-32650 / RUSTSEC-2024-0336 / GHSA-6g7w-8wpp-frhj | High — CVSS 7.5 (AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) — DoS | `rustls::ConnectionCommon::complete_io` enters an infinite loop when a peer sends a `close_notify` alert during the TLS handshake phase. Affects code using `rustls::Stream` and `rustls::StreamOwned`; rustls-tokio and rustls-ffi are not affected (those implementations do not call `complete_io`). All 0.20.x versions are affected; fix was backported to 0.21.x and 0.22.x. | 0.21.11, 0.22.4, 0.23.5 | [RUSTSEC-2024-0336](https://rustsec.org/advisories/RUSTSEC-2024-0336.html) |
| CVE-2024-11738 / RUSTSEC-2024-0399 / GHSA-qg5g-gv98-5ffh | Medium — DoS | A defect introduced in 0.23.13 causes a panic in `Acceptor::accept()` when a TLS ClientHello message arrives in fragmented records. Affects servers using the `Acceptor` API, tokio-rustls `LazyConfigAcceptor`, and rustls-ffi `rustls_acceptor_accept`; tokio-rustls `TlsAcceptor` is not affected. | 0.23.18 | [RUSTSEC-2024-0399](https://rustsec.org/advisories/RUSTSEC-2024-0399.html) |

*OSV live record: https://osv.dev/list?ecosystem=crates.io&q=rustls*

## Security Posture Notes

`rustls` is the dominant pure-Rust TLS implementation, used as the default TLS backend for `reqwest`, `hyper`, and many web frameworks across the Rust ecosystem. With ~719M total downloads and ~165M recent downloads it has very high ecosystem blast radius. Both published advisories are denial-of-service flaws; no confidentiality or integrity advisory has been filed against the `rustls` crate itself.

The project is actively maintained by the rustls team (which also provides security-only maintenance for `ring`). Current version 0.23.40 (released 2026-04-28) is well past all known fix boundaries.

Security disclosures are coordinated through GitHub Security Advisories with private GHSA drafts. The project publishes advisories via the GitHub security advisories page for the repository.

`rustls-webpki`, the certificate-path validation dependency of `rustls`, has five independent RUSTSEC advisories filed through 2026 (RUSTSEC-2023-0053, RUSTSEC-2026-0049, RUSTSEC-2026-0098, RUSTSEC-2026-0099, RUSTSEC-2026-0104) covering certificate-path CPU exhaustion and name-constraints / revocation-checking bugs. These are dependency-level risks — rustls consumers should verify `rustls-webpki` is pinned to the patched version for each record.

## Dependencies of Note

- `rustls-webpki` — certificate path validation; 5 independent RUSTSEC advisories through 2026; always pin to latest patched version.
- `ring` — cryptographic primitives; RUSTSEC-2025-0009 (AES/QUIC panic DoS, fixed in 0.17.12); 0.16.x unmaintained (RUSTSEC-2025-0010). See [[rust/ring]].
- `aws-lc-rs` — alternative cryptographic backend in 0.23.x; no published advisory at time of this pass.

## Open Questions

- Monitor rustsec/advisory-db for new `rustls-webpki` records: four advisories were filed in 2026 alone.
- Check whether `rustls-ffi` and `tokio-rustls` carry advisories that are not back-aliased to the top-level `rustls` record.

## Related Pages

- [[rust/ring]]
- [[rust/reqwest]]
- [[rust/hyper]]
- [[rust/index]]

---
*Last updated: 2026-06-21 | Sources: 3 (rustsec/advisory-db, github/advisory-database, crates.io API)*
