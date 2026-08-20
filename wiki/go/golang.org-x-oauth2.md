# golang.org/x/oauth2 (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (pkg.go.dev does not publish download counts; 48,088+ known importers as of 2026-08-20)
**Repository:** https://github.com/golang/oauth2 (mirror of cs.opensource.google/go/x/oauth2)
**Security Contact:** security@golang.org
**Disclosure Policy:** https://go.dev/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-22868 / GHSA-6v2p-p543-phr9 / GO-2025-3488 | High (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) | Malformed Bearer/JWS token causes unexpected memory consumption during parsing in the `jws` sub-package: `strings.Split()` was used to parse compact tokens, making the parser vulnerable to memory exhaustion when tokens contain a large number of `.` characters; unauthenticated DoS; no auth or user interaction required | 0.27.0 | [GHSA-6v2p-p543-phr9](https://github.com/advisories/GHSA-6v2p-p543-phr9) / [GO-2025-3488](https://pkg.go.dev/vuln/GO-2025-3488) / [go.dev/cl/652155](https://go.dev/cl/652155) |

## Security Posture Notes

`golang.org/x/oauth2` is the canonical Go OAuth 2.0 client library, part of the official Go extended standard library maintained by the Go team at Google. It provides OAuth 2.0 client flows (authorization code, device, password credentials, JWT bearer), PKCE support, and pre-configured endpoints for major providers (Google, GitHub, Facebook, Microsoft, etc.). Latest version: v0.36.0 (released 2026-02-11). pkg.go.dev shows 48,088+ known importers — extremely high blast radius including virtually all Google Cloud SDK users, Kubernetes auth components, and major OAuth2 integration libraries.

Security disclosures: report to security@golang.org per the [Go security policy](https://go.dev/security/policy). The Go security team publishes advisories via the Go Vulnerability Database (govulncheck integration at https://pkg.go.dev/vuln/).

**CVE-2025-22868 context:** The `jws` sub-package within `golang.org/x/oauth2` used `strings.Split()` to parse compact JWS/Bearer tokens. This made it susceptible to memory exhaustion when tokens contain pathologically large numbers of `.` characters — the same root bug class as CVE-2025-27144 in the `go-jose` library, which was patched in the same February 2025 timeframe. Fixed in v0.27.0 via [go.dev/cl/652155](https://go.dev/cl/652155) (tracked at [go.dev/issue/71490](https://go.dev/issue/71490)).

The package does not publish download counts; use the 48,088+ importer count as a lower bound on exposure. Downstreams that expose token-parsing endpoints to untrusted clients should upgrade to ≥ v0.27.0.

## Dependencies of Note

- `google.golang.org/api` is a major transitive consumer of `golang.org/x/oauth2`; ensure its minimum `golang.org/x/oauth2` dependency is ≥ 0.27.0 in your module graph.
- `golang.org/x/oauth2/google` and `golang.org/x/oauth2/jws` are sub-packages with dedicated security sensitivity — CVE-2025-22868 originates in `jws`.

## Open Questions

- Are there older pre-2025 advisories captured in the Go vulnerability database (`govulncheck`) but not yet in github/advisory-database? Run `govulncheck ./...` in dependent projects for a complete picture.
- Do other `golang.org/x/oauth2` sub-packages (`google`, `endpoints`, `transport`) have analogous malformed-input DoS surfaces? The `jws` fix addressed one; audit coverage of the other sub-packages is unclear.
- The package has not yet reached v1.0 stable; track whether the stable release changes the security support commitment.

## Related Pages

- [[go/github.com/go-jose/go-jose]] — go-jose: CVE-2025-27144 is the same malformed-token DoS class fixed in the same release window
- [[go/github.com/golang-jwt/jwt]] — golang-jwt: current maintained JWT library in the Go ecosystem
- [[go/github.com/dgrijalva/jwt-go]] — archived jwt-go with CVE-2020-26160 audience bypass
- [[go/golang.org-x-crypto]] — sibling golang.org/x module with SSH boundary advisory history
- [[go/index]]

---
*Last updated: 2026-08-20 | Sources: 2 (GHSA-6v2p-p543-phr9, GO-2025-3488)*
