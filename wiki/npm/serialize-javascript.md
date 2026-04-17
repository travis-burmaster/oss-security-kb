# serialize-javascript (npm)

**Registry:** npm
**Weekly Downloads:** ~48,790,379 (last week, fetched 2026-04-17)
**Repository:** https://github.com/yahoo/serialize-javascript
**Security Contact:** GitHub Security Advisory
**Disclosure Policy:** https://github.com/yahoo/serialize-javascript/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-17 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / upstream GitHub security advisories, public CVE records, upstream release notes / README, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page covering the package's published XSS, code-injection / RCE, and CPU-exhaustion history. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-16769 / GHSA-h9rv-jmmf-4pgx | Moderate | Serialized regular expressions were not sanitized correctly, enabling browser-side XSS when the generated string was embedded into executable script contexts. The public advisory explicitly says this issue does **not** affect pure Node.js usage. | 2.1.1 | https://osv.dev/vulnerability/GHSA-h9rv-jmmf-4pgx |
| CVE-2020-7660 / GHSA-hxcc-f52p-wc94 | High | Insecure placeholder replacement let attacker-controlled regexp and string values break serialization boundaries and inject code when the output was later evaluated or embedded in a script tag. | 3.1.0 | https://osv.dev/vulnerability/GHSA-hxcc-f52p-wc94 |
| CVE-2024-11831 / GHSA-76p7-773f-r4q5 | Moderate | XSS in newer lines tied to incorrect handling of serialized URL string contents; upstream `v6.0.2` release notes explicitly call out the XSS-prevention fix. | 6.0.2 | https://osv.dev/vulnerability/GHSA-76p7-773f-r4q5 |
| GHSA-5c6j-r48x-rmvq | High | Public GitHub advisory says the package remained vulnerable after the `CVE-2020-7660` fix because `RegExp.flags` and `Date.prototype.toISOString()` could still inject code into serialized output. | 7.0.3 | https://osv.dev/vulnerability/GHSA-5c6j-r48x-rmvq |
| CVE-2026-34043 / GHSA-qj8w-gfj5-8c6v | Moderate | Crafted array-like objects could trigger CPU-exhaustion denial of service during serialization; upstream `v7.0.5` release notes tie the fix directly to the advisory. | 7.0.5 | https://osv.dev/vulnerability/GHSA-qj8w-gfj5-8c6v |

## Security Posture Notes

- `serialize-javascript` is a **small but high-consequence boundary package** because it turns live JavaScript values into strings that many applications later embed into HTML, SSR bootstrap data, or other executable contexts.
- The public advisory history is concentrated around one recurring theme: **unsafe serialization of non-plain data types** such as regexps, dates, URLs, and array-like objects, especially when attacker-controlled input reaches `serialize()` and the output is later executed or interpreted as code.
- The 2019 and 2024 XSS advisories are best read as **browser / script-embedding issues**, not generic Node-only memory-corruption style bugs. Public records for `CVE-2019-16769` explicitly say the original regex XSS issue does not affect pure Node.js usage.
- The 2020 and 2026 code-injection advisories show a more serious pattern: if an application serializes attacker-controlled objects and later feeds the result into `eval`, `new Function`, or inline `<script>` hydration paths, serialization bugs can become **code execution** rather than mere output corruption.
- The newer `GHSA-5c6j-r48x-rmvq` matters because public advisory text explicitly frames it as an **incomplete fix** for `CVE-2020-7660`, which means older remediation assumptions around the placeholder / escaping logic were too optimistic.
- The 2026 `CVE-2026-34043` DoS issue broadens the risk surface beyond injection: public evidence now shows malformed array-like object handling can also create availability problems, not just script-safety bugs.
- Current public evidence from this pass points to **`7.0.5+` as the first release line covering the full currently reviewed published advisory set**.

## Dependencies of Note

- Often used in SSR and frontend-build pipelines that serialize server-side state into browser-consumable bootstrap payloads.
- Shows up in tooling and framework ecosystems where the serialized output may later be embedded into HTML or otherwise treated as executable JavaScript.
- Risk is highest when applications pass **attacker-controlled objects** into `serialize()` instead of limiting usage to trusted server-generated data.

## Open Questions

- Which high-download downstream frameworks or SSR helpers still pin vulnerable pre-`7.0.5` ranges transitively?
- Are there strong public maintainer writeups explaining safe usage patterns for `serialize-javascript` in modern SSR pipelines beyond the advisory / release-note trail?
- Should future KB work add a cross-link page for “HTML / hydration serialization boundaries” covering packages like `serialize-javascript`, template engines, and framework bootstrap helpers together?

## Related Pages

- [[npm/handlebars]]
- [[npm/js-yaml]]
- [[npm/mathjs]]
- [[npm/index]]

---
*Last updated: 2026-04-17 | Sources: 7 (OSV.dev, GitHub Advisory Database / upstream GitHub security advisories, public CVE records, upstream GitHub releases, upstream README, npm registry metadata, npm downloads API)*
