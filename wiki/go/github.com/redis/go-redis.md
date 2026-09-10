# go-redis (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (importer count: 17,374 as of 2026-09-10)
**Repository:** https://github.com/redis/go-redis
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
| CVE-2025-29923 / GHSA-92cp-5422-2mw7 | Low (CVSS 3.1 AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N) | Out-of-order responses when `CLIENT SETINFO` times out during connection establishment. On sticky connections: persistent wrong responses for the connection lifetime. In pipelines: all commands receive incorrect responses. In standard pool usage: typically one wrong response before the connection is discarded. Requires client identity transmission enabled plus network issues or aggressive timeouts. Mitigation: set `DisableIndentity: true`. | v9.5.5, v9.6.3, v9.7.3 | [GHSA-92cp-5422-2mw7](https://github.com/advisories/GHSA-92cp-5422-2mw7) |

## Security Posture Notes

`github.com/redis/go-redis` (v9 module path: `github.com/redis/go-redis/v9`) is the official Redis client for Go, maintained by the Redis team. It supports Redis 8.8+ features, RESP3 protocol, cluster, failover, and ring client configurations, plus OpenTelemetry instrumentation. With 17,374 importers on pkg.go.dev, it is the de facto standard Go Redis client.

The single published advisory (CVE-2025-29923 / GHSA-92cp-5422-2mw7, March 2025) is a low-severity race condition in the connection establishment handshake: if `CLIENT SETINFO` times out, queued responses can arrive out-of-order. Impact depends on connection mode (worst-case in pipelines; usually self-correcting in standard pool usage). The fix (v9.5.5, v9.6.3, v9.7.3) was released promptly. Users on v9.5.1–v9.7.1 should upgrade; current v9.22.0 is unaffected.

No SECURITY.md is listed in the repository. BSD-2-Clause licensed.

## Dependencies of Note

None flagged.

## Open Questions

- Does `github.com/go-redis/redis` (the older module path) have separate advisory history not covered here?
- Is there a formal SECURITY.md or security contact for the redis/go-redis project?

## Related Pages

- [[python/redis]] — redis-py Python client
- [[go/index]]

---
*Last updated: 2026-09-10 | Sources: 1 (GHSA-92cp-5422-2mw7 / CVE-2025-29923)*
