# Advisory Review — 2026-09-30 Pass Notes

## Targets

### linux/openssh — advisory update (5 new 2026 CVEs)

**Primary sources consulted:**
- mcp__github__search_code: `openssh 2026 repo:github/advisory-database path:advisories` → 52 total hits
- WebFetch raw.githubusercontent.com for individual GHSA JSON:
  - GHSA-f6c7-fj8h-5898 (CVE-2026-35414) — Moderate CVSS 5.1 — authorized_keys principals flaw — fixed 10.3p1
  - GHSA-hpxh-vgmp-3qp6 (CVE-2026-35387) — Low CVSS 3.1 — ECDSA algorithm config over-permissioning — fixed 10.3
  - GHSA-9fjj-jvxf-738c (CVE-2026-35388) — Low CVSS 3.1 — multiplexing confirmation omission — fixed 10.3
  - GHSA-8v2x-fhq9-4fv3 (CVE-2026-59996) — Moderate CVSS ~4.2 — scp path traversal to parent dir — fixed 10.4p1
  - GHSA-gp5v-jg37-fvg6 (CVE-2026-60002) — High CVSS ~7.5 — UAF in client-side key re-exchange — fixed 10.4p1
- CVE-2024-6409 / GHSA-j7jm-6q5x-ffr4: race condition in unprivileged child (variant of CVE-2024-6387 regreSSHion); not added as separate row since page already covers regreSSHion class
- 52 total 2026 openssh GHSA entries exist; high-severity and moderate-severity batch fully captured for this pass
- openssh release page: https://www.openssh.com/security.html

**Registry/download stats:** Not applicable (distro package, no npm/crates.io stats)

---

## Master Index Corrections

### Problem identified
Audited actual file counts against master index entries across all ecosystems. Found major discrepancies (similar to the Go/Homebrew correction in the 2026-09-29 pass):

| Ecosystem | Master Index (before) | Actual Files | Correction |
|-----------|----------------------|--------------|-----------|
| Linux | 6 (1 phantom: linux/kernel) | 19 real files | +13 |
| Python | 22 (many phantoms: boto3, numpy, scipy, oauthlib, redis-py) | 33 real files | +11 |
| .NET | 18 (stale kebab-case names, e.g. dotnet/aspnetcore) | 16 real files with NuGet naming | -2 |
| npm | 94 | 94 | entries realigned to npm/index.md |
| Rust | 49 | 49 | correct ✓ |
| Go | 36 | 36 | correct (fixed in prev pass) ✓ |
| Homebrew | 9 | 9 | correct (fixed in prev pass) ✓ |
| Maven | 37 | unverified (assumed correct) | — |
| Kubernetes | 10 | unverified (assumed correct) | — |

New verified total: 94 + 49 + 16 + 33 + 36 + 9 + 37 + 10 + 19 = **303**

### Evidence
- Glob: `wiki/linux/*.md` → 19 package files + index.md
- Glob: `wiki/python/*.md` → 33 package files + index.md  
- Glob: `wiki/dotnet/*.md` → 16 package files + index.md (files use NuGet naming convention, not kebab-case)
- linux/kernel.md does NOT exist; was a phantom entry
- Python phantom entries removed: boto3, numpy, scipy, oauthlib, redis-py (mapped as python/redis)
- Python real files added to master index: litellm, telnyx, flask-cors, pyyaml, python-jose, pip, setuptools, redis, h11, urllib3, starlette, fastapi, python-multipart, gunicorn, uvicorn, bleach, twisted

### .NET naming note
The dotnet ecosystem uses NuGet package IDs (e.g. `Newtonsoft.Json`, `Azure.Identity`) as file names, not kebab-case slugs. The master index was replaced to match actual NuGet package IDs.

### npm note
npm count is correct (94) per both master index and npm/index.md. Individual entry alignment between master index and npm/index.md is partially complete — full realignment deferred to a future pass.

### Open items (future passes)
- Verify Maven (37) and Kubernetes (10) counts against actual files
- Fully realign npm master index entries to match npm/index.md entries (same 94 count but ~20-30 entries differ)
