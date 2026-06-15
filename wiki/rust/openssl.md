# openssl (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** unknown (as of 2026-06-15)
**Repository:** https://github.com/sfackler/rust-openssl
**Security Contact:** https://github.com/sfackler/rust-openssl/security
**Disclosure Policy:** https://github.com/sfackler/rust-openssl/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2016-0001 / CVE-2016-10931 / GHSA-34p9-f4q3-c4r7 | High (CVSS 8.1) | SSL/TLS certificate verification off by default; no hostname verification API — MitM possible if developers did not configure verification manually. `SslConnector`/`SslAcceptor` added to enforce verification. | >= 0.9.0 | [RUSTSEC-2016-0001](https://rustsec.org/advisories/RUSTSEC-2016-0001.html) |
| RUSTSEC-2018-0010 / CVE-2018-20997 / GHSA-xjxc-vfw2-cg96 | Critical (CVSS 9.8) | Use-after-free in CMS signing: structures accessed after deallocation, enabling memory corruption. Unaffected: < 0.10.8. | >= 0.10.9 | [RUSTSEC-2018-0010](https://rustsec.org/advisories/RUSTSEC-2018-0010.html) |
| RUSTSEC-2023-0022 / GHSA-3gxf-9r58-2ghg | Medium | `X509NameBuilder::build` thread-safety: OpenSSL's internal `modified` bit on `X509_NAME` objects makes the returned value non-thread-safe even when callers do not modify it. | >= 0.10.48 | [RUSTSEC-2023-0022](https://rustsec.org/advisories/RUSTSEC-2023-0022.html) |
| RUSTSEC-2023-0023 / GHSA-9qwg-crg9-m2vc | High | `SubjectAlternativeName` and `ExtendedKeyUsage::other` pass caller-controlled strings through OpenSSL's `X509V3_EXT_nconf` mini-language, which can perform **arbitrary file reads**. Reported by David Benjamin (Google). | >= 0.10.48 | [RUSTSEC-2023-0023](https://rustsec.org/advisories/RUSTSEC-2023-0023.html) |
| RUSTSEC-2023-0024 | Medium | `X509Extension::new` and `X509Extension::new_nid`: null pointer dereference / panic when `context` is `None` with certain extension types — denial of service. Reported by David Benjamin (Google). | >= 0.10.48 | [RUSTSEC-2023-0024](https://rustsec.org/advisories/RUSTSEC-2023-0024.html) |
| RUSTSEC-2023-0044 | Medium | `X509VerifyParamRef::set_host`: calling with an empty string invokes `strlen` on that pointer, reading arbitrary memory until a NUL byte — information exposure. | >= 0.10.55 | [RUSTSEC-2023-0044](https://rustsec.org/advisories/RUSTSEC-2023-0044.html) |
| RUSTSEC-2023-0072 | Informational | `X509StoreRef::objects` returns a shared reference into an OpenSSL structure without accounting for interior mutability, allowing OpenSSL to modify the underlying data — unsound. Informational advisory; replaced by `X509StoreRef::all_certificates`. | >= 0.10.60 | [RUSTSEC-2023-0072](https://rustsec.org/advisories/RUSTSEC-2023-0072.html) |
| RUSTSEC-2024-0357 / GHSA-q445-7m23-qrmw | Medium | `MemBio::get_buf` invokes `slice::from_raw_parts` with a null pointer on empty buffers — undefined behavior; debug builds panic. | >= 0.10.66 | [RUSTSEC-2024-0357](https://rustsec.org/advisories/RUSTSEC-2024-0357.html) |
| RUSTSEC-2025-0004 / CVE-2025-24898 / GHSA-rpmj-rpgj-qmpm | High | `ssl::select_next_proto` returns a slice with a lifetime bound to the `client` argument but pointing into the `server` buffer — use-after-free when the server buffer is dropped first (e.g., `to_vec()` inside an ALPN callback). Can cause server crash or memory disclosure. | >= 0.10.70 | [GHSA-rpmj-rpgj-qmpm](https://github.com/sfackler/rust-openssl/security/advisories/GHSA-rpmj-rpgj-qmpm) |
| RUSTSEC-2025-0022 / GHSA-4fcv-w3qc-ppgg | High | `Md::fetch` and `Cipher::fetch`: passing `Some(...)` to the `properties` argument causes use-after-free — `CString` is dropped before OpenSSL reads the pointer, causing OpenSSL to treat properties as an empty string and potentially corrupt state. | >= 0.10.72 | [RUSTSEC-2025-0022](https://rustsec.org/advisories/RUSTSEC-2025-0022.html) |

*OSV link: https://osv.dev/list?ecosystem=crates.io&q=openssl*

## Security Posture Notes

This page tracks the `openssl` crate (sfackler/rust-openssl), which provides Rust bindings to the libssl/libcrypto C library. The crate does **not** bundle OpenSSL; it links to the system or a vendored OpenSSL installation. CVEs in the upstream OpenSSL C library are therefore not directly tracked here — see `[[linux/openssl]]` for upstream C library history.

The crate has an active SECURITY.md and a GitHub Security Advisories disclosure path. Most advisories in the history above are Rust-binding-specific issues: incorrect lifetime bounds, missing `unsafe` invariants, API defaults that violated caller expectations, or wrapper functions that did not sanitize inputs before passing them to OpenSSL's C mini-languages.

Notable patterns:
- The 2023-03-24 cluster (RUSTSEC-2023-0022 / 0023 / 0024) was filed together and fixed in a single PR (#1854), addressing file-read, thread-safety, and DoS vectors introduced by the raw `X509V3_EXT_nconf` parser exposure.
- RUSTSEC-2023-0023 (arbitrary file read via SAN strings) is the most impactful of the cluster: if an attacker can influence the string passed to `SubjectAlternativeName` or `ExtendedKeyUsage::other`, they can read files accessible to the process.
- RUSTSEC-2025-0004 and RUSTSEC-2025-0022 (both 2025) are lifetime/use-after-free issues in newer OpenSSL 3.x-specific APIs, indicating the binding surface continues to carry safety risk as new upstream APIs are wrapped.

## Dependencies of Note

- Upstream libssl/libcrypto (system or vendored): upstream OpenSSL C library CVEs are a separate but related surface.
- `openssl-sys` crate: the low-level FFI layer that `openssl` builds on; check `openssl-sys` advisories separately.

## Open Questions

- Track whether RUSTSEC-2025-0022 (Md::fetch/Cipher::fetch use-after-free) has a distro-level advisory; the affected versions span 0.10.39–0.10.71.
- Verify weekly download count via crates.io once API access is available; crate is expected to rank highly among Rust crypto dependencies.
- Confirm if `openssl-sys` carries its own separate advisory history that needs a linked page.

## Related Pages

- [[rust/hyper]] (depends on openssl for TLS in some configurations)
- [[linux/openssl]] (upstream C library history)
- [[rust/index]]

---
*Last updated: 2026-06-15 | Sources: 10 RustSec advisories (rustsec/advisory-db via raw.githubusercontent.com + GitHub code search)*
