# Evidence summary — 2026-05-06 advisory review

Targets reviewed:
- NuGet `System.Security.Cryptography.Xml`
- PyPI `telnyx`
- npm `merge` comparison check

Public source queries saved in this directory:
- `nuget-System.Security.Cryptography.Xml-osv.json` — OSV package query returned 5 records: GHSA-35hc-x2cw-2j4v / CVE-2018-0765, GHSA-rr3c-f55v-qhv5 / CVE-2018-0764, GHSA-vh55-786g-wjwj / CVE-2022-34716, GHSA-w3x6-4m5h-cxqf / CVE-2026-26171, GHSA-37gx-xxp4-5rgx / CVE-2026-33116.
- `pypi-telnyx-osv.json` — OSV package query returned 3 records for the March 2026 malicious-release incident: PYSEC-2026-3, GHSA-955r-262c-33jc, MAL-2026-2254.
- `npm-merge-osv.json` — OSV package query returned the same 2 prototype-pollution records already represented on the KB page: GHSA-7wpw-2hjm-89gp and GHSA-f9cm-qmx5-m98h.
- `proxy-request.json` / `proxy-response.json` — local Claude-compatible proxy synthesis used only as drafting aid.

Key public URLs used from OSV references:
- https://github.com/advisories/GHSA-rr3c-f55v-qhv5
- https://github.com/advisories/GHSA-35hc-x2cw-2j4v
- https://github.com/dotnet/aspnetcore/security/advisories/GHSA-vh55-786g-wjwj
- https://github.com/dotnet/runtime/security/advisories/GHSA-w3x6-4m5h-cxqf
- https://github.com/dotnet/runtime/security/advisories/GHSA-37gx-xxp4-5rgx
- https://github.com/dotnet/announcements/issues/232
- https://github.com/dotnet/announcements/issues/389
- https://github.com/dotnet/announcements/issues/392
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-34716
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26171
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33116
- https://github.com/team-telnyx/telnyx-python/security/advisories/GHSA-955r-262c-33jc
- https://github.com/team-telnyx/telnyx-python/issues/235
- https://blog.pypi.org/posts/2026-04-02-incident-report-litellm-telnyx-supply-chain-attack/
