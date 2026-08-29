# gofiber/fiber (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (30,850 importers for v2; 1,480 for v3, as of 2026-08-29)
**Repository:** https://github.com/gofiber/fiber
**Security Contact:** rene@gofiber.io
**Disclosure Policy:** https://github.com/gofiber/fiber/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-15111 / GHSA-9cx9-x2gp-9qvh | Moderate | `c.Attachment()` does not escape filenames → CRLF injection enabling HTTP response-header manipulation | v1.12.6 | [GHSA-9cx9-x2gp-9qvh](https://github.com/advisories/GHSA-9cx9-x2gp-9qvh) |
| CVE-2018-20744 / GHSA-927h-x4qj-r242 | Moderate | CORS middleware wildcard (`*`) reflects arbitrary `Origin` headers; also affects `rs/cors` ≤ 1.4.x | v2.43.0 | [GHSA-927h-x4qj-r242](https://github.com/advisories/GHSA-927h-x4qj-r242) |
| CVE-2023-41338 / GHSA-3q5p-3558-364f | Moderate | `ctx.IsFromLocal()` trusts `X-Forwarded-For: 127.0.0.1`, allowing remote callers to spoof localhost identity | v2.49.2 | [GHSA-3q5p-3558-364f](https://github.com/advisories/GHSA-3q5p-3558-364f) |
| CVE-2023-45128 / GHSA-94w9-97p3-p368 | Critical | CSRF middleware extracts tokens from cookies without sanitization, enabling token injection and forged requests | v2.50.0 | [GHSA-94w9-97p3-p368](https://github.com/advisories/GHSA-94w9-97p3-p368) |
| CVE-2023-45141 / GHSA-mv73-f69x-444p | High | CSRF tokens not bound to session or using Double Submit Cookie; token reuse enables cross-user forgery (CVSS 9.8 NVD) | v2.50.0 | [GHSA-mv73-f69x-444p](https://github.com/advisories/GHSA-mv73-f69x-444p) |
| CVE-2024-22199 / GHSA-4mq2-gc4j-cmw6 | Critical | `gofiber/template/django/v3`: autoescape disabled by default, embedding user-controlled data as raw HTML → XSS | gofiber/template django/v3 3.1.9 | [GHSA-4mq2-gc4j-cmw6](https://github.com/advisories/GHSA-4mq2-gc4j-cmw6) |
| CVE-2024-25124 / GHSA-fmg4-x8pw-hjhg | Critical | CORS middleware allowed wildcard origin (`*`) with `credentials: true` simultaneously → cross-origin authenticated requests | v2.52.1 | [GHSA-fmg4-x8pw-hjhg](https://github.com/advisories/GHSA-fmg4-x8pw-hjhg) |
| CVE-2024-38513 / GHSA-98j2-3j3p-fw2v | Critical | Session middleware accepts client-supplied `session_id` values → session fixation (CVSS 9.8) | v2.52.5 | [GHSA-98j2-3j3p-fw2v](https://github.com/advisories/GHSA-98j2-3j3p-fw2v) |
| CVE-2025-48075 / GHSA-hg3g-gphw-5hhm | High | `BodyParser` panics on negative array index in form data field names → unauthenticated DoS | v2.52.7 | [GHSA-hg3g-gphw-5hhm](https://github.com/advisories/GHSA-hg3g-gphw-5hhm) |
| CVE-2025-54801 / GHSA-qx2q-88mx-vhg7 | High | `BodyParser` allocates slice of `idx+1` without bounding large numeric indices → OOM/panic DoS | v2.52.9 | [GHSA-qx2q-88mx-vhg7](https://github.com/advisories/GHSA-qx2q-88mx-vhg7) |
| CVE-2025-66565 / GHSA-m98w-cqp3-qcqr | Critical | `gofiber/utils` `UUIDv4()`/`UUID()` silently return all-zero UUID when `crypto/rand` errors on Go < 1.24 → predictable session and CSRF tokens | gofiber/utils 1.2.0 / utils/v2 2.0.0-rc.4 | [GHSA-m98w-cqp3-qcqr](https://github.com/advisories/GHSA-m98w-cqp3-qcqr) |
| CVE-2025-66630 / GHSA-68rr-p4fp-j59v | Critical | fiber v2 UUID generation silently falls back to predictable all-zero UUID when `crypto/rand` errors on Go < 1.24 → session hijacking and CSRF token forgery | v2.52.11 | [GHSA-68rr-p4fp-j59v](https://github.com/advisories/GHSA-68rr-p4fp-j59v) |
| CVE-2026-25882 / GHSA-mrq8-rjmw-wpq3 | Moderate | Router panics when a request matches a route with more than 30 path parameters (fixed-size array, no bounds check) → unauthenticated DoS | v2.52.12 / v3.1.0 | [GHSA-mrq8-rjmw-wpq3](https://github.com/advisories/GHSA-mrq8-rjmw-wpq3) |
| CVE-2026-25891 / GHSA-m3c2-496v-cw3v | High | Static middleware (v3, Windows only): double-encoded backslashes bypass `sanitizePath` pre-decode check → path traversal | v3.1.0 | [GHSA-m3c2-496v-cw3v](https://github.com/advisories/GHSA-m3c2-496v-cw3v) |
| CVE-2026-25899 / GHSA-2mr3-m5q5-wgp6 | High | Flash cookie parser (v3): msgpack deserialization without array-size bounds → up to 85 GB RAM allocation; unauthenticated, affects all v3 endpoints | v3.1.0 | [GHSA-2mr3-m5q5-wgp6](https://github.com/advisories/GHSA-2mr3-m5q5-wgp6) |
| CVE-2026-30246 / GHSA-35hp-hqmv-8qg8 | Moderate | Cache middleware (v3) keys only on request path, ignoring query strings → different queries return identical cached responses | v3.2.0 | [GHSA-35hp-hqmv-8qg8](https://github.com/advisories/GHSA-35hp-hqmv-8qg8) |
| CVE-2026-42554 / GHSA-qjv7-627w-8qjv | Moderate | `AutoFormat()` embeds attacker-controlled data in HTML `<p>` wrapper without escaping when `Accept: text/html` → XSS | v2.52.13 / v3.2.0 | [GHSA-qjv7-627w-8qjv](https://github.com/advisories/GHSA-qjv7-627w-8qjv) |
| CVE-2026-44332 / GHSA-g5vh-55hw-rxm8 | Moderate | BasicAuth middleware (v3): short-circuit evaluation skips password-hash comparison for non-existent usernames → ~1,000,000:1 timing oracle enabling username enumeration | v3.3.0 | [GHSA-g5vh-55hw-rxm8](https://github.com/advisories/GHSA-g5vh-55hw-rxm8) |
| CVE-2026-53624 / GHSA-gv83-gqw6-9j2c | Moderate | Helmet middleware (v3): `c.Protocol()` returns HTTP version string (e.g. "HTTP/1.1") rather than scheme; HSTS header silently omitted in production | v3.4.0 | [GHSA-gv83-gqw6-9j2c](https://github.com/advisories/GHSA-gv83-gqw6-9j2c) |

## Security Posture Notes

Fiber is an Express-inspired Go web framework built on Fasthttp, with 40,100+ GitHub stars, 30,850+ known pkg.go.dev importers for v2, and 1,480 for v3 (as of 2026-08-29). Current stable releases: v2.52.15 and v3.5.0 (both August 12, 2026). The project maintains both major versions in parallel.

The advisory history (19 GHSAs spanning 2020–2026) reveals several recurring patterns:

- **CORS misconfiguration**: Wildcard-origin reflection (CVE-2018-20744, fixed v2.43.0) re-appeared as wildcard+credentials=true (CVE-2024-25124, fixed v2.52.1), indicating the CORS boundary is a persistent risk area.
- **BodyParser input validation**: Two separate DoS advisories in 2025 for negative (CVE-2025-48075) and unbounded-large (CVE-2025-54801) slice indices, fixed one minor version apart.
- **CSRF implementation**: Dual CSRF advisories in the same v2.50.0 fix train (CVE-2023-45128, CVE-2023-45141), suggesting the entire CSRF middleware was rewritten rather than patched incrementally.
- **UUID predictability**: A cross-cutting zero-fallback bug affected both the core fiber v2 package (CVE-2025-66630, fixed v2.52.11) and the companion `gofiber/utils` package (CVE-2025-66565), both under Go < 1.24 where `crypto/rand` can fail silently.
- **v3 migration surface**: The v3 rewrite introduced new issues—Windows path traversal in static middleware (CVE-2026-25891), a msgpack-DoS in the flash-cookie parser affecting all v3 endpoints regardless of flash usage (CVE-2026-25899), a BasicAuth timing oracle (CVE-2026-44332), and an inverted scheme-check in the Helmet middleware (CVE-2026-53624).

Security reports are accepted at rene@gofiber.io or via Discord DM to maintainers; public GitHub issues must not be used for security reports. Versions below 1.12.6 are unsupported.

Two rows in the vulnerability table cover companion packages (`gofiber/template/django/v3` for CVE-2024-22199 and `gofiber/utils` for CVE-2025-66565) rather than the core fiber module, but are included because both are first-party gofiber packages and the issues directly affect fiber-based applications.

## Dependencies of Note

- **Fasthttp**: The underlying HTTP engine; Fasthttp security issues propagate to all Fiber deployments. Not yet covered in this KB.
- **gofiber/utils**: Companion utility package; CVE-2025-66565 (UUID zero-fallback) affects session management and CSRF protection in applications running Go < 1.24.
- **gofiber/template/django**: Template engine sub-package; CVE-2024-22199 XSS from disabled autoescape default.

## Open Questions

- What is the security track record of Fasthttp (the underlying HTTP engine driving Fiber)?
- Are there advisories covering other gofiber ecosystem packages (storage adapters, JWT middleware, keyauth middleware)?
- Does Fiber v3 address the CORS and CSRF patterns that produced multiple advisories on v2?

## Related Pages

- [[go/github.com/gin-gonic/gin]]
- [[go/github.com/labstack/echo-v4]]
- [[go/github.com/go-chi/chi]]
- [[go/index]]

---
*Last updated: 2026-08-29 | Sources: 19*
