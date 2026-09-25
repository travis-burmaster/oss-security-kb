# gorm.io/gorm (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (86,926 known importers as of 2026-09-25)
**Repository:** https://github.com/go-gorm/gorm
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-15562 / GHSA-r28r-5q2m-wh2x | Critical CVSS 9.8 | SQL injection via incomplete parentheses in database query construction — allows unauthenticated remote attackers to execute arbitrary SQL commands; affected the legacy v1 module path (`github.com/jinzhu/gorm` / `github.com/go-gorm/gorm`) before 1.9.10; `gorm.io/gorm` (v2 rewrite, separate Go module) has no known direct GHSA/OSV advisories as of this pass | github.com/jinzhu/gorm ≥ 1.9.10 (v1); or migrate to gorm.io/gorm ≥ 1.0 (v2) | [GHSA-r28r-5q2m-wh2x](https://github.com/advisories/GHSA-r28r-5q2m-wh2x) |

*OSV: https://osv.dev/list?ecosystem=Go&q=gorm*

## Security Posture Notes

GORM is the dominant Go ORM, originally authored by Jinzhu and now maintained under the `go-gorm` GitHub organization. The project underwent a full rewrite as GORM v2, published under the import path `gorm.io/gorm` (a separate Go module from the legacy `github.com/jinzhu/gorm`). All modern Go projects should use `gorm.io/gorm` (v2) and its associated database driver modules.

The single published advisory (CVE-2019-15562 / GHSA-r28r-5q2m-wh2x, CRITICAL CVSS 9.8) targets the old v1 module path before 1.9.10. The root cause is failure to validate or sanitize parentheses in query-building paths, permitting SQL injection when attacker-controlled input reaches those paths. The `github/advisory-database` lists this under `github.com/go-gorm/gorm` (the repository), which covers both the old jinzhu module and the current v2 codebase; however, the fix was scoped to the 1.9.10 release on the v1 branch.

No GHSA or OSV advisory has been published directly against the `gorm.io/gorm` Go module path as of this pass (2026-09-25).

**Application-level SQL injection risk** remains the primary security concern for gorm.io/gorm users: calling `db.Raw()`, `db.Exec()`, `db.Where()` with string concatenation, or using `gorm.Expr()` with unsanitized user input bypasses GORM's parameterization. The library's standard query builders (Find, First, Where with positional `?` arguments, etc.) are safe. The raw-query surface area has historically caused injection bugs in downstream applications.

No SECURITY.md or dedicated security contact was found in the repository as of this pass. The latest stable release is v1.31.2 (June 2026); actively maintained.

## Dependencies of Note

- `gorm.io/driver/postgres` — wraps `github.com/jackc/pgx` or `lib/pq`; see [[go/github.com/jackc/pgx]] for pgx-specific SQL injection advisories.
- `gorm.io/driver/mysql` — wraps `go-sql-driver/mysql`.
- `gorm.io/driver/sqlite` — embeds or links mattn/go-sqlite3 (CGo); upstream SQLite CVEs apply.

## Open Questions

- Does GORM v2's `Raw()`/`Exec()` implementation have any injection surface beyond direct string interpolation? A targeted source audit of the v2 query-builder parameterization escape paths would confirm.
- Has any GHSA/OSV advisory been filed against the `gorm.io/gorm` module path since this pass?

## Related Pages

- [[go/github.com/jackc/pgx]]
- [[go/index]]

---
*Last updated: 2026-09-25 | Sources: 2*
