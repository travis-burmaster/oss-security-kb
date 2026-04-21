# webpack-dev-server (npm)

**Registry:** npm
**Weekly Downloads:** ~17,462,478 (2026-04-14 to 2026-04-20)
**Repository:** https://github.com/webpack/webpack-dev-server
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** https://github.com/webpack/webpack-dev-server/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-21 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / upstream GitHub security advisories, public CVE records, upstream release notes / changelog, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for `webpack-dev-server`'s published package security history, centered on origin-validation and cross-origin WebSocket / script-loading exposure in developer environments. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2018-14732 / GHSA-cf66-xwfp-gvc4 | Moderate | Versions before `3.1.11` were missing origin validation on the WebSocket server used for hot-module reload traffic, which public advisory text says could let a remote attacker steal a developer's source code. Upstream `v3.1.11` release notes explicitly mention checking the Origin header for WebSocket connections. | 3.1.11 | https://github.com/advisories/GHSA-cf66-xwfp-gvc4 |
| CVE-2025-30359 / GHSA-4v9v-hfq4-rm2v | Moderate | Public advisory text says a malicious website could load the predictable local dev-server script and, with the described runtime-variable exposure technique, recover source code from the webpack runtime. Upstream `v5.2.1` release notes tie the fix to stricter cross-origin request handling. | 5.2.1 | https://github.com/advisories/GHSA-4v9v-hfq4-rm2v |
| CVE-2025-30360 / GHSA-9jgg-88mc-972h | Moderate | Follow-on cross-site WebSocket exposure in non-Chromium browser scenarios: public advisory text says IP-address `Origin` headers were still accepted, reopening a source-code disclosure path until the `v5.2.1` hardening release. | 5.2.1 | https://github.com/advisories/GHSA-9jgg-88mc-972h |

## Security Posture Notes

- `webpack-dev-server` has a **small but clearly security-relevant public advisory trail** focused on one recurring trust boundary: who is allowed to reach the dev server's script and WebSocket/HMR surfaces from another origin.
- The advisories are unusually coherent across time. The 2018 issue fixed missing WebSocket origin validation, and the 2025 pair show that **cross-origin dev-server exposure remained subtle enough to need later hardening around script loading and IP-address-origin WebSocket cases**.
- Public release notes make the fix windows easy to normalize without guesswork. `v3.1.11` says it added an Origin-header check for WebSocket connections, while `v5.2.1` says cross-origin requests are no longer allowed unless explicitly permitted and that IP-address Origin headers are blocked for WebSocket connections unless configured via `allowedHosts` or a matching Host.
- This package is developer tooling rather than a typical production runtime dependency, but that does **not** make the issues irrelevant. In real teams, dev servers are often reachable from browsers, local networks, shared demos, Codespaces-like environments, or reverse-proxied preview stacks where cross-origin assumptions matter.
- Current npm metadata in this review shows `latest=5.2.3`, so the public package-advisory set reviewed here supports a simple modern floor of **`5.2.1+` on the maintained 5.x line**. Older 3.x users need at least `3.1.11` for the historical origin-validation fix, but that should not be mistaken for full coverage of the later 2025 hardening.

## Recommendations for Developers

1. **Upgrade to `5.2.1` or newer** on maintained lines; current npm metadata in this pass showed `5.2.3` as latest.
2. **Do not expose dev-server instances more broadly than necessary**; treat them as sensitive local tooling, not harmless static preview servers.
3. **Review `allowedHosts`, host binding, and reverse-proxy / tunnel setups carefully**, because the public advisory history is explicitly about cross-origin and origin-header trust decisions.
4. **Assume source code can be security-sensitive** in dev environments too, especially for private applications, internal APIs, feature flags, or bundled secrets accidentally present during local development.
5. **Do not treat the 2018 `3.1.11` fix as the end of the story**; the 2025 advisories show follow-on hardening was still necessary on modern lines.

## Dependencies of Note

- Commonly used in local frontend development, hot-module reload workflows, and preview environments rather than production request paths.
- Risk increases when local dev servers are reachable from untrusted web content, LAN peers, browser sessions visiting arbitrary sites, or externally exposed preview / tunnel endpoints.

## Open Questions

- Are there good maintainer-authored writeups that explain the exploit preconditions for the 2025 source-code disclosure pair more concretely than the advisory texts and release notes alone?
- Should the KB eventually add a small cluster view for developer tooling packages where browser-origin trust assumptions matter, rather than treating them like ordinary production middleware?
- Which still-common starter kits or build templates pin `webpack-dev-server` below `5.2.1` in long-lived branches?

## Related Pages

- [[npm/webpack]]
- [[npm/express]]
- [[npm/http-proxy-middleware]]
- [[npm/index]]

---
*Last updated: 2026-04-21 | Sources: 8 (OSV.dev package query for npm/webpack-dev-server, OSV vulnerability records for the three GHSA IDs listed above, GitHub Advisory Database / upstream GitHub security advisories, public CVE records, upstream release notes for v3.1.11 and v5.2.1, upstream changelog references, npm registry metadata, npm downloads API)*