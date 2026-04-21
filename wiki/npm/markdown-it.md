# markdown-it (npm)

**Registry:** npm
**Weekly Downloads:** ~22,156,478 (2026-04-14 to 2026-04-20)
**Repository:** https://github.com/markdown-it/markdown-it
**Security Contact:** none listed
**Disclosure Policy:** public GitHub security advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-21 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / GitHub security advisories, public CVE records, upstream CHANGELOG / release references, npm registry metadata, npm downloads API, local Claude-compatible proxy used only as a drafting aid) | Added a new advisory-mapped baseline page for `markdown-it`'s published package security history, covering three public resource-exhaustion / ReDoS records across the pre-3.0.0 line, the `12.3.2` newline-rule fix, and the `13.0.0`-through-`14.1.0` linkify regression fixed in `14.1.1`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2015-10005 / GHSA-j5p7-jf4q-742q | High | Public advisory records describe inefficient regular-expression complexity in older `markdown-it` releases. OSV maps the affected range to versions before `3.0.0`, and the reference set includes the upstream fix commit plus the `3.0.0` release tag. | 3.0.0 | https://github.com/advisories/GHSA-j5p7-jf4q-742q |
| CVE-2022-21670 / GHSA-6vfc-qv3f-vr6c | Moderate | Public advisory records describe uncontrolled resource consumption / ReDoS in the newline rule affecting versions before `12.3.2`. The upstream changelog for `12.3.2` explicitly says: `Security - Fix possible ReDOS in newline rule.` | 12.3.2 | https://github.com/advisories/GHSA-6vfc-qv3f-vr6c |
| CVE-2026-2327 / GHSA-38c4-r59v-3vqw | Moderate | Public advisory records describe a ReDoS regression in the linkify inline rule. OSV maps the affected range to `>= 13.0.0, < 14.1.1`, and the upstream `14.1.1` changelog notes that specific patterns could cause high CPU use after the v13 regression. | 14.1.1 | https://github.com/advisories/GHSA-38c4-r59v-3vqw |

## Security Posture Notes

- `markdown-it` now has a **clear three-record public advisory history** in the gathered evidence, all tied to denial-of-service / resource-exhaustion behavior rather than code-execution claims.
- The public record spans a long period: one older pre-`3.0.0` regex-complexity issue, a 2022 newline-rule ReDoS fix in `12.3.2`, and a newer 2026 linkify-rule regression affecting `13.x` through `14.0.x`.
- The evidence for the newest issue is unusually clean: OSV gives a precise affected range of `>= 13.0.0, < 14.1.1`, the GitHub advisory links the upstream fix commit, and the `14.1.1` changelog explicitly frames it as a security fix for high CPU use.
- All three published records in this pass are **availability-oriented parser issues**. The practical risk is crafted Markdown input driving high CPU or other resource consumption, not direct remote code execution.
- The package remains broadly relevant because it still saw **~22.2M weekly downloads** in this review window and is frequently inherited transitively in documentation tooling, static-site generators, note-taking apps, and Markdown-processing services.
- Current npm metadata in this pass showed **`latest=14.1.1`**, which clears all three public advisories gathered here.
- Consumers pinned to `13.x` or `14.0.x` deserve special attention because they miss only the newest published fix and may otherwise appear "recent enough" at a glance.
- No unpatched or disputed package-level OSV records were surfaced for `markdown-it` in this review pass.

## Recommendations for Developers

1. **Upgrade to `14.1.1` or newer**; current npm metadata in this pass showed `14.1.1` as the latest release.
2. **If you remain on an older maintained branch, verify which advisory floor applies**: at minimum `3.0.0`, then `12.3.2`, and for current major lines `14.1.1`.
3. **Treat Markdown parsing as an attacker-influenced parser surface** when processing untrusted content in web apps, SaaS editors, bots, or server-side rendering pipelines.
4. **Audit transitive copies in docs and content stacks** because `markdown-it` is often inherited indirectly rather than pinned deliberately.

## Dependencies of Note

- Frequently embedded in Markdown renderers, documentation generators, static-site pipelines, editors, and content-management features.
- Security relevance is highest where untrusted Markdown can be submitted repeatedly or at scale, turning parser inefficiency into an availability problem.

## Open Questions

- Which still-popular static-site or note-taking stacks pin `markdown-it` below `14.1.1`?
- Are there strong public maintainer or downstream writeups that better quantify exploitability differences between synchronous server-side parsing and client-side-only rendering?
- Should a future KB pass cluster `markdown-it` with other Markdown/rendering packages that show repeated parser-complexity or sanitization-boundary issues?

## Related Pages

- [[npm/marked]]
- [[npm/handlebars]]
- [[npm/js-yaml]]
- [[npm/index]]

---
*Last updated: 2026-04-21 | Sources: 11 (OSV.dev package query for npm/markdown-it, OSV vulnerability records for GHSA-j5p7-jf4q-742q / GHSA-6vfc-qv3f-vr6c / GHSA-38c4-r59v-3vqw, GitHub Advisory Database / public GitHub security advisories for the same records, public CVE records for CVE-2015-10005 / CVE-2022-21670 / CVE-2026-2327, upstream CHANGELOG entries for 12.3.2 and 14.1.1, upstream release / commit references linked from OSV and GHSA, npm registry metadata, npm downloads API)*
