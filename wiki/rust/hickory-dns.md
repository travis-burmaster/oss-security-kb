# hickory-dns / trust-dns (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~19.5M (hickory-proto), ~18.8M (hickory-resolver), ~2.8M (trust-dns-resolver legacy) (as of 2026-08-16)
**Repository:** https://github.com/hickory-dns/hickory-dns
**Security Contact:** https://github.com/hickory-dns/hickory-dns/security/advisories (GitHub private advisory)
**Disclosure Policy:** https://github.com/hickory-dns/hickory-dns/security/advisories
**Current Status:** advisory-mapped

## Overview

The hickory-dns project is a pure-Rust async DNS implementation originally published as `trust-dns`. The project was rebranded in 2023; all `trust-dns-*` crates are now unmaintained (RUSTSEC-2025-0017 informational) and should be replaced with their `hickory-*` equivalents.

**Crate mapping:**

| Old name | New name | Current version |
|----------|----------|----------------|
| trust-dns-proto | hickory-proto | 0.26.1 |
| trust-dns-resolver | hickory-resolver | 0.26.1 |
| trust-dns-server | hickory-server | 0.26.1 |
| trust-dns-client | hickory-client | (0.26.0-alpha.1) |
| — | hickory-net | 0.26.1 (new in 0.26) |
| hickory-recursor | (folded into hickory-resolver `recursor` feature) | — |

`hickory-proto` (~70M total downloads) and `hickory-resolver` (~68M total) are the highest-impact crates.

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| — | — | — | — | — | — |

*No public third-party audits on record as of 2026-08-16.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2018-0007 / CVE-2018-20994 / GHSA-369h-pjr2-6wrh | High (CVSS 7.5 AV:N) | `trust-dns-proto`: stack overflow parsing a malicious DNS packet — compression offset loop in RFC 1035 §4.1.4 name decompression causes infinite recursion and crash | trust-dns-proto ≥ 0.4.3 | [RUSTSEC-2018-0007](https://rustsec.org/advisories/RUSTSEC-2018-0007.html) |
| RUSTSEC-2020-0001 / CVE-2020-35857 / GHSA-4cww-f7w5-x525 | High (CVSS 7.5 AV:N) | `trust-dns-server`: stack overflow when resolving additional records for MX or SRV records whose target is the DNS null label (`.`); unauthenticated remote crash | trust-dns-server ≥ 0.18.1 (unaffected < 0.16.0) | [RUSTSEC-2020-0001](https://rustsec.org/advisories/RUSTSEC-2020-0001.html) |
| RUSTSEC-2023-0041 / GHSA-5fm9-h728-fwpj | High (DoS, AV:N) | `trust-dns-server`: QR=1 bit in incoming packet triggers FormErr response loop between two servers; single-server self-loop possible via spoofed source IP; multiple spoofed packets exhaust CPU cores | trust-dns-server ^0.22.1 or ≥ 0.23.0-alpha.3 | [RUSTSEC-2023-0041](https://rustsec.org/advisories/RUSTSEC-2023-0041.html) |
| RUSTSEC-2025-0006 / GHSA-37wc-h8xc-5hc4 / GHSA-v7pc-74h8-xq2h | High (crypto-failure) | `hickory-proto`: DNSSEC validation trusts all DNSKEYs in a zone once one key matches a configured trust anchor, without verifying self-signatures over the full DNSKEY RRset; second variant: a DS record authenticating one DNSKEY leads to unconditional trust in the whole RRset | hickory-proto ≥ 0.24.3 or ≥ 0.25.0-alpha.5; unaffected < 0.8.0 | [RUSTSEC-2025-0006](https://rustsec.org/advisories/RUSTSEC-2025-0006.html) |
| RUSTSEC-2026-0106 / GHSA-83hf-93m4-rgwq | High (cache-poisoning) | `hickory-recursor`: the DNS record cache stores AUTHORITY section NS records using the parent-pool zone as bailiwick, not the queried zone; an attacker controlling a sibling zone's nameserver can inject a poisoned NS record for a victim zone into the shared cache | No fix — crate deprecated; migrate to hickory-resolver with `recursor` feature (≥ 0.26.0) | [RUSTSEC-2026-0106](https://rustsec.org/advisories/RUSTSEC-2026-0106.html) |
| RUSTSEC-2026-0118 / GHSA-3v94-mw7p-v465 | High (DoS, AV:N) | `hickory-proto`: NSEC3 closest-encloser proof validation walks from QNAME to SOA owner; if the SOA is not an ancestor of the QNAME (e.g. cross-zone CNAME chain), the loop never terminates — release builds allocate until OOM; debug builds abort with `debug_assert_ne!` | Not patched in hickory-proto; functionality moved to hickory-net ≥ 0.26.1 | [RUSTSEC-2026-0118](https://rustsec.org/advisories/RUSTSEC-2026-0118.html) |
| RUSTSEC-2026-0119 / GHSA-q2qq-hmj6-3wpp | Moderate (DoS, AV:N) | `hickory-proto`: `BinEncoder` stores name compression candidates in a `Vec` searched linearly; a crafted message with many records causes O(n²) work during encoding, amplifying CPU exhaustion; similar to CVE-2024-8508 (Unbound) | hickory-proto ≥ 0.26.1; unaffected < 0.3.1 | [RUSTSEC-2026-0119](https://rustsec.org/advisories/RUSTSEC-2026-0119.html) |
| RUSTSEC-2026-0120 / GHSA-3v94-mw7p-v465 | High (DoS, AV:N) | `hickory-net`: same NSEC3 closest-encloser proof unbounded-loop / OOM as RUSTSEC-2026-0118, applying to the `DnssecDnsHandle` implementation that migrated from hickory-proto to hickory-net in 0.26.x | hickory-net ≥ 0.26.1 | [RUSTSEC-2026-0120](https://rustsec.org/advisories/RUSTSEC-2026-0120.html) |

*OSV link: https://osv.dev/list?ecosystem=crates.io&q=hickory-proto*

## Security Posture Notes

Active development under the `hickory-dns/hickory-dns` GitHub org. The 2026 advisories (RUSTSEC-2026-0106 / -0118 / -0119 / -0120) were published 2026-04 to 2026-05 as part of a coordinated batch; all were fixed in the 0.26.0/0.26.1 release.

The `hickory-recursor` crate has no fix for RUSTSEC-2026-0106 and is end-of-life; it was folded into `hickory-resolver` as a non-default `recursor` feature. Any deployment using `hickory-recursor` as a standalone crate must migrate.

The DNSSEC implementation has been the source of both a crypto-failure advisory (2025) and two DoS advisories (2026). Consumers doing DNSSEC validation with the `dnssec-ring` or `dnssec-aws-lc-rs` feature should track advisories carefully; the feature is not enabled by default in most user-facing crates.

All `trust-dns-*` crates are now unmaintained. RUSTSEC-2025-0017 explicitly marks `trust-dns-proto` as unmaintained; equivalent informational advisories apply to `trust-dns-resolver`, `trust-dns-server`, and other `trust-dns-*` packages.

## Dependencies of Note

- `ring` or `aws-lc-rs`: selected by feature flag for DNSSEC cryptographic operations; both have their own advisory histories (see rust/ring)
- `rustls` / `tokio-rustls`: TLS transport option; see rust/rustls for advisory history
- `tokio`: async runtime; see rust/tokio for advisory history

## Open Questions

- Do any advisories affect the experimental async `hickory-client` (0.26.0-alpha.1)?
- Is the DNSSEC NSEC3 loop (RUSTSEC-2026-0118/0120) reachable with publicly available DNSSEC-signed zones, or does it require a cooperative server?
- Check for any RUSTSEC advisories against `hickory-server` (authoritative server crate) post-0.26.0.

## Related Pages

- [[rust/ring]]
- [[rust/rustls]]
- [[rust/tokio]]
- [[rust/index]]

---
*Last updated: 2026-08-16 | Sources: 8 RustSec advisories (RUSTSEC-2018-0007, -2020-0001, -2023-0041, -2025-0006, -2026-0106, -2026-0118, -2026-0119, -2026-0120)*
