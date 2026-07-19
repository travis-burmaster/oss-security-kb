# github.com/miekg/dns (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (Go module proxy does not publish download counts); 16,234+ known importers on pkg.go.dev (as of 2026-07-19)
**Repository:** https://github.com/miekg/dns (v1.x); v2 moved to https://codeberg.org/miekg/dns
**Security Contact:** none listed (report via GitHub Issues)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2017-15133 / GHSA-p55x-7x9v-q8m4 | High (CVSS 7.5 / AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) | **TCP connection exhaustion DoS** — Carefully timed TCP packets can block the DNS server from accepting new connections. CWE-400 (Uncontrolled Resource Consumption). No authentication or user interaction required. | 1.0.4 | https://github.com/advisories/GHSA-p55x-7x9v-q8m4 |
| CVE-2018-17419 / GHSA-9jcx-pr2f-qvq5 | High (CVSS 7.5 / AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) | **ParseZone nil pointer dereference DoS** — A parsing error in `setTA()` within `scan_rr.go` causes `dns.ParseZone()` to trigger a nil pointer dereference (segmentation violation), crashing the process. Remotely triggerable via crafted zone-file content. | 1.0.10 | https://github.com/advisories/GHSA-9jcx-pr2f-qvq5 |
| CVE-2019-19794 / GHSA-44r7-7p62-q3fr | Moderate (CVSS ~5.9 / AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N) | **Predictable DNS transaction IDs via math/rand** — The library uses Go's `math/rand` (non-cryptographic) to generate DNS transaction IDs (TXIDs), making them predictable. An attacker with network access can forge DNS responses, enabling DNS cache poisoning and traffic misdirection. CWE-330 / CWE-338 (Use of Insufficiently Random Values). Also affected CoreDNS before 1.6.6. | 1.1.25 | https://github.com/advisories/GHSA-44r7-7p62-q3fr |

## Security Posture Notes

- `github.com/miekg/dns` is the dominant low-level Go DNS library and is a foundational dependency for CoreDNS (the Kubernetes default DNS server), HashiCorp Consul, dnscrypt-proxy, and many other infrastructure components. Its 16,234+ importers give it very wide ecosystem blast radius.
- The package is in maintenance mode at v1.x (no new features, less active development); the author has started a v2 rewrite at codeberg.org/miekg/dns. The v1 branch remains widely deployed and security-relevant.
- Current stable: v1.1.72 (January 22, 2026). The three public advisories span 2017–2019; no further GHSA or OSV records were confirmed for this crate in the 2026-07-19 search pass.
- CVE-2019-19794 (predictable TXIDs) is architecturally significant: DNS libraries without cryptographic randomness for TXIDs are vulnerable to Kaminsky-class attacks even when running over UDP with source-port randomization, because TXID guessing narrows the attack surface dramatically.
- The library implements a wide range of DNS RFCs including DNSSEC (signing, validation, key generation), TSIG, EDNS0 extensions, and 100+ resource record types. The attack surface for parsing is broad; any future zone-file or wire-format parser issues warrant attention.
- No `SECURITY.md` or dedicated security contact is published in the v1 repository. Issue reports are handled via GitHub Issues.

## Dependencies of Note

- `github.com/miekg/dns` is itself low-dependency; the main security-relevant blast-radius flows downstream through CoreDNS (Kubernetes DNS), Consul, and dnscrypt-proxy.
- [[go/go.etcd.io/etcd-v3]] uses etcd's own DNS-based discovery; DNS library security is relevant to etcd cluster bootstrapping in some configurations.

## Open Questions

- Has v2 (codeberg.org/miekg/dns) addressed the disclosure posture and established a `SECURITY.md` / dedicated contact?
- Are there additional advisories or security-relevant issues in v1.1.x beyond the three mapped here (search scope was GitHub Advisory Database; OSV blocked)?
- Does the CoreDNS project maintain a separate disclosure and advisory process that would surface miekg/dns-layer issues under CoreDNS CVEs rather than package-level advisories?

## Related Pages

- [[go/golang.org-x-crypto]]
- [[go/index]]

---
*Last updated: 2026-07-19 | Sources: 3 (GHSA-p55x-7x9v-q8m4, GHSA-9jcx-pr2f-qvq5, GHSA-44r7-7p62-q3fr via github/advisory-database; pkg.go.dev module metadata)*
