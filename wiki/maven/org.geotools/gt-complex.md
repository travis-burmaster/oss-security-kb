# org.geotools:gt-complex (Maven)

**Registry:** Maven (Maven Central)
**Project:** GeoTools
**Repository:** https://github.com/geotools/geotools
**Security Contact / Advisories:** GitHub Security Advisories (GeoTools org)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-03 | OpenClaw recurring review | advisory mapping (public records only) | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream GitHub Security Advisory text) | Added initial Maven section + baseline page for GeoTools `gt-complex` centered on CVE-2024-36404 / GHSA-w3pj-wh35-fq8w. | https://osv.dev/vulnerability/GHSA-w3pj-wh35-fq8w |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-36404 / GHSA-w3pj-wh35-fq8w | Critical | **Remote code execution** can be possible when an application uses certain GeoTools features to evaluate **XPath expressions supplied by user input**. The advisory notes that several GeoTools methods pass attacker-controlled XPath into `commons-jxpath`, which can execute arbitrary code. | 28.6, 29.6, 30.4, 31.2 (per OSV fixed-version ranges) | [OSV](https://osv.dev/vulnerability/GHSA-w3pj-wh35-fq8w), [GHSA](https://github.com/advisories/GHSA-w3pj-wh35-fq8w), [OSV JSON](https://api.osv.dev/v1/vulns/GHSA-w3pj-wh35-fq8w) |

## Security Posture Notes

- **Exploit precondition (per advisory):** the vulnerable surface is specifically when a downstream application feeds **untrusted** XPath/property expressions into the affected GeoTools evaluation paths.
- **Affected artifact set (per OSV “affected” packages):** the public OSV record for GHSA-w3pj-wh35-fq8w tracks coordinated fixes across multiple GeoTools artifacts, including:
  - `org.geotools:gt-complex`
  - `org.geotools:gt-app-schema`
  - `org.geotools.xsd:gt-xsd-core`
- **Fix-version model (per OSV ranges):** remediation is described as "fixed in" on multiple maintained lines. The OSV record lists fixed versions `28.6`, `29.6`, `30.4`, and `31.2`, indicating a backport strategy across release trains.
- **Non-Maven patch distribution caveat:** the GHSA/OSV text mentions “drop-in replacement jars” hosted on SourceForge for rapid remediation in some cases. This is operationally important: some deployments may need out-of-band patched JAR replacement if they cannot immediately consume a fixed Maven Central release. These out-of-band jars are *not* something Maven will automatically resolve; applying them typically requires manual replacement in the application packaging/runtime.
- **Mitigation scope caveat:** the advisory mentions removing the `gt-complex` JAR to run with reduced functionality; note that this breaks some GeoTools/GeoServer features (the advisory calls out the application schema datastore) and should be treated as a stopgap rather than a full remediation.

## Recommendations for Developers

1. **Do not evaluate attacker-controlled XPath / property expressions.** Treat expression strings as code.
2. **Upgrade to a fixed line** (28.6 / 29.6 / 30.4 / 31.2 or later, matching your major/minor line) as indicated by OSV/GHSA.
3. If you must run an affected line temporarily, consider the **mitigations described in the advisory** (for example, removing `gt-complex` for reduced functionality) where feasible — but treat mitigations as stopgaps.

## Related Pages

- [[maven/index]]

---
*Last updated: 2026-05-03 | Sources: 3 (OSV.dev vulnerability record for GHSA-w3pj-wh35-fq8w / CVE-2024-36404, GitHub Advisory Database entry for GHSA-w3pj-wh35-fq8w, OSV JSON affected-package version ranges and aliases)*
