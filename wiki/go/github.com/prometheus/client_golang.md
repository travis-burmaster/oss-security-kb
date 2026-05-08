# github.com/prometheus/client_golang (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-05-08)
**Repository:** https://github.com/prometheus/client_golang
**Security Contact:** GitHub Security Advisories / Prometheus security process
**Disclosure Policy:** https://github.com/prometheus/client_golang/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-08 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev package query, GitHub Advisory Database record, public CVE / NVD record, Go vulnerability database record, upstream release notes and fix PR, local proxy draft assist) | Added a dedicated page after normalizing the OSV / GitHub / Go records for `CVE-2022-21698` into one distinct `promhttp` denial-of-service vulnerability fixed in `1.11.1`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-21698 / GHSA-cg3q-j54f-5p7p / GO-2022-0322 | High | `promhttp` HTTP-server instrumentation before `1.11.1` could create unbounded metric-cardinality from non-standard HTTP methods when applications used affected `InstrumentHandler*` middleware with a `method` label and did not filter methods before instrumentation. The practical impact is memory exhaustion / denial of service from attacker-controlled method-label values. | 1.11.1 | https://github.com/advisories/GHSA-cg3q-j54f-5p7p |

*Full CVE history: https://osv.dev/list?ecosystem=Go&q=github.com/prometheus/client_golang*

## Security Posture Notes

- The OSV package query returned two records in this pass, but they collapse to **one distinct vulnerability**: the GitHub-reviewed advisory `GHSA-cg3q-j54f-5p7p` and the Go vulnerability record `GO-2022-0322` both track `CVE-2022-21698`.
- The affected public range is `<1.11.1`; GitHub's reviewed advisory lists `1.11.1` as the first patched version, and the upstream `v1.11.1` release notes explicitly mark the change as a security fix for `CVE-2022-21698`.
- Exposure is configuration-dependent. The Go vulnerability record and NVD description state that affected services must use `promhttp.InstrumentHandler*` middleware other than `RequestsInFlight`, pass a metric with a `method` label, avoid method filtering before the middleware, and lack an upstream proxy / firewall that rejects unknown methods.
- The bug class is observability-specific availability risk: attacker-supplied HTTP method strings can become unbounded label values, creating excessive Prometheus time-series cardinality and memory pressure.
- Upstream fix evidence is traceable through the `v1.11.1` release, which references PR `#987` and describes checking validity of `method` and `code` label values.
- This page should not be read as a general warning against `promhttp`; it is a narrow historical advisory with clear preconditions and a small fixed-version floor.

## Dependencies of Note

- `github.com/prometheus/client_golang` is a foundational metrics dependency for Go services and libraries, so even a single package-level advisory can have broad transitive visibility.
- Real-world risk depends heavily on how applications expose metrics handlers and whether reverse proxies, ingress controllers, or application middleware normalize / restrict HTTP methods before Prometheus instrumentation runs.
- Adjacent review work should distinguish application instrumentation libraries from Prometheus server components; this advisory belongs to the Go client module's `promhttp` package, not to Prometheus server itself.

## Open Questions

- Which popular Go service templates or frameworks still pin `client_golang` below `1.11.1`, if any, in public examples or starter repositories?
- Are there maintainer-authored hardening notes for controlling metric-label cardinality beyond the `v1.11.1` fix that should be captured on a broader observability-security page?
- Should future KB passes add a cross-reference for OpenTelemetry / Prometheus bridge packages where metric label cardinality is also a security-relevant availability boundary?

## Related Pages

- [[go/go.opentelemetry.io/otel]]
- [[go/github.com/gin-gonic/gin]]
- [[go/index]]

---
*Last updated: 2026-05-08 | Sources: 8 (OSV.dev package query for Go/github.com/prometheus/client_golang, OSV vulnerability records for GHSA-cg3q-j54f-5p7p and GO-2022-0322, GitHub Advisory Database entry, public NVD CVE record, Go vulnerability database record, upstream v1.11.1 release notes, upstream PR #987, local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid)*
