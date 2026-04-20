# github.com/labstack/echo/v4 (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-04-20)
**Repository:** https://github.com/labstack/echo
**Security Contact:** https://github.com/labstack/echo/security/advisories/new
**Disclosure Policy:** https://github.com/labstack/echo/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-20 | OpenClaw recurring review | package advisory normalization | manual | 2 publicly disclosed package vulnerabilities normalized from OSV / Go vuln / GHSA records, plus upstream support-policy and release-note context | https://osv.dev/list?ecosystem=Go&q=github.com/labstack/echo/v4 |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-36565 / GHSA-j453-hm5x-c46w / GO-2021-0051 | Moderate | Windows-only directory traversal in static file handling could allow reading files outside the intended directory. Public references agree on the bug class and fix commit; the GHSA normalizes the released fix boundary as `4.2.0`, while the Go vuln record also points to the earlier fixing pseudo-version commit `4422e3b66b9f`. | 4.2.0 | https://github.com/advisories/GHSA-j453-hm5x-c46w |
| CVE-2022-40083 / GHSA-crxj-hrmp-4rwf / GO-2022-1031 | High | Open redirect in the static handler surface (`Echo.Static`, `Echo.StaticFS`, `Group.Static`, `Group.StaticFS`, `StaticDirectoryHandler`) that upstream fixed in the `4.9.0` security release. | 4.9.0 | https://github.com/advisories/GHSA-crxj-hrmp-4rwf |

*Full package history: https://osv.dev/list?ecosystem=Go&q=github.com/labstack/echo/v4*

## Security Posture Notes

- Echo v4 has a small but real package-level public advisory history centered on static-file serving boundaries: one Windows-specific traversal issue and one open-redirect issue.
- Upstream's current `SECURITY.md` signals a reasonably clear support policy: `5.x` supported, `>=4.15.x` supported until `2026-12-31`, and older `v4` releases marked unsupported.
- The upstream changelog contains additional security-relevant maintenance beyond the two package-scoped advisories above, including later header-escaping hardening, dependency security bumps, and the removal of legacy JWT middleware from core in `v4.13.0`. Those are useful operator signals but are intentionally kept out of the Known Vulnerabilities table here unless they map cleanly to package-scoped public advisory records.
- The main risk surfaces worth watching in Echo core are static file serving, proxy / redirect handling, header construction, request binding, and any security-sensitive middleware that remains in-tree versus split into companion modules.

## Dependencies of Note

- `golang.org/x/net` and `golang.org/x/crypto` matter because Echo release notes repeatedly pull in security fixes from the Go networking / crypto stack.
- `github.com/labstack/echo-jwt` became the preferred home for JWT middleware after Echo removed JWT middleware from core in `v4.13.0`; security history there should be tracked separately from core Echo.
- Applications using static file middleware on Windows deserve extra scrutiny because the older traversal bug was specifically OS-dependent.

## Open Questions

- Should a future companion page track `github.com/labstack/echo-jwt` separately now that JWT middleware no longer lives in core?
- Are there enough public core-Echo fixes in changelog-only security notes to justify a separate "security-relevant changes without package CVEs" section across Go framework pages?
- Does Echo's newer `v5` line accumulate its own distinct package-scoped advisory history, or will most risk continue to sit in middleware and transitive dependencies?

## Related Pages

- [[go/github.com/gin-gonic/gin]]
- [[go/google.golang.org/grpc]]
- [[go/index]]

---
*Last updated: 2026-04-20 | Sources: 7 (OSV package query, OSV vulnerability records for GHSA-j453-hm5x-c46w / GO-2021-0051 / GHSA-crxj-hrmp-4rwf / GO-2022-1031, upstream CHANGELOG, upstream v4.9.0 release notes, upstream SECURITY.md)*
