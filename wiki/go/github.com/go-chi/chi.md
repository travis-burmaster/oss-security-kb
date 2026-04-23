# github.com/go-chi/chi (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-04-23)
**Repository:** https://github.com/go-chi/chi
**Security Contact:** GitHub Security Advisory "Report a Vulnerability"
**Disclosure Policy:** https://github.com/go-chi/chi/blob/master/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-23 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / public GHSA pages, public CVE records, Go vuln data, upstream `SECURITY.md`, public fix commit and tag metadata) | Added a new advisory-mapped page for `github.com/go-chi/chi` after confirming two public open-redirect issues in the `RedirectSlashes` middleware, including a later bypass / incomplete-fix chain through `v5.2.3`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-vrw8-fxc6-2r93 | Moderate | `RedirectSlashes` used the request `Host` header when constructing redirect targets, enabling a host-header-driven open redirect on applications that mounted that middleware. | 5.2.2 | https://github.com/go-chi/chi/security/advisories/GHSA-vrw8-fxc6-2r93 |
| CVE-2025-69725 / GHSA-mqqf-5wvp-8fh8 / GO-2026-4316 | Moderate | A later `RedirectSlashes` bypass left backslashes untrimmed, allowing redirect responses like `/\\evil.com` that major browsers normalize into protocol-relative redirects. | 5.2.4 | https://github.com/advisories/GHSA-mqqf-5wvp-8fh8 |

*Full CVE history: https://osv.dev/list?ecosystem=Go&q=github.com/go-chi/chi*

## Security Posture Notes

- Public package-level security history for `github.com/go-chi/chi` is currently **small but coherent**: both confirmed issues in this pass belong to the same middleware surface, `RedirectSlashes`, and both result in **open redirect behavior** rather than memory corruption or request-routing takeover at the router core.
- The first public advisory, `GHSA-vrw8-fxc6-2r93`, describes a **host-header injection** route to open redirect and points to `v5.2.2` as the fix point. That matters because it establishes a public incomplete-fix / follow-on context for later versions rather than a single isolated bug.
- The later public record, `GHSA-mqqf-5wvp-8fh8` / `CVE-2025-69725` / `GO-2026-4316`, cleanly shows that versions `5.2.2` and `5.2.3` still allowed a **backslash-based open redirect** even after the earlier host-header issue had been addressed.
- Public fix evidence for the later bug is unusually crisp: commit `6eb35881c0e438ffb663ddbad3a61babaa5e5d8a` adds a regression test that explicitly forbids backslashes and protocol-relative `//` redirects in the `Location` header and expects normalization to `/evil.com`.
- Scope should stay narrow. These are **middleware-specific** issues affecting applications that actually enable `middleware.RedirectSlashes`; they should not be overstated as all-purpose router vulnerabilities across every `chi` deployment.
- Upstream disclosure posture is healthy in the current pass: `SECURITY.md` directs reporters to GitHub's private security-advisory reporting flow.

## Dependencies of Note

- The relevant trust boundary here is the optional `middleware.RedirectSlashes` helper, not the full routing core in isolation.
- Reverse proxies, host-header handling, and browser URL normalization influence real-world impact, especially for phishing-style redirect abuse.
- Applications that do not use `RedirectSlashes` or that normalize / reject unusual request paths before middleware execution substantially reduce exposure.

## Open Questions

- Are there additional public maintainer notes or release annotations around `v5.2.2` and `v5.2.4` that would help distinguish intended redirect semantics from security hardening changes?
- Do common `chi` starter templates or middleware bundles enable `RedirectSlashes` by default in ways that deserve a downstream note?
- Should future Go KB work separate router-core issues from first-party middleware issues more explicitly when package-level advisories cluster on optional middleware surfaces?

## Related Pages

- [[go/github.com/gorilla/mux]]
- [[go/github.com/labstack/echo-v4]]
- [[go/index]]

---
*Last updated: 2026-04-23 | Sources: 8 (OSV.dev, GitHub Advisory Database / public GHSA pages, public CVE records, Go vuln data, upstream `SECURITY.md`, public fix commit, public advisory discussion, tag metadata)*
