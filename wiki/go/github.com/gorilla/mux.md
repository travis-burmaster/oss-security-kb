# github.com/gorilla/mux (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-04-20)
**Repository:** https://github.com/gorilla/mux
**Security Contact:** https://github.com/gorilla/mux/security (GitHub private vulnerability reporting) · gorilla-maintainers@googlegroups.com
**Disclosure Policy:** https://github.com/gorilla/mux/security (reports via GitHub “Report a vulnerability” form or maintainer email)
**Current Status:** baseline stub

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-20 | OpenClaw recurring review | package advisory baseline | manual | No direct package-scoped OSV or GitHub security advisories were confirmed in this pass; repository activity was still present in 2024, so this page stays a conservative baseline rather than an archived-project warning page. | https://osv.dev/list?ecosystem=Go&q=github.com/gorilla/mux |
| 2026-04-26 | OpenClaw recurring review | reporting / disclosure metadata | manual | Recorded GitHub Security tab reporting path (GitHub private vulnerability reporting + maintainer email). No package-scoped OSV entries observed at review time. | https://github.com/gorilla/mux/security |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| (none confirmed in this pass) | — | No clean package-scoped OSV.dev or GitHub Security Advisory record was confirmed for `github.com/gorilla/mux` in this review window. | — | https://osv.dev/list?ecosystem=Go&q=github.com/gorilla/mux |

## Security Posture Notes

- `gorilla/mux` remains a widely recognized Go router dependency, but this pass did **not** confirm direct package-scoped public advisories through OSV.dev or the repository's GitHub security-advisory listing.
- The repository was still publicly active in 2024 (`pushed_at` 2024-08-15 via the public GitHub repository API), so older assumptions that the project was simply archived should be treated cautiously.
- The repository publishes a security-reporting path on its GitHub *Security* tab: reports can be filed via GitHub’s “Report a vulnerability” flow or by emailing `gorilla-maintainers@googlegroups.com`. Source: https://github.com/gorilla/mux/security
- No standalone `SECURITY.md` document was confirmed in this pass; treat the GitHub Security tab as the canonical disclosure metadata for now.
- Because `gorilla/mux` sits on request-routing and path-matching boundaries, future review work should focus on public route-matching edge cases, path normalization behavior, header-derived routing, and static-file helper examples if any package-scoped advisories or maintainer disclosures later emerge.

## Dependencies of Note

- Go's standard `net/http` stack shapes much of the surrounding request-routing behavior, so some future findings may belong on adjacent pages rather than on `gorilla/mux` itself.
- Middleware layered on top of `gorilla/mux` may carry more practical security risk than the router core when applications trust forwarded headers, CORS policy helpers, or static-file serving shortcuts.

## Open Questions

- Are there public maintainer or community write-ups on `gorilla/mux` route-matching edge cases that deserve tracking separately from formal advisories?
- Should a later Go framework pass compare `gorilla/mux` posture against `gin`, `echo`, and standard-library `ServeMux` hardening guidance?
- Is there a clean public disclosure path for security reports beyond standard issue filing, even though no `SECURITY.md` was found here?

## Related Pages

- [[go/github.com/gin-gonic/gin]]
- [[go/github.com/labstack/echo-v4]]
- [[go/index]]

---
*Last updated: 2026-04-26 | Sources: 6 (OSV package query, public GitHub repository API, public GitHub security-advisory listing, upstream README, repository SECURITY.md path check, GitHub Security tab reporting guidance)*
