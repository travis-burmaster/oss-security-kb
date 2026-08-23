# diesel (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~6.3M recent (as of 2026-08-23); ~33.8M all-time
**Repository:** https://github.com/diesel-rs/diesel
**Security Contact:** none listed (GitHub Security Advisories via diesel-rs/diesel)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-28305 / RUSTSEC-2021-0037 / GHSA-j8q9-5rp9-4mv9 | Critical (CVSS v3.1 9.8 AV:N/AC:L/PR:N/UI:N) | **Use-after-free in SQLite `query_by_name`.** Diesel stored `sqlite3_column_name()` return pointers as string slices, then called `sqlite3_step()` (which invalidates those pointers), then accessed them — classic UAF. Reachable by any application using diesel's SQLite backend on affected versions. | 1.4.6 | [GHSA-j8q9-5rp9-4mv9](https://github.com/advisories/GHSA-j8q9-5rp9-4mv9) / [RUSTSEC-2021-0037](https://rustsec.org/advisories/RUSTSEC-2021-0037.html) |
| RUSTSEC-2024-0365 / GHSA-wq9x-qwcq-mmgf | High (CVSS v3.1 8.6 / CVSS v4 8.6 AV:N/AC:H) | **PostgreSQL binary protocol query smuggling via integer overflow.** Values larger than 4 GiB cause the PostgreSQL wire-protocol length prefix to overflow (u32 cast truncation), enabling protocol-level message manipulation — effectively SQL injection via the binary protocol. Affects PostgreSQL backend users sending large values. No CVE assigned. | 2.2.3 | [GHSA-wq9x-qwcq-mmgf](https://github.com/advisories/GHSA-wq9x-qwcq-mmgf) / [RUSTSEC-2024-0365](https://rustsec.org/advisories/RUSTSEC-2024-0365.html) |
| GHSA-h5x4-m2qf-r4f2 | Moderate | **UTF-8 corruption in SQLite backend.** `str::from_utf8_unchecked` called on `sqlite3_value_text()` output without validation — for columns with SQLite storage type BLOB, this produces invalid Rust `str` values in safe code (UB via incorrect UTF-8 invariant assumption). | 2.3.8 | [GHSA-h5x4-m2qf-r4f2](https://github.com/advisories/GHSA-h5x4-m2qf-r4f2) |
| RUSTSEC-2026-0136 / GHSA-m9p2-fxp5-v3fp | Moderate (CWE-88) | **Argument injection in PostgreSQL COPY FROM/TO options.** User-supplied option values (delimiter, null, quote, escape, default) were not sanitized for embedded quote characters, allowing option manipulation within a single COPY statement. Does not enable separate-statement injection but can alter COPY semantics. | 2.3.8 | [GHSA-m9p2-fxp5-v3fp](https://github.com/advisories/GHSA-m9p2-fxp5-v3fp) / [RUSTSEC-2026-0136](https://rustsec.org/advisories/RUSTSEC-2026-0136.html) |
| RUSTSEC-2026-0137 / GHSA-q8x8-jrhj-fh9p | Moderate | **Unaligned allocation in `SqliteAggregate`.** `sqlite3_aggregate_context()` provides no alignment guarantee; custom aggregate types with non-standard alignment placed at misaligned addresses trigger undefined behavior. Affects users implementing custom SQLite aggregate functions. | 2.3.8 | [GHSA-q8x8-jrhj-fh9p](https://github.com/advisories/GHSA-q8x8-jrhj-fh9p) / [RUSTSEC-2026-0137](https://rustsec.org/advisories/RUSTSEC-2026-0137.html) |
| GHSA-ggxf-9f6j-w742 | Moderate (CWE-416) | **Use-after-free in `SqliteConnection::deserialize_readonly_database`.** The function loads a SQLite database from a `&[u8]` buffer, but libsqlite3 requires the buffer to remain valid for the entire connection lifetime; dropping the buffer early causes libsqlite3 to access freed memory. Fixed by storing a copy of the buffer inside `SqliteConnection`. | 2.3.10 | [GHSA-ggxf-9f6j-w742](https://github.com/advisories/GHSA-ggxf-9f6j-w742) |

## Security Posture Notes

Diesel is the most established synchronous ORM and query builder for Rust, supporting PostgreSQL, MySQL, and SQLite. It emphasizes compile-time SQL query verification via a schema DSL. The advisory history shows two clear patterns: most vulnerabilities concentrate in the **SQLite backend** (memory safety: UAF ×2, UTF-8 invariant violation, alignment — all FFI unsafe-contract violations with libsqlite3), while PostgreSQL backend issues involve **wire-protocol integrity** (RUSTSEC-2024-0365 length overflow, GHSA-m9p2-fxp5-v3fp COPY argument injection).

RUSTSEC-2024-0365 (PostgreSQL binary-protocol overflow) is closely analogous to RUSTSEC-2024-0363 affecting the competing `sqlx` crate — both are u32 wire-protocol length prefix overflows when encoding values > 4 GiB, suggesting this is a class-level defect in Rust PostgreSQL wire-protocol implementations.

The companion crate `diesel-async` (async counterpart) has a separate advisory GHSA-ff9q-rm55-q7qr (MySQL temporal column uninitialized padding bytes, fixed 0.9.0); not covered on this page.

Newest version 2.3.12 is unaffected by all listed advisories (all fixed by 2.3.10). No formal `SECURITY.md` or dedicated security contact listed in the repository as of 2026-08-23. No third-party audits on record.

## Dependencies of Note

- **libsqlite3** (SQLite C library) — multiple advisories stem from FFI/unsafe contract violations with this library's pointer lifecycle semantics
- **libpq** (PostgreSQL C client library) — PostgreSQL backend links against libpq
- `diesel-async` — async counterpart crate with its own advisory (GHSA-ff9q-rm55-q7qr, MySQL)

## Open Questions

- Whether a formal `SECURITY.md` and security contact will be established.
- Potential for further SQLite-backend FFI unsafe-contract violations not yet surfaced (diesel uses `unsafe` extensively for SQLite interaction).
- MySQL backend: advisory coverage thinner than SQLite and PostgreSQL backends; worth a targeted pass.

## Related Pages

- [[rust/sqlx]] — competing async SQL toolkit with parallel advisory class (RUSTSEC-2024-0363)
- [[rust/index]]

---
*Last updated: 2026-08-23 | Sources: 6*
