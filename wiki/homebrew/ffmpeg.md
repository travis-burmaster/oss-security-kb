# ffmpeg (Homebrew)

**Registry:** Homebrew
**Weekly Downloads:** unknown (Homebrew analytics blocked; consistently one of the most-installed formulas on macOS; widely used by developers for audio/video processing)
**Repository:** https://github.com/FFmpeg/FFmpeg
**Security Contact:** ffmpeg-security@ffmpeg.org (private list for coordinated disclosure)
**Disclosure Policy:** https://ffmpeg.org/security.html — coordinated disclosure via ffmpeg-security@ffmpeg.org; CVE IDs assigned via MITRE; advisories posted to ffmpeg-devel mailing list
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

FFmpeg is a comprehensive audio/video codec and processing framework written in C. Its codebase spans hundreds of decoder/encoder/muxer/demuxer implementations and has one of the largest CVE histories of any open-source library (700+ NVD entries). The table below maps four representative advisories covering distinct vulnerability classes; for the full history see https://nvd.nist.gov/vuln/search/results?query=FFmpeg and https://ffmpeg.org/security.html.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-7055 / GHSA-5gxm-744m-qfgp | Medium (CVSS:3.1 5.4 AV:N/AC:L/PR:N/UI:R CWE-122) | Heap-based buffer overflow in the PNM image decoder (`pnm_decode_frame` in `libavcodec/pnmdec.c`). Exploitable via a crafted PNM image file; public PoC available. Network-reachable when FFmpeg is used in a server-side media processing pipeline consuming user-supplied files. Affects ≤ 7.0.1. | FFmpeg 7.0.2 | [GHSA-5gxm-744m-qfgp](https://github.com/advisories/GHSA-5gxm-744m-qfgp) |
| CVE-2024-7272 / GHSA-7q2g-j3r8-hgwh | Medium (CVSS:3.1 5.4 AV:N/AC:L/PR:N/UI:R CWE-122) | Heap-based buffer overflow in the audio resampler (`fill_audiodata` in `libswresample/swresample.c`). Exploitable via crafted audio input. Affects ≤ 5.1.5; partially fixed by FFmpeg's branch strategy: 5.1.6 / 6.0 introduced the fix. | FFmpeg 5.1.6 / 6.0+ | [GHSA-7q2g-j3r8-hgwh](https://github.com/advisories/GHSA-7q2g-j3r8-hgwh) |
| CVE-2016-1897 / GHSA-4p87-h585-c5xj | Moderate (CVSS:3.0 AV:L/AC:L/PR:N/UI:R C:H/I:N/A:N) | Arbitrary local file read via the `concat` protocol in an HTTP Live Streaming (HLS) M3U8 playlist: an attacker-controlled M3U8 file can include a `concat://` URL referencing an absolute local file path, causing FFmpeg to read and expose the first line of that file via an outbound HTTP request. Cross-origin / SSRF vector when processing attacker-supplied playlists. Affects FFmpeg 2.x. | FFmpeg ≥ 3.0 (January 2016) | [GHSA-4p87-h585-c5xj](https://github.com/advisories/GHSA-4p87-h585-c5xj) |
| CVE-2016-1898 / GHSA-2mw9-cpc8-cf9f | Moderate (CVSS:3.0 AV:L/AC:L/PR:N/UI:R C:H/I:N/A:N) | Companion to CVE-2016-1897: arbitrary local file read via the `subfile` protocol in an HLS M3U8 playlist, similarly leaking local file content via an outbound HTTP request. Affects FFmpeg 2.x. | FFmpeg ≥ 3.0 (January 2016) | [GHSA-2mw9-cpc8-cf9f](https://github.com/advisories/GHSA-2mw9-cpc8-cf9f) |

## Security Posture Notes

FFmpeg is one of the most widely deployed audio/video processing libraries on macOS developer systems via Homebrew and is embedded as a shared or static dependency in thousands of downstream applications (video editors, streaming servers, transcoding pipelines, browser media engines). Its C codebase with complex parsing logic across 700+ codecs creates an extremely large attack surface.

The dominant historical vulnerability classes are:

1. **Heap/stack buffer overflows** in codec decoders (`libavcodec`) and container demuxers — triggered by crafted media files and represent the majority of 700+ NVD CVEs. Critical findings in this class have historically enabled remote code execution when FFmpeg processes untrusted media server-side.
2. **Information disclosure via protocol abuse** (CVE-2016-1897/1898: `concat`/`subfile` protocols in HLS M3U8 playlists) — relevant when FFmpeg processes user-supplied playlist or container files containing attacker-controlled URLs.
3. **Use-after-free and integer overflows** in format container parsers (MOV, MKV, and similar) — recurring class in older versions.

The Homebrew formula tracks FFmpeg upstream releases. Current formula version: **8.1.2** (as of 2026-07-23). Formula depends on `openssl@3`, `libvpx`, `x264`, `x265`, `dav1d`, `opus`, and other codec libraries that may carry their own advisory histories.

The upstream project maintains a private security mailing list (ffmpeg-security@ffmpeg.org) and a public advisory page at https://ffmpeg.org/security.html. Coordinated disclosure is documented; turnaround varies by issue complexity. No formal bug-bounty program.

## Dependencies of Note

- `openssl@3` (Homebrew dep) — TLS support for HTTPS streams; see [[homebrew/openssl@3]]
- `libvpx`, `x264`, `x265`, `dav1d` — codec libraries bundled with the formula; each may carry their own CVE history not reflected here.
- Applications embedding FFmpeg as a library should track FFmpeg upstream releases and do not automatically receive Homebrew formula updates.

## Open Questions

- Map additional High/Critical advisories from 2022–2026 beyond the four representative entries above; the full NVD/CVE set is too large for a single pass.
- Confirm Homebrew bottle patch lag for CVE-2024-7055 (fixed 7.0.2) and CVE-2024-7272 (fixed 5.1.6/6.0+): determine bottle publication date relative to upstream release date.
- Check https://ffmpeg.org/security.html for any advisories not yet assigned CVEs or not yet in GHSA.
- Assess whether Homebrew analytics (if unblocked in a future pass) confirm download count; ffmpeg is a top-10 formula candidate.

## Related Pages

- [[homebrew/imagemagick]]
- [[homebrew/openssl@3]]
- [[homebrew/index]]

---
*Last updated: 2026-07-23 | Sources: 4*
