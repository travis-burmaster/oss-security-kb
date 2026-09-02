# BIND 9 (linux)

**Registry:** distro
**Weekly Downloads:** unknown
**Repository:** https://github.com/isc-projects/bind9
**Security Contact:** security-officer@isc.org
**Disclosure Policy:** https://kb.isc.org/docs/aa-00913
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-5946 | High CVSS 9.1 AV:N | DNS non-Internet class assertion failures — specially crafted queries via recursion, dynamic updates, zone notifications, or specific record types trigger assertion failures terminating named | 9.18.49 / 9.20.23 / 9.21.22 | [GHSA-cqgq-ff3f-rj7r](https://github.com/advisories/GHSA-cqgq-ff3f-rj7r) |
| CVE-2026-3104 | High CVSS 9.1 AV:N | Memory leak via crafted domain — recursive resolver leaks memory per query on specially crafted domain names, enabling remote OOM DoS; affects 9.20.x and 9.21.x only | 9.20.21 / 9.21.20 | [GHSA-vwv5-298p-pw28](https://github.com/advisories/GHSA-vwv5-298p-pw28) |
| CVE-2026-3039 | High CVSS 7.5 AV:N | TKEY/GSS-API memory exhaustion — maliciously crafted GSS-API token packets cause per-packet memory allocation without release in TKEY-based authentication paths; primarily affects Active Directory–integrated and Kerberos-secured DNS deployments | 9.18.49 / 9.20.23 / 9.21.22 | [GHSA-p65f-mhrm-vhrc](https://github.com/advisories/GHSA-p65f-mhrm-vhrc) |
| CVE-2026-13204 | High CVSS 7.5 AV:N | DNSSEC provably-insecure assertion DoS — named terminates when a provably insecure domain is covered by both NSEC and NSEC3 records with an RRSIG for only one of those types (CWE-617) | 9.20.26 / 9.21.24 | [GHSA-89q8-qc36-7m58](https://github.com/advisories/GHSA-89q8-qc36-7m58) |
| CVE-2026-11605 | High CVSS 7.5 AV:N | DNSSEC excessive RRSIG validation CPU exhaustion — BIND validates all RRSIG records in an answer even when unnecessary; adversary-controlled resolver response triggers disproportionate CPU consumption | 9.20.26 / 9.21.24 | [GHSA-qhh7-j7w3-xfxq](https://github.com/advisories/GHSA-qhh7-j7w3-xfxq) |
| CVE-2026-11331 | High AV:N | RPZ wildcard CNAME NAMETOOLONG crash/bypass — crafted long query names trigger an unhandled NAMETOOLONG error during RPZ wildcard CNAME processing, potentially bypassing RPZ rules and terminating named (CWE-790) | 9.20.26 / 9.21.24 | [GHSA-8p39-mp4q-99c8](https://github.com/advisories/GHSA-8p39-mp4q-99c8) |
| CVE-2026-3592 | Moderate AV:N | Resolver resource exhaustion via crafted zones — specially crafted DNS zones cause the recursive resolver to consume disproportionate resources | 9.18.49 / 9.20.23 / 9.21.22 | [GHSA-63mj-2fw3-4w3h](https://github.com/advisories/GHSA-63mj-2fw3-4w3h) |
| CVE-2026-10723 | Moderate AV:N | NSEC3 NXDOMAIN forgery (DNSSEC integrity bypass) — BIND accepts incorrect child-zone NSEC3 records as valid, allowing an attacker to forge authenticated NXDOMAIN responses | 9.20.26 / 9.21.24 | [GHSA-4fw4-hmvf-4www](https://github.com/advisories/GHSA-4fw4-hmvf-4www) |

## Security Posture Notes

BIND 9 (`named`) is the world's most widely deployed DNS server software, maintained by ISC (Internet Systems Consortium). Packaged as `bind9` in Debian/Ubuntu, `bind` in RHEL/Fedora/CentOS family distributions, and `bind` in Alpine. Current ESV (Extended Support Version) is 9.20.x; development track is 9.21.x. BIND 9.18.x and 9.16.x are end-of-life.

ISC publishes security advisories at [kb.isc.org](https://kb.isc.org/docs/aa-00913) going back to the late 1990s. The GHSA records captured in this pass cover 8 confirmed advisories from early 2026, representing only the tip of BIND's historical advisory archive. ISC coordinates disclosures and ships fixes across all actively supported branches simultaneously.

**2026 advisory pattern:** The eight 2026 CVEs cluster into three categories:
1. **Assertion failures via crafted input** (CVE-2026-5946, CVE-2026-11331, CVE-2026-13204) — non-Internet class queries, RPZ edge cases, and DNSSEC corner cases crash named with no authentication required.
2. **Memory exhaustion** (CVE-2026-3039, CVE-2026-3104, CVE-2026-3592) — resolver and TKEY paths leak or exhaust memory on adversary-supplied input.
3. **DNSSEC CPU exhaustion and integrity bypass** (CVE-2026-11605, CVE-2026-10723) — BIND's eagerness to validate all RRSIG records creates CPU-exhaustion vectors; NSEC3 acceptance flaw allows NXDOMAIN forgery.

Running an authoritative-only server (`recursion no;`) significantly reduces exposure to resolver-side DoS advisories. Disabling TKEY eliminates the GSS-API attack surface (CVE-2026-3039) if Active Directory DNS is not in use.

## Dependencies of Note

- **OpenSSL / LibreSSL** — DNSSEC signing and TSIG HMAC operations; distro OpenSSL CVEs can affect BIND if OpenSSL is not patched (see [[linux/openssl]])
- **Kerberos / GSSAPI (optional)** — TKEY-based GSS-API authentication path affected by CVE-2026-3039; disable TKEY if not using Active Directory DNS

## Open Questions

- ISC advisory archive pre-2026 not yet mapped; historically includes critical assertion-failure, buffer-overflow, and memory-corruption advisories going back to the BIND 9.2 era.
- Impact of BIND 9.18.x reaching EOL on distros still shipping it (Debian stable, Ubuntu LTS) needs ongoing monitoring.
- BIND Supported Preview Edition (BIND 9.xx-S1) advisory variants not individually differentiated; the -S1 affected-version ranges are noted per advisory.

## Related Pages

- [[linux/openssl]] — DNSSEC crypto dependency
- [[kubernetes/coredns]] — alternative DNS server used by default in Kubernetes
- [[linux/index]]

---
*Last updated: 2026-09-02 | Sources: 8 (GHSA)*
