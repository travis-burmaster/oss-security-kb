# actix-web (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~663,000 (as of 2026-06-24)
**Repository:** https://github.com/actix/actix-web
**Security Contact:** https://github.com/actix/actix-web/security/advisories
**Disclosure Policy:** https://github.com/actix/actix-web/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-24 | OSS Security KB | advisory-db lookup | automated | 8 public advisory rows mapped across actix-web / actix-http / actix-files | [rustsec/advisory-db](https://github.com/rustsec/advisory-db/tree/main/crates/actix-web), [github/advisory-database](https://github.com/advisories?query=actix-web) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2018-25024 / RUSTSEC-2018-0019 / GHSA-9qj6-4rfq-vm84 | Critical (CVSS 9.8) | actix-web: unsound coercion of immutable references to mutable references, enabling memory corruption / out-of-bounds write in < 0.7.19 | actix-web 0.7.19 | [GHSA-9qj6-4rfq-vm84](https://github.com/advisories/GHSA-9qj6-4rfq-vm84) |
| CVE-2018-25025 / RUSTSEC-2018-0019 / GHSA-fgfm-hqjw-3265 | Critical (CVSS 9.8) | actix-web: unsound lifetime extension of string references leading to use-after-free / memory corruption in < 0.7.15 | actix-web 0.7.15 | [GHSA-fgfm-hqjw-3265](https://github.com/advisories/GHSA-fgfm-hqjw-3265) |
| CVE-2018-25026 / RUSTSEC-2018-0019 / GHSA-7x36-h62w-vw65 | Critical (CVSS 9.8) | actix-web: unsound application of Send marker to non-thread-safe objects enabling data races and memory corruption in < 0.7.15 | actix-web 0.7.15 | [GHSA-7x36-h62w-vw65](https://github.com/advisories/GHSA-7x36-h62w-vw65) |
| CVE-2020-35901 / RUSTSEC-2020-0048 / GHSA-v3j6-xf77-8r9c | High (CVSS 9.1) | actix-http (1.x): BodyStream use-after-free due to unpinned buffer; BodyStream did not require MessageBody to be pinned, enabling memory corruption when buffer moved | actix-http 2.0.0 (actix-web 3.0) | [GHSA-v3j6-xf77-8r9c](https://github.com/advisories/GHSA-v3j6-xf77-8r9c) |
| CVE-2021-38512 / GHSA-8928-2fgm-6x9x | High (CVSS 7.5) | actix-http (< 2.2.1): HTTP/1 request smuggling; malformed framing not properly rejected, enabling backend desynchronization in proxy deployments | actix-http 2.2.1 | [GHSA-8928-2fgm-6x9x](https://github.com/advisories/GHSA-8928-2fgm-6x9x) |
| GHSA-8v2v-wjwg-vx6r | Moderate | actix-files (< 0.6.10): information exposure — Files::new() with a non-existent folder path defaults to an empty path, causing the service to resolve and serve arbitrary relative-path files from the working directory | actix-files 0.6.10 | [GHSA-8v2v-wjwg-vx6r](https://github.com/advisories/GHSA-8v2v-wjwg-vx6r) |
| GHSA-gcqf-3g44-vc9p | Moderate | actix-files (< 0.6.10): panic DoS via empty Range header on static-file GET requests; HttpRange::parse() returns Ok(vec![]) for empty input, triggering an unwrap-on-empty panic at named.rs:534 — process crash if panic="abort" | actix-files 0.6.10 | [GHSA-gcqf-3g44-vc9p](https://github.com/advisories/GHSA-gcqf-3g44-vc9p) |
| GHSA-xhj4-vrgc-hr34 | Medium (CVSS 4.0) | actix-http (≤ 3.12.0): CL.TE HTTP/1.1 request smuggling — requests carrying both Content-Length and Transfer-Encoding: chunked accepted rather than rejected; enables backend desynchronization in CL.TE proxy deployments | actix-http 3.12.1 | [GHSA-xhj4-vrgc-hr34](https://github.com/advisories/GHSA-xhj4-vrgc-hr34) |

*OSV live record: https://osv.dev/list?ecosystem=crates.io&q=actix-web*

## Security Posture Notes

`actix-web` is a high-performance Rust web framework (~71M total crates.io downloads, ~663K/week as of 2026-06-24). Current version is 4.14.0. The crate is maintained by the Actix organization; security disclosures go through GitHub Security Advisories.

The framework's advisory history divides into three eras:

**2018 memory safety cluster (RUSTSEC-2018-0019):** Three distinct GHSA records share a single RustSec advisory for pre-0.7.19 versions of the main `actix-web` crate. All three represent unsafe Rust patterns — unsound ref coercion, lifetime extension, and Send marker misapplication — that were resolved through a comprehensive refactoring of the internal architecture. These issues affect only old 0.x releases and are well past the fix boundary in any maintained deployment.

**2020–2021 actix-http parser / memory-safety cluster:** The `actix-http` companion crate (a direct dependency of `actix-web`) accumulated two advisories: a use-after-free in `BodyStream` pinning semantics (RUSTSEC-2020-0048 / CVE-2020-35901, fixed in actix-http 2.0.0 / actix-web 3.0) and an HTTP/1 request-smuggling record (CVE-2021-38512, fixed in actix-http 2.2.1). Both are patched in the 3.x and 4.x lines.

**2026 actix-files / actix-http cluster:** Two Moderate advisories for `actix-files` were published in February 2026 (GHSA-8v2v-wjwg-vx6r information exposure; GHSA-gcqf-3g44-vc9p DoS on empty Range header — both fixed in actix-files 0.6.10) followed by a Medium HTTP/1.1 CL.TE request-smuggling advisory for `actix-http` ≤ 3.12.0 (GHSA-xhj4-vrgc-hr34, fixed in actix-http 3.12.1, published April 2026). Users of `actix-web` 4.x should ensure `actix-http` resolves to ≥ 3.12.1 and `actix-files` to ≥ 0.6.10.

The project provides coordinated disclosure via GitHub Security Advisories. No SECURITY.md in the root as of this pass; the GitHub Security tab is the primary disclosure path.

## Dependencies of Note

- `actix-http` — direct dependency carrying the BodyStream use-after-free (CVE-2020-35901) and CL.TE request-smuggling (GHSA-xhj4-vrgc-hr34) history; ensure ≥ 3.12.1.
- `actix-files` — optional file-serving companion crate with two 2026 Moderate advisories; ensure ≥ 0.6.10 if used.
- `tokio` — async runtime; see [[rust/tokio]] for its own advisory history.
- `h2` — HTTP/2 implementation (transitive); see [[rust/h2]] for resource-exhaustion DoS history.

## Open Questions

- Confirm whether `actix-web-lab` (companion crate) host-header-poisoning advisory GHSA-vhj5-x93p-67jw (CVE-2025-63762, March 2026) is in scope for a separate page or should be noted here.
- Check whether `actix-http` 4.x (if released) introduces new advisory surface beyond the 3.x CL.TE fix.
- Monitor rustsec/advisory-db for new actix-web crate advisories after 0.7.19 (4.x line).

## Related Pages

- [[rust/tokio]]
- [[rust/h2]]
- [[rust/hyper]]
- [[rust/index]]

---
*Last updated: 2026-06-24 | Sources: 4 (rustsec/advisory-db, github/advisory-database, crates.io API, actix-web GitHub Security Advisories)*
