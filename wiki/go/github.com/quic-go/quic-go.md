# quic-go (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** ~1,603 importers (as of 2026-09-15)
**Repository:** https://github.com/quic-go/quic-go
**Security Contact:** security@quic-go.net (per SECURITY.md)
**Disclosure Policy:** https://github.com/quic-go/quic-go/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-46239 / GHSA-3q6m-v84f-6p9h | High (CVSS 7.5 AV:N) | Nil pointer dereference during QUIC handshake: sending an ACK frame immediately after the CRYPTO frame that completes handshake negotiation triggers a panic when the library tries to discard the Handshake packet number space. Unauthenticated, completes in one round trip. Affects 0.37.0–0.37.2 only; earlier versions unaffected. | 0.37.3 | [GHSA-3q6m-v84f-6p9h](https://github.com/advisories/GHSA-3q6m-v84f-6p9h) |
| CVE-2023-49295 / GHSA-ppxx-5m9h-6vxf | Moderate | PATH_CHALLENGE memory exhaustion DoS: attacker floods the victim with PATH_CHALLENGE frames while using selective ACKs and RTT manipulation to collapse the victim's congestion window, preventing PATH_RESPONSE frames from draining — unbounded memory growth. No user interaction required. Affects versions before 0.37.7 / 0.38.0–0.38.1 / 0.39.0–0.39.3 / 0.40.0. | 0.37.7 / 0.38.2 / 0.39.4 / 0.40.1 | [GHSA-ppxx-5m9h-6vxf](https://github.com/advisories/GHSA-ppxx-5m9h-6vxf) |
| CVE-2024-22189 / GHSA-c33x-xqrf-c478 | High (CVSS 7.5 AV:N) | NEW_CONNECTION_ID memory exhaustion: attacker sends many NEW_CONNECTION_ID frames forcing the victim to queue RETIRE_CONNECTION_ID responses; simultaneous congestion-window manipulation prevents the response queue from draining — unbounded memory growth. Unauthenticated. Fixed in 0.42.0. | 0.42.0 | [GHSA-c33x-xqrf-c478](https://github.com/advisories/GHSA-c33x-xqrf-c478) |
| CVE-2024-53259 / GHSA-px8v-pp82-rcvr | Moderate (CVSS 7.1 AV:A) | Off-path ICMP Packet Too Big MTU injection on Linux: when `IP_PMTUDISC_DO` is set, an adjacent-network attacker can forge ICMP unreachable packets claiming an artificially small MTU (below QUIC's 1200-byte minimum), disrupting established connections. Workaround: iptables filtering of ICMP unreachable. | 0.48.2 | [GHSA-px8v-pp82-rcvr](https://github.com/advisories/GHSA-px8v-pp82-rcvr) |
| CVE-2025-29785 / GHSA-j972-j939-p2v3 | High (CVSS 7.5 AV:N) | Nil pointer dereference in path probe loss recovery (introduced in 0.50.0): sending valid packets from a different source address initiates path validation; a crafted ACK then panics the loss-recovery path. Affects 0.50.0 only; easily triggerable by any QUIC peer. | 0.50.1 | [GHSA-j972-j939-p2v3](https://github.com/advisories/GHSA-j972-j939-p2v3) |
| CVE-2025-59530 / GHSA-47m2-4cr7-mhcw | High (CVSS 7.5 AV:N) | Premature HANDSHAKE_DONE client crash: a misbehaving QUIC server sends the HANDSHAKE_DONE frame before handshake completion; the client incorrectly discards Handshake keys before Initial keys, triggering an assertion failure / panic. Any server can crash quic-go clients using affected versions. | 0.49.1 / 0.54.1 / 0.55.0 | [GHSA-47m2-4cr7-mhcw](https://github.com/advisories/GHSA-47m2-4cr7-mhcw) |
| CVE-2025-64702 / GHSA-g754-hx8w-x2g6 | Moderate (CVSS 3.1 AV:N) | QPACK static-table header expansion attack: HEADERS frames can expand ~50× encoded size via QPACK static table entries; compressed frame size limits were enforced but decoded field section size limits (required by RFC 9114) were not, enabling memory exhaustion on both HTTP/3 servers and clients with no authentication required. | 0.57.0 | [GHSA-g754-hx8w-x2g6](https://github.com/advisories/GHSA-g754-hx8w-x2g6) |
| CVE-2026-40898 / GHSA-vvgj-x9jq-8cj9 | Moderate (CVSS 5.3 AV:N) | QPACK trailer memory exhaustion: HEADERS frames sent as HTTP/3 trailers bypass decoded field section size limits even though regular HEADERS frames were already bounded (incomplete fix for CVE-2025-64702 root cause); attacker crafts trailer frames with large values to trigger ~50× expansion and memory exhaustion. | 0.59.1 | [GHSA-vvgj-x9jq-8cj9](https://github.com/advisories/GHSA-vvgj-x9jq-8cj9) |

## Security Posture Notes

quic-go is the dominant pure-Go implementation of the QUIC protocol (RFC 9000/9001/9002) and HTTP/3, developed primarily by Marten Seemann under the `quic-go` GitHub organization. It serves as the QUIC transport substrate for projects including Caddy, Traefik (since v2.8.2), and numerous CNCF-adjacent tools; 1,603 pkg.go.dev importers as of 2026-09-15. Current stable: v0.62.0. FIPS 140-3 mode supported with Go 1.26+.

The advisory history shows two recurring vulnerability classes:

1. **Protocol-complexity DoS**: connection ID management (CVE-2024-22189), path validation (CVE-2023-49295, CVE-2025-29785), and QPACK header expansion (CVE-2025-64702, CVE-2026-40898) — all unauthenticated, network-reachable, availability-only impact.
2. **Handshake state-machine panics**: nil pointer dereferences triggered by crafted or out-of-sequence handshake messages (CVE-2023-46239, CVE-2025-59530), reliably crashable with a single connection.

All 8 confirmed advisories result in availability impact only — no confidentiality or integrity impact confirmed on the `github.com/quic-go/quic-go` module directly.

The companion packages `github.com/quic-go/webtransport-go` and `github.com/quic-go/qpack` carry additional advisories not mapped here.

## Dependencies of Note

- `golang.org/x/net` — HTTP/2 upstream; see [[go/golang.org-x-net]]
- `github.com/quic-go/qpack` — QPACK header compression (embedded); security boundary for CVE-2025-64702 / CVE-2026-40898

## Open Questions

- Are there pre-0.37.0 advisories not yet captured in the GitHub advisory database?
- Are CVE-2025-64702 and CVE-2026-40898 independent incomplete-fix steps, or does 0.59.1 fully cover the QPACK field section limit gap?
- Does the webtransport-go advisory set (CVE-2026-21435/21438/57497) warrant a separate page?

## Related Pages

- [[rust/quinn]]
- [[go/golang.org-x-net]]
- [[go/index]]

---
*Last updated: 2026-09-15 | Sources: 8 GHSA advisories (github/advisory-database), pkg.go.dev*
