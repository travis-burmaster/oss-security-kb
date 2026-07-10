# Linux Index

## Seed Pages
- [[linux/openssl]] — core cryptographic library with distro-specific packaging but shared upstream vulnerability history
- [[linux/openssh]] — remote access daemon present on virtually all Linux servers · advisory mapped · ssh-agent PKCS#11 RCE, regreSSHion SIGALRM race, Terrapin prefix truncation, and VerifyHostKeyDNS MITM history through 9.9p2

- [[linux/bash]] — GNU Bourne-Again SHell · advisory mapped · ShellShock cluster (CVE-2014-6271 Critical CVSS 9.8 and 3 incomplete-fix follow-ons through bash43-028) plus heap-buffer overflow in parameter_transform.c (CVE-2022-3715 Critical CVSS 9.8); fixed through bash 5.2
- [[linux/curl]] — CLI/library URL transfer tool · advisory mapped · SOCKS5 heap overflow, OCSP stapling bypass, use-after-free, and credential/protocol-selection history through CVE-2025-0167
- [[linux/glibc]] — GNU C Library · advisory mapped · GHOST heap overflow (CVE-2015-0235 Critical), getaddrinfo stack overflow (CVE-2015-7547 High), iconv assertion abort, mq_notify UAF, Looney Tunables ld.so LPE in CISA KEV (CVE-2023-4911 High), and 2026 getrandom entropy flaw
- [[linux/nginx]] — dominant web server and reverse proxy · advisory mapped · range-filter integer overflow, HTTP request smuggling, critical DNS resolver off-by-one, and persistent ngx_http_mp4_module memory-corruption/disclosure cluster through CVE-2024-7347
- [[linux/git]] — foundational VCS pre-installed on all Linux systems · advisory mapped · two Critical RCE batches (2023-01, 2024-05), path traversal via git apply, submodule config injection, and case-insensitive FS clone hook execution (CVE-2024-32002)
- [[linux/sudo]] — privilege-boundary package · advisory mapped · pwfeedback, Baron Samedit, host-option, and chroot local privilege-escalation history
- [[linux/cve-2026-31431-copy-fail]] — Linux kernel Copy Fail advisory note · advisory mapped · page-cache write / local privilege escalation discussion from public write-up
- [[linux/systemd]] — system init daemon and service manager · advisory mapped · numeric-username LPE (CVE-2017-1000082 Critical CVSS 9.8), heap UAF in Polkit dbus path (CVE-2020-1712 High), systemd-tmpfiles recursion DoS (CVE-2021-3997), and systemctl+less pager LPE (CVE-2023-26604 High CVSS 7.8); 6 advisories
