# Homebrew Index

## Seed Pages
- [[homebrew/openssl@3]] — cryptographic foundation formula and common transitive dependency for TLS-enabled tooling on macOS

- [[homebrew/curl]] — URL transfer CLI/library formula · advisory mapped · 6 upstream CVEs through CVE-2025-0167 including High CVE-2023-38545 SOCKS5 heap overflow; Homebrew uses OpenSSL backend (not macOS system LibreSSL); tracks upstream closely with ~1-2 day patch lag
- [[homebrew/git]] — developer VCS formula tracking upstream git-scm.com · advisory mapped · 7 CVEs including Critical macOS-affecting CVE-2024-32002 (submodule+symlink hook execution on case-insensitive FS)
- [[homebrew/imagemagick]] — image-processing formula · advisory mapped · 4 representative advisories from 698+ CVE history: ImageTragick CVE-2016-3714 (High RCE via shell-metachar delegate injection, CISA KEV), CVE-2022-44268 (High PNG arbitrary file read), CVE-2023-34151 (High SVG/MVG integer overflow), CVE-2026-61857 (Moderate XMP heap UAF crash); fixed in ≥ 7.1.2-26
- [[homebrew/wget]] — GNU Wget CLI download tool · advisory mapped · CVE-2024-38428 (Critical CVSS 9.1: semicolon userinfo mishandling enabling SSRF/credential exposure, fixed ≥ 1.25.0) and CVE-2016-4971 (High CVSS 8.8: HTTP-to-FTP redirect arbitrary file write, fixed ≥ 1.18)

- [[homebrew/ffmpeg]] — multimedia codec/processing framework · advisory mapped · 4 representative advisories from 700+ CVE history: PNM heap overflow (CVE-2024-7055 Medium, fixed 7.0.2), audio resampler heap overflow (CVE-2024-7272 Medium, fixed 5.1.6/6.0+), HLS M3U8 concat/subfile arbitrary file read (CVE-2016-1897/1898 Moderate); current formula 8.1.2

- [[homebrew/sqlite]] — embedded database C library formula · advisory mapped · CVE-2022-35737 (High CVSS 9.1: printf array-bounds overflow, fixed upstream 3.39.2) and CVE-2025-6965 (High CVSS 9.8: aggregate function memory corruption, fixed upstream 3.50.2); macOS system SQLite lags independently
- [[homebrew/gnupg]] — GNU Privacy Guard OpenPGP implementation · advisory mapped · 4 advisories: CVE-2018-9234 (High: missing offline-master-key enforcement, design limitation), CVE-2019-13050 (High CVSS 9.0: SKS keyserver certificate-flood DoS, no patch; mitigate by switching keyserver), CVE-2021-40528 (Moderate: Libgcrypt ElGamal plaintext recovery, fixed Libgcrypt 1.9.4), CVE-2022-34903 (Moderate: GPGME status-line signature forgery, fixed GnuPG 2.3.7/2.2.36)

- [[homebrew/python]] — Homebrew Python formula tracking upstream CPython · advisory mapped · 6 confirmed GHSA advisories 2024–2026: CVE-2026-11940 (High: tarfile hardlink→symlink path traversal, incomplete fix for CVE-2025-4330), CVE-2024-12254 (High: asyncio writelines() OOM on 3.12+), CVE-2026-4519 (Moderate: webbrowser.open() leading-dash CLI injection), CVE-2026-3446 (Moderate: base64 silent malformed-data truncation), CVE-2024-3219 (Medium: socket.socketpair() race on Windows), CVE-2026-18503 (Low: csv.Sniffer ReDoS); formula tracks CPython with 1–3 day patch lag; 138 total GHSA records not yet fully mapped

## Future Targets
- `git-lfs` — Git Large File Storage; separate CVE history from upstream git
