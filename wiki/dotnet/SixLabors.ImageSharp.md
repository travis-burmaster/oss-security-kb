# SixLabors.ImageSharp (.NET / NuGet)

**Registry:** NuGet
**Weekly Downloads:** ~273,300,000 total downloads as of 2026-06-20 (NuGet does not expose per-week download stats via public API)
**Repository:** https://github.com/SixLabors/ImageSharp
**Security Contact:** https://github.com/SixLabors/ImageSharp/security (GitHub private vulnerability reporting)
**Disclosure Policy:** https://github.com/SixLabors/ImageSharp/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-20 | OSS Security KB | advisory-db lookup | automated | 7 GHSA advisories mapped across PNG, JPEG, TGA, and GIF decoders | [github/advisory-database](https://github.com/github/advisory-database) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-27929 / GHSA-65x7-c272-7g7r | High | Heap use-after-free in `PngDecoderCore.InitializeImage()` triggered by specially crafted PNG files; can expose sensitive memory contents from other parts of the application (information disclosure). CVSS 3.1: AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:H. | 2.1.7, 3.1.3 | [GHSA-65x7-c272-7g7r](https://github.com/advisories/GHSA-65x7-c272-7g7r) |
| CVE-2024-32035 / GHSA-g85r-6x2q-45w7 | Moderate | Memory allocation with excessive size value across multiple decoders when processing specially crafted image files; enables process-memory exhaustion denial of service. CVSS 3.1: AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L. | 2.1.8, 3.1.4 | [GHSA-g85r-6x2q-45w7](https://github.com/advisories/GHSA-g85r-6x2q-45w7) |
| CVE-2024-32036 / GHSA-5x7m-6737-26cr | Moderate | Data leakage flaw in JPEG and TGA decoders; specially crafted files can cause uninitialized or adjacent memory contents to appear in the resulting image output buffer. CVSS 3.1: AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:N/A:N. | 2.1.8, 3.1.4 | [GHSA-5x7m-6737-26cr](https://github.com/advisories/GHSA-5x7m-6737-26cr) |
| CVE-2024-41131 / GHSA-63p8-c4ww-9cg7 | High | Out-of-bounds write in the GIF decoder triggered by specially crafted GIF files; causes a crash / denial of service. CVSS 3.1: AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H. | 2.1.9, 3.1.5 | [GHSA-63p8-c4ww-9cg7](https://github.com/advisories/GHSA-63p8-c4ww-9cg7) |
| CVE-2024-41132 / GHSA-qxrv-gp6x-rc23 | Moderate | Excessive memory allocation in the GIF decoder triggered by specially crafted GIF files; enables process-memory exhaustion denial of service. Workaround: call `Image.Identify` before `Image.Decode(Async)` to enforce dimension limits. CVSS 3.1: AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L. | 2.1.9, 3.1.5 | [GHSA-qxrv-gp6x-rc23](https://github.com/advisories/GHSA-qxrv-gp6x-rc23) |
| CVE-2025-27598 / GHSA-2cmq-823j-5qj8 | High | Out-of-bounds write in the GIF decoder triggered by specially crafted GIF files; causes a crash / denial of service. CVSS 3.1: AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H. | 2.1.10, 3.1.7 | [GHSA-2cmq-823j-5qj8](https://github.com/advisories/GHSA-2cmq-823j-5qj8) |
| CVE-2025-54575 / GHSA-rxmq-m78w-7wmc | Moderate | Infinite loop in the GIF decoder when parsing a GIF file with a missing block terminator in a comment extension block; causes CPU-exhaustion denial of service. CVSS 3.1: AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L. | 2.1.11, 3.1.11 | [GHSA-rxmq-m78w-7wmc](https://github.com/advisories/GHSA-rxmq-m78w-7wmc) |

## Security Posture Notes

SixLabors.ImageSharp is a fully managed cross-platform .NET image processing library with ~273M total NuGet downloads, widely used in web applications, media pipelines, cloud functions, and content-management systems that process user-supplied image files.

Three recurring advisory themes stand out:

- **GIF decoder fragility** — four of seven advisories (CVE-2024-41131, CVE-2024-41132, CVE-2025-27598, CVE-2025-54575) target the GIF decoder across out-of-bounds writes, excessive memory allocation, and an infinite loop on malformed block structures. The GIF format's variable-length sub-block design appears to be the persistent source of parser fragility.
- **Memory safety in managed code** — use-after-free (PNG, CVE-2024-27929) and uninitialized-memory disclosure (JPEG/TGA, CVE-2024-32036) demonstrate that the .NET managed runtime has not fully eliminated unsafe memory-handling patterns in hot decoder paths that use `unsafe` blocks for performance.
- **Network-reachable DoS** — all DoS advisories carry `AV:N` in their CVSS vector, meaning any application that processes remotely supplied image files is directly in the attack path.

Both 2.x and 3.x branches received patches for all advisories; the current actively developed line is 4.x. Versions before 2.1.11 / 3.1.11 carry unpatched vulnerabilities. The project uses GitHub Security Advisories for disclosure and has maintained a prompt patch cadence.

## Dependencies of Note

- The library is primarily managed C# code; no native binary dependencies are bundled.

## Open Questions

- Confirm whether SixLabors.ImageSharp 4.x has received any security fixes not yet reflected in public GHSA records (no 4.x-specific GHSA found in this pass).
- Investigate whether the GIF decoder OOB-write and infinite-loop pattern reflects a shared root cause in the LZW decompressor or the block-structure parser.
- Assess exposure for Azure Functions / AWS Lambda deployments using ImageSharp for thumbnail generation where image source is user-controlled.

## Related Pages

- [[dotnet/index]]

---
*Last updated: 2026-06-20 | Sources: 7 (github/advisory-database via raw.githubusercontent.com, NuGet gallery)*
