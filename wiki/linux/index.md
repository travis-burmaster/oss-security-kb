# Linux Index

## Seed Pages
- [[linux/openssl]] — core cryptographic library with distro-specific packaging but shared upstream vulnerability history
- [[linux/openssh]] — remote access daemon present on virtually all Linux servers · advisory mapped · ssh-agent PKCS#11 RCE, regreSSHion SIGALRM race, Terrapin prefix truncation, and VerifyHostKeyDNS MITM history through 9.9p2
- [[linux/sudo]] — privilege-boundary package · advisory mapped · pwfeedback, Baron Samedit, host-option, and chroot local privilege-escalation history

- [[linux/curl]] — CLI/library URL transfer tool · advisory mapped · SOCKS5 heap overflow, OCSP stapling bypass, use-after-free, and credential/protocol-selection history through CVE-2025-0167
- [[linux/nginx]] — dominant web server and reverse proxy · advisory mapped · range-filter integer overflow, HTTP request smuggling, critical DNS resolver off-by-one, and persistent ngx_http_mp4_module memory-corruption/disclosure cluster through CVE-2024-7347

## Future Targets
- `glibc` — foundational libc with process-wide memory-safety implications
