# open-policy-agent/opa (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (CNCF graduated project; ~12,097 GitHub stars; 1,649 forks as of 2026-08-13)
**Repository:** https://github.com/open-policy-agent/opa
**Security Contact:** https://github.com/open-policy-agent/opa/security/policy
**Disclosure Policy:** https://github.com/open-policy-agent/opa/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|---------|
| 2023 | Cure53 | full-source | manual | unknown | [SECURITY_AUDIT.pdf](https://github.com/open-policy-agent/opa/blob/main/SECURITY_AUDIT.pdf) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|---------|
| CVE-2022-23628 / GHSA-hcw3-j74m-qc58 | Moderate (CVSS 5.4 AV:N/AC:L/PR:L/UI:N) | AST pretty-printer reorders elements in array literals when printing synthetic AST nodes (those not originating from parsed source); compiled policy logic may be silently altered from author intent | 0.37.2 | [GHSA-hcw3-j74m-qc58](https://github.com/advisories/GHSA-hcw3-j74m-qc58) |
| CVE-2022-28946 / GHSA-x7f3-62pm-9p38 | High (CVSS 7.5 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) | Out-of-bounds memory access in `ast/parser.go` — crafted Rego input causes incorrect expression interpretation and OPA server crash (DoS) | 0.40.0 | [GHSA-x7f3-62pm-9p38](https://github.com/advisories/GHSA-x7f3-62pm-9p38) |
| CVE-2022-33082 / GHSA-2m4x-4q9j-w97g | High | Denial of service via crafted input to the AST parser (`ast/compile.go` ~line 1224); improper handling of exceptional conditions allows external input to crash the OPA process | 0.42.0 | [GHSA-2m4x-4q9j-w97g](https://github.com/advisories/GHSA-2m4x-4q9j-w97g) |
| CVE-2022-36085 / GHSA-f524-rf33-2jjr | High (CVSS 7.1 AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N) | Bypass of `WithUnsafeBuiltins` restriction via Rego `with` keyword function mocking — callers using the Go SDK to sandbox dangerous built-ins (e.g., `http.send`, `net.lookup_ip_addr`) can have those restrictions circumvented by policy authors through mock substitution | 0.43.1 | [GHSA-f524-rf33-2jjr](https://github.com/advisories/GHSA-f524-rf33-2jjr) |
| CVE-2024-8260 / GHSA-c77r-fh37-x2px | Moderate (CVSS:3.1 AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:L/A:L; CVSS:4.0 AV:L/AC:L/AT:N/PR:L/UI:A) | OPA for Windows — improper input validation allows an attacker to pass an arbitrary SMB share path instead of a Rego file path; the OPA process performs SMB authentication against the attacker-controlled share, leaking NTLM credential hashes (force-authentication / NTLM relay primitive) | 0.68.0 | [GHSA-c77r-fh37-x2px](https://github.com/advisories/GHSA-c77r-fh37-x2px) |
| CVE-2025-46569 / GHSA-6m8w-jc87-6cr7 | High (CVSS:4.0 7.3 AV:N/AC:L/AT:P/PR:L/UI:N/VC:H/VI:N/VA:H/SC:H/SI:H/SA:H) | OPA Data API HTTP path injection — a Rego query is constructed from the request path without sanitization; injected Rego code can alter policy decision outcomes (oracle attack), force incorrect allow/deny results, or trigger computationally expensive operations (DoS); exploitable when OPA runs as a standalone server exposed externally with a policy that does not exactly match `input.path` | 1.4.0 | [GHSA-6m8w-jc87-6cr7](https://github.com/advisories/GHSA-6m8w-jc87-6cr7) |

### Related package: opa-envoy-plugin

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|---------|
| CVE-2026-26205 / GHSA-9f29-v6mm-pw6w | High (CVSS:4.0 4.0 AV:N/AC:L/AT:P/PR:N/UI:N/SC:H/SI:H/SA:H) | Authorization bypass in `github.com/open-policy-agent/opa-envoy-plugin` via double-slash path misinterpretation — HTTP paths beginning with `//` are parsed by OPA as having an authority component; the path OPA evaluates differs from the path the backend receives, enabling policy bypass | 1.13.2-envoy-2 | [GHSA-9f29-v6mm-pw6w](https://github.com/advisories/GHSA-9f29-v6mm-pw6w) |

## Security Posture Notes

OPA is a CNCF-graduated open-source policy engine widely used for Kubernetes admission control (via OPA Gatekeeper), API gateway authorization, and application-level policy evaluation. It implements the Rego policy language and exposes both a Go SDK and a standalone HTTP server (the latter used for sidecar and standalone deployments).

Key posture observations:
- OPA maintains a `SECURITY.md` with a responsible disclosure process and acknowledges security reports promptly (CNCF project practices apply).
- A third-party audit by Cure53 was conducted in 2023 (report: `SECURITY_AUDIT.pdf` in the repo root).
- The `WithUnsafeBuiltins` bypass (CVE-2022-36085) is the most architecturally significant advisory: organizations using OPA's Go SDK to sandbox policies from less-trusted authors should verify they are on ≥ 0.43.1.
- CVE-2025-46569 (Data API Rego injection) affects any deployment where OPA runs as a standalone server exposed to untrusted HTTP callers — sidecar or internal-only deployments are less exposed.
- CVE-2024-8260 only affects Windows deployments where OPA reads Rego files from attacker-influenced paths.
- The 2022 AST parser/compiler DoS cluster (CVE-2022-28946, CVE-2022-33082) was fixed in sequential minor releases; the attack surface is any code path that accepts and compiles untrusted Rego.
- Current stable: v1.19.0 (2026-07-30). All mapped advisories are fixed in versions released before 2026.

## Dependencies of Note

OPA bundles significant Go standard-library and third-party dependencies including `golang.org/x/net` (covered: [[go/golang.org-x-net]]) and `golang.org/x/crypto` (covered: [[go/golang.org-x-crypto]]). The opa-envoy-plugin companion package is a separate module tracked in the related-package table above.

## Open Questions

- pkg.go.dev importer counts for `github.com/open-policy-agent/opa` not collected in this pass — a future pass should quantify ecosystem exposure.
- The 2023 Cure53 audit findings are recorded as present but the full findings list was not individually mapped; a future pass should ingest the audit PDF.
- Confirm whether any post-1.4.0 advisories exist (pass searched 2022–2026 window; the 2026/02 path in github/advisory-database returned one entry for the envoy-plugin only).

## Related Pages

- [[go/github.com/go-jose/go-jose]] — JWT/JOSE library commonly used alongside OPA for token validation
- [[kubernetes/argo-cd]] — Argo CD uses OPA-based policies; critical auth bypass history
- [[go/golang.org-x-crypto]]
- [[go/golang.org-x-net]]
- [[go/index]]

---
*Last updated: 2026-08-13 | Sources: 7 (github/advisory-database GHSA records)*
