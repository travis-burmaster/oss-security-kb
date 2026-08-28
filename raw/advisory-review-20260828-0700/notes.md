# Advisory Review — 2026-08-28 07:00 UTC

## Targets

### rust/zip
- **crates.io API:** https://crates.io/api/v1/crates/zip — downloads: 250,111,502 all-time; recent: 64,015,424
- **RustSec advisory-db search:** `zip path:crates repo:rustsec/advisory-db` → 1 result in `crates/zip/`
- **RUSTSEC-2025-0168:** https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/zip/RUSTSEC-2025-0168.md
  - Alias: GHSA-94vh-gphv-8pm8, CVE-2025-29787
  - Path traversal via symlinks during extraction
  - Affects zip 1.3.0–2.2.x; fixed 2.3.0
  - CVSS 4.0 Medium
  - Published: 2026-03-16
  - Upstream advisory: https://github.com/zip-rs/zip2/security/advisories/GHSA-94vh-gphv-8pm8
- **GHSA advisory database:** No additional direct advisories for `zip` crate found
- **Note:** `crates/zip_next/RUSTSEC-2024-0337.md` is a separate package (`zip_next`), not mapped here

### go/github.com/microcosm-cc/bluemonday
- **pkg.go.dev:** https://pkg.go.dev/github.com/microcosm-cc/bluemonday — 2,680 known importers; latest v1.0.27 (2024-07-04)
- **GHSA search:** `bluemonday repo:github/advisory-database path:advisories` → 7 results
- **Direct package advisories (2):**
  - GHSA-3x58-xr87-2fcj / CVE-2021-29272: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/05/GHSA-3x58-xr87-2fcj/GHSA-3x58-xr87-2fcj.json
    - Cyrillic SCRIPT bypass; Moderate CVSS 6.1; fixed 1.0.5; published 2021-05-18
  - GHSA-x95h-979x-cf3j / CVE-2021-42576: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/10/GHSA-x95h-979x-cf3j/GHSA-x95h-979x-cf3j.json
    - SELECT/STYLE/OPTION element bypass; High (NVD CVSS 9.8); fixed 1.0.16; published 2021-10-19
- **Excluded advisories (downstream/not direct):**
  - GHSA-wmwp-pggc-h4mj (CVE-2019-19619): affects github.com/documize/community, not bluemonday
  - GHSA-xrcr-gmf5-2r8j (CVE-2026-26022): affects gogs.io/gogs (bluemonday misconfiguration)
  - GHSA-45q4-x4r9-8fqj (CVE-2026-35600): affects code.vikunja.io/api (missing sanitization)
  - GHSA-vcm5-gvmp-78mp (CVE-2026-52807): affects gogs.io/gogs (Semantic UI re-parsing bypass)
  - GHSA-3w28-36p9-w929 (CVE-2026-52816): affects gogs.io/gogs (data-URI in bluemonday UGC policy)

## Candidates Investigated but Not Pursued
- **rust/zeroize:** RustSec search found only RUSTSEC-2021-0115 for `zeroize_derive` (a companion crate, not the main `zeroize` crate). No direct `zeroize` crate RUSTSEC found.
- **go/github.com/klauspost/compress:** GHSA search returned GHSA-87m9-rv8p-rgmg which is for `go-grpc-compression` (which calls compress's Decoder.DecodeAll); no direct advisory on `klauspost/compress` itself found.
- **go/github.com/go-playground/validator:** No GHSA advisory found.
- **rust/zip_next:** RUSTSEC-2024-0337 found; separate package from `zip`, not a current investigation target.

## Master Index Corrections Applied This Pass
- `wiki/index.md` still showed 270 pages / 2026-08-26 despite the 2026-08-27 commit (PR #238) that added linux/rsync.md and dotnet/Swashbuckle.AspNetCore.md. Those files exist on disk but were not reflected in the master index. Corrected this pass to 274 (270+2 retroactive+2 new).
