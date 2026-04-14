# golang.org/x/crypto (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-04-13)
**Repository:** https://github.com/golang/crypto
**Security Contact:** https://go.dev/security/policy
**Disclosure Policy:** https://go.dev/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-13 | OpenClaw recurring review | module advisory history | manual | 12 publicly disclosed module vulnerabilities curated from OSV, Go vuln records, GHSA, CVE aliases, and upstream fix / announcement references | https://osv.dev/list?ecosystem=Go&q=golang.org%2Fx%2Fcrypto |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2017-3204 / GHSA-xhjq-w7xm-p8qj / GO-2020-0013 | High | `ssh` clients did not require explicit host-key verification by default, making MITM exposure easy when callers forgot to set `ClientConfig.HostKeyCallback`. | `0.0.0-20170330155735-e4e2799dd7aa` | https://github.com/advisories/GHSA-xhjq-w7xm-p8qj |
| CVE-2019-11840 / GHSA-r5c5-pr8j-pfp7 / GO-2022-0209 | Moderate | The amd64 `salsa20/salsa` implementation could repeat keystream after very large inputs, risking confidentiality or RNG predictability in extreme-use cases. | `0.0.0-20190320223903-b7391e95e576` | https://github.com/advisories/GHSA-r5c5-pr8j-pfp7 |
| CVE-2019-11841 / GHSA-x3jr-pf6g-c48f / GO-2023-1992 | Moderate | `openpgp/clearsign` accepted malformed signed messages in ways that could mislead human readers about what text was actually verified. | `0.0.0-20190424203555-c05e17bb3b2d` | https://github.com/advisories/GHSA-x3jr-pf6g-c48f |
| CVE-2020-7919 / GO-2022-0229 | High | `cryptobyte` shared a 32-bit-architecture certificate / ASN.1 parsing panic with Go's stdlib `crypto/x509`; malformed input could crash affected clients. | `0.0.0-20200124225646-8b5121be2f68` | https://pkg.go.dev/vuln/GO-2022-0229 |
| CVE-2020-9283 / GHSA-ffhg-7mh4-33c4 / GO-2020-0012 | High | Crafted Ed25519 public keys could panic signature verification in `ssh`, enabling denial of service when verifying attacker-controlled keys. | `0.0.0-20200220183623-bac4c82f6975` | https://github.com/advisories/GHSA-ffhg-7mh4-33c4 |
| CVE-2020-29652 / GHSA-3vm4-22fp-5rfm / GO-2021-0227 | High | `ssh` servers could panic on crafted `gssapi-with-mic` authentication messages when `GSSAPIWithMICConfig` was nil. | `0.0.0-20201216223049-8b5274cf687f` | https://github.com/advisories/GHSA-3vm4-22fp-5rfm |
| CVE-2021-43565 / GHSA-gwc9-m7rh-j2ww / GO-2022-0968 | High | Unauthenticated malformed packets could panic `ssh` servers when AES-GCM or ChaCha20-Poly1305 was in use. | `0.0.0-20211202192323-5770296d904e` | https://github.com/advisories/GHSA-gwc9-m7rh-j2ww |
| CVE-2022-27191 / GHSA-8c26-wmh5-6g9v / GO-2021-0356 | High | `ssh` servers could crash if configured with a crafted or nonstandard `Signer` passed through `ServerConfig.AddHostKey`. | `0.0.0-20220314234659-1baeb1ce4c0b` | https://github.com/advisories/GHSA-8c26-wmh5-6g9v |
| CVE-2022-30636 / GO-2024-2961 | Moderate | On Windows, `acme/autocert` could perform a limited directory traversal when deriving HTTP-01 token cache paths, though the impact was constrained by a forced `+http-01` suffix. | `0.0.0-20220525230936-793ad666bf5e` | https://pkg.go.dev/vuln/GO-2024-2961 |
| CVE-2023-48795 / GHSA-45x7-px36-x8w8 / GO-2023-2402 | Moderate | The Terrapin SSH prefix-truncation weakness affected `ssh` secure-channel integrity and could suppress early post-handshake messages such as `SSH_MSG_EXT_INFO`. | `0.17.0` / `0.0.0-20231218163308-9d2ee975ef9f` | https://github.com/advisories/GHSA-45x7-px36-x8w8 |
| CVE-2024-45337 / GHSA-v778-237x-gjrc / GO-2024-3321 | Critical | Applications that misused `ServerConfig.PublicKeyCallback` could make authorization decisions based on a key the client never proved ownership of; `v0.31.0` added a partial mitigation and stronger guidance. | `0.31.0` | https://github.com/advisories/GHSA-v778-237x-gjrc |
| CVE-2025-22869 / GHSA-hcg3-q754-cr77 / GO-2025-3487 | High | `ssh` servers implementing file-transfer protocols could accumulate data in memory during slow or incomplete key exchange, enabling denial of service. | `0.35.0` | https://github.com/advisories/GHSA-hcg3-q754-cr77 |

*Later public advisories also exist for the `ssh/agent` surface (`GO-2025-4116`, `GO-2025-4134`, `GO-2025-4135` / fixes in `0.43.0` and `0.45.0`), but the table above captures the clearest module-wide lineage for this first pass.*

*Full CVE / GO vulnerability history: https://osv.dev/list?ecosystem=Go&q=golang.org%2Fx%2Fcrypto*

## Security Posture Notes

- `golang.org/x/crypto` is not one thing: the public advisory record spans SSH transport / auth flows, `openpgp` message handling, `acme/autocert` path handling, `cryptobyte` parsing, and low-level stream-cipher code. That breadth makes it an unusually important infrastructure package to track at module level.
- The densest cluster is clearly `golang.org/x/crypto/ssh`. Public advisories repeatedly hit handshake parsing, malformed-packet handling, auth callback semantics, and protocol-boundary assumptions rather than classic memory corruption.
- The 2024 `PublicKeyCallback` authorization-bypass advisory is especially worth highlighting because upstream described `v0.31.0` as a partial mitigation for a widely misused API pattern, not a magic fix for every application that stored callback state incorrectly.
- Terrapin (`CVE-2023-48795`) is partly a protocol problem rather than a Go-only implementation bug; the x/crypto fix aligns with the broader OpenSSH 9.6 "strict kex" hardening story.
- Operators should avoid reading the package as "safe if not on the latest tag". Several older fixes landed only as pseudo-versions before semantic tags caught up, so consumers pinned to older commits can easily miss important fixes.

## Dependencies of Note

- `golang.org/x/crypto/ssh` is the dominant high-risk surface and likely deserves a future dedicated sub-surface page if the KB starts tracking Go modules at package-path granularity.
- `golang.org/x/crypto/acme/autocert` matters for internet-facing certificate automation and can quietly widen blast radius on Windows-specific deployments.
- `golang.org/x/crypto/openpgp` remains relevant for legacy verification flows even though the wider OpenPGP ecosystem has been de-emphasized.

## Open Questions

- Should the KB eventually split large multi-surface Go modules like `golang.org/x/crypto` into companion pages (`ssh`, `autocert`, `openpgp`) once the module-level page becomes too dense?
- Is it worth adding a focused note about the 2025 `ssh/agent` advisory cluster now, or waiting until a broader agent / forwarding review also covers exposure patterns in real applications?
- Are there enough public postmortems or ecosystem incident writeups around `PublicKeyCallback` misuse to justify a dedicated cross-project misuse-pattern appendix?

## Related Pages

- [[go/google.golang.org/grpc]]
- [[go/github.com/gin-gonic/gin]]
- [[go/index]]

---
*Last updated: 2026-04-13 | Sources: 11 (OSV package query, Go vuln records, GitHub Advisory Database entries, public CVE aliases, OpenSSH 9.6 release notes, golang-announce posts)*
