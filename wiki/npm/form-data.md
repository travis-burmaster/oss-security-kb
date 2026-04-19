# form-data (npm)

**Registry:** npm
**Weekly Downloads:** ~145,555,919 (2026-04-11 to 2026-04-17)
**Repository:** https://github.com/form-data/form-data
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** https://github.com/form-data/form-data/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-18 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream GitHub security advisory, upstream fix commit and release notes, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for form-data's currently published package security history, centered on the 2025 multipart boundary predictability issue fixed across the maintained `2.x`, `3.x`, and `4.x` lines. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-7783 / GHSA-fjxv-7rqg-78g4 | Moderate | Public advisory records say `form-data` used `Math.random()` to choose multipart boundary values, creating a predictable-boundary weakness. The linked upstream fix commit explicitly switches boundary generation to crypto-backed randomness, and release `v4.0.4` includes that change. | 2.5.4, 3.0.4, 4.0.4 | https://github.com/advisories/GHSA-fjxv-7rqg-78g4 |

## Security Posture Notes

- `form-data` has a **small published advisory footprint so far** in this review pass: one modern package-level issue rather than a long historical chain.
- The advisory is still important because it spans **multiple maintained major lines at once** (`2.x`, `3.x`, and `4.x`), so downstream projects cannot assume that being on a newer major alone was enough before the fix landed.
- Public evidence aligns well here: the GitHub Advisory Database entry, OSV record, CVE alias, repo security advisory, fix commit, and `v4.0.4` release notes all point at the same boundary-generation weakness and fix window.
- The package remains one of the highest-volume npm dependencies reviewed in this KB (~145.6M weekly downloads in this pass), so even a single advisory can have a large downstream maintenance footprint.
- This package sits on a **request-construction trust boundary** rather than a parser boundary. That means the security question is less about inbound malformed input and more about whether predictable multipart framing can weaken assumptions in systems that accept or inspect generated multipart bodies.

## Recommendations for Developers

1. **Upgrade to `4.0.4` or newer**; if you are pinned to older lines, use at least `3.0.4` or `2.5.4`.
2. **Review transitive usage** in HTTP client wrappers, SDKs, upload helpers, and test fixtures that generate multipart requests on your behalf.
3. **Prefer security patches even for "just client-side" request builders**, because predictable framing can matter in multi-tenant gateways, signed upload workflows, and request-integrity assumptions.
4. **Treat `4.0.4` as the minimum reviewed safe floor** from the currently published public record gathered here.

## Dependencies of Note

- Frequently used beneath higher-level HTTP clients, SDKs, API wrappers, upload helpers, and integration-test tooling that need multipart request generation.
- Security-sensitive deployments include applications that construct authenticated upload requests, proxy multipart bodies, or rely on downstream parsers to distinguish generated boundaries safely.

## Open Questions

- Are there maintainer or third-party public writeups that explain the practical exploit preconditions for the predictable-boundary weakness in more operational detail than the advisory text alone?
- Which popular Node.js HTTP client stacks still pin `form-data` below `4.0.4` transitively?
- Should a future KB pass cross-reference this package more explicitly with downstream packages that generate multipart requests for cloud-storage uploads or API SDK flows?

## Related Pages

- [[npm/axios]]
- [[npm/node-fetch]]
- [[npm/undici]]
- [[npm/multer]]
- [[npm/index]]

---
*Last updated: 2026-04-18 | Sources: 8 (OSV.dev package query for npm/form-data, OSV vulnerability record for GHSA-fjxv-7rqg-78g4, GitHub Advisory Database entry for the same GHSA ID, public CVE / NVD record, upstream GitHub security advisory, upstream fix commit, upstream `v4.0.4` release notes, npm registry metadata, npm downloads API)*