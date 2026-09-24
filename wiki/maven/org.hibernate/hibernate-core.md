# hibernate-core (Maven)

**Registry:** Maven Central
**Weekly Downloads:** unknown (Maven Central download stats not publicly available via API)
**Repository:** https://github.com/hibernate/hibernate-orm
**Security Contact:** none listed (Red Hat / JBoss security team handles; report via Red Hat Bugzilla)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-14900 / GHSA-8grg-q944-cch5 | Moderate CVSS 7.1 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N) | SQL injection (CWE-89) via unsanitized literals in SELECT or GROUP BY clauses of JPA Criteria API queries; attackers with low privileges can access restricted data | 5.3.18.Final, 5.4.18.Final, 5.5.0.Beta1 | [GHSA-8grg-q944-cch5](https://github.com/advisories/GHSA-8grg-q944-cch5) |
| CVE-2020-25638 / GHSA-j8jw-g6fq-mp7h | High CVSS 9.1 (AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N) | SQL injection (CWE-89) via unsanitized literals embedded in SQL comment portion of JPA Criteria API queries; enables unauthorized data access and database manipulation | 5.3.20.Final, 5.4.24.Final | [GHSA-j8jw-g6fq-mp7h](https://github.com/advisories/GHSA-j8jw-g6fq-mp7h) |
| CVE-2026-0603 / GHSA-2p5w-cvg5-gc5c | High CVSS 8.1 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L) | Second-order SQL injection (CWE-89) in InlineIdsOrClauseBuilder: unsanitized non-alphanumeric characters in ID columns are interpolated into generated SQL; enables data access, manipulation, deletion, and app-level DoS | No fix documented; affects 5.2.8–5.6.15 (EOL 5.x branch only) | [GHSA-2p5w-cvg5-gc5c](https://github.com/advisories/GHSA-2p5w-cvg5-gc5c) |

## Security Posture Notes

Hibernate ORM is the dominant Java persistence/ORM framework, used in the majority of Spring Boot applications via the `spring-boot-starter-data-jpa` auto-configuration. It implements the Jakarta Persistence (JPA) specification and is maintained by Red Hat / JBoss.

All three confirmed GHSA advisories target the now-EOL **Hibernate 5.x branch**. Hibernate 5.x reached end of life (no further patches) approximately 2023. The current actively maintained lines are **6.x and 7.x**, which represent a major architectural rewrite of the ORM core and JPA implementation. No confirmed package-level GHSA advisories for `hibernate-core` 6.x or 7.x were found in this pass.

**Recurring advisory pattern — CWE-89 SQL injection via JPA Criteria API:** Hibernate 5.x interpolated certain literal values (especially those passed via `.literal()` or analogous Criteria API surfaces) into generated SQL without adequate escaping. When application code passed user-controlled values through these paths, SQL injection was possible. The 6.x rewrite rearchitected the SQL generation layer and appears to have closed many of these interpolation gaps.

**Note on a related package:** CVE-2020-10693 (GHSA-rmrm-75hp-phr2) affects `org.hibernate.validator:hibernate-validator` (Bean Validation / constraint annotations), not `org.hibernate:hibernate-core`. Teams auditing dependency trees should note the separate Maven coordinates.

## Dependencies of Note

- `antlr4-runtime` — used for HQL/JPQL query parsing; ANTLR4 runtime has had resource-exhaustion advisories in other contexts.
- Applications commonly pair hibernate-core with connection pools (HikariCP, c3p0) and database drivers (PostgreSQL JDBC, MySQL Connector/J), each with their own advisory histories.

## Open Questions

- Are there GHSA advisories for `hibernate-core` 6.x or 7.x beyond those found in this pass?
- Does the InlineIdsOrClauseBuilder SQL injection pattern (CVE-2026-0603) exist in the 6.x architecture, or was it eliminated by the ORM rewrite?
- What is the Hibernate team's disclosed security contact and CVE disclosure process for the current 6.x/7.x lines?

## Related Pages

- [[maven/org.springframework/spring-web]]
- [[maven/org.springframework/spring-webmvc]]
- [[maven/index]]

---
*Last updated: 2026-09-24 | Sources: 3*
