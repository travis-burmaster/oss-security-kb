# pug (npm)

**Registry:** npm
**Weekly Downloads:** ~3,173,825 (last week, fetched 2026-04-23)
**Repository:** https://github.com/pugjs/pug
**Security Contact:** Tidelift security contact
**Disclosure Policy:** https://github.com/pugjs/pug/blob/master/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-23 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream `SECURITY.md`, upstream release notes, npm registry metadata, npm downloads API, public fix PR / commit references) | Added a new advisory-mapped page for `pug` after confirming two published code-execution issues in compiler-option handling, fixed in `3.0.1` and `3.0.3`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-21353 / GHSA-p493-635q-r6gr | Moderate | Remote code execution was possible if an attacker could control the `pretty` compiler option, such as by spreading untrusted request data into Pug compile options. | 3.0.1 | https://github.com/advisories/GHSA-p493-635q-r6gr |
| CVE-2024-36361 / GHSA-3965-hpx2-q597 | Moderate | `compileClient`-style APIs allowed JavaScript code execution when applications accepted untrusted values for `name`, `templateName`, or `globals`-style compilation options. | 3.0.3 | https://github.com/advisories/GHSA-3965-hpx2-q597 |

*Full CVE history: https://osv.dev/list?ecosystem=npm&q=pug*

## Security Posture Notes

- Public advisory history for `pug` is currently small but high-consequence: both published package records are **code-execution bugs in compile-option handling**, not generic template-rendering flaws.
- Scope matters. The 2021 and 2024 issues require an application to pass **attacker-controlled values into compiler options**, not merely to render attacker-controlled template variables. That narrower trigger should not be flattened into “all Pug use is RCE,” but it still matters because several common server patterns spread request objects or config fragments into template calls.
- Upstream disclosure posture is reasonably clear. Public `SECURITY.md` states that versions `<3.0.1` are unsupported, marks `^3.0.1` as the supported line, and routes reporters to the Tidelift security contact.
- Public release notes provide clean maintainer confirmation for both fixes: `pug@3.0.1` says the `pretty` option was sanitized to prevent server-side code execution, and `pug@3.0.3` says `templateName` and `globals` validation was tightened to prevent code execution when untrusted input reaches compilation options.
- Current npm metadata in this pass shows `3.0.4` as latest, so the present maintained line is beyond the known public fix points. The bigger operational risk is **old pinned 2.x / early 3.x deployments** or transitive use of compile-client helpers in custom build systems.

## Dependencies of Note

- `pug` wraps lower-level compiler packages such as `pug-code-gen`, and both published advisories also mention that lower-level package in the affected/fixed evidence.
- Risk is highest in applications that compile templates dynamically, expose compile helpers in custom tooling, or merge request-derived objects into template-engine options.
- Precompiled-template workflows and applications that keep compile options static reduce the practical attack surface, but they still benefit from moving to fixed versions because the published fixes are small and well-defined.

## Open Questions

- Which popular Express / SSR starter stacks or generators still pin `pug` below `3.0.3`?
- Are there public maintainer notes beyond the release text that explain safe patterns for `compileClient` use with externally supplied metadata?
- Do downstream build or CMS plugins expose `pug-code-gen` functionality directly in ways that deserve their own KB cross-references?

## Related Pages

- [[npm/ejs]]
- [[npm/handlebars]]
- [[npm/marked]]
- [[npm/index]]

---
*Last updated: 2026-04-23 | Sources: 8 (OSV.dev, GitHub Advisory Database, public CVE records, upstream `SECURITY.md`, upstream release notes, npm registry metadata, npm downloads API, public fix PR / commit references)*
