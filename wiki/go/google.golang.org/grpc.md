# google.golang.org/grpc (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-04-10)
**Repository:** https://github.com/grpc/grpc-go
**Security Contact:** https://github.com/grpc/proposal/blob/master/P4-grpc-cve-process.md
**Disclosure Policy:** https://github.com/grpc/proposal/blob/master/P4-grpc-cve-process.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-11 | OpenClaw recurring review | api-surface | manual | 3 publicly disclosed module vulnerabilities curated from OSV, GHSA, CVE, and upstream release notes | https://osv.dev/list?ecosystem=Go&q=google.golang.org/grpc |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-44487 / GHSA-m425-mq94-257g / GO-2023-2153 | High | gRPC-Go servers could exceed the configured maximum stream limit under HTTP/2 Rapid Reset request patterns, causing denial-of-service risk. | 1.56.3, 1.57.1, 1.58.3, 1.59.0+ | https://github.com/grpc/grpc-go/security/advisories/GHSA-m425-mq94-257g |
| GHSA-xr7q-jx4m-x55m / GO-2024-2978 | Low | Private tokens or other metadata could appear in logs if applications logged contexts containing gRPC metadata. | 1.64.1, 1.65.0+ | https://github.com/grpc/grpc-go/security/advisories/GHSA-xr7q-jx4m-x55m |
| CVE-2026-33186 / GHSA-p77j-4mvh-x3m3 / GO-2026-4762 | Critical | A malformed HTTP/2 `:path` missing the leading slash could bypass path-based authorization deny rules in interceptors such as `grpc/authz` when fallback allow rules were present. | 1.79.3 | https://github.com/grpc/grpc-go/security/advisories/GHSA-p77j-4mvh-x3m3 |

*Full CVE history: https://osv.dev/list?ecosystem=Go&q=google.golang.org/grpc*

## Security Posture Notes

- `grpc-go` sits on a security-critical boundary for many Go services: HTTP/2 framing, RPC method routing, metadata propagation, authentication context, and interceptor-enforced authorization policy.
- The public advisory record shows three distinct bug classes worth tracking separately: transport resource exhaustion (Rapid Reset / HTTP/2), confidentiality risk from metadata logging, and authorization bypass from non-canonical method-path handling.
- Upstream's published gRPC CVE process is a comparatively mature disclosure signal, and the v1.79.3 release notes explicitly document the 2026 authorization-bypass fix.
- Exploitability is highly deployment-dependent: the 2026 authz bypass requires path-based authorization logic with a permissive fallback, and the 2024 logging issue depends on application code logging contexts that contain metadata.

- The 2026 authorization-bypass advisory explicitly calls out a mismatch between **non-canonical** `:path` strings accepted by the server router and the **canonical** path patterns used by path-based authorization interceptors; that makes canonicalization (and avoiding permissive fallback rules) a key operational takeaway for affected deployments.

### Operational Takeaways (GHSA-p77j-4mvh-x3m3)

**Affected only when all of the following are true (per the published advisory):**

- The server uses **path-based authorization interceptors** (for example `google.golang.org/grpc/authz`, or custom interceptors relying on `info.FullMethod` or `grpc.Method(ctx)`).
- The authorization policy has **deny rules written for canonical paths** (starting with `/`) but permits other requests via a **fallback allow rule**.
- An attacker can send **raw HTTP/2 frames** with a malformed `:path` pseudo-header directly to the gRPC server.

**Root cause:** gRPC-Go previously accepted HTTP/2 `:path` values without a leading slash (e.g., `Service/Method` instead of `/Service/Method`) and still routed them. Authorization interceptors evaluated the raw, non-canonical path string, so deny rules written against canonical paths failed to match, allowing bypass when a fallback allow rule existed.

**Fix behavior:** Upgrading to **v1.79.3+** causes requests whose `:path` does not begin with `/` to be rejected with a `codes.Unimplemented` error.

**Workarounds (if upgrade is blocked):**

- Add an **outermost interceptor** that validates `info.FullMethod` begins with `/` and rejects malformed requests before authorization logic runs.
- Enforce strict HTTP/2 pseudo-header compliance at an ingress proxy / load balancer that rejects or normalizes malformed `:path` values.
- Harden auth policy toward **default-deny** rather than relying on permissive fallback allow rules.

## Dependencies of Note

- `google.golang.org/grpc/authz` is a high-value adjacent surface because official path-based authorization logic was directly implicated in the 2026 bypass conditions.
- `google.golang.org/protobuf` remains a natural future page because message parsing and schema evolution often shape downstream exploitability even when a bug is not in transport code.
- Infrastructure that terminates or forwards HTTP/2 (for example Envoy or managed L7 load balancers) can materially affect exposure to malformed pseudo-header handling and Rapid Reset-style traffic patterns.

## Open Questions

- Are there public audits focused specifically on grpc-go interceptor ordering, metadata propagation, or HTTP/2 state-machine edge cases beyond individual advisories?
- Should this page eventually separate server-side transport flaws from application-layer misuse patterns so the advisory history stays easy to scan?
- Is it worth adding a future companion page for `grpc/authz` if more public policy-bypass or interceptor-ordering issues accumulate there?

## Related Pages

- [[go/index]]

---
*Last updated: 2026-04-30 | Sources: 7 (OSV package query, GHSA advisory pages, upstream grpc-go release notes, NVD CVE records)*
