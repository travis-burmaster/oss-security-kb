# Homebrew Index

## Seed Pages
- [[homebrew/openssl@3]] — cryptographic foundation formula and common transitive dependency for TLS-enabled tooling on macOS

- [[homebrew/curl]] — URL transfer CLI/library formula · advisory mapped · 6 upstream CVEs through CVE-2025-0167 including High CVE-2023-38545 SOCKS5 heap overflow; Homebrew uses OpenSSL backend (not macOS system LibreSSL); tracks upstream closely with ~1-2 day patch lag
- [[homebrew/git]] — developer VCS formula tracking upstream git-scm.com · advisory mapped · 7 CVEs including Critical macOS-affecting CVE-2024-32002 (submodule+symlink hook execution on case-insensitive FS)
- [[homebrew/imagemagick]] — image-processing formula · advisory mapped · 4 representative advisories from 698+ CVE history: ImageTragick CVE-2016-3714 (High RCE via shell-metachar delegate injection, CISA KEV), CVE-2022-44268 (High PNG arbitrary file read), CVE-2023-34151 (High SVG/MVG integer overflow), CVE-2026-61857 (Moderate XMP heap UAF crash); fixed in ≥ 7.1.2-26
- [[homebrew/wget]] — GNU Wget CLI download tool · advisory mapped · CVE-2024-38428 (Critical CVSS 9.1: semicolon userinfo mishandling enabling SSRF/credential exposure, fixed ≥ 1.25.0) and CVE-2016-4971 (High CVSS 8.8: HTTP-to-FTP redirect arbitrary file write, fixed ≥ 1.18)

## Future Targets
- `sqlite` — embedded database dependency used by many local tools
- `git-lfs` — Git Large File Storage; separate CVE history from upstream git
