# StackExchange.Redis (.NET)

**Registry:** NuGet
**Weekly Downloads:** unknown (NuGet download stats API unavailable in this environment)
**Repository:** https://github.com/StackExchange/StackExchange.Redis
**Security Contact:** security@redis.com (via Redis Vulnerability Disclosure Program)
**Disclosure Policy:** https://redis.io/redis-responsible-vulnerability-disclosure/
**Current Status:** baseline stub

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| (none on record) | — | — | — | — |

*No package-level GHSA or NVD advisories confirmed for StackExchange.Redis in this pass. Verify live record: https://osv.dev/list?ecosystem=NuGet&q=StackExchange.Redis*

## Security Posture Notes

StackExchange.Redis is the de facto Redis client for .NET, maintained by the Stack Overflow engineering team (Stack Exchange). It provides both synchronous and asynchronous access to Redis 3.0+ and supports Sentinel, cluster mode, and SSL/TLS. Latest stable: 3.1.13 (2026-08-06), MIT license.

No package-level CVE or GHSA advisories were found in the GitHub Advisory Database in this pass. The absence of advisories should not be read as a clean bill of health — the package handles serialized data from untrusted sources in many deployments and exposes configurable TLS/auth settings. The security disclosure channel points to redis.io rather than directly to the StackExchange.Redis GitHub repository, which may affect responsiveness for library-specific issues.

Key security-relevant areas for future review:
- TLS configuration: StackExchange.Redis supports ssl=true and custom certificate validation via SslProtocols and CertificateValidation event. Misconfigurations (e.g., ignoring certificate errors) do not generate library-level advisories but are a common deployment risk.
- AUTH authentication bypass: Versions before the 2.x multiplexer rewrite had edge cases around authentication state in reconnection; no public CVE confirmed.
- Command injection via scripted Lua or EVAL: Applications passing unsanitized user input to ScriptEvaluate are vulnerable to arbitrary Lua execution on the Redis server side; no package-level advisory assigned.

## Dependencies of Note

None flagged in this pass. Key transitive deps include System.IO.Pipelines and System.Threading.Channels (.NET runtime packages; no known advisories at package level).

## Open Questions

- Fetch actual NuGet total download count (unavailable in this environment; check nuget.org directly).
- Confirm whether StackExchange.Redis has a dedicated security policy distinct from the upstream redis.io disclosure channel.
- Review whether the command-pipelining reconnection logic in the 2.x multiplexer is susceptible to SSRF or credential-leakage class bugs similar to go-redis CVE-2025-29923.

## Related Pages

- [[dotnet/index]]

---
*Last updated: 2026-09-19 | Sources: 1*
