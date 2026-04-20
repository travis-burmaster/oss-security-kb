# xml2js (npm)

**Registry:** npm
**Weekly Downloads:** ~35,112,312 (2026-04-13 to 2026-04-19)
**Repository:** https://github.com/Leonidas-from-XIV/node-xml2js
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** https://github.com/Leonidas-from-XIV/node-xml2js/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-20 | OpenClaw recurring review | package advisory normalization | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream issue / PR / fix references, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for xml2js's currently published package vulnerability history. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-0842 / GHSA-776f-qx25-q3cc | Moderate | Prototype pollution before `0.5.0`; public advisory records say attacker-controlled keys such as `__proto__` could modify object properties when unsafe input reached the parser's object-building path. | 0.5.0 | https://github.com/advisories/GHSA-776f-qx25-q3cc |

## Security Posture Notes

- `xml2js` has a **compact but real public package advisory history** in the evidence gathered here: one moderate-severity prototype-pollution record fixed in `0.5.0`.
- The published bug class is familiar for JavaScript parser / object-construction libraries: attacker-controlled structured input eventually reaches object property assignment, and reserved keys such as `__proto__` are not blocked strongly enough.
- Although the current public package record set is small, `xml2js` still matters because it sits directly on **untrusted document parsing boundaries** in many integration, import, and API-adapter workflows.
- Current npm metadata shows meaningful ongoing usage (~35.1M downloads in the review week), so older `0.4.x` deployments remain worth flagging even though the fix is not new.
- This page intentionally stays conservative: the review window gathered one clear package-level advisory, and it does not over-claim broader XML-parser bug classes without package-scoped public records.

## Recommendations for Developers

1. **Upgrade to `0.5.0` or newer** to cover the currently published package advisory set reviewed in this pass.
2. Treat parsed XML-to-object conversion as a **deserialization-style trust boundary**, especially when the resulting JavaScript objects are merged, serialized again, or passed into authorization / templating / configuration logic.
3. Add regression tests for reserved property names like `__proto__`, `constructor`, and `prototype` if your application accepts attacker-controlled XML and then transforms it into plain JavaScript objects.
4. If you cannot upgrade quickly, review downstream code for any assumptions that parsed object keys are benign.

## Dependencies of Note

- `xml2js` is commonly used in integration middleware, SOAP / XML adapters, feed importers, and legacy interoperability layers where untrusted XML is transformed into plain JavaScript objects.
- Object-construction logic, not just raw XML tokenization, is the main security-relevant surface in the currently published advisory trail.

## Open Questions

- Are there maintainer-authored release notes for `0.5.0` that would make the prototype-pollution fix boundary easier to document beyond the advisory-linked issue / commit trail?
- Which high-download transitive dependents still pin `xml2js` below `0.5.0`?
- Should a future KB pass compare `xml2js` with other parser-to-object libraries where prototype-pollution risks recur at the data-structure layer rather than the syntax layer?

## Related Pages

- [[npm/js-yaml]]
- [[npm/jsonwebtoken]]
- [[npm/index]]

---
*Last updated: 2026-04-20 | Sources: 6 (OSV.dev package query for npm/xml2js, OSV vulnerability record for GHSA-776f-qx25-q3cc, GitHub Advisory Database entry for the same GHSA ID, public CVE record via advisory alias, upstream issue / PR / fix references linked from the advisory record, npm registry metadata, npm downloads API)*
