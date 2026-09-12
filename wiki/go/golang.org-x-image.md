# golang.org/x/image (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (part of Go extended stdlib; not tracked separately by a public download API)
**Repository:** https://github.com/golang/image
**Security Contact:** security@golang.org
**Disclosure Policy:** https://go.dev/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-09-12 | oss-security-kb nightly pass | api-surface | automated | 6 advisories confirmed | [GitHub Security Advisories](https://github.com/golang/image/security/advisories) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-41727 / GHSA-qgc7-mgm3-q253 | Moderate (CVSS 7.1) | TIFF `image.DecodeConfig` processes images with excessively large dimensions without a size guard, causing uncontrolled memory allocation on a malformed/malicious TIFF. Any service accepting user-supplied TIFF images via `x/image/tiff` is exposed. | 0.5.0 | [GHSA-qgc7-mgm3-q253](https://github.com/advisories/GHSA-qgc7-mgm3-q253) |
| CVE-2023-29407 / GHSA-j3p8-6mrq-6g7h | Moderate (CVSS 7.5) | TIFF decoder processes tiled images where individual tiles have zero height but a very large width value, triggering near-infinite CPU consumption. CWE-400 / CWE-834. | 0.10.0 | [GHSA-j3p8-6mrq-6g7h](https://github.com/advisories/GHSA-j3p8-6mrq-6g7h) |
| CVE-2023-29408 / GHSA-x92r-3vfx-4cv3 | Moderate (CVSS 7.5) | TIFF decoder places no limit on the total size of compressed tile data fetched for a single image, enabling a crafted TIFF to exhaust memory and CPU by encoding a small image with enormous compressed tile payloads. CWE-400 / CWE-770. Published same day as CVE-2023-29407; both fixed in the same 0.10.0 release. | 0.10.0 | [GHSA-x92r-3vfx-4cv3](https://github.com/advisories/GHSA-x92r-3vfx-4cv3) |
| CVE-2024-24792 / GHSA-9phm-fm57-rhg8 | High (CVSS 7.5) | Palette-color images with an invalid color index (out-of-bounds reference into the palette) trigger a panic in the decoder, crashing any process that does not recover from the panic. Affected formats include TIFF and any other palette-color decoder in `x/image`. | 0.18.0 | [GHSA-9phm-fm57-rhg8](https://github.com/advisories/GHSA-9phm-fm57-rhg8) |
| CVE-2026-33809 / GHSA-44p7-9xx4-hf2g | Moderate (CVSS 5.3) | Crafted TIFF files cause the decoder to attempt to allocate up to 4 GiB of memory during image decoding, leading to excessive resource consumption or an out-of-memory crash. A narrower variant of the 2022–2023 TIFF allocation-limit pattern. | 0.38.0 | [GHSA-44p7-9xx4-hf2g](https://github.com/advisories/GHSA-44p7-9xx4-hf2g) |
| CVE-2026-46599 / GHSA-q675-qj96-32m9 | High (CVSS 7.5) | PackBits-compressed TIFF data has no decompressed-size limit; a crafted image with small file dimensions but huge PackBits-encoded payloads triggers excessive CPU and memory decompression. Latest in the recurring TIFF-decoder DoS chain. | 0.41.0 | [GHSA-q675-qj96-32m9](https://github.com/advisories/GHSA-q675-qj96-32m9) |

*OSV link: https://osv.dev/list?ecosystem=Go&q=golang.org%2Fx%2Fimage*

## Security Posture Notes

`golang.org/x/image` is part of the official Go extended standard library, maintained by the Go team at Google. It provides supplementary image codecs (BMP, TIFF, WebP, RIFF containers), font rendering (TrueType / OpenType via `x/image/font`), vector rasterization (`x/image/vector`), and color-name utilities.

The **recurring theme is TIFF decoder resource exhaustion**: six public advisories from February 2023 through July 2026 all follow the same pattern — crafted TIFF files exploit missing size limits in compressed tile data, palette color indices, PackBits decompression, or general dimension validation. Each fix addresses one specific code path, and a new variant surfaces within 6–18 months. Services accepting user-supplied TIFF images should treat input validation as defense-in-depth even on current versions.

The current release as of 2026-09-12 is **v0.46.0**, which is unaffected by all listed advisories.

**Disclosure path:** The Go security team follows the standard Go disclosure process at https://go.dev/security. Advisories are published simultaneously on the GitHub Security Advisories page and via the Go vulnerability database (https://pkg.go.dev/vuln/).

The module is used widely as a transitive dependency in image processing pipelines, document renderers, PDF processors, and any Go application that ingests raster images beyond what the standard `image/*` packages handle.

## Dependencies of Note

- `golang.org/x/text` — used for font utilities; has its own separate advisory history ([[go/golang.org-x-text]])
- `golang.org/x/net` — indirect; see [[go/golang.org-x-net]]

## Open Questions

- The recurring TIFF-decoder DoS pattern suggests systematic missing limits rather than isolated bugs. A targeted audit of all remaining TIFF decompression paths would be valuable.
- WebP and BMP decoders have not appeared in the advisory history; confirm whether they are in scope for future passes.
- Track whether v0.46.0 addresses any forthcoming TIFF variant not yet published.

## Related Pages

- [[go/golang.org-x-crypto]]
- [[go/golang.org-x-net]]
- [[go/golang.org-x-text]]
- [[go/index]]

---
*Last updated: 2026-09-12 | Sources: 6 (GHSA-qgc7-mgm3-q253, GHSA-j3p8-6mrq-6g7h, GHSA-x92r-3vfx-4cv3, GHSA-9phm-fm57-rhg8, GHSA-44p7-9xx4-hf2g, GHSA-q675-qj96-32m9)*
