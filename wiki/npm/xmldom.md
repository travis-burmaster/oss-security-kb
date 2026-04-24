# xmldom (npm)

**Registry:** npm
**Weekly Downloads:** ~1,547,951 (`xmldom`, 2026-04-17 to 2026-04-23)
**Repository:** https://github.com/xmldom/xmldom
**Security Contact:** security@xmldom.org
**Disclosure Policy:** https://github.com/xmldom/xmldom/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-24 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / public GitHub security advisories, public CVE records, maintainer fix commits and release tags, npm registry metadata, npm downloads API) | Added a new advisory-mapped page for the `xmldom` package family, separating the legacy unscoped `xmldom` package from the maintained `@xmldom/xmldom` fork and normalizing the published XML-parsing, serialization-injection, and deep-recursion DoS history across both names. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-21366 / GHSA-h6q6-9hqw-rwfv | Moderate | Public advisory records describe malformed XML handling that can cause downstream misinterpretation of malicious input in legacy `xmldom` releases before `0.5.0`. | 0.5.0 (`xmldom`) | https://github.com/advisories/GHSA-h6q6-9hqw-rwfv |
| CVE-2021-32796 / GHSA-5fg8-2547-mr8q | Moderate | Removed elements could be serialized without correct escaping, creating XML syntax changes and downstream misinterpretation risks. | 0.7.0 (`@xmldom/xmldom`); legacy `xmldom` remains affected through `0.6.0` | https://github.com/advisories/GHSA-5fg8-2547-mr8q |
| CVE-2022-39353 / GHSA-crh6-fp67-6883 | Critical | The parser could accept XML with multiple top-level elements and build a DOM with multiple root nodes, breaking assumptions that downstream code often makes about document structure. | 0.7.7 / 0.8.4 / 0.9.0-beta.4 (`@xmldom/xmldom`); legacy `xmldom` remains affected through `0.6.0` | https://github.com/advisories/GHSA-crh6-fp67-6883 |
| CVE-2026-34601 / GHSA-wh4c-j3r5-mjhp | High | Unsafe CDATA serialization could allow attacker-controlled markup injection when applications serialized attacker-influenced DOM content. | 0.8.12 / 0.9.9 (`@xmldom/xmldom`); legacy `xmldom` remains affected through `0.6.0` | https://github.com/advisories/GHSA-wh4c-j3r5-mjhp |
| CVE-2026-41672 / GHSA-j759-j44w-7fr8 | High | Unvalidated comment serialization could enable XML node injection in serialized output. | 0.8.13 / 0.9.10 (`@xmldom/xmldom`); legacy `xmldom` remains affected through `0.6.0` | https://github.com/advisories/GHSA-j759-j44w-7fr8 |
| CVE-2026-41673 / GHSA-2v35-w6hq-6mfw | High | Deeply nested DOM trees could trigger uncontrolled recursion and process-crashing `RangeError` exceptions during serialization and several other recursive DOM operations. | 0.8.13 / 0.9.10 (`@xmldom/xmldom`); legacy `xmldom` remains affected through `0.6.0` | https://github.com/advisories/GHSA-2v35-w6hq-6mfw |
| CVE-2026-41674 / GHSA-f6ww-3ggp-fr8h | High | Unvalidated `DocumentType` serialization could allow XML injection through attacker-controlled DOCTYPE content. | 0.8.13 / 0.9.10 (`@xmldom/xmldom`); legacy `xmldom` remains affected through `0.6.0` | https://github.com/advisories/GHSA-f6ww-3ggp-fr8h |
| CVE-2026-41675 / GHSA-x6wf-f3px-wcqx | High | Unvalidated processing-instruction serialization could enable XML node injection in serialized output. | 0.8.13 / 0.9.10 (`@xmldom/xmldom`); legacy `xmldom` remains affected through `0.6.0` | https://github.com/advisories/GHSA-x6wf-f3px-wcqx |

## Security Posture Notes

- `xmldom` is an unusual but important case where the public advisory trail spans **two npm package names**: the legacy unscoped `xmldom` package and the maintained scoped fork `@xmldom/xmldom`.
- The legacy `xmldom` package is still the npm package named `xmldom`, and the registry snapshot gathered in this pass still shows **`0.6.0` as latest**, which means several later security fixes only exist under the scoped fork.
- Public advisories show a **clear recurring pattern around XML boundary handling**, not a one-off bug: malformed-input interpretation, multi-root parsing integrity failures, serialization-time XML injection through multiple node types, and deep-recursion denial of service.
- The maintained fork has shipped successive fixes through `0.8.13` and `0.9.10`, but users who continue to depend on the legacy unscoped package name remain exposed to the later 2022 and 2026 advisory set.
- Even the legacy package still showed **~1.55M weekly downloads** in the review snapshot, so this is not merely historical cleanup; the package family still has real downstream exposure.

## Recommendations for Developers

1. **Prefer `@xmldom/xmldom` over legacy `xmldom`** for any maintained deployment.
2. To cover the currently published advisory set reviewed here, use at least **`@xmldom/xmldom` `0.8.13` on the 0.8 line** or **`0.9.10` on the 0.9 line**.
3. Audit dependency trees with tools like `npm ls xmldom @xmldom/xmldom` to find indirect use of the legacy unscoped package.
4. Treat XML parsing and especially **XML serialization** as security-relevant trust boundaries: attacker-controlled comments, CDATA, processing instructions, or document type nodes should not be assumed safe merely because they came from a parsed DOM.
5. Add regression tests for malformed XML structure, multiple top-level elements, serializer edge cases, and deeply nested documents if your application accepts untrusted XML.

## Dependencies of Note

- `xmldom` and `@xmldom/xmldom` matter in import/export pipelines, XML-to-object conversion flows, SOAP / SAML / feed handling, and other interoperability layers that often sit on untrusted input boundaries.
- The main security boundary visible in the public advisory trail is not only parsing: **serialized output correctness** is also a recurring attack surface.
- Because the fixed code landed in the scoped fork while the unscoped package remained frozen, transitive dependency inventories can understate risk if they only look for one package name.

## Open Questions

- Which major downstream packages still transitively depend on the legacy unscoped `xmldom` package rather than `@xmldom/xmldom`?
- Do additional maintainer release notes or migration guides exist that would make the unscoped-to-scoped package transition easier to document for downstream maintainers?
- Would a future KB cross-package review of `xmldom`, `xml2js`, and other XML tooling help highlight when the main risk is parser correctness versus serializer correctness?

## Related Pages

- [[npm/xml2js]]
- [[npm/js-yaml]]
- [[npm/index]]

---
*Last updated: 2026-04-24 | Sources: 8 (OSV.dev package query for npm/xmldom, OSV vulnerability records for the eight GHSA entries, GitHub Advisory Database / public GitHub security advisories, public CVE / NVD records, maintainer fix commits linked from the advisory records, upstream release tags for 0.7.7 / 0.8.4 / 0.8.12 / 0.8.13 / 0.9.9 / 0.9.10, npm registry metadata, npm downloads API)*