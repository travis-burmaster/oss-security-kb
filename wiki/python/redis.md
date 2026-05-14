# redis (python)

**Registry:** PyPI  
**Weekly Downloads:** ~64,114,334 (PyPIStats last week, fetched 2026-05-14)  
**Repository:** https://github.com/redis/redis-py  
**Security Contact:** none listed in PyPI metadata  
**Disclosure Policy:** GitHub private vulnerability reporting / GitHub Security Advisories  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-14 | OpenClaw recurring review | package-level public advisory mapping for PyPI `redis` / redis-py | public-source curation from OSV.dev package and vulnerability records, GitHub Advisory Database records, public CVE / NVD pages, upstream issue / PR / release references, PyPI metadata, PyPIStats download data, and local proxy-assisted drafting | Added initial advisory-mapped page for redis-py's published package vulnerability history: one async connection-reuse / race-condition vulnerability class represented by CVE-2023-28858 plus incomplete-fix follow-up CVE-2023-28859. | https://osv.dev/list?ecosystem=PyPI&q=redis |

## Known Vulnerabilities

OSV returns both canonical GHSA records and duplicate PYSEC records for the same two CVEs. This page counts the underlying vulnerability chain once per CVE and keeps the incomplete-fix relationship explicit.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-28858 / GHSA-24wv-mv5m-xv4h / PYSEC-2023-45 | Moderate | redis-py left a connection open after cancellation of an async Redis command at an inopportune time, specifically described for pipeline operation, so response data could be delivered to an unrelated client request in an off-by-one manner. Public records note that the initial fixed versions were later believed incomplete. | 4.3.6 / 4.4.3 / 4.5.3 were the initial fixed releases, but consumers should treat them as an intermediate boundary because CVE-2023-28859 covers the incomplete fix. | https://github.com/advisories/GHSA-24wv-mv5m-xv4h ; https://osv.dev/vulnerability/GHSA-24wv-mv5m-xv4h ; https://nvd.nist.gov/vuln/detail/CVE-2023-28858 |
| CVE-2023-28859 / GHSA-8fww-64cx-x8p5 / PYSEC-2023-46 | High | Incomplete fix for CVE-2023-28858: redis-py through the earlier fix boundary could still leave a connection open after cancellation of an async command, described for non-pipeline operation, and send response data to an unrelated request. | 4.4.4 / 4.5.4 | https://github.com/advisories/GHSA-8fww-64cx-x8p5 ; https://osv.dev/vulnerability/GHSA-8fww-64cx-x8p5 ; https://nvd.nist.gov/vuln/detail/CVE-2023-28859 |

*Full OSV package listing: https://osv.dev/list?ecosystem=PyPI&q=redis*

## Security Posture Notes

- redis-py is a high-blast-radius Python Redis client used directly by applications and transitively by queues, caches, rate-limiters, session stores, and framework integrations. Connection-pool and async cancellation behavior can become a cross-request confidentiality boundary.
- The public package-advisory footprint found in this pass is compact but important: two CVEs describe the same async connection-reuse leak class, with the second record explicitly caused by an incomplete first fix.
- Upgrade guidance should prefer the final fixed boundary rather than the intermediate CVE-2023-28858 boundary. Users on affected async-capable 4.2.x through 4.5.3 releases should move to at least 4.4.4 / 4.5.4 or, preferably, the current supported release line.
- The public records tie the issue to cancellation of async Redis commands. This page does not claim exploitability for synchronous-only use beyond what the published advisory text supports.
- Current PyPI metadata during this review showed `latest=7.4.0`, well beyond the 2023 fixed versions.
- This review did not perform active vulnerability hunting, exploit validation, or live target testing. It only normalized already-public advisory, CVE, upstream issue / PR / release, and package metadata.

## Dependencies of Note

- Redis client risk depends heavily on deployment boundaries: shared Redis clusters, connection pools, async task workers, caches, and session stores can amplify confidentiality impact when response data is misrouted.
- Applications using redis-py underneath Celery, Django / Flask cache integrations, FastAPI services, or custom async workers should verify the actually imported client version rather than only the top-level framework package.
- Redis server hardening, network isolation, authentication, and TLS remain separate concerns not captured by the Python client package advisories.

## Open Questions

- Should future KB maintenance add dedicated pages for `kombu`, `django-redis`, or other high-usage Redis integration layers that inherit redis-py risk through dependency pins?
- Are there public downstream incident reports, beyond the advisory-linked OpenAI postmortem reference, that clarify common reachability patterns for the async cancellation leak?
- Should the KB add a shared Python async-client note for cancellation-safe connection reuse across Redis, HTTP, database, and message-queue clients?

## Related Pages

- [[python/celery]]
- [[python/django]]
- [[python/fastapi]]
- [[python/index]]

---
*Last updated: 2026-05-14 | Sources: OSV package query and individual vulnerability records for PyPI `redis`; GitHub Advisory Database entries for GHSA-24wv-mv5m-xv4h and GHSA-8fww-64cx-x8p5; public CVE / NVD records for CVE-2023-28858 and CVE-2023-28859; upstream redis-py issues #2624 and #2665, PR #2641, and 4.3.6 / 4.4.4 / 4.5.4 release references surfaced during review; PyPI metadata; PyPIStats recent download data; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid.*
