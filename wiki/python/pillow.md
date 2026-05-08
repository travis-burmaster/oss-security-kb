# pillow (python)

**Registry:** PyPI
**Repository:** https://github.com/python-pillow/Pillow
**Security Contact:** https://github.com/python-pillow/Pillow/security/advisories
**Disclosure Policy:** https://github.com/python-pillow/Pillow/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-08 | OpenClaw recurring review | package advisory history | manual | 66 unique-ish public Pillow vulnerability records normalized from 118 OSV rows, including duplicate GHSA / PYSEC / Bitnami aliases and OSS-Fuzz records; representative high-signal records mapped below | https://osv.dev/list?ecosystem=PyPI&q=pillow |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-42311 / GHSA-pwv6-vv43-88gr | High | Follow-on PSD tile-extent bounds issue: the CVE-2026-25990 checks used integer-overflow-prone extent arithmetic, allowing crafted PSD dimensions to bypass the earlier bounds checks and reach out-of-bounds writes in decode / encode paths. | 12.2.0 | https://github.com/python-pillow/Pillow/security/advisories/GHSA-pwv6-vv43-88gr |
| CVE-2026-40192 / GHSA-whj4-6x5x-4v2j | High | FITS decoder decompression-bomb issue: GZIP-compressed FITS input could trigger unbounded memory consumption because Pillow did not limit the amount of compressed data read for the image. | 12.2.0 | https://github.com/python-pillow/Pillow/security/advisories/GHSA-whj4-6x5x-4v2j |
| CVE-2026-42310 / GHSA-r73j-pqj5-w3x7 | Moderate | PDF parser denial of service: cyclic `Prev` trailer offsets could make the parser loop indefinitely while reading cross-reference sections. | 12.2.0 | https://github.com/python-pillow/Pillow/security/advisories/GHSA-r73j-pqj5-w3x7 |
| CVE-2026-42308 / GHSA-wjx4-4jcj-g98j | Moderate | Font processing integer overflow when accumulating very large glyph advances. | 12.2.0 | https://github.com/python-pillow/Pillow/security/advisories/GHSA-wjx4-4jcj-g98j |
| CVE-2026-25990 / GHSA-cfh3-3jmp-rvhc | High | PSD image loading could trigger an out-of-bounds write; the upstream advisory recommends using `Image.open(..., formats=...)` to exclude PSD where upgrading is not immediately possible. | 12.1.1 | https://github.com/python-pillow/Pillow/security/advisories/GHSA-cfh3-3jmp-rvhc |
| CVE-2025-48379 / GHSA-xg8h-j46f-w952 / PYSEC-2025-61 | High | DDS BCn encoding heap buffer overflow introduced with the 11.2.0 feature: saving sufficiently large untrusted data as compressed DDS could write past the available buffer. | 11.3.0 | https://github.com/python-pillow/Pillow/security/advisories/GHSA-xg8h-j46f-w952 |
| CVE-2024-28219 / GHSA-44wm-f244-xhp3 | High | Buffer overflow in `_imagingcms.c` where `strcpy` was used instead of bounded copying. | 10.3.0 | https://github.com/advisories/GHSA-44wm-f244-xhp3 |
| CVE-2023-50447 / GHSA-3f63-hfp8-52jq | Critical | `PIL.ImageMath.eval` arbitrary code execution through the `environment` parameter; distinct from the earlier expression-parameter issue tracked as CVE-2022-22817. | 10.2.0 | https://github.com/advisories/GHSA-3f63-hfp8-52jq |
| CVE-2023-44271 / GHSA-8ghj-p4vj-mr35 / PYSEC-2023-227 | High | ImageFont / ImageDraw `textlength` handling could allocate memory uncontrollably for long text, causing denial of service. | 10.0.0 | https://github.com/advisories/GHSA-8ghj-p4vj-mr35 |
| CVE-2022-22817 / GHSA-8vj2-vxx3-667w / PYSEC-2022-10 | Critical | `PIL.ImageMath.eval` expression handling allowed arbitrary expression evaluation; 9.0.0 restricted top-level builtins and 9.0.1 also restricted builtins reachable through lambda expressions. | 9.0.1 | https://github.com/advisories/GHSA-8vj2-vxx3-667w |
| CVE-2022-24303 / GHSA-9j59-75qj-795w / PYSEC-2022-168 | High | Temporary pathname handling could allow file deletion / path traversal behavior when spaces in temporary paths were mishandled. | 9.0.1 | https://github.com/advisories/GHSA-9j59-75qj-795w |
| CVE-2021-34552 / GHSA-7534-mm45-c74v / PYSEC-2021-331 | Critical | Buffer overflow in `Convert.c` when controlled parameters reached image conversion code. | 8.3.0 | https://github.com/advisories/GHSA-7534-mm45-c74v |
| CVE-2021-23437 / GHSA-98vv-pw6r-q6q4 / PYSEC-2021-317 | High | `getrgb` regular-expression denial of service in versions before 8.3.2. | 8.3.2 | https://github.com/advisories/GHSA-98vv-pw6r-q6q4 |
| CVE-2014-3007 / GHSA-8m9x-pxwq-j236 / PYSEC-2014-87 | Critical | Legacy PIL / Pillow command-injection issue around shell metacharacters in image-helper paths related to the temporary-file handling lineage. | 2.5.0 | https://github.com/advisories/GHSA-8m9x-pxwq-j236 |
| CVE-2014-1932 / GHSA-x895-2wrm-hvp7 / PYSEC-2014-22 | High | Legacy temporary-file symlink attack in image helper paths, allowing local overwrite / information disclosure via unsafe temporary-file creation. | 2.3.1 | https://github.com/advisories/GHSA-x895-2wrm-hvp7 |

*Full public advisory query: https://osv.dev/list?ecosystem=PyPI&q=pillow*

## Security Posture Notes

- Pillow is a high-value parser boundary: applications often pass attacker-controlled images through C-backed decoders, encoders, font code, PDF/FITS helpers, and optional external-library integrations.
- The public record is dense. OSV returned 118 rows in this pass, but that includes duplicate aliases for the same CVEs, Bitnami mirrors, PYSEC records, and OSS-Fuzz records. Treat the table above as representative, not exhaustive.
- Recurrent bug classes are image-format memory corruption, integer-overflow-derived bounds mistakes, decompression / allocation denial of service, and historically dangerous helper APIs such as `ImageMath.eval` and temporary-file / external-helper paths.
- Recent 2025-2026 advisories show active maintenance and coordinated GitHub Security Advisory use, but they also show that new decoder / encoder features can introduce fresh C-memory-safety issues.
- For services processing untrusted uploads, version freshness is necessary but not sufficient. Restrict accepted formats with `Image.open(..., formats=...)`, enforce file-size / pixel-count / CPU / memory limits outside Pillow, and isolate image processing where feasible.

## Dependencies of Note

- Pillow can use external image libraries depending on build and wheel/platform choices, including libjpeg, zlib, libtiff, libwebp, openjpeg, littlecms, freetype, and imagequant-style optional components. Review bundled or system-library exposure separately for distribution-specific risk.
- Web applications that accept uploads should also review their framework upload limits and storage paths; Pillow advisories often become exploitable only when upstream request handling allows large or attacker-controlled image bodies.

## Open Questions

- Should the KB split Pillow's advisory history into a dedicated parser-family page covering image decoders, external libraries, and upload isolation patterns?
- Which downstream packages make Pillow reachable on attacker-controlled input by default and deserve cross-links from this page?
- Are distro package backports for recent 12.x-era fixes easy to track, or should distro-specific Pillow pages be added later?

## Related Pages

- [[python/django]]
- [[python/flask]]
- [[python/aiohttp]]
- [[python/index]]

---
*Last updated: 2026-05-08 | Sources: OSV package query and vulnerability details, GitHub Advisory Database records, public CVE / NVD records, upstream Pillow GitHub Security Advisories, Pillow release notes, and local proxy synthesis used as a drafting aid only after manual evidence review.*
