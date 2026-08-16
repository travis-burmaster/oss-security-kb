# Homebrew Index

## Seed Pages
- [[homebrew/openssl@3]] — cryptographic foundation formula and common transitive dependency for TLS-enabled tooling on macOS

- [[homebrew/curl]] — URL transfer CLI/library formula · advisory mapped · 6 upstream CVEs through CVE-2025-0167 including High CVE-2023-38545 SOCKS5 heap overflow; Homebrew uses OpenSSL backend (not macOS system LibreSSL); tracks upstream closely with ~1-2 day patch lag
- [[homebrew/git]] — developer VCS formula tracking upstream git-scm.com · advisory mapped · 7 CVEs including Critical macOS-affecting CVE-2024-32002 (submodule+symlink hook execution on case-insensitive FS)
- [[homebrew/imagemagick]] — image-processing formula · advisory mapped · 4 representative advisories from 698+ CVE history: ImageTragick CVE-2016-3714 (High RCE via shell-metachar delegate injection, CISA KEV), CVE-2022-44268 (High PNG arbitrary file read), CVE-2023-34151 (High SVG/MVG integer overflow), CVE-2026-61857 (Moderate XMP heap UAF crash); fixed in ≥ 7.1.2-26
- [[homebrew/wget]] — GNU Wget CLI download tool · advisory mapped · CVE-2024-38428 (Critical CVSS 9.1: semicolon userinfo mishandling enabling SSRF/credential exposure, fixed ≥ 1.25.0) and CVE-2016-4971 (High CVSS 8.8: HTTP-to-FTP redirect arbitrary file write, fixed ≥ 1.18)

- [[homebrew/ffmpeg]] — multimedia codec/processing framework · advisory mapped · 4 representative advisories from 700+ CVE history: PNM heap overflow (CVE-2024-7055 Medium, fixed 7.0.2), audio resampler heap overflow (CVE-2024-7272 Medium, fixed 5.1.6/6.0+), HLS M3U8 concat/subfile arbitrary file read (CVE-2016-1897/1898 Moderate); current formula 8.1.2

- [[homebrew/sqlite]] — embedded database C library formula · advisory mapped · CVE-2022-35737 (High CVSS 9.1: printf array-bounds overflow, fixed upstream 3.39.2) and CVE-2025-6965 (High CVSS 9.8: aggregate function memory corruption, fixed upstream 3.50.2); macOS system SQLite lags independently

- [[homebrew/gnupg]] — GNU Privacy Guard (OpenPGP) formula · advisory mapped · 4 CVEs 2019–2025: SHA-1 signature forgery (CVE-2019-14855 Moderate, fixed 2.2.18), signature spoofing via injected key (CVE-2022-34903 Moderate, fixed 2.3.8), form-feed signature bypass (CVE-2025-68972 Moderate, affects through 2.4.8), armor.c memcpy issue (CVE-2025-68973 High, fixed 2.2.51 LTS / 2.5.x); current formula 2.5.21

## Future Targets
- `git-lfs` — Git Large File Storage; separate CVE history from upstream git
