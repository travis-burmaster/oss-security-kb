# celery (python)

**Registry:** PyPI
**Repository:** https://github.com/celery/celery
**Security Contact:** https://github.com/celery/celery/security/policy
**Disclosure Policy:** https://github.com/celery/celery/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-08 | OpenClaw recurring review | package advisory history | manual | 2 unique public Celery vulnerability classes normalized from OSV / GHSA / PYSEC / CVE records, upstream changelog, and fix commits; duplicate PYSEC records kept with canonical GHSA rows | https://osv.dev/list?ecosystem=PyPI&q=celery |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-23727 / GHSA-q4xr-rc97-m4xx / PYSEC-2021-858 | High | Celery before 5.2.2 trusted task metadata stored in result backends when reading and deserializing failure information. If an attacker could access or manipulate backend metadata, the crafted metadata could trigger stored OS command injection. | 5.2.2 | https://github.com/advisories/GHSA-q4xr-rc97-m4xx |
| CVE-2011-4356 / GHSA-rpc6-h455-3rx5 / PYSEC-2011-17 | Moderate | Celery 2.1, 2.2 before 2.2.8, 2.3 before 2.3.4, and 2.4 before 2.4.4 changed effective IDs but not real IDs while processing `--uid` / `--gid` options in worker and beat helper commands, allowing local privilege escalation when attacker-controlled code ran in the process. | 2.2.8 / 2.3.4 / 2.4.4 | https://github.com/advisories/GHSA-rpc6-h455-3rx5 |

*Full public advisory query: https://osv.dev/list?ecosystem=PyPI&q=celery*

## Security Posture Notes

- Celery has a small direct public advisory set for a package with a large deployment footprint, but both confirmed records sit on important trust boundaries: result-backend integrity and privilege-dropping semantics for worker / scheduler processes.
- The 2021 command-injection advisory is conditional on an attacker being able to access or tamper with the result backend. Production deployments should treat Redis, database, AMQP, and other Celery result backends as sensitive infrastructure, not as semi-public queues.
- The upstream 5.2.2 changelog explicitly identifies the CVE-2021-23727 fix as a stored command-injection security fix and ties it to safer handling of serialized failure information.
- The 2011 privilege-escalation record applies to legacy 2.x deployments and service wrappers using `--uid` / `--gid`; modern deployments should still prefer service-manager-level privilege isolation over relying only on application-level user switching.
- Duplicate PYSEC entries appear alongside the GHSA records in OSV for both CVEs; count the underlying CVEs once each, not as four independent vulnerabilities.

## Dependencies of Note

- Celery security often depends on broker and backend hardening. Review Redis, RabbitMQ / AMQP, SQL result stores, and deployment service units separately when assessing a live system.
- Applications should pin Celery and its transport stack explicitly; transitive serializer, broker, or backend libraries can create separate exposure not captured by Celery package advisories alone.
- Deployments that enable result backends should restrict network access, credentials, and write permissions because backend write access is part of the precondition for CVE-2021-23727.

## Open Questions

- Which high-download Celery transport/backend dependencies deserve dedicated KB pages first: Redis clients, Kombu, AMQP libraries, or broker packages?
- Are common Docker Compose / Helm examples still exposing Celery result backends in ways that would make backend tampering realistic?
- Should the KB add a broader distributed-task-queue threat-model page covering broker trust, result backend integrity, serializer choices, and worker privilege isolation?

## Related Pages

- [[python/fastapi]]
- [[python/flask]]
- [[python/requests]]
- [[python/index]]

---
*Last updated: 2026-05-08 | Sources: OSV package query and vulnerability details, GitHub Advisory Database records, public CVE aliases, NVD CVE records, upstream Celery changelog / fix commits / security policy, and local proxy synthesis used as a drafting aid only.*
