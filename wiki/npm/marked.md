# marked (npm)

**Registry:** npm
**Weekly Downloads:** ~37,986,032 (last week, fetched 2026-04-17)
**Repository:** https://github.com/markedjs/marked
**Security Contact:** project committers and npm owners via upstream `SECURITY.md`
**Disclosure Policy:** https://github.com/markedjs/marked/blob/master/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-17 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream `SECURITY.md`, upstream README / release notes, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for `marked` covering its published XSS / content-injection lineage, repeated ReDoS history, and upstream sanitization boundary guidance. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2014-3743 / GHSA-9cw2-jqp5-7x39 | Moderate | Multiple content-injection / XSS issues remained reachable even with `sanitize: true`, including JavaScript URL handling. | 0.3.1 | https://osv.dev/vulnerability/GHSA-9cw2-jqp5-7x39 |
| CVE-2015-1370 / GHSA-cfjh-p3g4-3q2f | Moderate | VBScript content injection on older releases despite `sanitize: true`. | 0.3.3 | https://osv.dev/vulnerability/GHSA-cfjh-p3g4-3q2f |
| CVE-2015-8854 / GHSA-hjcp-j389-59ff | Moderate | ReDoS in the `em` inline rule on older releases. | 0.3.4 | https://osv.dev/vulnerability/GHSA-hjcp-j389-59ff |
| CVE-2016-10531 / GHSA-vfvf-mqq8-rwqc | Moderate | Sanitization bypass using HTML entities in link components when `sanitize: true` was enabled. | 0.3.6 | https://osv.dev/vulnerability/GHSA-vfvf-mqq8-rwqc |
| CVE-2017-1000427 / GHSA-7px7-7xjx-hxm8 | Moderate | XSS from unsafe `data:` URI handling on older releases. | 0.3.7 | https://osv.dev/vulnerability/GHSA-7px7-7xjx-hxm8 |
| CVE-2017-16114 / GHSA-x5pg-88wf-qq4p | Moderate | ReDoS via catastrophic backtracking in older parsing regexes. | 0.3.9 | https://osv.dev/vulnerability/GHSA-x5pg-88wf-qq4p |
| CVE-2018-25110 / GHSA-p9wx-2529-fp83 | Moderate | ReDoS in HTML-tag and markdown-link parsing before 0.3.17. | 0.3.17 | https://osv.dev/vulnerability/GHSA-p9wx-2529-fp83 |
| GHSA-xf5p-87ch-gxw2 | Moderate | ReDoS due to email addresses being evaluated in quadratic time. | 0.6.2 | https://osv.dev/vulnerability/GHSA-xf5p-87ch-gxw2 |
| GHSA-ch52-vgq2-943f | Moderate | ReDoS in malformed links with backticks. | 0.7.0 | https://osv.dev/vulnerability/GHSA-ch52-vgq2-943f |
| CVE-2021-21306 / GHSA-4r62-v4vq-hr96 | High | ReDoS in older 1.x releases. | 2.0.0 | https://osv.dev/vulnerability/GHSA-4r62-v4vq-hr96 |
| CVE-2022-21680 / GHSA-rrrm-qjm4-v8hf | High | Inefficient regular-expression complexity in `block.def` could cause denial of service. | 4.0.10 | https://osv.dev/vulnerability/GHSA-rrrm-qjm4-v8hf |
| CVE-2022-21681 / GHSA-5v2h-r2cx-5xgj | High | Inefficient regular-expression complexity in `inline.reflinkSearch` could cause denial of service. | 4.0.10 | https://osv.dev/vulnerability/GHSA-5v2h-r2cx-5xgj |

## Security Posture Notes

- Public advisory history for `marked` is dominated by **two recurring themes**: early output/content-injection problems around built-in sanitization behavior, and a long sequence of **regex-complexity / ReDoS** bugs in markdown parsing.
- The older 0.3.x line is especially noisy: public records show repeated fixes from `0.3.1` through `0.3.17`, which makes any long-pinned pre-1.x dependency particularly risky.
- Upstream's README now states plainly that **Marked does not sanitize output HTML** and recommends downstream sanitizers such as DOMPurify. That warning matters because several older advisories explicitly involved users relying on `sanitize: true` for safety.
- Public release notes for `0.7.0` show a meaningful security boundary change: the release both fixed another ReDoS issue and **deprecated the `sanitize` / `sanitizer` options**, reinforcing that output sanitization is a consumer responsibility rather than a parser guarantee.
- Later release notes for `4.0.10` explicitly call out a security fix for ReDoS vulnerabilities, and current OSV package data in this pass did not surface newer published advisories beyond that point.
- Upstream `SECURITY.md` provides a private disclosure path and states that maintainers aim for an initial assessment within 48 hours and a fix within two weeks when a report is validated, which is a healthy disclosure signal for a library with this much downstream exposure.
- Operationally, `marked` should be treated as **unsafe to expose directly to untrusted markdown without separate HTML sanitization and input-size controls**. Even when current releases close known published advisories, markdown parsing remains a historically regex-sensitive surface.

## Dependencies of Note

- Often embedded directly into content-management systems, docs tooling, comment/render pipelines, and static-site workflows rather than hidden only as a transitive dependency.
- Risk increases when applications render attacker-controlled markdown straight to browsers without a dedicated HTML sanitizer, or when they allow unusually large / adversarial markdown inputs without resource limits.

## Open Questions

- Have later 5.x+ release lines undergone a public regex-complexity review beyond the fixes documented in `4.0.10`?
- Which popular documentation or CMS stacks still pin old pre-`4.0.10` versions of `marked`?
- Are there public maintainer notes explaining whether any legacy consumers still rely on deprecated `sanitize` / `sanitizer` behavior despite upstream guidance to sanitize output separately?

## Related Pages

- [[npm/handlebars]]
- [[npm/ejs]]
- [[npm/mathjs]]
- [[npm/index]]

---
*Last updated: 2026-04-17 | Sources: 8 (OSV.dev, GitHub Advisory Database, public CVE records, upstream `SECURITY.md`, upstream README, upstream GitHub release notes, npm registry metadata, npm downloads API)*
