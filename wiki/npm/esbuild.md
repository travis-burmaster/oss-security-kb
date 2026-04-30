# esbuild (npm)

**Registry:** npm
**Weekly Downloads:** ~200,587,828 (2026-04-14 to 2026-04-20)
**Repository:** https://github.com/evanw/esbuild
**Security Contact:** none listed
**Disclosure Policy:** public GitHub security advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-21 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / GitHub security advisories, upstream fix references, npm registry metadata, npm downloads API, local Claude-compatible proxy used only as a drafting aid) | Added a new advisory-mapped baseline page for `esbuild`'s currently published package security history, centered on the 2025 development-server CORS issue that allowed malicious websites to read responses from the local dev server before `0.25.0`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-67mh-4wv8-2f99 | Moderate | Public advisory records describe overly permissive default CORS behavior in the `esbuild` development server / `serve()` API, allowing a malicious website to send requests to the dev server and read responses cross-origin. OSV maps the affected range to versions before `0.25.0`, and the advisory's reference set includes the upstream fix commit. | 0.25.0 | https://github.com/advisories/GHSA-67mh-4wv8-2f99 |

## Security Posture Notes

- `esbuild` has a **small currently published package-level advisory footprint** in this review pass: one public GitHub / OSV record rather than a long chain of parser or supply-chain issues.
- The scope matters: the published advisory is about the **development server feature**, not generic production bundling output. That makes the page worth keeping explicit and non-alarmist.
- The GHSA text is concrete about the attack model: a malicious website could issue requests to the local dev server and read responses because of default CORS behavior, including development assets and potentially source-map-backed source content.
- OSV maps the remediation point cleanly to **`0.25.0`**, and current npm metadata in this pass showed **`latest=0.28.0`**.
- The package's footprint is still hard to ignore: **~200.6M weekly downloads** in this review window, making even a dev-only exposure worth documenting because it appears in an enormous number of local build workflows.
- Real-world exposure depends heavily on use of `--serve` / `serve()` and on local network / browser conditions; teams using esbuild only as a bundler without the development server are outside the core published impact.
- No additional package-scoped OSV records for `esbuild` were surfaced in this review pass.
- OSV's **UI list view** at `https://osv.dev/list?ecosystem=npm&package=esbuild` returned *no results* during this run, but the OSV API `v1/query` endpoint returned the `GHSA-67mh-4wv8-2f99` record for `ecosystem=npm, name=esbuild`. Until that UI behavior is understood, treat the GitHub Advisory Database / upstream GHSA page as the canonical cross-link, and use OSV API queries for verification.

## Recommendations for Developers

1. **Upgrade to `0.25.0` or newer**; current npm metadata in this pass showed `0.28.0` as the latest release.
2. **Prioritize upgrades anywhere the `esbuild` dev server is used**, especially on developer workstations that browse arbitrary websites while local dev services are running.
3. **Treat local development servers as security boundaries**, not just convenience tooling; browser-origin interactions can still expose source or configuration data.
4. **If immediate upgrade is blocked, reduce exposure** by avoiding unnecessary dev-server use, restricting local network reachability, and being cautious about concurrently browsing untrusted sites during active dev sessions.

## Dependencies of Note

- Commonly appears in frontend build systems, framework dev servers, bundling pipelines, and toolchains that wrap esbuild rather than exposing it directly.
- Practical risk is concentrated in local development workflows rather than deployed production service paths.

## Open Questions

- Which framework wrappers or dev-tool stacks continued to pin `esbuild` below `0.25.0` after the public advisory landed?
- Are there strong public downstream release notes that explicitly called out this fix for users who consume esbuild transitively?
- Should a future KB pass cross-link a cluster of local-dev-server exposure issues across `esbuild`, `webpack-dev-server`, and similar tools?

## Related Pages

- [[npm/webpack-dev-server]]
- [[npm/http-proxy-middleware]]
- [[npm/index]]

---
*Last updated: 2026-04-21 | Sources: 6 (OSV.dev package query for npm/esbuild, OSV vulnerability record for GHSA-67mh-4wv8-2f99, GitHub Advisory Database / public GitHub security advisory for the same record, upstream fix commit reference linked from OSV / GHSA, npm registry metadata, npm downloads API)*
