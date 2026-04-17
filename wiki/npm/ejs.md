# ejs (npm)

**Registry:** npm
**Weekly Downloads:** ~29,669,718 (last week, fetched 2026-04-17)
**Repository:** https://github.com/mde/ejs
**Security Contact:** maintainer email via upstream `SECURITY.md`
**Disclosure Policy:** https://github.com/mde/ejs/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-17 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream `SECURITY.md`, upstream issue / commit history, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for `ejs` covering its published XSS, DoS, SSTI / RCE, and prototype-pollution-adjacent history. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2017-1000188 / GHSA-hwcf-pp87-7x6p | High | Cross-site scripting in `ejs.renderFile()` on older 2.x releases. | 2.5.5 | https://osv.dev/vulnerability/GHSA-hwcf-pp87-7x6p |
| CVE-2017-1000189 / GHSA-6x77-rpqf-j6mw | High | Denial of service due to weak input validation in `ejs.renderFile()` on older 2.x releases. | 2.5.5 | https://osv.dev/vulnerability/GHSA-6x77-rpqf-j6mw |
| CVE-2017-1000228 / GHSA-3w5v-p54c-f74x | High | Remote code execution due to weak input validation in older `renderFile()` handling. | 2.5.5 | https://osv.dev/vulnerability/GHSA-3w5v-p54c-f74x |
| CVE-2022-29078 / GHSA-phwq-j96m-2c2q | Critical | Server-side template injection / code execution via `settings[view options][outputFunctionName]` reaching internal option handling. | 3.1.7 | https://osv.dev/vulnerability/GHSA-phwq-j96m-2c2q |
| CVE-2024-33883 / GHSA-ghr5-ch3p-vcr6 | Moderate | Lacked certain prototype-pollution protections before 3.1.10, enabling pollution-assisted escalation paths in applications that also expose a prototype-pollution primitive. | 3.1.10 | https://osv.dev/vulnerability/GHSA-ghr5-ch3p-vcr6 |

## Security Posture Notes

- Public advisory history for `ejs` clusters around a **small number of recurring high-risk surfaces**: `renderFile()` input handling on older releases, internal option plumbing, and prototype-chain / object-property lookups that can become dangerous when applications mix template rendering with unsafe object merging.
- The 2017 records are notable because **three distinct published advisories** (XSS, DoS, and RCE) all converge on the same older release line and were remediated in `2.5.5`, which makes that release a clear historical security watershed for pre-3.x users.
- Public OSV and GHSA data show a second major watershed at `3.1.7`, where `CVE-2022-29078` documents server-side template injection through an internal option boundary rather than general template misuse.
- The public maintainer trail is also worth preserving: commit `49264e0` (“Blacklist a few other unsafe opts from passing in data obj”) and the later public issue `#730` both point to sustained hardening work around **unsafe option flow and prototype-pollution-adjacent gadget paths**, not just one isolated bug.
- Upstream `SECURITY.md` provides a private reporting path, which is a positive disclosure signal, but this review pass also found a **public policy-version mismatch**: the security policy currently says `4.x.x` is the supported version while npm metadata reports `5.0.2` as the latest release. That may be documentation lag rather than a product issue, but it is still useful context for reporters and maintainers.
- Operationally, `ejs` should be treated as a **high-consequence library when fed user-controlled templates, template options, or application objects**. Upstream's own security policy explicitly says giving end users unfettered access to `render()` is inherently insecure, so consumers should not confuse the package's safe default expectations with a sandbox guarantee.
- Current public evidence from this pass points to `3.1.10+` as the minimum release line that covers the known published advisory set reviewed here.

## Dependencies of Note

- Often used directly as an application templating engine rather than buried as a hidden transitive dependency.
- Risk increases when applications pass user-controlled data structures into rendering helpers, merge request objects into template locals / options, or rely on EJS execution as though it were a sandbox.

## Open Questions

- Does upstream intend `SECURITY.md`'s supported-version table to include the current 5.x line, or is the `4.x.x` entry simply stale documentation?
- Does public issue `mde/ejs#730` map fully onto `CVE-2024-33883`, or does it describe a broader prototype-pollution-to-RCE gadget family that deserves separate normalization in future KB passes?
- Are there public maintainer notes or release artifacts that explain how the `3.1.7` and `3.1.10` hardening changes were carried forward into 5.x?
- Which popular Express or view-engine starter stacks still pin vulnerable pre-`3.1.10` versions of `ejs`?

## Related Pages

- [[npm/express]]
- [[npm/handlebars]]
- [[npm/mathjs]]
- [[npm/index]]

---
*Last updated: 2026-04-17 | Sources: 7 (OSV.dev, GitHub Advisory Database, public CVE records, upstream `SECURITY.md`, upstream issue / commit history, npm registry metadata, npm downloads API)*
