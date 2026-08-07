# go-git (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (pkg.go.dev does not publish download statistics; ~4,979 known importers as of 2026-08-07)
**Repository:** https://github.com/go-git/go-git
**Security Contact:** https://github.com/go-git/go-git/security/advisories
**Disclosure Policy:** https://github.com/go-git/go-git/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Notes |
|------|---------|-------|-------|
| 2026-08-07 | nightly-bot | GHSA advisory search + raw fetch | 6 advisories mapped; OSV.dev blocked; sourced from github/advisory-database |

## Known Vulnerabilities

| ID | Severity | CVSS | Description | Affected Versions | Fixed In | Primary Source |
|----|----------|------|-------------|-------------------|----------|----------------|
| CVE-2023-49569 / GHSA-449p-3h89-pw88 | Critical | 9.8 | Path traversal → arbitrary code execution via malicious server when using `ChrootOS` filesystem abstraction; server can write files outside the checkout root | < 5.11.0 | 5.11.0 | [GHSA-449p-3h89-pw88](https://github.com/advisories/GHSA-449p-3h89-pw88) |
| CVE-2023-49568 / GHSA-mw99-9chc-xw7r | High | 7.5 | Denial of service via panic triggered by malicious server response during repository operations | < 5.11.0 | 5.11.0 | [GHSA-mw99-9chc-xw7r](https://github.com/advisories/GHSA-mw99-9chc-xw7r) |
| CVE-2025-21613 / GHSA-v725-9546-7q7m | Critical | 9.8 | Argument injection via malformed `file://` URL enabling remote code execution when cloning from untrusted sources | < 5.13.0 | 5.13.0 | [GHSA-v725-9546-7q7m](https://github.com/advisories/GHSA-v725-9546-7q7m) |
| CVE-2025-21614 / GHSA-r9px-m959-cxf4 | High | 7.5 | Denial of service via malformed server response; distinct root cause from CVE-2023-49568 | < 5.13.0 | 5.13.0 | [GHSA-r9px-m959-cxf4](https://github.com/advisories/GHSA-r9px-m959-cxf4) |
| CVE-2026-45022 / GHSA-389r-gv7p-r3rp | Moderate | 4.0 | Commit signature verification bypass via malformed object parsing; allows presenting an unsigned or differently-signed commit as valid | < 5.19.0 | 5.19.0 | [GHSA-389r-gv7p-r3rp](https://github.com/advisories/GHSA-389r-gv7p-r3rp) |
| GHSA-w5pp-99ch-qj29 | Moderate | 7.5 | Denial of service via malformed `.pack`, `.idx`, or loose object files causing memory exhaustion or panic during repository parsing | < 5.19.1 | 5.19.1 | [GHSA-w5pp-99ch-qj29](https://github.com/advisories/GHSA-w5pp-99ch-qj29) |

## Security Posture Notes

go-git is a pure-Go implementation of the Git protocol and object model, used widely in CI/CD pipelines, Git automation tooling, and programmatic repository management. Its attack surface concentrates in two areas: parsing untrusted server-provided content (pack files, refs, protocol messages) and handling untrusted repository content (objects, paths, pack/idx files).

**Code execution class (Critical):** CVE-2023-49569 and CVE-2025-21613 are the highest-priority advisories. Both allow a malicious remote server or repository URL to achieve arbitrary code execution on the client. CVE-2023-49569 exploits path traversal in the `ChrootOS` abstraction, allowing server-controlled file writes outside the intended checkout root. CVE-2025-21613 exploits improper sanitization of `file://` URLs to inject arguments to the underlying process. Applications that clone from user-supplied or untrusted repository URLs are directly exposed.

**DoS class (High):** CVE-2023-49568 and CVE-2025-21614 are separate denial-of-service advisories triggered by malformed server responses, fixed in the same releases as their corresponding code-execution advisories. Distinct root causes indicate the DoS vectors were discovered alongside the code-execution research.

**2026 advisory cluster:** CVE-2026-45022 (signature bypass) and GHSA-w5pp-99ch-qj29 (object parsing DoS) indicate active ongoing security review. The signature bypass is relevant for supply-chain integrity use cases where go-git is used to verify commit signatures.

**Recommended version:** ≥ 5.19.1 (covers all 6 mapped advisories).

## Dependencies of Note

- `golang.org/x/crypto` — SSH transport layer; carries its own advisory history
- `golang.org/x/net` — HTTP transport layer

## Open Questions

- pkg.go.dev does not publish download statistics; the ~4,979 importer count is a lower-bound proxy for downstream exposure.
- No formal SECURITY.md policy was confirmed in the repository at time of this pass; advisories appear to be reported via GitHub's private vulnerability reporting.

## Related Pages

- [[go/golang.org-x-crypto]]
- [[go/golang.org-x-net]]
