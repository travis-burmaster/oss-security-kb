# sqlx (crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~2.5M/week est. (as of 2026-08-05)
**Repository:** https://github.com/launchbadge/sqlx
**Security Contact:** GitHub security advisories (https://github.com/launchbadge/sqlx/security)
**Disclosure Policy:** GitHub security advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2024-0363 / GHSA-xmrp-424f-vfpx | Moderate (no CVSS assigned; category: format injection) | Binary protocol format injection via integer overflow: encoding a value larger than 4 GiB causes the `u32` length-prefix field to overflow back toward zero, causing the server to interpret the remaining bytes as new binary protocol commands or data. Root cause is multiple truncating casts in SQLx's encoding logic present since project inception. Exploitability demonstrated against the PostgreSQL wire protocol; MySQL and SQLite show no apparent exploitability in the same path. Recommended mitigations: reject inputs exceeding 4 GiB before encoding, apply web-server request-body size limits, use `Encode::size_hint()` as a sanity check. | sqlx ≥ 0.8.1 (all versions ≤ 0.8.0 affected) | [GHSA-xmrp-424f-vfpx](https://github.com/advisories/GHSA-xmrp-424f-vfpx) / [RUSTSEC-2024-0363](https://rustsec.org/advisories/RUSTSEC-2024-0363.html) |

## Security Posture Notes

`sqlx` is the dominant async Rust SQL toolkit, providing compile-time checked queries without a DSL against PostgreSQL, MySQL, and SQLite. With ~126M total crates.io downloads and ~2.5M/week (as of 2026-08-05), it is widely used in Rust production web services, particularly those built on Axum or Actix-Web. Current stable version is 0.9.0, released well after the 0.8.1 fix.

RUSTSEC-2024-0363 represents a protocol-level injection risk affecting any application that accepts user-supplied data larger than 4 GiB without bounds-checking before passing it to the `Encode` trait implementation. In practice, most web frameworks impose request-body size limits that make exploitation unlikely under typical web workloads. However, internal APIs that process large binary blobs — bulk data ingest pipelines, file upload endpoints, or streaming ingestion services — without explicit size guards are plausible attack surfaces. The advisory was published 2024-08-15; the fix shipped in 0.8.1 on 2024-08-23. No CVE was assigned.

The project discloses via GitHub security advisories. The upstream remediation plan includes adding Clippy lint denials for `cast_possible_truncation`, `cast_wrap`, and `cast_sign_loss` to prevent recurrence.

## Dependencies of Note

- PostgreSQL wire protocol (`tokio-postgres` internals): directly affected by the overflow in the `Encode` path.
- `sqlx-macros` / compile-time query checking: not affected by this advisory (macro checks operate at the type level, not size level).
- Downstream crates or services pinning `sqlx < 0.8.1` carry the vulnerability in any code path that encodes very large values.

## Open Questions

- Verify whether the upstream Clippy lint denials for truncating casts were added as stated in the advisory remediation notes.
- Confirm current advisory status for the MySQL and SQLite encode paths — the advisory notes no apparent exploitability but no definitive independent analysis was published.
- Check for any 2025–2026 advisories that may have been filed after this pass (current pass date: 2026-08-05).

## Related Pages

- [[rust/tokio]]
- [[rust/axum]]
- [[rust/actix-web]]
- [[rust/index]]

---
*Last updated: 2026-08-05 | Sources: 2*
