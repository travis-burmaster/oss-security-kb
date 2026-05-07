# google.golang.org/protobuf (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-05-07)
**Repository:** https://github.com/protocolbuffers/protobuf-go
**Security Contact:** GitHub Security Advisories / Go vulnerability reporting
**Disclosure Policy:** none package-specific confirmed in this pass
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-07 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev package query, GitHub Advisory Database records, public CVE records, Go vulnerability records, upstream issue / release notes / fix references, local proxy draft assist) | Added a dedicated page for `google.golang.org/protobuf` after normalizing four public OSV results into two distinct denial-of-service vulnerabilities in protobuf text / JSON parsing paths. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-24535 / GHSA-hw7c-3rfg-p46j / GO-2023-1631 | High | `prototext` parsing of an incomplete number could panic, producing denial-of-service risk for services that parse attacker-controlled protobuf text-format input. The affected public range is narrow: `1.29.0` before `1.29.1`. | 1.29.1 | https://github.com/advisories/GHSA-hw7c-3rfg-p46j |
| CVE-2024-24786 / GHSA-8r3f-844c-mc37 / GO-2024-2611 | High | `protojson.Unmarshal` could enter an infinite loop on certain invalid JSON inputs, including cases involving `google.protobuf.Any` or `UnmarshalOptions.DiscardUnknown`, causing availability impact when untrusted JSON is unmarshaled into protobuf messages. | 1.33.0 | https://github.com/advisories/GHSA-8r3f-844c-mc37 |

*Full CVE history: https://osv.dev/list?ecosystem=Go&q=google.golang.org/protobuf*

## Security Posture Notes

- The OSV package query returned four records in this pass, but they collapse to **two distinct vulnerabilities**: each issue is represented once as a GitHub-reviewed advisory and once as a Go vulnerability database record.
- Both confirmed package-level issues are availability bugs in parsing code rather than confidentiality or integrity breaks: one panic in protobuf text-format number parsing and one infinite loop in protobuf JSON parsing.
- The 2023 record has an unusually narrow affected window (`1.29.0` only before `1.29.1`). Upstream release notes for `v1.29.1` cite `CL/475995` as fixing incomplete-number parsing.
- The 2024 record has a broader `<1.33.0` affected range. Upstream `v1.33.0` release notes explicitly call it a security fix for `encoding/protojson` and name `CVE-2024-24786` / `GHSA-8r3f-844c-mc37`.
- Package scope matters: OSV lists affected import paths such as `encoding/protojson`, `internal/encoding/json`, `encoding/prototext`, and `internal/encoding/text`, but Go module versioning means the actionable upgrade floor is on the root module `google.golang.org/protobuf`.
- Real-world exposure depends on whether services parse untrusted protobuf text or JSON. Systems that only marshal trusted internal objects have a different risk profile than API gateways, ingestion services, or multi-tenant parsers accepting external payloads.

## Dependencies of Note

- `google.golang.org/protobuf` is a foundational serialization dependency for Go services, SDKs, gRPC stacks, Kubernetes-adjacent tooling, and generated API clients.
- `google.golang.org/grpc` is an adjacent page because many gRPC-Go deployments also depend on protobuf message parsing, even when a published transport bug is recorded against `grpc-go` rather than `protobuf-go`.
- Services exposing JSON-to-protobuf translation, API gateways, webhook receivers, or user-supplied configuration parsers should treat `protojson` / `prototext` upgrade floors as operationally important.

## Open Questions

- Are there public fuzzing or parser-hardening writeups from the protobuf-go maintainers that explain current coverage for `protojson` and `prototext` beyond individual fix CLs?
- Should future KB work add a companion page for the legacy `github.com/golang/protobuf` module if public records diverge from the modern `google.golang.org/protobuf` module?
- Which high-usage Go frameworks or generated clients still pin protobuf below `1.33.0` transitively?

## Related Pages

- [[go/google.golang.org/grpc]]
- [[go/golang.org-x-crypto]]
- [[go/index]]

---
*Last updated: 2026-05-07 | Sources: 9 (OSV.dev package query for Go/google.golang.org/protobuf, OSV vulnerability records for GHSA-8r3f-844c-mc37 / GO-2024-2611 and GHSA-hw7c-3rfg-p46j / GO-2023-1631, GitHub Advisory Database entries, public NVD CVE records, Go vulnerability database records, upstream issue golang/protobuf#1530, upstream release notes for v1.29.1 and v1.33.0, upstream fix references CL/475995 and CL/569356, local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid)*
