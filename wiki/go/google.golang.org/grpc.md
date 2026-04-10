# google.golang.org/grpc (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-04-10)
**Repository:** https://github.com/grpc/grpc-go
**Security Contact:** https://github.com/grpc/proposal/blob/master/P4-grpc-cve-process.md
**Disclosure Policy:** https://github.com/grpc/proposal/blob/master/P4-grpc-cve-process.md
**Current Status:** baseline stub

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| Review pending | — | This page has not yet been populated with module-specific advisory history. Use OSV, Go vulnerability data, and upstream issue history as starting points. | — | https://osv.dev/list?ecosystem=Go&q=google.golang.org/grpc |

*Full CVE history: https://osv.dev/list?ecosystem=Go&q=google.golang.org/grpc*

## Security Posture Notes

- `grpc-go` is a high-leverage Go module because request parsing, HTTP/2 handling, metadata propagation, credential use, and streaming behavior often become application-wide trust boundaries.
- The public Go package ecosystem does not expose simple weekly-download metrics in the same way npm or PyPI do, so this stub leaves download volume as unknown rather than inventing a proxy. As a rough importance signal, deps.dev currently shows more than 2,000 dependent projects.
- Upstream publishes a dedicated gRPC CVE process, which is a stronger disclosure signal than many baseline stubs currently have.

## Dependencies of Note

- `google.golang.org/protobuf` is a natural follow-on page because message parsing and wire-format handling often shape downstream exploitability.
- HTTP/2 implementation details in the Go standard library and adjacent transport packages may matter when deepening this page later.

## Open Questions

- Have any public targeted reviews covered grpc-go's HTTP/2 state machine, metadata handling, or credential transport boundaries?
- Which historical issues belong on `grpc-go` itself versus the core gRPC project, Envoy integrations, or application-level misuse?
- Should this page eventually split transport-layer flaws from authn/authz misuse patterns so the KB stays evidence-based?

## Related Pages

- [[go/index]]

---
*Last updated: 2026-04-10 | Sources: 3 (Go package metadata, deps.dev package summary, upstream SECURITY.md / gRPC CVE process link)*
