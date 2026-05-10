# commons-fileupload:commons-fileupload (Maven)

**Registry:** Maven Central
**Weekly Downloads:** unknown (as of 2026-05-10)
**Repository:** https://github.com/apache/commons-fileupload
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
| CVE-2013-0248 / GHSA-vm69-474v-7q2w | Low | Incorrect default permissions / temporary-file handling issue in Apache Commons FileUpload. | 1.2.2 | [OSV](https://osv.dev/vulnerability/GHSA-vm69-474v-7q2w), [GitHub Advisory](https://github.com/advisories/GHSA-vm69-474v-7q2w) |
| CVE-2013-2186 / GHSA-qx6h-9567-5fqw | High | Arbitrary file write issue associated with filename handling in Apache Commons FileUpload. | 1.3.1 | [OSV](https://osv.dev/vulnerability/GHSA-qx6h-9567-5fqw), [GitHub Advisory](https://github.com/advisories/GHSA-qx6h-9567-5fqw) |
| CVE-2014-0050 / GHSA-xx68-jfcg-xmmf | High | Denial of service in multipart parsing / boundary handling. | 1.3.1 | [OSV](https://osv.dev/vulnerability/GHSA-xx68-jfcg-xmmf), [GitHub Advisory](https://github.com/advisories/GHSA-xx68-jfcg-xmmf) |
| CVE-2016-3092 / GHSA-fvm3-cfvj-gxqq | High | Multipart upload denial of service affecting versions before 1.3.2. | 1.3.2 | [OSV](https://osv.dev/vulnerability/GHSA-fvm3-cfvj-gxqq), [GitHub Advisory](https://github.com/advisories/GHSA-fvm3-cfvj-gxqq) |
| CVE-2016-1000031 / GHSA-7x9j-7223-rg5m | Critical | `DiskFileItem` file-manipulation / deserialization remote-code-execution issue in versions before 1.3.3. | 1.3.3 | [OSV](https://osv.dev/vulnerability/GHSA-7x9j-7223-rg5m), [GitHub Advisory](https://github.com/advisories/GHSA-7x9j-7223-rg5m) |
| CVE-2023-24998 / GHSA-hfrx-6qgj-fp6c | High | Request-part count was not limited before 1.5, allowing denial of service via malicious multipart uploads; OSV notes the new `FileUploadBase#setFileCountMax` option must be explicitly configured. | 1.5 | [OSV](https://osv.dev/vulnerability/GHSA-hfrx-6qgj-fp6c), [GitHub Advisory](https://github.com/advisories/GHSA-hfrx-6qgj-fp6c) |
| CVE-2025-48976 / GHSA-vv7r-c36w-3prj | High | Multipart part-header resource allocation had insufficient limits, enabling denial of service in 1.x before 1.6.0 and the 2.x milestone line before 2.0.0-M4. | 1.6.0 | [OSV](https://osv.dev/vulnerability/GHSA-vv7r-c36w-3prj), [GitHub Advisory](https://github.com/advisories/GHSA-vv7r-c36w-3prj) |

## Security Posture Notes

Apache Commons FileUpload is a mature multipart upload parser maintained under the Apache Commons project. Maven metadata shows `commons-fileupload:commons-fileupload` latest/release version `1.6.0`, published on the 1.x coordinate after the 2025 part-header DoS fix. The upstream `changes.xml` records the 1.6.0 addition of `partHeaderSizeMax`, a per-part multipart-header byte limit whose default is 512 bytes, and records 1.5 adding a configurable limit for number of uploaded files per request.

Important coordinate note: newer 2.x milestone releases use separate Maven coordinates such as `org.apache.commons:commons-fileupload2-core`. Keep 1.x (`commons-fileupload:commons-fileupload`) and 2.x (`commons-fileupload2-*`) advisory mappings separate when reviewing OSV or GitHub Advisory records.

Disclosure maturity is strong: the project points security reports to the Apache Commons security process and publishes fixes through Maven Central. The main sensitive surface remains untrusted multipart parsing, especially limits for part count, header size, temporary-file handling, and integration defaults in downstream web frameworks.

## Dependencies of Note

- None flagged in this pass; future review should separately inspect Commons IO and Servlet API exposure in deployed application stacks.

## Open Questions

- Which downstream frameworks still embed or shade vulnerable 1.x versions, and do their defaults enable `setFileCountMax` / header-size protections?
- Should the KB add a separate page for `org.apache.commons:commons-fileupload2-core` to track the 2.x milestone line independently?
- Are there public audits or fuzzing reports for multipart parser limits beyond the published CVE/GHSA records?

## Related Pages

- [[maven/org.apache.commons/commons-compress]]
- [[maven/index]]

---
*Last updated: 2026-05-10 | Sources: 18*
