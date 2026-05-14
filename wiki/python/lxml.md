# lxml (python)

**Registry:** PyPI  
**Weekly Downloads:** ~89,197,199 (PyPIStats last week, fetched 2026-05-14)  
**Repository:** https://github.com/lxml/lxml  
**Security Contact:** GitHub Security Advisories / project security process  
**Disclosure Policy:** GitHub private vulnerability reporting / upstream advisories where published  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-14 | OpenClaw recurring review | package-level public advisory mapping for PyPI `lxml` | public-source curation from OSV.dev package and vulnerability records, GitHub Advisory Database records, public CVE / NVD pages, upstream lxml changelog / release references, PyPI metadata, PyPIStats download data, and local proxy-assisted drafting | Added initial advisory-mapped page for lxml's published package vulnerability history: recurring `lxml.html.clean` XSS / sanitizer-bypass issues, a libxml2-backed parser DoS boundary, and the 2026 `iterparse()` / `ETCompatXMLParser` XXE default-configuration fix. | https://osv.dev/list?ecosystem=PyPI&q=lxml |

## Known Vulnerabilities

OSV returns canonical GHSA records plus older PYSEC aliases for several entries. This page counts the seven GHSA-backed underlying vulnerability records once each and keeps fixed-version boundaries tied to the public advisory metadata.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2014-3146 / GHSA-57qw-cc2g-pv5p | Medium | `lxml.html.clean` did not properly neutralize some control-character forms in cleaned HTML, allowing XSS-relevant input to bypass the cleaner. | 3.3.5 | https://github.com/advisories/GHSA-57qw-cc2g-pv5p ; https://nvd.nist.gov/vuln/detail/CVE-2014-3146 ; http://lxml.de/3.3/changes-3.3.5.html |
| CVE-2018-19787 / GHSA-xp26-p53h-6h2p | Medium | The HTML cleaner failed to remove JavaScript URLs when URL escaping was used, so cleaned output could still contain scriptable links. | 4.2.5 | https://github.com/advisories/GHSA-xp26-p53h-6h2p ; https://nvd.nist.gov/vuln/detail/CVE-2018-19787 ; https://github.com/lxml/lxml/commit/6be1d081b49c97cfd7b3fbd934a193b668629109 |
| CVE-2020-27783 / GHSA-pgww-xf46-h92r | Medium | Another `lxml.html.clean` bypass allowed JavaScript-relevant content to pass through via crafted style / HTML constructs. Upstream changelog text says the cleaner removed more sneaky `style` content in 4.6.2. | 4.6.2 | https://github.com/advisories/GHSA-pgww-xf46-h92r ; https://nvd.nist.gov/vuln/detail/CVE-2020-27783 ; https://github.com/lxml/lxml/commit/a105ab8dc262ec6735977c25c13f0bdfcdec72a7 |
| CVE-2021-28957 / GHSA-jq4v-f5q6-mjqq | Medium | The HTML cleaner allowed JavaScript to pass through through the HTML5 `formaction` attribute; upstream 4.6.3 changelog says the cleaner now removes that attribute. | 4.6.3 | https://github.com/advisories/GHSA-jq4v-f5q6-mjqq ; https://nvd.nist.gov/vuln/detail/CVE-2021-28957 ; https://github.com/lxml/lxml/pull/316 |
| CVE-2021-43818 / GHSA-55x5-fj6c-h6m8 | Medium | Crafted SVG / embedded script and CSS-import constructs could bypass `lxml.html.clean`. The upstream 4.6.5 changelog records two GitHub Security Lab findings under the same CVE. | 4.6.5 | https://github.com/advisories/GHSA-55x5-fj6c-h6m8 ; https://github.com/lxml/lxml/security/advisories/GHSA-55x5-fj6c-h6m8 ; https://nvd.nist.gov/vuln/detail/CVE-2021-43818 |
| CVE-2022-2309 / GHSA-wrxv-2j5q-m38w | Medium | A libxml2 2.9.10-2.9.14 namespace-cleanup issue could let namespace declarations from a failed parser run leak into later parser runs and produce a NULL-pointer-dereference / denial-of-service condition; lxml worked around the issue while libxml2 resolved it in 2.10.0. | 4.9.1 according to GHSA; upstream changelog also documents the CVE context in 4.9.2 | https://github.com/advisories/GHSA-wrxv-2j5q-m38w ; https://nvd.nist.gov/vuln/detail/CVE-2022-2309 ; https://github.com/lxml/lxml/commit/86368e9cf70a0ad23cccd5ee32de847149af0c6f |
| CVE-2026-41066 / GHSA-vfmq-68hx-4jfw | High | Default `resolve_entities=True` behavior for `iterparse()` and `ETCompatXMLParser` allowed local-file XXE when callers used those parsers without explicitly overriding entity resolution. lxml 6.1.0 changed the default to `internal`, matching the normal XML / HTML parser direction since lxml 5.0. | 6.1.0 | https://github.com/advisories/GHSA-vfmq-68hx-4jfw ; https://github.com/lxml/lxml/security/advisories/GHSA-vfmq-68hx-4jfw ; https://github.com/lxml/lxml/releases/tag/lxml-6.1.0 ; https://nvd.nist.gov/vuln/detail/CVE-2026-41066 |

*Full OSV package listing: https://osv.dev/list?ecosystem=PyPI&q=lxml*

## Security Posture Notes

- `lxml` is a high-blast-radius XML / HTML parsing library and C-extension binding for libxml2 / libxslt. Parser defaults, sanitizer expectations, and bundled/native library behavior can affect many applications indirectly.
- The public package-advisory footprint is concentrated in two areas: recurring `lxml.html.clean` sanitizer bypasses / XSS-relevant output boundaries, and XML parser / libxml2 interaction issues that affect DoS or XXE behavior.
- Users who rely on `lxml.html.clean` as a security boundary should treat it as an allowlist-sensitive sanitizer, not a substitute for context-aware output encoding or browser-side defenses. Several public records show that seemingly narrow HTML / SVG / attribute parsing edge cases have required repeated fixes.
- The 2026 XXE advisory is especially important for services parsing untrusted XML with `iterparse()` or `ETCompatXMLParser`, because the vulnerable condition was a default parser option rather than an opt-in dangerous mode for those APIs.
- Current PyPI metadata during this review showed `latest=6.1.0`, which is the public fixed version for CVE-2026-41066.
- This review did not perform active vulnerability hunting, exploit validation, or live target testing. It only normalized already-public advisory, CVE, upstream changelog / release, and package metadata.

## Dependencies of Note

- lxml's security posture depends partly on libxml2 / libxslt behavior and on whether consumers install binary wheels, build against system libraries, or receive distro-backported fixes.
- Applications should verify the actually imported `lxml` version and the bundled/system libxml2 versions when investigating parser behavior or distro packaging.
- Downstream packages that expose HTML cleaning, XML import, feed parsing, office-document parsing, or web-scraping inputs may inherit lxml risk even when `lxml` is only a transitive dependency.

## Open Questions

- Should future KB maintenance add a shared XML-parser page covering XXE / entity-resolution defaults across `lxml`, `defusedxml`, Java XML parsers, and Go XML stacks?
- Which high-usage Python packages expose `lxml.html.clean` or `iterparse()` to attacker-controlled content and therefore deserve dependency-aware notes?
- Should the KB separately track distro-packaged lxml builds where libxml2 fixes are backported independently of PyPI release numbers?

## Related Pages

- [[python/pyyaml]]
- [[python/python-multipart]]
- [[python/index]]

---
*Last updated: 2026-05-14 | Sources: OSV package query and individual vulnerability records for PyPI `lxml`; GitHub Advisory Database entries for GHSA-57qw-cc2g-pv5p, GHSA-xp26-p53h-6h2p, GHSA-pgww-xf46-h92r, GHSA-jq4v-f5q6-mjqq, GHSA-55x5-fj6c-h6m8, GHSA-wrxv-2j5q-m38w, and GHSA-vfmq-68hx-4jfw; public CVE / NVD records for CVE-2014-3146, CVE-2018-19787, CVE-2020-27783, CVE-2021-28957, CVE-2021-43818, CVE-2022-2309, and CVE-2026-41066; upstream lxml changelog and 6.1.0 release references; PyPI metadata; PyPIStats recent download data; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid.*
