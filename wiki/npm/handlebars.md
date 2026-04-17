# handlebars (npm)

**Registry:** npm
**Weekly Downloads:** ~35,940,075 (last week, fetched 2026-04-16)
**Repository:** https://github.com/handlebars-lang/handlebars.js
**Security Contact:** GitHub Security Advisory
**Disclosure Policy:** https://github.com/handlebars-lang/handlebars.js/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-16 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / upstream GitHub security advisories, public CVE aliases, upstream release notes, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for Handlebars' published vulnerability history, including the large 2026 `v4.7.9` fix cluster. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2015-8861 / GHSA-9prh-257w-9277 | moderate | Historical XSS issue in older Handlebars releases; OSV tracks the public advisory lineage as fixed in the `4.0.0` line. | 4.0.0 | https://osv.dev/vulnerability/GHSA-9prh-257w-9277 |
| GHSA-q42p-pg8m-cqh6 | high | Prototype-pollution bug with multiple fix trains across older major/minor lines. | 3.0.7 / 4.0.14 / 4.1.2 | https://osv.dev/vulnerability/GHSA-q42p-pg8m-cqh6 |
| GHSA-2cf5-4w76-r9qv / GHSA-q2c6-c6pm-g3gh | critical | Arbitrary-code-execution advisory lineage in older compiler/runtime behavior; OSV shows fixes first landing in `3.0.8`, `4.5.2`, and then `4.5.3` depending on the tracked advisory record. | 3.0.8 / 4.5.2 / 4.5.3 | https://osv.dev/vulnerability/GHSA-2cf5-4w76-r9qv |
| CVE-2019-19919 / GHSA-w457-6q6x-cgp9 and GHSA-g9r4-xpmj-mj65 | critical | Follow-on prototype-pollution hardening issues in the 3.x and 4.x lines; OSV records fixes in `4.3.0` and `4.5.3`, with `3.0.8` covering the older branch. | 3.0.8 / 4.3.0 / 4.5.3 | https://osv.dev/vulnerability/GHSA-w457-6q6x-cgp9 |
| CVE-2019-20922 / GHSA-62gr-4qp9-h98f | moderate | Regular-expression denial of service in 4.x releases. | 4.4.5 | https://osv.dev/vulnerability/GHSA-62gr-4qp9-h98f |
| CVE-2021-23369 / GHSA-f2jv-r9rf-7988 | critical | Remote code execution when compiling attacker-controlled templates / AST-like input; upstream `v4.7.7` release notes call out stricter prototype-property access checks in this security-fix window. | 4.7.7 | https://osv.dev/vulnerability/GHSA-f2jv-r9rf-7988 |
| CVE-2021-23383 / GHSA-765h-qjxv-5f44 | high | Prototype-pollution / prototype-property access issue in older lines, remediated in `4.7.7`. | 4.7.7 | https://osv.dev/vulnerability/GHSA-765h-qjxv-5f44 |
| GHSA-2qvq-rjwj-gvw9 / GHSA-2w6w-674q-4c4q / GHSA-3mfm-83xf-c92r / GHSA-442j-39wm-28r2 / GHSA-7rx3-28cr-v5wh / GHSA-9cx6-37pm-9jff / GHSA-xhpv-hc6g-r9c6 / GHSA-xjpj-3mr7-gcpf | multiple | Coordinated `v4.7.9` security cluster covering prototype-pollution-to-XSS via partial resolution, several AST type-confusion / JavaScript-injection paths, property-access / blocklist bypasses, CLI precompiler injection, and malformed-decorator compilation DoS. The upstream `v4.7.9` release explicitly lists all eight advisories under one security-fix commit. | 4.7.9 | https://github.com/handlebars-lang/handlebars.js/releases/tag/v4.7.9 |

## Security Posture Notes

- Handlebars has a **long, security-relevant history** across XSS, prototype pollution, arbitrary code execution / JavaScript injection, and parser / compiler denial-of-service classes. This is not a one-off advisory package.
- The package's 2026 `v4.7.9` release matters because it fixed **eight published advisories at once**, suggesting a concentrated hardening pass over compiler, runtime, partial resolution, and access-control boundaries rather than one isolated bug.
- Public release notes show several earlier security inflection points as well: `v4.3.0` tightened constructor / `lookup` behavior to prevent RCE, `v4.4.5` addressed the published ReDoS issue, `v4.5.3` continued the 2019 hardening sequence, and `v4.7.7` tightened prototype-property access checks.
- Upstream `SECURITY.md` currently recommends staying on the latest versions and marks `< 4.7` unsupported. That aligns with the advisory record: older lines accumulated repeated fix trains and are poor long-term risk bets.
- Real-world exploitability is highly context-dependent. Many Handlebars findings require one of these conditions: attacker-controlled template compilation, attacker-controlled AST input, unsafe use of dynamic partials or precompiler options, or a separate prototype-pollution primitive elsewhere in the app stack.
- Operationally, the safest posture is to treat Handlebars as a package that should be **kept current and isolated from untrusted template / AST inputs**, not as a passive formatting helper.

## Dependencies of Note

- Often embedded in SSR / template-rendering stacks rather than used as a leaf utility
- Downstream exposure increases when applications compile untrusted templates at runtime
- Prototype-pollution issues elsewhere in the dependency graph can become more dangerous when Handlebars partial or property-resolution paths are reachable

## Open Questions

- Are there good public maintainer writeups or issue threads that explain the exploit preconditions for each `v4.7.9` advisory more cleanly than the advisory texts alone?
- Should this page eventually split the `v4.7.9` cluster into a more detailed appendix if more public exploit / fix analysis appears?
- Which high-usage downstream packages still pin vulnerable pre-`4.7.9` Handlebars ranges transitively?

## Related Pages

- [[npm/qs]]
- [[npm/minimist]]
- [[npm/lodash]]
- [[npm/index]]

---
*Last updated: 2026-04-16 | Sources: 8 (OSV.dev, GitHub Advisory Database / upstream GitHub security advisories, public CVE aliases, upstream release notes, upstream SECURITY.md, GitHub release metadata, npm registry metadata, npm downloads API)*
