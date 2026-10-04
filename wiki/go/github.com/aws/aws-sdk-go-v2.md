# github.com/aws/aws-sdk-go-v2 (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (high; 200+ service sub-modules each with thousands of importers; S3 module alone: 37,000+ importers; root module v1.47.1 released 2026-09-24)
**Repository:** https://github.com/aws/aws-sdk-go-v2
**Security Contact:** aws-security@amazon.com
**Disclosure Policy:** https://aws.amazon.com/security/vulnerability-reporting/
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-xmrv-pmrh-hhx2 | Moderate (CVSS:3.1 5.9 AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H) | EventStream header decoder: a malformed server response frame with a crafted header-value type byte outside the valid range causes the host process to panic and terminate; unauthenticated network attacker who can inject or forge an EventStream response can DoS any client using EventStream-capable services (Kinesis, Transcribe, Lex v2, Bedrock Runtime, Lambda invoke-with-streaming, CloudWatch Logs, S3 SelectObjectContent, and others); CWE-20; no CVE assigned | Multiple sub-modules (see table below) — all fixed in release 2026-03-23 | [GHSA-xmrv-pmrh-hhx2](https://github.com/advisories/GHSA-xmrv-pmrh-hhx2) |

**GHSA-xmrv-pmrh-hhx2 — fixed versions by sub-module (release 2026-03-23):**

| Sub-module | Fixed version |
|---|---|
| `aws/protocol/eventstream` | ≥ 1.7.8 |
| `service/s3` | ≥ 1.97.3 |
| `service/bedrockruntime` | ≥ 1.50.4 |
| `service/bedrockagentruntime` | ≥ 1.51.8 |
| `service/bedrockagentcore` | ≥ 1.15.2 |
| `service/kinesis` | ≥ 1.43.5 |
| `service/lambda` | ≥ 1.88.5 |
| `service/lexruntimev2` | ≥ 1.35.15 |
| `service/cloudwatchlogs` | ≥ 1.65.0 |
| `service/iotsitewise` | ≥ 1.52.19 |
| `service/sagemakerruntime` | ≥ 1.39.6 |
| `service/transcribestreaming` | ≥ 1.34.5 |

*OSV link: https://osv.dev/list?ecosystem=Go&q=aws-sdk-go-v2*

## Security Posture Notes

`github.com/aws/aws-sdk-go-v2` is the actively maintained AWS SDK for Go, successor to the now-archived `github.com/aws/aws-sdk-go` (v1, EOL 2025-07-31). The v2 SDK uses a multi-module layout: each AWS service is an independent Go module under the `service/` path prefix, sharing infrastructure from `config/`, `credentials/`, and `aws/`. Root module version: v1.47.1 (2026-09-24). Minimum Go version: 1.24. License: Apache-2.0.

The confirmed public advisory (GHSA-xmrv-pmrh-hhx2, disclosed April 2026) is a DoS via panic in the EventStream frame decoder. The EventStream binary protocol (multiplexed message framing over HTTP/2) is used by AWS services that stream responses: Kinesis Data Streams, Amazon Transcribe Streaming, Lex Runtime v2, Bedrock Runtime, Lambda invoke-with-streaming, CloudWatch Logs, S3 SelectObjectContent, IoT SiteWise, and others. An attacker who can inject a malformed EventStream frame with a header-value type byte outside the valid range (0–7) triggers an unrecoverable panic in the Go decoder process. The fix (2026-03-23 release) bounds all affected service modules. Applications using any EventStream-capable service should update the relevant service module to the fixed version, or explicitly pin `aws/protocol/eventstream` ≥ 1.7.8.

**S3 encryption continuity:** The S3 client-side encryption (CSE) library in v2 (`service/s3/s3crypto`) has not been the subject of a published formal security review. The cryptographic design weaknesses found in v1 (CBC padding oracle CVE-2020-8911, unauthenticated algorithm selection CVE-2020-8912) should be verified as remediated in v2 before using S3 CSE in security-sensitive deployments.

AWS security disclosures are coordinated through aws-security@amazon.com and published at https://github.com/aws/aws-sdk-go-v2/security/advisories.

## Dependencies of Note

- `github.com/aws/smithy-go` — AWS Smithy protocol layer; no confirmed public advisories
- `golang.org/x/net` — used for HTTP/2; see [[go/golang.org-x-net]]
- `golang.org/x/crypto` — used for request signing; see [[go/golang.org-x-crypto]]

## Open Questions

- Has the S3 CSE sub-package in v2 been formally audited to confirm the v1 CBC/algorithm-selection weaknesses are absent?
- Are there additional EventStream-capable service modules not listed in GHSA-xmrv-pmrh-hhx2 that shipped un-patched until a later release?
- Does the credential-refresh goroutine in the shared config package carry race conditions under high concurrency?

## Related Pages

- [[go/github.com/aws/aws-sdk-go]] (v1, archived/EOL 2025-07-31)
- [[go/golang.org-x-crypto]]
- [[go/golang.org-x-net]]
- [[go/index]]

---
*Last updated: 2026-10-04 | Sources: github/advisory-database (GHSA-xmrv-pmrh-hhx2); pkg.go.dev metadata*
