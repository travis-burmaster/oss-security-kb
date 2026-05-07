# go.opentelemetry.io/otel (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-05-07)
**Repository:** https://github.com/open-telemetry/opentelemetry-go
**Security Contact:** https://github.com/open-telemetry/opentelemetry-go/security/advisories
**Disclosure Policy:** https://github.com/open-telemetry/opentelemetry-go/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-07 | OpenClaw recurring review | package advisory refresh | public-source curation (OSV.dev, GitHub Advisory Database, NVD CVE record, upstream PR / commit / release notes) | Added the published 2026 baggage-header allocation-amplification DoS advisory fixed in 1.41.0. | raw/advisory-review-20260507-1805 |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-29181 / GHSA-mh2q-q3fh-2475 | High | Multi-value W3C `baggage` header extraction parsed each header field-value independently and aggregated members, allowing remote request-header amplification of CPU and allocations when applications extracted baggage from attacker-controlled HTTP headers. Public OSV / GHSA / NVD records identify affected versions as `>= 1.36.0, < 1.41.0`. | 1.41.0 | https://github.com/advisories/GHSA-mh2q-q3fh-2475 |

## Security Posture Notes

- `go.opentelemetry.io/otel` is a high-blast-radius observability dependency: tracing, metrics, logging, propagation, and semantic-convention helpers often sit in request paths across many Go services.
- The current public package-scoped advisory record found in this pass centers on **availability risk in propagation**, not confidentiality or integrity: many `baggage` header field-values could multiply parse and allocation work even though each individual value stayed within the pre-existing 8192-byte parse limit.
- NVD describes the affected range as OpenTelemetry-Go `1.36.0` through `1.40.0`, fixed in `1.41.0`; OSV encodes the same semver range as introduced `1.36.0` and fixed `1.41.0`.
- Upstream PR `#7880` documents the fix mechanics: comply with W3C Baggage limits, cap combined baggage size across all headers at 8192 bytes, cap combined member count at 64, and report extraction errors to the global error handler.
- The v1.41.0 release notes include the baggage-limit fix but do not label it as a security release in the changelog; the GHSA / OSV / NVD records published afterward provide the security framing.
- Practical exposure depends on whether an application extracts OpenTelemetry baggage from untrusted inbound HTTP request headers and how much total header size/count is allowed by front proxies and Go `net/http` configuration.

### Operational Takeaways

- Upgrade OpenTelemetry-Go to **v1.41.0 or later** when using baggage propagation on externally reachable HTTP services.
- If immediate upgrade is blocked, reduce total accepted request-header size and header count at the edge, especially for repeated `baggage` headers; this is a mitigation only, not a package fix.
- Treat propagation code as part of the request resource-consumption boundary: even observability metadata can become a remote DoS surface when parsing work scales with attacker-controlled header multiplicity.

## Dependencies of Note

- Instrumentation packages and HTTP middleware that call OpenTelemetry propagators may inherit the exposure even when application code does not directly parse `baggage` headers.
- Reverse proxies, API gateways, and load balancers that enforce total header limits can materially reduce exploitability, but do not change the affected package version.

## Open Questions

- Are there public audits focused on other OpenTelemetry-Go propagators, exporter input parsing, or high-cardinality resource-exhaustion boundaries?
- Which common Go web-framework integrations enable baggage extraction by default versus requiring explicit propagator configuration?
- Should future KB pages separate OpenTelemetry core module advisories from contrib instrumentation advisories once more public records accumulate?

## Related Pages

- [[go/index]]
- [[go/google.golang.org/grpc]]
- [[go/golang.org-x-crypto]]

---
*Last updated: 2026-05-07 | Sources: 6 (OSV.dev, GitHub Advisory Database / GHSA, NVD CVE record, upstream PR #7880, upstream fix commit, upstream v1.41.0 release notes)*
