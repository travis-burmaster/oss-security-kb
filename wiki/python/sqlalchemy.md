# sqlalchemy (python)

**Registry:** PyPI
**Repository:** https://github.com/sqlalchemy/sqlalchemy
**Security Contact:** https://github.com/sqlalchemy/sqlalchemy/security/policy
**Disclosure Policy:** https://github.com/sqlalchemy/sqlalchemy/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-08 | OpenClaw recurring review | package advisory history | manual | 3 unique public SQLAlchemy vulnerability classes normalized from OSV / GitHub Advisory Database / PYSEC / CVE aliases plus upstream issue and fix-context records; duplicate PYSEC aliases retained with canonical GHSA rows rather than counted separately | https://osv.dev/list?ecosystem=PyPI&q=sqlalchemy |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2012-0805 / GHSA-hfg2-wf6j-x53p / PYSEC-2012-9 | Critical | SQL injection in older SQLAlchemy versions when untrusted input reached SQL construction paths; public records point to the 0.7-era fix train and downstream Keystone / distro advisories. | 0.7.0 / 0.7.0b4 record boundary varies by source | https://github.com/advisories/GHSA-hfg2-wf6j-x53p |
| CVE-2019-7164 / GHSA-887w-45rq-vxgf / PYSEC-2019-123 | Critical | SQL injection via implicit textual coercion of untrusted strings passed to `order_by()`; upstream issue #4481 documents the unsafe `order_by` pattern and the removal / deprecation of raw-string coercions. | 1.3.0b3 in GHSA / OSV GHSA record; PYSEC duplicate lists 1.2.18 | https://github.com/advisories/GHSA-887w-45rq-vxgf |
| CVE-2019-7548 / GHSA-38fc-9xqv-7f7q / PYSEC-2019-124 | Critical | SQL injection via related textual coercion in `group_by()`; upstream issue #4510 discusses backporting the `order_by` / `group_by` text-coercion raise to the 1.2 line. | 1.2.19 in GHSA / OSV GHSA record; PYSEC duplicate lists 1.2.18 | https://github.com/advisories/GHSA-38fc-9xqv-7f7q |

*Full public advisory query: https://osv.dev/list?ecosystem=PyPI&q=sqlalchemy*

## Security Posture Notes

- SQLAlchemy's currently surfaced direct PyPI advisory history is compact but high-impact: the confirmed package-level records are SQL-injection issues in SQL construction / textual-coercion boundaries rather than parser DoS or supply-chain events.
- The 2019 records share a root pattern: applications that pass attacker-controlled strings into ORM / Core expression helpers such as `order_by()` or `group_by()` can bypass the safety normally provided by SQLAlchemy's structured expression and parameter binding APIs.
- Upstream issue #4481 is useful context because it documents the maintainer response: deprecating / rejecting plain string expression coercions and directing callers toward explicit textual APIs when raw SQL is intentional.
- Treat the fixed-version boundary carefully. The GHSA-derived OSV records and older PYSEC duplicates disagree on exact 1.2.x fixed versions for the 2019 records (`1.3.0b3` vs `1.2.18` for `order_by`, `1.2.19` vs `1.2.18` for `group_by`). The KB should prefer the active GHSA / OSV GHSA records for vulnerability rows and preserve the discrepancy as an evidence note, not silently collapse it.
- Modern SQLAlchemy 1.4 / 2.x applications are outside these old affected ranges, but code review should still reject user-controlled sort / grouping strings unless they are mapped through an allowlist of known column expressions.

## Dependencies of Note

- These advisories are direct SQLAlchemy package issues. Public records do not implicate DBAPI drivers such as `psycopg2`, `mysqlclient`, or `sqlite3` as the vulnerable component.
- Frameworks and application templates that expose user-selected ordering, grouping, or filtering should map request parameters to explicit SQLAlchemy column/expression objects rather than concatenating or forwarding raw strings.
- Distribution advisories from Debian, Red Hat, openSUSE, and Oracle appear in OSV references for the 2019 issues, which suggests a broad downstream packaging surface even though the upstream package record set is small.

## Open Questions

- Should the KB later add a short cross-reference note for frameworks that commonly expose user-sort APIs backed by SQLAlchemy, to point users toward allowlisted expression mapping?
- Can upstream / distro history fully reconcile the 2019 fixed-version discrepancy between GHSA-derived records and PYSEC duplicates for the 1.2.x line?
- Are there public SQLAlchemy security-release notes beyond the issue / commit references that should be preserved alongside the advisory rows?

## Related Pages

- [[python/fastapi]]
- [[python/flask]]
- [[python/werkzeug]]
- [[python/requests]]
- [[python/index]]

---
*Last updated: 2026-05-08 | Sources: OSV package query and vulnerability details, GitHub Advisory Database records, public CVE / PYSEC aliases, upstream SQLAlchemy issue / commit references, distro advisory references, PyPI metadata, and local proxy synthesis used as a drafting aid only.*
