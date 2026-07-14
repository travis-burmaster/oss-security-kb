# imagemagick (Homebrew)

**Registry:** Homebrew
**Weekly Downloads:** unknown (formulae.brew.sh API blocked in this environment; ImageMagick is one of the most-installed image-processing tools via Homebrew, widely used in macOS development environments)
**Repository:** https://github.com/ImageMagick/ImageMagick
**Security Contact:** GitHub security advisories (https://github.com/ImageMagick/ImageMagick/security)
**Disclosure Policy:** https://github.com/ImageMagick/ImageMagick/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No public proactive audits on record for the Homebrew formula specifically.*

## Known Vulnerabilities

ImageMagick has one of the largest CVE histories of any open-source image-processing library — 698+ entries in the GitHub Advisory Database as of 2026-07-14, the majority arising from legacy image coders and parser edge cases. The rows below document the most security-significant advisories: the original remote code execution cluster (ImageTragick, CISA KEV), a notable 2022 information-disclosure finding, a 2023 recurring integer-overflow class, and the most recent 2026 advisory.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2016-3714 / GHSA-24cp-26gx-3pp4 | **High** (CVSS:3.0 7.8 AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H; CISA KEV) | ImageTragick: EPHEMERAL, HTTPS, MVG, MSL, TEXT, SHOW, WIN, and PLT coders pass shell metacharacters from attacker-controlled image input to `popen()` without sanitization, enabling arbitrary OS command execution in the context of the image-processing service. Widely exploited against web upload pipelines. Metasploit module available. CISA Known Exploited Vulnerability. | ImageMagick ≥ 6.9.3-10, ≥ 7.0.1-1 (May 2016) | [GHSA-24cp-26gx-3pp4](https://github.com/advisories/GHSA-24cp-26gx-3pp4) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-3714) |
| CVE-2022-44268 / GHSA-g5qh-f5rv-grcp | **High** (CVSS:3.1 7.5 AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N) | PNG parse-time arbitrary file read (CWE-200): when ImageMagick processes a PNG image containing a `tEXt` chunk referencing an absolute file path, it embeds the content of that file in the output image. An attacker who can influence the PNG input to an image-processing service (e.g., a resize endpoint) can exfiltrate arbitrary files readable by the process (e.g., `/etc/passwd`, application secrets). Affects 7.1.0-49; demonstrated publicly by Metabaseq. | upstream releases following 7.1.0-49 (see NVD) | [GHSA-g5qh-f5rv-grcp](https://github.com/advisories/GHSA-g5qh-f5rv-grcp) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-44268) |
| CVE-2023-34151 / GHSA-cm6m-2vvh-cxc6 | **High** (CVSS:3.1 7.1 AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H) | Undefined behavior via integer overflow (CWE-190) when casting `double` to `size_t` in the SVG, MVG, and related coders — a recurring instance of the CVE-2022-32546 class. Can cause memory corruption or process crash when processing untrusted SVG/MVG image files. | upstream releases following 7.1.0-x (see NVD; Red Hat errata RHEL-sourced fix) | [GHSA-cm6m-2vvh-cxc6](https://github.com/advisories/GHSA-cm6m-2vvh-cxc6) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-34151) |
| CVE-2026-61857 / GHSA-84mh-5fq7-7fx5 / GHSA-qh5g-q395-cx4j (upstream) | **Moderate** (CVSS:3.1 AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L) | Heap use-after-free in XMP profile parsing (CWE-252 / CWE-476): a missing null check in the XMP profile parser allows a crafted image with malformed XMP data to trigger a use-after-free, causing an application crash. Availability-only impact; no code execution demonstrated. Affects ImageMagick < 7.1.2-26 and < 6.9.13-51. Disclosed 2026-06-26. | 7.1.2-26, 6.9.13-51 | [GHSA-84mh-5fq7-7fx5](https://github.com/advisories/GHSA-84mh-5fq7-7fx5) · [GHSA-qh5g-q395-cx4j](https://github.com/ImageMagick/ImageMagick/security/advisories/GHSA-qh5g-q395-cx4j) |

## Security Posture Notes

- **Scale of vulnerability history:** ImageMagick processes dozens of image formats through hundreds of format-specific coders. The 698+ GitHub Advisory Database entries are mostly low-to-medium severity memory errors (NULL dereference, heap overflow, use-after-free, memory leak) in obscure format coders triggered by malformed input. The majority are pre-2020 and primarily relevant to services that process untrusted files without sandboxing.
- **ImageTragick (CVE-2016-3714, CISA KEV):** The most operationally impactful ImageMagick advisory ever published. The delegate system that invokes external programs (Ghostscript, cURL, etc.) via shell command strings interpolated user-supplied filenames without escaping. Public exploits exist (Exploit-DB 39767, 39791; Metasploit `unix/fileformat/imagemagick_delegate`). All deployments must be on ≥ 6.9.3-10 or ≥ 7.0.1-1.
- **CVE-2022-44268 (arbitrary file read):** Demonstrated practically by Metabaseq researchers. The `tEXt` chunk file-path embedding is reachable through a standard resize or convert operation on a maliciously crafted PNG — a particularly dangerous path for profile-picture upload services.
- **Homebrew formula context:** The `imagemagick` Homebrew formula tracks upstream releases directly with no formula-specific patches. The formula installs the 7.x branch. macOS applications relying on the Homebrew-installed ImageMagick binary should monitor the formula version against the upstream changelog at https://github.com/ImageMagick/ImageMagick/releases. Homebrew bottle publication typically lags upstream release by 1–2 days.
- **Hardening recommendation:** Services processing untrusted images should (1) run ImageMagick in a restricted sandbox (systemd-nspawn, seccomp, containers with dropped capabilities), (2) apply a restrictive `policy.xml` disabling dangerous coders (HTTPS, MSL, MVG, PS, PDF, XPS, EPHEMERAL), and (3) pin to the latest 7.1.x release. The default Homebrew installation does not apply `policy.xml` restrictions.

## Dependencies of Note

- **Homebrew `ghostscript` formula** — ImageMagick invokes Ghostscript for PDF/PS processing via the delegate mechanism. Multiple CVEs in the ImageTragick era involved Ghostscript delegate command injection.
- Applications using the `MagickCore` or `MagickWand` C APIs embed the full coder surface and inherit the entire CVE history.

## Open Questions

- What is the current Homebrew formula bottle version, and does it track ≥ 7.1.2-26 (CVE-2026-61857 fix)?
- Does the Homebrew `imagemagick` formula ship with a restrictive `policy.xml` or is the default configuration permissive?
- Are there additional 2024–2026 GitHub-reviewed advisories in the ImageMagick security advisory space beyond the unreviewed GHSA set?
- Should a dedicated Linux page (`linux/imagemagick` or via distro packages) be created to track distribution-specific patch lag?

## Related Pages

- [[homebrew/curl]]
- [[homebrew/git]]
- [[linux/curl]]
- [[homebrew/index]]

---
*Last updated: 2026-07-14 | Sources: 4 (GHSA-24cp-26gx-3pp4 / CVE-2016-3714, GHSA-g5qh-f5rv-grcp / CVE-2022-44268, GHSA-cm6m-2vvh-cxc6 / CVE-2023-34151, GHSA-84mh-5fq7-7fx5 / CVE-2026-61857)*
