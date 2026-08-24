# Azure.Identity (.NET / NuGet)

**Registry:** NuGet
**Weekly Downloads:** ~23.8M/week (~3.4M/day); 1.9B total (as of 2026-08-24)
**Repository:** https://github.com/Azure/azure-sdk-for-net
**Security Contact:** secure@microsoft.com (MSRC)
**Disclosure Policy:** https://msrc.microsoft.com/create-report
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-36414 / GHSA-5mfx-4wcx-rv27 | High (CVSS v3.1 8.8, AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) | Remote Code Execution via command injection (CWE-77) — credential providers that invoke external CLI tools construct process arguments from environment-supplied input without sufficient sanitization; network-reachable, low complexity, low-privilege required | 1.10.2 | [GHSA-5mfx-4wcx-rv27](https://github.com/advisories/GHSA-5mfx-4wcx-rv27) |
| CVE-2024-29992 / GHSA-wvxc-855f-jvrv | Moderate (CVSS v3.1 7.1, AV:L/AC:L/PR:L/UI:N/C:H) | Information disclosure — credentials or tokens insufficiently protected in local storage paths accessible to other local processes (CWE-522); local access, low privilege required | 1.11.0 | [GHSA-wvxc-855f-jvrv](https://github.com/advisories/GHSA-wvxc-855f-jvrv) |
| CVE-2024-35255 / GHSA-m5vv-6r4h-3vj9 | High (CVSS v3.1 7.1) | Elevation of privilege via TOCTOU race condition in token-cache file handling (CWE-362) — cross-ecosystem: affects Azure.Identity (NuGet ≥ 1.10.0, < 1.11.4), azure-identity (PyPI < 1.16.1), @azure/identity (npm < 4.2.1), azure-identity (Maven < 1.12.2), azidentity (Go); also affects Microsoft.Identity.Client (MSAL) 4.49.1–4.61.2 | 1.11.4 (NuGet) | [GHSA-m5vv-6r4h-3vj9](https://github.com/advisories/GHSA-m5vv-6r4h-3vj9) |

## Security Posture Notes

Azure.Identity is Microsoft's official authentication library for Azure services, providing `DefaultAzureCredential` and a pluggable credential chain covering workload identity, managed identity, environment variables, Azure CLI, Visual Studio, Azure PowerShell, and device code flows. It is a transitive dependency of virtually every .NET application deployed to Azure (Azure Blob Storage, Cosmos DB, Service Bus, Key Vault, Cognitive Services SDKs, etc.).

CVE-2023-36414 (CVSS 8.8 High, published October 2023) is the highest-severity advisory on record. The CWE-77 classification (command injection) and AV:N/PR:L CVSS vector indicate that credential providers which spawn external processes (e.g., `AzureCliCredential`, `AzurePowerShellCredential`) constructed process arguments from insufficiently sanitized input, and the resulting impact is network-accessible. Fixed in 1.10.2 (released 2023-10-10). See the MSRC advisory at https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36414 for canonical details.

CVE-2024-35255 (published June 2024) is notable for its cross-ecosystem scope: the TOCTOU race condition in token-cache file handling was patched simultaneously across five language SDKs (NuGet, PyPI, npm, Maven, Go) and also affected Microsoft.Identity.Client (MSAL.NET) across 4.49.1–4.61.2. A low-privileged local process can exploit the race to elevate privileges by swapping the token-cache file between a stat/check and a subsequent read or write.

The latest stable version as of 2026-08-24 is **1.21.0** (released 2026-04-11), which is unaffected by all three known advisories. All three fixed versions (1.10.2, 1.11.0, 1.11.4) are well back in the release history; any deployment on these or earlier versions should be considered at risk.

## Dependencies of Note

- `Microsoft.Identity.Client` (MSAL.NET) — underlying token acquisition library; co-affected by CVE-2024-35255 (MSAL 4.49.1–4.61.2). See [[dotnet/Microsoft.IdentityModel.JsonWebTokens]] for related JWT validation context.
- `Azure.Core` — foundational Azure SDK HTTP transport; no direct advisory record confirmed in this pass.

## Open Questions

- Are there additional Azure.Identity advisories in 2025–2026 not surfaced by this pass (the GHSA search matched only 3 records)?
- Does CVE-2023-36414 affect only CLI/PowerShell credential providers, or does it also affect managed identity token-request paths that call platform APIs?
- What is the version distribution of Azure.Identity in production deployments? 1.9B total downloads suggests broad adoption, but the gap between 1.10.2 (Oct 2023) and 1.21.0 (Apr 2026) leaves many patch versions to audit.

## Related Pages

- [[dotnet/Microsoft.IdentityModel.JsonWebTokens]]
- [[dotnet/Microsoft.Data.SqlClient]]
- [[dotnet/Microsoft.AspNetCore.Authentication.Negotiate]]
- [[dotnet/index]]

---
*Last updated: 2026-08-24 | Sources: 3*
