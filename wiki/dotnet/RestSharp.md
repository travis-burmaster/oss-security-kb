# RestSharp (NuGet)

**Registry:** NuGet
**Weekly Downloads:** unknown weekly; ~561.7M total NuGet downloads (as of 2026-07-03)
**Repository:** https://github.com/restsharp/RestSharp
**Security Contact:** GitHub security advisories (https://github.com/restsharp/RestSharp/security)
**Disclosure Policy:** GitHub security advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-9pq7-rcxv-47vq / CVE-2021-27293 | High (CVSS:3.1 7.5) | ReDoS in DateTime string parsing: a malicious server response containing a crafted date string causes catastrophic backtracking in a vulnerable regex used by the `DateTimeDeserializer`, causing the client to hang indefinitely; remotely triggerable by any server that the client contacts | RestSharp ≥ 106.11.8-alpha.0.13 | [GHSA-9pq7-rcxv-47vq](https://github.com/advisories/GHSA-9pq7-rcxv-47vq) |
| GHSA-4rr6-2v9v-wcpc / CVE-2024-45302 | Moderate (CVSS:3.1 local, CVSS:4.0 network) | CRLF injection in `RestRequest.AddHeader`, `AddOrUpdateHeader`, and `RestClient.AddDefaultHeader`: header values are passed to `HttpHeaders.TryAddWithoutValidation`, which does not strip `\r\n`; an application that passes user-controlled input to these methods becomes vulnerable to HTTP header injection and request splitting / SSRF; affects RestSharp 107.0.0-preview.1 through 111.x | RestSharp ≥ 112.0.0 | [GHSA-4rr6-2v9v-wcpc](https://github.com/advisories/GHSA-4rr6-2v9v-wcpc) |

## Security Posture Notes

RestSharp is a lightweight wrapper around `HttpClient` for .NET with over 561 million total NuGet downloads. It is widely used in backend services, test harnesses, and API clients.

The ReDoS advisory (CVE-2021-27293) affected versions prior to the 106.x series and was remotely triggerable by any server that the client communicated with — a dependency on untrusted HTTP responses common in microservice architectures. Current versions (107.x+) rewrote the DateTime parsing path; the regex is no longer used.

The CRLF injection advisory (CVE-2024-45302) affects versions 107.0.0-preview.1 through 111.x — notably the entire v107–v111 range — and is fixed in 112.0.0. The vulnerability exists because RestSharp uses `TryAddWithoutValidation` rather than the validating `Add` method when setting headers; any application that forwards user-controllable values (query parameters, form fields, user IDs, tokens) into header values via these APIs is directly affected. The current recommended version (114.0.0) is patched.

The advisory scope notes this as a library design issue: the library's failure to validate CRLF characters makes callers inadvertently vulnerable. Applications that pin an older version in the affected range should upgrade to 112.0.0 or later.

The GitHub Advisory Database contains exactly two reviewed advisories for this package; no additional public records were found in this pass.

## Dependencies of Note

None flagged. RestSharp wraps `System.Net.Http.HttpClient` and has no security-relevant transitive dependencies of note in recent versions.

## Open Questions

- Confirm whether any open CRLF-validation issues remain in the header-merging code paths added after 112.0.0 (the fix was a single commit targeting the identified methods; other header-setting paths may not have been audited).
- Assess whether the `TryAddWithoutValidation` pattern recurs in other RestSharp methods beyond the three named in the advisory.

## Related Pages

- [[dotnet/System.Text.Json]]
- [[dotnet/Npgsql]]
- [[dotnet/index]]

---
*Last updated: 2026-07-03 | Sources: 2*
