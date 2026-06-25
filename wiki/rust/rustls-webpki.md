# rustls-webpki (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~12.1M est. (156.8M / 90 days, as of 2026-06-25)
**Repository:** https://github.com/rustls/webpki
**Security Contact:** https://github.com/rustls/webpki/security/advisories
**Disclosure Policy:** https://github.com/rustls/webpki/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-25 | OSS Security KB | advisory-db lookup | automated | 5 advisory rows mapped for rustls-webpki (RUSTSEC-2023-0053, RUSTSEC-2026-0049, RUSTSEC-2026-0098, RUSTSEC-2026-0099, RUSTSEC-2026-0104) plus 1 row for predecessor crate webpki (RUSTSEC-2023-0052) | [rustsec/advisory-db](https://github.com/rustsec/advisory-db/tree/main/crates/rustls-webpki), [github/advisory-database](https://github.com/rustls/webpki/security/advisories) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2023-0053 | High (CVSS 7.5, DoS) | CPU denial of service in certificate path building: path-building time was exponential in the number of candidate certificates at each step. Both TLS clients and TLS servers accepting client certificates are affected. Reoccurrence of the upstream issue from CVE-2018-16875 / RUSTSEC-2023-0052 (see predecessor crate below). Fix introduces a budget of 100 signature verification operations per path-building session. | ≥ 0.100.2 (0.100.x line) or ≥ 0.101.4 | [RUSTSEC-2023-0053](https://rustsec.org/advisories/RUSTSEC-2023-0053.html) |
| RUSTSEC-2026-0049 / GHSA-pwjx-qhcg-rvj4 | Moderate (revocation bypass) | CRLs not considered authoritative by Distribution Point due to faulty matching: when a certificate had more than one `distributionPoint`, only the first was checked against each CRL's `IssuingDistributionPoint`; subsequent distribution points were silently ignored. Under `UnknownStatusPolicy::Allow` this caused revoked certificates to pass revocation checking. Under the default `UnknownStatusPolicy::Deny` the result is `Error::UnknownRevocationStatus` (safe but incorrect). Exploiting maliciously requires compromising a trusted issuing CA. Unaffected: versions before 0.102.0-alpha.0 (CRL distribution-point matching not yet implemented). | ≥ 0.103.10 | [GHSA-pwjx-qhcg-rvj4](https://github.com/advisories/GHSA-pwjx-qhcg-rvj4) |
| RUSTSEC-2026-0098 / GHSA-965h-392x-2mh5 | Moderate (name constraint bypass) | URI name constraints ignored and accepted: `rustls-webpki` provides no API for asserting URI names and its URI name constraint logic was unimplemented, causing URI name constraints in certificates to be silently accepted rather than rejected. Fix unconditionally rejects URI name constraints. Reachable only after signature verification; requires certificate misissuance to exploit. | ≥ 0.103.12 or ≥ 0.104.0-alpha.6 | [GHSA-965h-392x-2mh5](https://github.com/advisories/GHSA-965h-392x-2mh5) |
| RUSTSEC-2026-0099 / GHSA-xgp8-3hg3-c2mh | Moderate (name constraint bypass) | DNS wildcard name constraint bypass: a permitted-subtree name constraint for a specific hostname (e.g., `accept.example.com`) incorrectly authorized certificates asserting a wildcard (e.g., `*.example.com`), allowing names like `reject.example.com` to pass. Mirrors CVE-2025-61727. Reachable only after signature verification; requires certificate misissuance to exploit. | ≥ 0.103.12 or ≥ 0.104.0-alpha.6 | [GHSA-xgp8-3hg3-c2mh](https://github.com/advisories/GHSA-xgp8-3hg3-c2mh) |
| RUSTSEC-2026-0104 | High (DoS) | CRL parsing panic DoS (pre-auth): a syntactically valid empty `BIT STRING` in the `onlySomeReasons` field of an `IssuingDistributionPoint` CRL extension triggers a panic via `BorrowedCertRevocationList::from_der` or `OwnedCertRevocationList::from_der`. The panic is reachable **prior to** CRL signature verification — a network attacker who can supply a malicious CRL can crash any application using CRL-based revocation checking without needing a valid certificate. Affects only applications that use CRL verification. | ≥ 0.103.13 or ≥ 0.104.0-alpha.7 | [RUSTSEC-2026-0104](https://rustsec.org/advisories/RUSTSEC-2026-0104.html) |

### Predecessor crate (`webpki`)

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2023-0052 / GHSA-8qv2-5vq6-g2g7 | High (CVSS 7.5, DoS) | webpki (original `briansmith/webpki`): same CPU DoS in certificate path building as RUSTSEC-2023-0053 — exponential time with candidate certificates at each step. Partial fix in 0.22.1; full fix in 0.22.2. Users on the legacy `webpki` crate (not `rustls-webpki`) should pin to ≥ 0.22.2. | ≥ 0.22.2 | [RUSTSEC-2023-0052](https://rustsec.org/advisories/RUSTSEC-2023-0052.html) |

*OSV live record: https://osv.dev/list?ecosystem=crates.io&q=rustls-webpki*

## Security Posture Notes

`rustls-webpki` is the X.509 certificate verification engine used by `rustls`, the dominant pure-Rust TLS implementation. It is a fork of Brian Smith's original `webpki` crate, now maintained under the `rustls` organization. Current stable version is 0.103.13 (~601.5M total crates.io downloads; ~156.8M in the past 90 days). Every Rust application that uses `rustls` for TLS depends on this crate for certificate chain validation, making its security posture directly relevant to a very large fraction of Rust network code.

**2023 path-building CPU DoS cluster:** Both `rustls-webpki` (RUSTSEC-2023-0053) and its predecessor `webpki` (RUSTSEC-2023-0052) had the same exponential-time certificate path-building vulnerability, published simultaneously in August 2023. The flaw is a reoccurrence of CVE-2018-16875, which was only partially patched in older `webpki` releases. The fix is a hard budget of 100 signature verification operations per path-building session. TLS clients (validating server certificates) and TLS servers accepting client certificates are both affected. The fix boundary for `rustls-webpki` is 0.100.2 / 0.101.4; the predecessor `webpki` fix boundary is 0.22.2.

**2026 CRL revocation cluster:** Two CRL-specific advisories published in 2026. RUSTSEC-2026-0049 (March 2026) is a logic bug in CRL distribution point matching: certificates with multiple CRL distribution points may have revocation status incorrectly computed because only the first distribution point was matched against CRL issuance data. Under `UnknownStatusPolicy::Allow` a revoked credential could be accepted. RUSTSEC-2026-0104 (April 2026) is more severe from a network-attacker perspective: a crafted CRL with an empty `BIT STRING` in `onlySomeReasons` panics the parser before signature verification, enabling an unauthenticated DoS against any service using CRL-based revocation. Users enabling CRL verification must be on 0.103.13+ for full protection.

**2026 name constraint cluster:** RUSTSEC-2026-0098 and RUSTSEC-2026-0099 were published simultaneously on 2026-04-14, both reported by @1seal. They describe two separate X.509 name constraint bypass conditions — one for URI names (unimplemented constraint type silently accepted) and one for DNS wildcard names (wildcard certs incorrectly authorized by specific-host permitted-subtree constraints). Both require certificate misissuance to exploit in practice. Both fixed in 0.103.12.

**Fully patched floor:** `rustls-webpki` 0.103.13 (released 2026-04-21) addresses all 5 published advisories. Applications pinned to earlier versions carry one or more of the above risks depending on which CRL / name-constraint features are in use.

## Dependencies of Note

- `rustls` — primary consumer; see [[rust/rustls]] for the TLS-layer advisory history (close_notify DoS, fragmented ClientHello panic).

## Open Questions

- Verify whether `rustls-webpki` 0.104.x has reached stable release and whether its advisory posture differs from 0.103.x.
- Confirm whether the `ring` or `aws-lc-rs` crypto backends have any interaction with the certificate verification path that could affect these advisories.
- Monitor rustsec/advisory-db for further advisories; the 2026 cluster suggests active security research by @1seal and @tynus3.

## Related Pages

- [[rust/rustls]]
- [[rust/ring]]
- [[rust/hyper]]
- [[rust/axum]]
- [[rust/index]]

---
*Last updated: 2026-06-25 | Sources: 2 (rustsec/advisory-db, github/advisory-database)*
