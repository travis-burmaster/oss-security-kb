# Microsoft.AspNetCore.SignalR (.NET / NuGet)

**Registry:** NuGet
**Weekly Downloads:** unknown
**Repository:** https://github.com/dotnet/aspnetcore
**Security Contact:** https://github.com/dotnet/aspnetcore/security/policy
**Disclosure Policy:** https://github.com/dotnet/aspnetcore/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-0982 / GHSA-4jxx-4qxw-prxm | High (CVSS 7.5 AV:N) | DoS via improper web request handling in `Microsoft.AspNetCore.SignalR.Protocols.MessagePack`; affects 1.0.0–1.0.10 and 1.1.0–1.1.4 | 1.0.11 / 1.1.5 | [GHSA-4jxx-4qxw-prxm](https://github.com/advisories/GHSA-4jxx-4qxw-prxm) |
| CVE-2023-35391 / GHSA-j8rm-cm55-qqj6 | High (CVSS 7.5 AV:L) | Information disclosure via Redis backplane in `Microsoft.AspNetCore.SignalR.StackExchangeRedis` (6.0.0–6.0.20, 7.0.0–7.0.9) and `Microsoft.AspNetCore.SignalR.Redis` (< 1.0.40); relevant only to multi-server scaleout deployments | 7.0.10 / 6.0.21 / 1.0.40 | [GHSA-j8rm-cm55-qqj6](https://github.com/advisories/GHSA-j8rm-cm55-qqj6) |
| CVE-2024-21386 / GHSA-g74q-5xw3-j7q9 | High (CVSS 7.5 AV:N) | DoS via malicious SignalR client triggering uncontrolled resource consumption in `Microsoft.AspNetCore.App.Runtime`; affects .NET 6.0 (≤ 6.0.26), 7.0 (≤ 7.0.15), 8.0 (≤ 8.0.1) | .NET 8.0.2 / 7.0.16 / 6.0.27 | [GHSA-g74q-5xw3-j7q9](https://github.com/advisories/GHSA-g74q-5xw3-j7q9) |
| CVE-2026-26130 / GHSA-4vgm-c2wm-63mw | High (CVSS 7.5 AV:N) | DoS via uncontrolled resource consumption (CWE-770) in ASP.NET Core; affects `Microsoft.AspNetCore.App.Runtime` .NET 8.0 (≤ 8.0.24), 9.0 (≤ 9.0.13), 10.0 (≤ 10.0.3) | .NET 10.0.4 / 9.0.14 / 8.0.25 | [GHSA-4vgm-c2wm-63mw](https://github.com/advisories/GHSA-4vgm-c2wm-63mw) |
| CVE-2026-56170 / GHSA-j8gr-8fp3-5q5h | High (CVSS 7.5 AV:N) | DoS via stateful reconnect in SignalR — reconnect can be exploited to deny service to other connected clients (CWE-770); affects `Microsoft.AspNetCore.App.Runtime` .NET 8.0 (≤ 8.0.25), 9.0 (≤ 9.0.14), 10.0 (≤ 10.0.5) | .NET 10.0.6 / 9.0.15 / 8.0.26 | [GHSA-j8gr-8fp3-5q5h](https://github.com/advisories/GHSA-j8gr-8fp3-5q5h) |
| CVE-2026-45591 / GHSA-f8h2-vmm9-qhj6 | High (CWE-400 / CWE-787) | Stack overflow DoS via deeply-nested MessagePack arrays sent to SignalR or Blazor Server in `Microsoft.AspNetCore.SignalR.Protocols.MessagePack`; affects .NET 8.0 (≤ 8.0.27), 9.0 (≤ 9.0.16), 10.0 (≤ 10.0.8) | .NET 10.0.9 / 9.0.17 / 8.0.28 | [GHSA-f8h2-vmm9-qhj6](https://github.com/advisories/GHSA-f8h2-vmm9-qhj6) |

*OSV link: https://osv.dev/list?ecosystem=NuGet&q=Microsoft.AspNetCore.SignalR*

## Security Posture Notes

`Microsoft.AspNetCore.SignalR` is the ASP.NET Core real-time communication library providing WebSocket, Server-Sent Events, and long-polling transports with Hub-based RPC. It is bundled in every ASP.NET Core app via `Microsoft.AspNetCore.App` (shipped in-box with .NET SDK) and is a core dependency of Blazor Server and SignalR-based real-time features.

The advisory history shows a recurring **denial-of-service via resource exhaustion** pattern across multiple major .NET release lines:
- **CVE-2019-0982**: early MessagePack protocol DoS in the standalone 1.x packages (pre-merger into ASP.NET Core App).
- **CVE-2024-21386**: client-driven DoS, patched in .NET 8.0.2.
- **CVE-2026-26130**: ASP.NET Core resource-consumption DoS (broader than SignalR alone; .NET 8–10).
- **CVE-2026-56170**: stateful reconnect DoS specific to SignalR (.NET 8–10).
- **CVE-2026-45591**: MessagePack deeply-nested array stack overflow, also affecting Blazor Server (.NET 8–10).

The Redis backplane advisory (CVE-2023-35391) is a distinct information disclosure risk applicable only to multi-server (scaleout) deployments that use `Microsoft.AspNetCore.SignalR.StackExchangeRedis`.

For .NET 6+, SignalR ships as part of the ASP.NET Core App Runtime; fixing it means patching the .NET runtime itself. Standalone NuGet package (`Microsoft.AspNetCore.SignalR`) latest stable: **1.2.13** (September 2026). Security policy: https://github.com/dotnet/aspnetcore/security/policy (Microsoft coordinated disclosure via MSRC).

## Dependencies of Note

- `Microsoft.AspNetCore.SignalR.Protocols.MessagePack`: carries its own vulnerability history (CVE-2019-0982, CVE-2026-45591); requires explicit opt-in; update this package independently when the runtime advisory is not sufficient.
- `Microsoft.AspNetCore.SignalR.StackExchangeRedis` / `Microsoft.AspNetCore.SignalR.Redis`: Redis backplane packages; CVE-2023-35391 affects `.StackExchangeRedis` in .NET 6.x/7.x; only relevant in scaleout deployments.
- `StackExchange.Redis`: underlying Redis client; see [[dotnet/StackExchange.Redis]].

## Open Questions

- CVE-2026-26130 (GHSA-4vgm-c2wm-63mw): public advisory text describes "ASP.NET Core" broadly — exact code path (SignalR-specific or general middleware) not confirmed from public text; included here due to SignalR context in advisory search.
- Track ongoing .NET 8/9/10 Patch Tuesday releases for additional SignalR-class DoS CVEs.

## Related Pages

- [[dotnet/Microsoft.AspNetCore.Authentication.Negotiate]] — sibling ASP.NET Core authentication package
- [[dotnet/Swashbuckle.AspNetCore]] — ASP.NET Core OpenAPI middleware
- [[dotnet/StackExchange.Redis]] — Redis client used by the SignalR Redis backplane
- [[dotnet/index]]

---
*Last updated: 2026-09-26 | Sources: 2*
