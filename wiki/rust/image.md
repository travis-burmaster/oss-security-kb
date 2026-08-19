# image (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~3.3M/week est. (as of 2026-08-19; 42.6M/90-day; 170M total)
**Repository:** https://github.com/image-rs/image
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-16138 / RUSTSEC-2019-0014 / GHSA-m2pf-hprp-3vqm | Critical (CVSS 3.1: 9.8 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Flaw in interface may drop uninitialized instance of arbitrary types: `HDRDecoder::read_image_transform` calls `Vec::set_len` on an uninitialized vector with a user-controlled type parameter. If any code between `set_len` and full initialization panics, `Drop` runs on uninitialized memory — equivalent to use-after-free — potentially enabling arbitrary code execution via a crafted HDR image. Affects versions 0.10.2–0.21.2. | 0.21.3 (0.22+ introduces a safe pre-allocated-buffer interface that removes the unsafe code path entirely) | [RUSTSEC-2019-0014](https://rustsec.org/advisories/RUSTSEC-2019-0014.html) / [GHSA-m2pf-hprp-3vqm](https://github.com/advisories/GHSA-m2pf-hprp-3vqm) |
| CVE-2020-35916 / RUSTSEC-2020-0073 / GHSA-9wgh-vjj7-7433 | Moderate (CVSS 3.1: 7.1) | Mutable reference constructed from `slice::as_ptr` instead of `slice::as_mut_ptr` in six pixel-type conversion methods (`Bgr`, `Bgra`, `Luma`, `LumaA`, `Rgb`, `Rgba`): a pointer obtained from `as_ptr()` (shared / immutable provenance) was dereferenced to create a `&mut T`, producing aliased mutable references — undefined behaviour per Rust's aliasing rules. Maintainers found no evidence of miscompilation in practice; unoptimized LLVM IR was confirmed not to contain observable UB. | 0.23.12 | [RUSTSEC-2020-0073](https://rustsec.org/advisories/RUSTSEC-2020-0073.html) / [GHSA-9wgh-vjj7-7433](https://github.com/advisories/GHSA-9wgh-vjj7-7433) |

## Security Posture Notes

`image` is the dominant Rust image encoding/decoding library, supporting PNG, JPEG, GIF, BMP, TIFF, WebP, TGA, ICO, HDR, and more. It is maintained by the `image-rs` organization and is a ubiquitous transitive dependency in graphics, game, media, and machine-learning tooling.

Both advisories are fixed; current stable 0.25.10 is unaffected by both. The 2019 advisory (RUSTSEC-2019-0014) is the higher-severity finding: processing attacker-supplied HDR images with a version before 0.21.3 creates a code-execution risk. The 0.22.x release introduced a breaking but safer interface to eliminate the unsafe code path.

**Companion crate `imageproc`** (image processing algorithms built on top of `image`) has 3 Moderate advisories published in May 2026:
- RUSTSEC-2026-0115 / GHSA-5qv7-j6w5-fr4m: fragile bounds check in pixel-sampling allows integer-overflow bypass (OOB read); fixed imageproc 0.23.1 / 0.24.1 / 0.25.1 / 0.26.2
- RUSTSEC-2026-0116 / GHSA-w5p8-4jcx-2j6r: integer overflow in kernel size check leads to OOB read in unsafe code; same fix versions
- RUSTSEC-2026-0117 / GHSA-qg8r-f7x3-25f7: OOB read via NaN coordinates in bilinear/bicubic sampling (NaN passes a floating-point bounds check that should have rejected it); same fix versions

These affect `imageproc`, not `image` itself, and are noted here as dependency context for projects using both crates.

## Dependencies of Note

- `imageproc` — companion image-processing library with 3 Moderate OOB-read advisories from 2026 (RUSTSEC-2026-0115/0116/0117); not yet a separate wiki page.

## Open Questions

- Are there additional memory-safety issues in other format decoders (TIFF, JPEG, WebP) not yet publicly disclosed?
- `imageproc` RUSTSEC-2026-0115/0116/0117 warrant a dedicated page.

## Related Pages

- [[rust/index]]

---
*Last updated: 2026-08-19 | Sources: 4 (RUSTSEC-2019-0014, RUSTSEC-2020-0073, GHSA-m2pf-hprp-3vqm, GHSA-9wgh-vjj7-7433)*
