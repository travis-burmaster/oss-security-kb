# hickory-dns (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~26.4M recent (hickory-proto; as of 2026-10-01)
**Repository:** https://github.com/hickory-dns/hickory-dns
**Security Contact:** https://github.com/hickory-dns/hickory-dns/security/advisories/new (GitHub private vulnerability reporting)
**Disclosure Policy:** https://github.com/hickory-dns/hickory-dns/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Scope Note

Hickory DNS (formerly trust-dns) is published as a workspace of multiple crates on crates.io:

| Crate | Role | Downloads |
|-------|------|-----------|
| `hickory-proto` | Core DNS wire-protocol implementation | ~85.7M total, ~26.4M recent |
| `hickory-resolver` | Stub resolver (replaces `trust-dns-resolver`) | high |
| `hickory-net` | Network transport layer | moderate |
| `hickory-recursor` | Experimental recursive resolver (deprecated) | low |
| `hickory-server` | Authoritative DNS server binary | low |
| `hickory-dns` | Combined server binary | ~26K total |
| `trust-dns-proto` | Legacy crate name — unmaintained (RUSTSEC-2025-0017) | historical |

This page covers the full project. Advisory focus is on `hickory-proto` (core library), `hickory-net` (transport), and `hickory-recursor` (recursive resolver).

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|---------|

*No formal third-party audits on record.*

## Known Vulnerabilities

| CVE / RUSTSEC | Severity | Description | Affected Crate / Versions | Fixed in | Source |
|---------------|----------|-------------|--------------------------|----------|--------|
| RUSTSEC-2025-0006 / GHSA-37wc-h8xc-5hc4 | High (Crypto Failure) | DNSSEC DNSKEY RRset trust-propagation bypass: validating one DNSKEY in an RRset causes all other DNSKEYs in the set to be trusted without individual self-signature verification; parallel DS-authenticated key flaw allows signatures from unrelated DNSKEYs to be accepted | hickory-proto ≥ 0.8.0, < 0.24.3 | 0.24.3 / 0.25.0-alpha.5 | [GHSA-37wc-h8xc-5hc4](https://github.com/hickory-dns/hickory-dns/security/advisories/GHSA-37wc-h8xc-5hc4) |
| RUSTSEC-2026-0106 / GHSA-83hf-93m4-rgwq | High (Privilege Escalation / Cache Poisoning) | DNS cache poisoning in the experimental recursive resolver: `hickory-recursor` caches authority-section records by their own (name, type) rather than the queried zone, allowing a parent-zone nameserver operator to inject NS records for sibling zones into the shared cache; subsequent legitimate queries for the victim zone are routed to the attacker's nameserver | hickory-recursor — all published versions | No patch; crate deprecated; migrate to `hickory-resolver` 0.26.0 with `recursor` feature | [GHSA-83hf-93m4-rgwq](https://github.com/hickory-dns/hickory-dns/security/advisories/GHSA-83hf-93m4-rgwq) |
| RUSTSEC-2026-0118 / GHSA-3v94-mw7p-v465 | Moderate (Denial of Service) | NSEC3 closest-encloser proof validation unbounded loop in hickory-proto: the iterator assumes the QNAME is a descendant of the SOA owner; cross-zone responses with a mismatched SOA record from a non-ancestor zone stall the iterator at the DNS root, causing unbounded memory allocation (OOM crash in release builds; assertion panic in debug) | hickory-proto 0.25.0-alpha.3 to < 0.26.0-beta.1 | No fix in 0.25.x; migrate to hickory-net ≥ 0.26.1 (code relocated in 0.26.0) | [GHSA-3v94-mw7p-v465](https://github.com/hickory-dns/hickory-dns/security/advisories/GHSA-3v94-mw7p-v465) |
| RUSTSEC-2026-0119 / GHSA-q2qq-hmj6-3wpp (related: CVE-2024-8508) | Moderate (Denial of Service) | `BinEncoder` name-compression linear-scan CPU exhaustion: the encoder stores name-compression candidates in a `Vec<(usize, Vec<u8>)>` and performs linear scanning to find matches; crafted DNS messages with many records force repeated O(n) scans producing O(n²) total CPU work, enabling CPU exhaustion DoS | hickory-proto < 0.26.1 | 0.26.1 | [GHSA-q2qq-hmj6-3wpp](https://github.com/hickory-dns/hickory-dns/security/advisories/GHSA-q2qq-hmj6-3wpp) |
| RUSTSEC-2026-0120 / GHSA-3v94-mw7p-v465 | Moderate (Denial of Service) | NSEC3 closest-encloser proof validation unbounded loop in `DnssecDnsHandle` (`hickory-net`): same root cause as RUSTSEC-2026-0118 but manifesting in the network transport layer; any caller using DNSSEC validation with the `dnssec-ring` or `dnssec-aws-lc-rs` feature is affected; release builds exhaust memory and crash | hickory-net < 0.26.1 | 0.26.1 | [GHSA-3v94-mw7p-v465](https://github.com/hickory-dns/hickory-dns/security/advisories/GHSA-3v94-mw7p-v465) |
| RUSTSEC-2025-0017 | Informational | `trust-dns-proto` unmaintained: the project was rebranded to Hickory DNS; all versions of `trust-dns-proto` > 0.23.0 receive no security updates | trust-dns-proto > 0.23.0 | No fix; migrate to `hickory-proto` | [RUSTSEC-2025-0017](https://rustsec.org/advisories/RUSTSEC-2025-0017.html) |

*OSV link: https://osv.dev/list?ecosystem=crates.io&q=hickory-proto*

## Security Posture Notes

Hickory DNS is a pure-Rust async DNS implementation targeting modern security properties (DNSSEC, DoT, DoH, DoQ). The project maintains a SECURITY.md with a GitHub private disclosure workflow and commits to responding within 5 business days. Only the most-recent minor release train receives full security support; earlier versions may receive patches depending on severity and version prevalence. The project does not offer bug bounties.

The 2025–2026 advisory cluster reveals three systemic concerns:

1. **DNSSEC validation correctness (RUSTSEC-2025-0006)** — a trust-propagation flaw in DNSKEY RRset handling meant that verifying one key implicitly trusted all others in the same RRset. The fix (0.24.3 / 0.25.0-alpha.5) enforces per-key self-signature verification and tightens DS-authenticated key chain logic.
2. **Recursive resolver immaturity (RUSTSEC-2026-0106)** — the experimental `hickory-recursor` crate had a critical bailiwick-check gap enabling cross-zone cache poisoning. The crate has been deprecated with no patch; users must migrate to `hickory-resolver` 0.26.0.
3. **NSEC3 validation loops (RUSTSEC-2026-0118 / 0120)** — the NSEC3 closest-encloser proof code incorrectly assumed zone relationships during iteration, producing unbounded loops on cross-zone DNSSEC responses. The affected 0.25.x alpha series has no fix; migration to ≥ 0.26.0 is required.

Current stable `hickory-proto` 0.26.3 and `hickory-net` 0.26.3 are unaffected by all mapped advisories.

## Dependencies of Note

- `ring` or `aws-lc-rs` — cryptographic backends for DNSSEC signature verification; see [[rust/ring]]
- `rustls` — TLS transport for DoT/DoH; see [[rust/rustls]]
- `tokio` — async runtime; see [[rust/tokio]]

## Open Questions

- The `trust-dns-*` legacy crates (trust-dns-resolver, trust-dns-server, trust-dns-https) each received separate RUSTSEC-2025-0017-series unmaintained advisories; a future pass should confirm all legacy crate advisories are captured.
- No third-party security audit of the Hickory DNS DNSSEC implementation has been published; the complexity of DNSSEC validation makes this a meaningful gap.
- CVE-2024-8508 was originally filed against Unbound (C); the precise relationship to RUSTSEC-2026-0119 should be verified against the NVD record.

## Related Pages

- [[rust/rustls]] — TLS transport used by Hickory DoT/DoH
- [[rust/ring]] — cryptographic backend for DNSSEC verification
- [[rust/tokio]] — async runtime foundation
- [[go/github.com/miekg/dns]] — comparable Go DNS implementation
- [[rust/index]]

---
*Last updated: 2026-10-01 | Sources: 6 RUSTSEC advisories, crates.io API, GitHub SECURITY.md*
