# diesel (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~6.1M (as of 2026-08-15)
**Repository:** https://github.com/diesel-rs/diesel
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04 | diesel-rs maintainers / community contributors | full-source | manual | 6 advisories filed (RUSTSEC-2026-0111/-0134/-0135/-0136/-0137/-0172) | [rustsec/advisory-db](https://github.com/rustsec/advisory-db) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2021-0037 / CVE-2021-28305 | Critical (CVSS 9.8) | Use-after-free in diesel's SQLite backend — a raw pointer to a temporary value is retained past the owning allocation's lifetime, enabling heap UAF when executing queries involving time intervals on SQLite; exploitable through the public query API | ≥ 1.4.6 | [RUSTSEC-2021-0037](https://rustsec.org/advisories/RUSTSEC-2021-0037.html) |
| RUSTSEC-2024-0365 | Moderate | Binary protocol format injection — encoding a value larger than 4 GiB over the PostgreSQL wire protocol causes an integer overflow in the length prefix, causing the server to misinterpret subsequent encoded bytes as new protocol messages; shares root cause class with RUSTSEC-2024-0363 (sqlx) | ≥ 2.2.3 | [RUSTSEC-2024-0365](https://rustsec.org/advisories/RUSTSEC-2024-0365.html) |
| RUSTSEC-2026-0111 | Informational | Unsoundness in diesel internals — safe API can trigger undefined behaviour via an unsound `unsafe` construct; no known exploit in typical usage; part of April 2026 bulk unsoundness audit | ≥ 2.3.8 | [RUSTSEC-2026-0111](https://rustsec.org/advisories/RUSTSEC-2026-0111.html) |
| RUSTSEC-2026-0134 | Informational | Unsoundness in diesel internals — safe API can trigger undefined behaviour via an unsound `unsafe` construct; no known exploit in typical usage; part of April 2026 bulk unsoundness audit | ≥ 2.3.8 | [RUSTSEC-2026-0134](https://rustsec.org/advisories/RUSTSEC-2026-0134.html) |
| RUSTSEC-2026-0135 | Informational | Unsoundness in diesel internals — safe API can trigger undefined behaviour via an unsound `unsafe` construct; no known exploit in typical usage; part of April 2026 bulk unsoundness audit | ≥ 2.3.8 | [RUSTSEC-2026-0135](https://rustsec.org/advisories/RUSTSEC-2026-0135.html) |
| RUSTSEC-2026-0136 | Moderate | PostgreSQL COPY format injection — values supplied to diesel's `copy_from` API are embedded in a `COPY FROM` statement without adequate sanitization; an attacker controlling column data can inject control characters to confuse the server's COPY format parser | ≥ 2.3.8 | [RUSTSEC-2026-0136](https://rustsec.org/advisories/RUSTSEC-2026-0136.html) |
| RUSTSEC-2026-0137 | Informational | Unsoundness in diesel internals — safe API can trigger undefined behaviour via an unsound `unsafe` construct; no known exploit in typical usage; part of April 2026 bulk unsoundness audit | ≥ 2.3.8 | [RUSTSEC-2026-0137](https://rustsec.org/advisories/RUSTSEC-2026-0137.html) |
| RUSTSEC-2026-0172 | Informational | Unsoundness in diesel connection or pool handling — safe API can trigger undefined behaviour; requires an additional fix beyond the 2.3.8 batch; part of 2026 unsoundness follow-up | ≥ 2.3.10 | [RUSTSEC-2026-0172](https://rustsec.org/advisories/RUSTSEC-2026-0172.html) |

## Security Posture Notes

diesel is the dominant synchronous Rust ORM and SQL query builder, supporting PostgreSQL, MySQL, and SQLite backends. Current max_version on crates.io is 2.3.12 (~6.1M weekly downloads, ~33.2M total downloads as of 2026-08-15). The library is actively maintained by the diesel-rs organization but does not publish a formal `SECURITY.md` or dedicated security disclosure contact.

The April 2026 bulk unsoundness audit produced 6 advisories (RUSTSEC-2026-0111/-0134/-0135/-0136/-0137/-0172). Five are informational with no known exploit path outside contrived conditions; one (RUSTSEC-2026-0136, Moderate) is a directly exploitable COPY format injection against PostgreSQL when user-controlled data is passed to `copy_from`. All six were addressed in diesel 2.3.8 (April 2026), except RUSTSEC-2026-0172 which required an additional fix in 2.3.10.

RUSTSEC-2021-0037 / CVE-2021-28305 (Critical CVSS 9.8) is a use-after-free in the SQLite time-interval query path, fixed in diesel 1.4.6 (2021). Any installation using diesel's SQLite feature on a pre-1.4.6 release is exposed to potential memory corruption.

RUSTSEC-2024-0365 (Moderate) shares a root cause class with the sqlx advisory RUSTSEC-2024-0363: integer overflow in the PostgreSQL wire-protocol length prefix when encoding large values. Practical exploitability depends on the ability to supply multi-GiB values through the ORM.

The async diesel ecosystem (diesel-async) is a separate crate and is not covered by this page.

## Dependencies of Note

- `libpq` — PostgreSQL C client library linked dynamically; subject to PostgreSQL's own CVE history
- `mysqlclient` / `libmysqlclient` — MySQL C connector; subject to MySQL C connector CVE exposure
- `libsqlite3-sys` / bundled SQLite — SQLite C library; see [[homebrew/sqlite]] for upstream CVE context

## Open Questions

- Do the unsoundness fixes in RUSTSEC-2026-0111/-0134/-0135/-0137 carry behavioural changes that could break downstream crates relying on the prior (unsound) semantics?
- Does RUSTSEC-2026-0136 require callers to manually sanitize input to `copy_from`, or does 2.3.8 add server-side escaping internally?
- Are any of the April 2026 informational advisories reproduced in the `diesel-async` crate, which uses its own `unsafe` connection-pooling code?
- What is the full GHSA coverage for diesel in github/advisory-database? Cross-reference against rustsec/advisory-db pass done here.

## Related Pages

- [[rust/sqlx]] — async SQL toolkit; shares binary-protocol injection root cause class (RUSTSEC-2024-0363)
- [[rust/tokio]] — async runtime commonly used alongside diesel-async
- [[rust/index]]

---
*Last updated: 2026-08-15 | Sources: 8 (rustsec/advisory-db: RUSTSEC-2021-0037, RUSTSEC-2024-0365, RUSTSEC-2026-0111, RUSTSEC-2026-0134, RUSTSEC-2026-0135, RUSTSEC-2026-0136, RUSTSEC-2026-0137, RUSTSEC-2026-0172)*
