# commons-io:commons-io (Maven)

**Registry:** Maven Central
**Weekly Downloads:** unknown (as of 2026-05-11)
**Repository:** https://github.com/apache/commons-io
**Security Contact:** https://commons.apache.org/security.html
**Disclosure Policy:** https://commons.apache.org/security.html
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No audits on record.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-29425 / GHSA-gwrp-pvrq-jmwv | Moderate | `FilenameUtils.normalize` / filename-normalization issue where improper inputs such as `//../foo` or `\\..\foo` could normalize to a value still usable for limited parent-directory traversal if downstream caller code trusted the normalized path. | 2.7 | [OSV](https://osv.dev/vulnerability/GHSA-gwrp-pvrq-jmwv), [GitHub Advisory](https://github.com/advisories/GHSA-gwrp-pvrq-jmwv), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-29425) |
| CVE-2024-47554 / GHSA-78wr-2p64-hpwj | High in GHSA/OSV; Low in Apache advisory | `org.apache.commons.io.input.XmlStreamReader` could excessively consume CPU resources when processing maliciously crafted input. OSV records affected versions as 2.0 before 2.14.0; the Apache security page recommends upgrading to 2.14.0 or later. | 2.14.0 | [OSV](https://osv.dev/vulnerability/GHSA-78wr-2p64-hpwj), [GitHub Advisory](https://github.com/advisories/GHSA-78wr-2p64-hpwj), [Apache advisory](https://commons.apache.org/proper/commons-io/security.html), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-47554) |

## Security Posture Notes

Apache Commons IO is a mature Java I/O utility library maintained under the Apache Commons project. Maven Central metadata for `commons-io:commons-io` showed latest/release version `2.22.0` in this pass, and the upstream release notes list continuing maintenance through the 2026-04-19 `2.22.0` release.

The public advisory set is compact but security-relevant because Commons IO often sits in file-path, stream, temporary-file, and parsing helper code. The 2021 issue is caller-context-sensitive: the vulnerable normalization result becomes security-impacting when application code uses it as a path-containment or traversal boundary. The 2024 `XmlStreamReader` issue is a resource-consumption / DoS class; note the public severity disagreement between GHSA/OSV (`High`) and the Apache project page (`Low`) when triaging downstream exposure.

Disclosure maturity is strong: Apache Commons publishes a component security page, points reporters to the Apache Commons / Apache Security process, and states that binary patches are not provided, so consumers should remediate by upgrading to fixed releases rather than expecting patched binaries for old lines.

## Dependencies of Note

- None flagged as direct dependency risks in this pass. Commons IO itself is more often the transitive dependency of note for other Java pages; future reviews should check downstream projects that pin versions before 2.14.0.

## Open Questions

- Which high-usage Maven artifacts still pin `commons-io:commons-io` before 2.14.0, especially in file-upload, archive, or XML-processing paths?
- Should downstream KB pages call out the GHSA/Apache severity discrepancy for CVE-2024-47554 when they expose `XmlStreamReader` to untrusted data?
- Are there public fuzzing or CodeQL reports for Commons IO path, stream, and XML-reader helpers beyond the two published GHSA/CVE records?

## Related Pages

- [[maven/commons-fileupload/commons-fileupload]]
- [[maven/org.apache.commons/commons-compress]]
- [[maven/index]]

---
*Last updated: 2026-05-11 | Sources: 8*
