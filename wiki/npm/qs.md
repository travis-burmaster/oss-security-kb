# qs (npm)

**Registry:** npm
**Weekly Downloads:** ~143,160,104 (as of 2026-04-12)
**Repository:** https://github.com/ljharb/qs
**Security Contact:** none listed
**Disclosure Policy:** no dedicated security policy found in this pass; repository advisories are published through GitHub Security Advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-13 | OpenClaw recurring review | package advisory history | manual | 6 publicly disclosed package vulnerabilities curated from OSV, GitHub Advisory Database records, CVE aliases, upstream changelog entries, and npm registry metadata | https://osv.dev/list?ecosystem=npm&q=qs |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2014-7191 / GHSA-jjv7-qpx3-h62q | High | Crafted sparse-array input could trigger memory exhaustion and crash the process during parsing. | 1.0.0 | https://osv.dev/vulnerability/GHSA-jjv7-qpx3-h62q |
| CVE-2014-10064 / GHSA-f9cm-p3w6-xvr3 | High | Excessively deep nesting could trigger excessive recursion and event-loop blocking during parsing. | 1.0.0 | https://osv.dev/vulnerability/GHSA-f9cm-p3w6-xvr3 |
| CVE-2017-1000048 / GHSA-gqgv-6jq5-jjj9 | High | Prototype-pollution protection bypass via crafted input containing bracket characters; public fixes landed across several maintained lines. | 6.0.4 / 6.1.2 / 6.2.3 / 6.3.2 | https://osv.dev/vulnerability/GHSA-gqgv-6jq5-jjj9 |
| CVE-2022-24999 / GHSA-hrpp-h998-j3pp | High | `__proto__` payloads could cause process hangs and prototype-pollution side effects; fix was backported broadly across older release lines. | 6.10.3 / 6.9.7 / 6.8.3 / 6.7.3 / 6.6.1 / 6.5.3 / 6.4.1 / 6.3.3 / 6.2.4 | https://osv.dev/vulnerability/GHSA-hrpp-h998-j3pp |
| CVE-2025-15284 / GHSA-6rw7-vpxm-498p | Moderate | `arrayLimit` enforcement could be bypassed with bracket notation (`a[]=...`), enabling memory-growth / DoS scenarios when applications relied on that limit. | 6.14.1 | https://osv.dev/vulnerability/GHSA-6rw7-vpxm-498p |
| CVE-2026-2391 / GHSA-w7fw-mjwx-w883 | Moderate | With `comma: true`, comma-separated input could bypass `arrayLimit` checks and create unexpectedly large arrays from a single parameter. | 6.14.2 | https://osv.dev/vulnerability/GHSA-w7fw-mjwx-w883 |

*Full advisory history: https://osv.dev/list?ecosystem=npm&q=qs*

## Security Posture Notes

- `qs` is a high-leverage parser because it sits directly on user-controlled query-string input and is embedded transitively in major Node.js web stacks.
- The public advisory record clusters around two recurring bug classes: **resource-exhaustion / parser-complexity bugs** (2014, 2025, 2026) and **prototype-pollution / object-shape manipulation bugs** (2017, 2022).
- Upstream changelog history shows both direct security fixes and follow-on hardening: 6.10.3 and 6.9.7 explicitly note `parse: ignore __proto__ keys`, while 6.0.4 / 6.1.2 / 6.2.3 / 6.3.2 note `follow allowPrototypes option during merge`.
- More recent changelog entries also show defense-in-depth work around parser limits: 6.13.0 added `strictDepth`, and 6.14.0 added `throwOnParameterLimitExceeded`, which is useful context for operators who rely on parser-boundary controls.
- The 2025 GHSA explicitly notes that the default `parameterLimit` of 1000 reduces worst-case impact for one of the `arrayLimit` bypass scenarios, so exposure depends in part on application configuration and whether defaults were changed.

## Dependencies of Note

- Frequently appears beneath Express and other Node.js request-parsing stacks, which gives even old parser bugs a large transitive blast radius.
- Query-parser options such as `allowPrototypes`, `arrayLimit`, `parameterLimit`, `strictDepth`, and `comma` materially affect exposure and are worth checking in downstream frameworks.

## Open Questions

- Which popular frameworks or middleware still expose risky `qs` options or pin older vulnerable release lines transitively?
- Has anyone published a modern dedicated audit of `qs` after the 2025-2026 limit-bypass fixes?
- Should the KB eventually track downstream framework defaults separately from package-level vulnerabilities so parser-risk exposure is easier to assess?

## Related Pages

- [[npm/index]]
- [[npm/express]]
- [[npm/minimist]]

---
*Last updated: 2026-04-13 | Sources: 10 (OSV package query, 6 OSV / GHSA advisory records, upstream `qs` changelog, npm registry metadata, npm downloads API)*
