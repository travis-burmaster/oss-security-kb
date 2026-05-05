# org.apache.commons:commons-compress (Maven)

**Registry:** Maven (Maven Central)
**Weekly Downloads:** unknown
**Repository:** https://github.com/apache/commons-compress
**Security Contact:** Apache Commons / ASF Security Team
**Disclosure Policy:** https://commons.apache.org/security.html
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-05 | OpenClaw recurring review | advisory mapping (public records only) | public-source curation (OSV.dev package query and vulnerability records, GitHub Advisory Database aliases, Apache Commons Compress security page, public CVE aliases, local proxy synthesis used only as a drafting aid) | Added initial Maven package page mapping 11 public DoS / resource-exhaustion advisories across archive parsing and compression surfaces. | https://osv.dev/list?ecosystem=Maven&q=org.apache.commons%3Acommons-compress |

## Known Vulnerabilities

The table below is a package-level public advisory map from OSV.dev for `org.apache.commons:commons-compress`, cross-checked against the Apache Commons Compress security page where available.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-25710 / GHSA-4g9r-vxhx-9pgx | Important (Apache) / DoS | Infinite loop while reading a corrupted DUMP archive. The Apache security page says versions 1.3 through 1.25.0 are affected. | 1.26.0 | https://osv.dev/vulnerability/GHSA-4g9r-vxhx-9pgx ; https://commons.apache.org/compress/security.html |
| CVE-2024-26308 / GHSA-4265-ccf5-phj5 | Moderate (Apache) / DoS | OutOfMemoryError while unpacking a broken Pack200 file; OSV describes allocation of resources without limits or throttling. | 1.26.0 | https://osv.dev/vulnerability/GHSA-4265-ccf5-phj5 ; https://commons.apache.org/compress/security.html |
| CVE-2023-42503 / GHSA-cgwf-w82q-5jrr | Moderate (Apache) / DoS | TAR parsing can consume excessive CPU when malformed PAX timestamp fields trigger expensive `BigDecimal` parsing. Apache notes this applies to TAR parsing via `CompressorStreamFactory` auto-detection, `TarArchiveInputStream`, and `TarFile`. | 1.24.0 | https://osv.dev/vulnerability/GHSA-cgwf-w82q-5jrr ; https://commons.apache.org/compress/security.html |
| CVE-2021-35515 / GHSA-7hfm-57qf-j43q | Low (Apache) / DoS | Specially crafted 7Z archive can cause an infinite loop while constructing the codec list for an entry. | 1.21 | https://osv.dev/vulnerability/GHSA-7hfm-57qf-j43q ; https://commons.apache.org/compress/security.html |
| CVE-2021-35516 / GHSA-crv7-7245-f45f | Low (Apache) / DoS | Specially crafted 7Z archive can trigger large memory allocation and OutOfMemoryError even for small inputs. | 1.21 | https://osv.dev/vulnerability/GHSA-crv7-7245-f45f ; https://commons.apache.org/compress/security.html |
| CVE-2021-35517 / GHSA-xqfj-vm6h-2x34 | Low (Apache) / DoS | Specially crafted TAR archive can trigger large memory allocation and OutOfMemoryError even for small inputs. | 1.21 | https://osv.dev/vulnerability/GHSA-xqfj-vm6h-2x34 ; https://commons.apache.org/compress/security.html |
| CVE-2021-36090 / GHSA-mc84-pj99-q6hh | Low (Apache) / DoS | Specially crafted ZIP archive can trigger large memory allocation and OutOfMemoryError even for small inputs. | 1.21 | https://osv.dev/vulnerability/GHSA-mc84-pj99-q6hh ; https://commons.apache.org/compress/security.html |
| CVE-2019-12402 / GHSA-53x6-4x5p-rrvv | Low (Apache) / DoS | File-name encoding algorithm can enter an infinite loop when archive filenames are attacker-controlled. | 1.19 | https://osv.dev/vulnerability/GHSA-53x6-4x5p-rrvv ; https://commons.apache.org/compress/security.html |
| CVE-2018-11771 / GHSA-hrmr-f5m6-m9pq | Low (Apache) / DoS | `ZipArchiveInputStream.read()` can fail to signal EOF correctly after the end of a crafted ZIP stream, which can lead to an infinite stream when combined with `InputStreamReader`. | 1.18 | https://osv.dev/vulnerability/GHSA-hrmr-f5m6-m9pq ; https://commons.apache.org/compress/security.html |
| CVE-2018-1324 / GHSA-h436-432x-8fvx | Low (Apache) / DoS | Crafted ZIP archive can cause an infinite loop in the ZIP extra-field parser used by `ZipFile` and `ZipArchiveInputStream`. | 1.16 | https://osv.dev/vulnerability/GHSA-h436-432x-8fvx ; https://commons.apache.org/compress/security.html |
| CVE-2012-2098 / GHSA-6fxm-66hq-fc96 | Low (Apache) / DoS | BZip2 compression stream used sorting algorithms with poor worst-case performance on repetitive input, causing CPU exhaustion. | 1.4.1 | https://osv.dev/vulnerability/GHSA-6fxm-66hq-fc96 ; https://commons.apache.org/compress/security.html |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.apache.commons%3Acommons-compress*

## Security Posture Notes

- The public advisory pattern is strongly concentrated around **archive parsing and compression denial-of-service**: malformed DUMP, Pack200, TAR, ZIP, 7Z, and BZip2 inputs can drive infinite loops, excessive CPU, or excessive memory allocation.
- The highest-priority current remediation line in the public Apache page is **1.26.0 or later**, because it fixes the 2024 DUMP and Pack200 advisories. The Apache site currently identifies the project page as version `1.28.0` and was last published 2025-07-26.
- Exposure is application-dependent: services that parse attacker-supplied archives, auto-detect archive formats, unpack uploads, or process archives from queues / integrations have materially higher risk than applications that only handle trusted local archives.
- Apache's security page states that binary patches are not provided and directs users who need source-level patching or build help to the public Compress users mailing list. Operationally, most downstreams should prefer upgrading to a fixed release rather than carrying local patches.
- Multiple 2021 issues were discovered or expanded by OSS-Fuzz, which is useful positive evidence that archive parsers have received fuzzing attention, while also showing that malformed archive inputs remain the main risk surface.

## Dependencies of Note

- `commons-compress` is itself commonly embedded as an archive-processing dependency in larger Java applications and build / packaging tools. Downstream exposure often comes through transitive use, so SBOM and dependency-tree checks matter.
- No transitive dependency advisory was normalized in this pass; this page is focused on direct `org.apache.commons:commons-compress` package advisories.

## Open Questions

- Which high-download Maven artifacts still pin `commons-compress` below 1.26.0, especially in file-upload, ETL, document-processing, or build-server contexts?
- Are there public downstream advisories where `commons-compress` archive parsing was reachable through application upload features rather than direct library use?
- Should the KB add a cross-ecosystem archive-extraction risk page comparing `commons-compress`, npm `tar` / `tar-fs`, and Python archive-handling packages?

## Related Pages

- [[npm/tar]]
- [[npm/tar-fs]]
- [[maven/index]]

---
*Last updated: 2026-05-05 | Sources: 4 (OSV package query and individual vulnerability records, GitHub Advisory Database public aliases, Apache Commons Compress security page, public CVE aliases referenced by OSV/GHSA records)*
