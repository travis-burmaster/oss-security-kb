# pgx (Go)

**Registry:** Go / pkg.go.dev
**Weekly Downloads:** ~1.5M/week est. (v5 module; 13,000+ pkg.go.dev importers)
**Repository:** https://github.com/jackc/pgx
**Security Contact:** https://github.com/jackc/pgx/security/advisories (GitHub private disclosure)
**Disclosure Policy:** Coordinated disclosure via GitHub Security Advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-07-22 | OSS Security KB | GHSA database lookup | automated | 7 public advisories mapped (2024–2026) | [github/advisory-database](https://github.com/github/advisory-database) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-27289 / GHSA-m7wr-2xf7-cm9p | **Moderate** | **SQL injection via line comment creation (v4 simple protocol):** When using the non-default simple protocol (`prefer_simple_protocol=true`), a numeric placeholder immediately preceded by a minus sign and followed by a string placeholder on the same line allows a crafted negative numeric value to create a `--` SQL line comment that escapes the string placeholder, causing the second parameter value to be interpreted as raw SQL. Requires attacker control of both a numeric and a string parameter in the same query line. The default extended protocol with parameterized binding is not affected. | v4.18.2 | [GHSA-m7wr-2xf7-cm9p](https://github.com/advisories/GHSA-m7wr-2xf7-cm9p) |
| CVE-2024-27304 / GHSA-mrww-27vc-gghv | **Moderate** | **SQL injection via protocol message size integer overflow:** An integer overflow in the computed size of a query or bind message allows a single payload exceeding 4 GB to be fragmented into multiple wire-protocol messages under the attacker's control, each interpreted as a valid command. If user-supplied input can cause a single query or bind argument to exceed 4 GB, SQL injection is achievable. Affects both simple and extended protocols. Fixed in pgx v4.18.2 and v5.5.4. | v4.18.2 / v5.5.4 | [GHSA-mrww-27vc-gghv](https://github.com/advisories/GHSA-mrww-27vc-gghv) |
| GHSA-fqpg-rq76-99pq | **Moderate** | **Pipeline panic when PgConn is busy or closed (DoS):** Calling `Pipeline` on a `PgConn` that is already in use or has been closed triggers a nil-pointer dereference panic in pgx v5, crashing the affected goroutine. No CVE assigned. Applications that expose pipeline initiation to external input may be susceptible to denial of service. | v5.5.2 | [GHSA-fqpg-rq76-99pq](https://github.com/advisories/GHSA-fqpg-rq76-99pq) |
| CVE-2026-32286 / GHSA-jqcq-xjh3-6g23 | **High — CVSS 7.5** | **pgproto3/v2 DataRow.Decode panic DoS via negative field length:** `DataRow.Decode` in `github.com/jackc/pgproto3/v2` does not validate field lengths before using them to slice the receive buffer. A malicious or compromised PostgreSQL server can send a `DataRow` message containing a negative field-length value, causing an index out-of-range panic that crashes the pgx client process. Any application connecting to an untrusted PostgreSQL endpoint is at risk. | pgproto3/v2 > 2.3.3 | [GHSA-jqcq-xjh3-6g23](https://github.com/advisories/GHSA-jqcq-xjh3-6g23) |
| CVE-2026-33815 / GHSA-xgrm-4fwx-7qm8 | **High** | **Memory-safety vulnerability in pgx/v5:** A memory-safety vulnerability was identified in `github.com/jackc/pgx/v5` prior to v5.9.0. The advisory does not fully specify the exploitable code path, but the class is memory-safety, indicating a potential for memory corruption or unsafe memory access. | v5.9.0 | [GHSA-xgrm-4fwx-7qm8](https://github.com/advisories/GHSA-xgrm-4fwx-7qm8) |
| CVE-2026-33816 / GHSA-9jj7-4m8r-rfcm | **High** | **Memory-safety vulnerability in pgx/v5 (second):** A second distinct memory-safety vulnerability in `github.com/jackc/pgx/v5` prior to v5.9.0, fixed in the same v5.9.0 release alongside CVE-2026-33815. | v5.9.0 | [GHSA-9jj7-4m8r-rfcm](https://github.com/advisories/GHSA-9jj7-4m8r-rfcm) |
| CVE-2026-41889 / GHSA-j88v-2chj-qfwx | **Moderate** | **SQL injection via dollar-quoted string literal placeholder confusion (simple protocol):** When using the simple query protocol, a dollar-quoted string literal in the query combined with a crafted placeholder value can confuse pgx's parameter substitution, resulting in SQL injection. Affects pgx/v5 (fixed v5.9.2), pgx/v4 (EOL through v4.18.3 — no patch), and pgx/v3 (EOL through v3.6.2 — no patch). Applications on v4 or v3 using the simple protocol have no upstream fix. | v5.9.2 (v4 and v3 are EOL; no patch available) | [GHSA-j88v-2chj-qfwx](https://github.com/advisories/GHSA-j88v-2chj-qfwx) |

## Security Posture Notes

`pgx` is the dominant pure-Go PostgreSQL driver and toolkit, used directly or as the backend for Go ORMs (GORM, sqlx, Bun) and data-access layers across the Go ecosystem. Its client-side implementation of the PostgreSQL wire protocol is the primary attack surface.

**Recurring vulnerability class — simple protocol SQL injection:**

Three of the seven advisories (CVE-2024-27289, CVE-2024-27304, CVE-2026-41889) involve SQL injection when the **simple query protocol** is in use. The default pgx configuration uses the **extended protocol with parameterized binding**, which is not affected by any of these SQL injection issues. However:
- Any caller that enables `PreferSimpleProtocol: true` in `ConnConfig`, or passes raw query strings without parameter binding, loses the safety guarantee.
- pgx v4 is **EOL** and receives no patch for CVE-2026-41889; migration to pgx/v5 ≥ 5.9.2 is required for full coverage.
- Applications wrapping pgx with a query builder or ORM should verify the protocol mode; some ORMs historically defaulted to simple protocol for certain query types.

**Memory-safety (2026):**

Two memory-safety issues (CVE-2026-33815, CVE-2026-33816) were fixed together in v5.9.0. The public advisories are sparse on technical detail; operators running pgx/v5 < 5.9.0 should upgrade without waiting for full disclosure.

**Malicious-server DoS:**

CVE-2026-32286 (pgproto3/v2) and the pipeline panic (GHSA-fqpg-rq76-99pq) require either a malicious/compromised PostgreSQL server or a specific usage pattern. Applications that connect to trusted, operator-controlled PostgreSQL instances and do not expose pipeline initiation to external input face lower practical risk from these two issues.

**Recommended minimum version:** `pgx/v5 ≥ 5.9.2` covers all seven advisories for v5 users.

## Dependencies of Note

- **`github.com/jackc/pgproto3/v2`** — PostgreSQL wire-protocol implementation; CVE-2026-32286 (GHSA-jqcq-xjh3-6g23) affects this sub-package directly (negative `DataRow` field length). In pgx/v5 later releases this code is inlined as internal packages; check whether standalone `pgproto3` is pinned in your module graph.
- **`github.com/jackc/pgconn`** — low-level connection management; the Pipeline panic (GHSA-fqpg-rq76-99pq) originates in this layer.
- **`github.com/jackc/pgtype`** — extended type-coercion support; separate from the above advisories but warrants periodic review for type-boundary edge cases.

## Open Questions

- CVE-2026-33815 and CVE-2026-33816: full technical details are not disclosed in the public GHSA records at this time; monitor upstream for post-patch write-ups.
- Verify whether the pgproto3/v2 DataRow fix (CVE-2026-32286) is incorporated in the inlined wire-protocol code in pgx/v5 ≥ 5.9.0.
- Survey pre-2024 pgx advisories (v3 era, standalone pgconn/pgproto3) for any untracked historical issues.

## Related Pages

- [[dotnet/Npgsql]] — .NET PostgreSQL driver; see GHSA-x9vc-6hfv-hg8c / CVE-2024-32655 for a comparable integer-overflow wire-protocol SQL injection pattern
- [[go/index]]

---
*Last updated: 2026-07-22 | Sources: github/advisory-database (GHSA-m7wr-2xf7-cm9p, GHSA-mrww-27vc-gghv, GHSA-fqpg-rq76-99pq, GHSA-xgrm-4fwx-7qm8, GHSA-9jj7-4m8r-rfcm, GHSA-jqcq-xjh3-6g23, GHSA-j88v-2chj-qfwx)*
