# Homebrew Index

## Seed Pages
- [[homebrew/openssl@3]] — cryptographic foundation formula and common transitive dependency for TLS-enabled tooling on macOS

- [[homebrew/git]] — developer VCS formula tracking upstream git-scm.com · advisory mapped · 7 CVEs including Critical macOS-affecting CVE-2024-32002 (submodule+symlink hook execution on case-insensitive FS)
- [[homebrew/wget]] — GNU Wget CLI download tool · advisory mapped · CVE-2024-38428 (Critical CVSS 9.1: semicolon userinfo mishandling enabling SSRF/credential exposure, fixed ≥ 1.25.0) and CVE-2016-4971 (High CVSS 8.8: HTTP-to-FTP redirect arbitrary file write, fixed ≥ 1.18)
- [[homebrew/curl]] — upstream curl formula tracking curl releases for macOS · advisory mapped · 6 CVEs through CVE-2025-0167 cross-referenced from linux/curl; SOCKS5 heap overflow (CVE-2023-38545 High), UAF in CERTINFO, OCSP stapling bypass (GnuTLS backend), and credential exposure fixed through curl ≥ 8.12.0

## Future Targets
- `sqlite` — embedded database dependency used by many local tools
- `git-lfs` — Git Large File Storage; separate CVE history from upstream git
