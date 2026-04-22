# sharp (npm)

**Registry:** npm
**Weekly Downloads:** ~56,858,420 (last week, fetched 2026-04-22)
**Repository:** https://github.com/lovell/sharp
**Security Contact:** maintainer email listed in package metadata / SECURITY.md
**Disclosure Policy:** latest npm release supported for security updates; upstream SECURITY.md says genuine reports should receive a response within 48 hours
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-22 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev package query, GitHub Advisory Database / upstream GitHub security advisories, public CVE record, upstream SECURITY.md, fix commits, npm registry metadata, npm downloads API, GitHub tag metadata) | Added a new advisory-mapped baseline page for sharp's currently published package security history, covering the 2022 install-time build-environment command-injection issue and the 2023 libwebp-based WebP decoding exposure fixed in `0.32.6`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-29256 / GHSA-gp95-ppv5-3jc5 | Moderate | Public advisory records describe a possible command-injection path in sharp's **install-time** logic when an attacker can control `PKG_CONFIG_PATH` in the build environment. Upstream explicitly says this is not runtime code, does not affect Windows, and mainly matters when the build environment itself is already under hostile influence. | 0.30.5 | https://github.com/advisories/GHSA-gp95-ppv5-3jc5 |
| CVE-2023-4863 / GHSA-54xq-cgqr-rpm3 | High | Public advisory records say sharp versions before `0.32.6` are exposed through the bundled `libwebp` dependency when decoding untrusted WebP input. Upstream maps the package-level fix to `0.32.6`, which ships `libwebp 1.3.2`, and notes that users of a globally installed `libvips` need that stack patched independently. | 0.32.6 | https://github.com/advisories/GHSA-54xq-cgqr-rpm3 |

## Security Posture Notes

- `sharp` has a **small but important public package-advisory history** in this pass: one install-time build-environment issue and one runtime exposure inherited through a bundled native codec dependency.
- The `CVE-2022-29256` advisory is **highly context-dependent**. Public upstream text is unusually clear that the bug lives only in `npm install` logic, is not a runtime bug, does not affect Windows, and requires attacker influence over the build environment variable `PKG_CONFIG_PATH`.
- The `CVE-2023-4863` record matters more broadly for ordinary consumers because sharp sits on a native image-decoding boundary. Processing attacker-controlled WebP content on versions before `0.32.6` can inherit the underlying `libwebp` exposure tracked by the upstream advisory chain.
- This package is a good reminder that **npm package risk is not only JavaScript-source risk**. For most users, sharp ships prebuilt native components through `libvips`, so security posture depends partly on bundled third-party codec libraries as well as on the package's own JavaScript and install scripts.
- Upstream's public `SECURITY.md` keeps support policy intentionally narrow: **only the latest npm release is supported with security updates**. Long-pinned older lines should not be assumed to receive backports.
- Current package metadata in this pass shows the package remains extremely widely deployed (`~56.9M` weekly downloads; latest npm tag `0.34.5`), so old image-processing stacks pinned below `0.30.5` or `0.32.6` are still worth cleaning up.

## Recommendations for Developers

1. **Upgrade to the latest supported release**; at minimum, avoid versions below `0.32.6`, and do not remain below `0.30.5` in old build pipelines.
2. **Treat image-decoding dependencies as security-sensitive** when accepting untrusted uploads or remotely supplied images.
3. **Harden CI / build environments** so untrusted actors cannot steer environment variables such as `PKG_CONFIG_PATH` during native package installation.
4. **Audit any globally installed `libvips` path separately**; the upstream package fix for `0.32.6` only solves the bundled-dependency case, while system-library users need patched native dependencies too.
5. **Limit accepted image formats where practical**; upstream's own advisory suggests blocking WebP decoding as a workaround when immediate upgrade paths are constrained.

## Dependencies of Note

- Wraps the native `libvips` image-processing stack and, for many users, ships prebuilt binaries that pull in codec-level risk from dependencies such as `libwebp`.
- Often appears in file-upload, media-processing, avatar, thumbnailing, and CMS pipelines where attacker-controlled content is common.

## Open Questions

- Is there a clean public source that enumerates bundled native-library versions across each sharp release line in a way that is easy to map into future codec-CVE tracking?
- Which major downstream frameworks or starter kits still commonly pin sharp below `0.32.6`?
- Should the KB eventually add a small cluster view for widely deployed media-decoding packages where native dependency exposure matters as much as package-local JavaScript flaws?

## Related Pages

- [[npm/multer]]
- [[npm/body-parser]]
- [[npm/index]]

---
*Last updated: 2026-04-22 | Sources: 8 (OSV.dev package query for npm/sharp, GitHub Advisory Database / upstream GitHub security advisories for GHSA-gp95-ppv5-3jc5 and GHSA-54xq-cgqr-rpm3, public CVE / NVD record for CVE-2022-29256, upstream SECURITY.md, upstream fix commits, npm registry metadata, npm downloads API, GitHub tag metadata for v0.30.5 and v0.32.6)*
