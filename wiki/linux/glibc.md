# glibc (Linux)

**Registry:** distro
**Weekly Downloads:** unknown (system library distributed via OS package managers; not tracked through a single registry)
**Repository:** https://sourceware.org/git/?p=glibc.git (mirror: https://github.com/bminor/glibc)
**Security Contact:** security@sourceware.org
**Disclosure Policy:** https://sourceware.org/glibc/wiki/Security%20Exceptions
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

The GNU C Library (`glibc`) underpins virtually all Linux systems. CVEs affect the upstream library and are then backported by downstream distributions (RHEL, Debian, Ubuntu, Fedora, SUSE, etc.). Fixed versions below refer to upstream glibc releases; distro-specific backport status varies. Current upstream stable: glibc 2.43 (released 2026-01-23).

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2015-0235 / GHSA-jwcp-p679-fcr4 ("GHOST") | Critical (CVSS:2.0 10.0) | Heap buffer overflow in `__nss_hostname_digits_dots` reachable via `gethostbyname` / `gethostbyname2`; allows remote code execution from any application calling these functions with attacker-controlled input; present since glibc 2.2 (Nov 2000), patch committed upstream in 2013 but not backported by distros before disclosure | glibc ≥ 2.18 | [GHSA-jwcp-p679-fcr4](https://github.com/advisories/GHSA-jwcp-p679-fcr4) |
| CVE-2015-7547 / GHSA-5xr7-h7cp-w9pc | High (CVSS:3.0 8.1) | Stack-based buffer overflow in `send_dg` and `send_vc` inside `libresolv` triggered by `getaddrinfo` with `AF_UNSPEC` or `AF_INET6`; glibc allocates 2048 bytes on the stack for DNS answers and overflows it when a crafted DNS response exceeds this; allows remote RCE or crash via a malicious DNS server; affects ssh, sudo, curl and any application calling `getaddrinfo` | glibc ≥ 2.23 | [GHSA-5xr7-h7cp-w9pc](https://github.com/advisories/GHSA-5xr7-h7cp-w9pc) |
| CVE-2021-3326 / GHSA-w279-vhxx-7qx8 | High (CVSS:3.1 7.5) | `iconv` hits an assertion failure and aborts the calling process when processing invalid input sequences in the `ISO-2022-JP-3` charset; reachable from any application that calls `iconv` on untrusted input with this encoding | upstream patch commit `7d88c61` | [GHSA-w279-vhxx-7qx8](https://github.com/advisories/GHSA-w279-vhxx-7qx8) |
| CVE-2021-33574 / GHSA-rx5m-j84j-22pg | Critical (CVSS:3.1 9.8, NVD; disputed — distros rate lower) | `mq_notify` use-after-free: the function may dereference notification thread attributes from its `struct sigevent` parameter after the caller has already freed that object, leading to crash or potential code execution; severity is disputed — Amazon Linux, Ubuntu, and Red Hat rate it as Low/Medium given practical exploit prerequisites | upstream bugzilla #27896 | [GHSA-rx5m-j84j-22pg](https://github.com/advisories/GHSA-rx5m-j84j-22pg) |
| CVE-2023-4911 / GHSA-m77w-6vjw-wh2f ("Looney Tunables") | High (CVSS:3.1 7.8 — local LPE) | Buffer overflow in `ld.so` dynamic loader while parsing the `GLIBC_TUNABLES` environment variable; allows a local user to execute code with elevated privileges when launching a SUID binary; in CISA Known Exploited Vulnerabilities catalog; affects glibc ≈ 2.34–2.38 | distro patches released 2023-10-03 (RHEL, Debian, Ubuntu, Fedora) | [GHSA-m77w-6vjw-wh2f](https://github.com/advisories/GHSA-m77w-6vjw-wh2f) |
| CVE-2025-0577 / GHSA-7qhw-4fcq-2g37 | Moderate (CVSS:3.1 5.4) | Insufficient entropy: `getrandom` and `arc4random` family functions may return predictable values if called after `fork` when another thread is concurrently inside one of these functions; affects programs that fork while RNG state is being initialized; affected and fixed versions not enumerated in the advisory | see advisory | [GHSA-7qhw-4fcq-2g37](https://github.com/advisories/GHSA-7qhw-4fcq-2g37) |

## Security Posture Notes

glibc is the foundational C library shipped on virtually all Linux distributions; every process on a standard Linux system links against it. Vulnerabilities in functions like `getaddrinfo` (CVE-2015-7547) or `gethostbyname` (CVE-2015-0235 GHOST) therefore have near-universal blast radius across languages and runtimes — Go, Python, Java, and Rust programs making DNS calls are all affected if the underlying system glibc is unpatched.

The upstream project releases advisories via the GNU C Library mailing list (`libc-alpha`) and the sourceware Bugzilla. The current stable release is glibc **2.43** (2026-01-23); distros typically lag several minor releases behind upstream. The Looney Tunables vulnerability (CVE-2023-4911) was added to the CISA KEV catalog, indicating confirmed in-the-wild exploitation.

The `ld.so` dynamic linker surface (demonstrated by Looney Tunables) is a recurring high-value attack target because it runs in privileged context for SUID binaries and processes environment variables before user code executes.

## Dependencies of Note

- All standard C / POSIX system calls on glibc-based Linux go through glibc; no application-level mitigation can prevent exposure to vulnerabilities in foundational libc functions.
- Distro backport lag is the main practical risk factor: upstream glibc may fix an issue in 2.23 while a long-term-support distribution ships a patched 2.17 backport months later.

## Open Questions

- Document CVE-2021-33574 (`mq_notify`) fixed-version across major distros (the upstream fix commit is known but the GHSA advisory does not enumerate patched releases).
- Track CVE-2025-0577 (`getrandom`/`arc4random` entropy) — affected and fixed glibc version ranges are not yet specified in the GHSA advisory; revisit when Red Hat / upstream enumerate them.
- Expand coverage to additional glibc CVEs: CVE-2017-1000366 (stack/heap alias via `LD_LIBRARY_PATH`), CVE-2016-10739 (`getaddrinfo` trailing-character IPv4 bypass).

## Related Pages

- [[linux/openssh]]
- [[linux/sudo]]
- [[linux/index]]

---
*Last updated: 2026-07-03 | Sources: 6*
