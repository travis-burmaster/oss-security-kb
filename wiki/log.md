## [2026-08-19] advisory-review | dgrijalva/jwt-go (Go, new), image (Rust/crates.io, new)
Ran a public-information-only review pass targeting the Go and Rust/crates.io ecosystems. OSV.dev API blocked (HTTP 403); advisory content sourced from github/advisory-database and rustsec/advisory-db (via mcp__github__search_code and WebFetch on raw.githubusercontent.com). crates.io API accessible for image download stats; pkg.go.dev used for jwt-go importer count. Evidence saved under `raw/advisory-review-20260819-0000/notes.md`.

`go/github.com/dgrijalva/jwt-go` added as new advisory-mapped page with 1 confirmed advisory: CVE-2020-26160 / GHSA-w73w-5m7g-f7qc / GO-2020-0017 (High CVSS 3.1 7.5 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N / CWE-287 CWE-755: audience claim bypass — when a token's `aud` field is a JSON array `[]string{}`, the type assertion in `MapClaims.VerifyAudience` to `string` fails silently and the effective audience becomes `""`, bypassing audience checks in services that rely on jwt-go's result alone; no fix — package archived; migrate to github.com/golang-jwt/jwt ≥ 3.2.1). Package archived with no future patches; 29,217 packages import it on pkg.go.dev (2026-08-19). Advisory search: mcp__github__search_code returning total_count: 1 for "dgrijalva/jwt-go" in github/advisory-database; 1 advisory fetched and reviewed.

`rust/image` added as new advisory-mapped page with 2 confirmed advisories: RUSTSEC-2019-0014 / CVE-2019-16138 / GHSA-m2pf-hprp-3vqm (Critical CVSS 9.8 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H / CWE-416: HDR image format decoder — `HDRDecoder::read_image_transform` calls `Vec::set_len` on an uninitialized vector with a user-provided type parameter; if subsequent code panics before initialization completes, `Drop` runs on uninitialized memory, creating a use-after-free / ACE primitive via crafted HDR images; affects 0.10.2–0.21.2; fixed 0.21.3; 0.22+ introduces a safe pre-allocated-buffer interface); RUSTSEC-2020-0073 / CVE-2020-35916 / GHSA-9wgh-vjj7-7433 (Moderate CVSS 3.1 7.1 / CWE-119: mutable reference constructed from `slice::as_ptr()` instead of `slice::as_mut_ptr()` in 6 pixel-type conversion methods — creates aliased mutable references, UB per Rust aliasing rules; maintainers confirmed no evidence of miscompilation in practice; fixed 0.23.12). Notable finding: `mcp__github__search_code` for "image-rs/image" in github/advisory-database returned 5 results; 3 (GHSA-5qv7-j6w5-fr4m, GHSA-qg8r-f7x3-25f7, GHSA-w5p8-4jcx-2j6r) are for the companion `imageproc` crate (RUSTSEC-2026-0115/0116/0117, Moderate OOB reads in sampling/kernel), not `image`; documented as notes on the image page. image is the dominant Rust image I/O library at ~3.3M/week est., ~170M total crates.io downloads; current 0.25.10.

Go index updated from 25 to 26 pages; Rust index updated from 34 to 35 pages; master index updated from 256 to 258 pages.

## [2026-08-13] advisory-review | open-policy-agent/opa (Go, new), log4net (.NET/NuGet, new)
Ran a public-information-only review pass targeting the Go and .NET/NuGet ecosystems. OSV.dev API blocked (HTTP 403); advisory content sourced from github/advisory-database (via mcp__github__search_code and WebFetch on raw.githubusercontent.com). NuGet stats sourced from nuget.org. OPA GitHub stars and metadata retrieved via mcp__github__ tools. Evidence saved under `raw/advisory-review-20260813-0000/notes.md`.

`go/github.com/open-policy-agent/opa` added as new advisory-mapped page with 6 direct package advisories confirmed in github/advisory-database, plus 1 companion-package advisory (opa-envoy-plugin): CVE-2022-23628 / GHSA-hcw3-j74m-qc58 (Moderate CVSS 5.4: AST pretty-printer reorders array literals when printing synthetic nodes, silently altering compiled policy logic; fixed 0.37.2); CVE-2022-28946 / GHSA-x7f3-62pm-9p38 (High CVSS 7.5 AV:N: OOB memory access in ast/parser.go causing OPA server crash via crafted Rego; fixed 0.40.0); CVE-2022-33082 / GHSA-2m4x-4q9j-w97g (High: AST parser DoS via crafted input in ast/compile.go ~line 1224; fixed 0.42.0); CVE-2022-36085 / GHSA-f524-rf33-2jjr (High CVSS 7.1 AV:N: WithUnsafeBuiltins Go SDK restriction bypassed via Rego `with` keyword function mocking — sandbox escape for dangerous built-ins like http.send; fixed 0.43.1); CVE-2024-8260 / GHSA-c77r-fh37-x2px (Moderate AV:L: Windows SMB force-authentication — OPA passes an attacker-controlled SMB share path as a Rego file, causing NTLM credential hash leakage; fixed 0.68.0); CVE-2025-46569 / GHSA-6m8w-jc87-6cr7 (High CVSS:4.0 7.3: Data API HTTP path injection — OPA constructs a Rego query from the unsanitized request path, enabling policy oracle attacks, incorrect allow/deny decisions, and DoS via expensive computation; fixed 1.4.0); CVE-2026-26205 / GHSA-9f29-v6mm-pw6w (companion opa-envoy-plugin — High: double-slash path misinterpretation in input.parsed_path causing auth bypass when evaluated path differs from backend-received path; fixed 1.13.2-envoy-2). OPA is a CNCF-graduated policy engine (~12,097 GitHub stars); third-party Cure53 audit confirmed (2023). Advisory search: mcp__github__search_code returning 7 results for "open-policy-agent/opa" in github/advisory-database; all 7 fetched and individually reviewed.

`dotnet/log4net` added as new advisory-mapped page with 3 direct library advisories confirmed: CVE-2006-0743 / GHSA-f9fr-w54q-772h (Moderate CWE-134: format string vulnerability in LocalSyslogAppender in log4net 1.2.9; fixed 1.2.10); CVE-2018-1285 / GHSA-2cwj-8chv-9pp9 (Critical CVSS 9.8 AV:N/AC:L/PR:N: XXE injection — XML external entity processing not disabled in configuration file parsing; fixed 2.0.10); CVE-2026-40021 / GHSA-4f7c-pmjv-c25w (Moderate CVSS 5.3 AV:N: XmlLayout and XmlLayoutSchemaLog4J silently discard log events containing XML-1.0-forbidden characters, enabling audit-record suppression by attackers controlling log content; fixed 3.3.0). Two unreviewed GHSAs (GHSA-6vh7-mxw3-7f49 / CVE-2021-44028 and GHSA-64fx-j998-rqp7 / CVE-2023-45253) reference log4net in a downstream product context but are NOT direct log4net library advisories; documented as notes on the page. 418M+ total NuGet downloads; current stable 3.3.2 (2026-06-25). Key note: log4net is NOT affected by Log4Shell (CVE-2021-44228) — that vulnerability is specific to Java log4j 2.x. Advisory search: mcp__github__search_code returning 5 results for "log4net" in github/advisory-database; all 5 fetched and classified.

Go index updated from 24 to 25 pages; .NET index updated from 11 to 12 pages; master index updated from 254 to 256 pages.

## [2026-08-10] advisory-review | zerocopy (Rust/crates.io, new), sqlite (Homebrew, new); master-index corrections
Ran a public-information-only review pass targeting the Rust/crates.io and Homebrew ecosystems, plus corrections to the master wiki/index.md. OSV.dev API blocked (HTTP 403); advisory content sourced from rustsec/advisory-db and github/advisory-database (via mcp__github__search_code and WebFetch on raw.githubusercontent.com). crates.io API accessible for zerocopy download stats; formulae.brew.sh blocked (marked "unknown" for SQLite Homebrew downloads). Evidence saved under `raw/advisory-review-20260810-0000/notes.md`.

`rust/zerocopy` added as new advisory-mapped page with 1 confirmed advisory: RUSTSEC-2023-0074 / GHSA-3mv5-343c-w2qg / GHSA-rjhf-4mh8-9xjq (Moderate: unsoundness in `Ref::into_ref`, `into_mut`, `into_slice`, and `into_slice_mut` when the buffer type parameter is `cell::Ref<'_, T>` or `cell::RefMut<'_, T>`; safe callers can trigger undefined behaviour; mainstream usage patterns using slice/Vec references are unaffected; no CVE assigned; affects 0.2.2–0.2.8, 0.3.0–0.3.1, 0.4.0, 0.5.0–0.5.1, 0.6.0–0.6.5, 0.7.0–0.7.30; fixed 0.2.9 / 0.3.2 / 0.4.1 / 0.5.2 / 0.6.6 / 0.7.31; disclosed 2023-12-14). zerocopy is maintained by Google for Fuchsia OS and is used in Chromium, Android, and TensorFlow; ~17M/week est., ~792M total downloads as of 2026-08-10. Advisory search: 1 RUSTSEC in rustsec/advisory-db (crates/zerocopy/RUSTSEC-2023-0074.md); 2 github-reviewed GHSAs (both cover the same advisory); no additional advisories found for 0.8.x or 0.9.x lines.

`homebrew/sqlite` added as new advisory-mapped page with 2 confirmed advisories: CVE-2022-35737 / GHSA-jw36-hf63-69r9 / RUSTSEC-2022-0090 (High CVSS 9.1 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H: printf array-bounds overflow in `sqlite3_str_vappendf` when billions of bytes specified as string argument via C API; heap OOB write on 64-bit, integer overflow crash on 32-bit; affects SQLite 1.0.12 through 3.39.1 and all bundled wrappers including libsqlite3-sys < 0.25.1; fixed upstream 3.39.2 on 2022-08-04) and CVE-2025-6965 / GHSA-2m69-gcr7-jv3q (High CVSS 9.8 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H: aggregate function memory corruption — aggregate term count may exceed available result columns, triggering OOB access; affects SQLite before 3.50.2 and bundled wrappers including SQLitePCLRaw.lib.e_sqlite3 ≤ 2.1.11; fixed upstream 3.50.2 on 2025-06-21). Security posture notes include macOS system SQLite lag, high deployment surface (estimated 1 trillion devices), and references to sqlite.org/cves.html for the full upstream CVE history.

Master wiki/index.md corrections: (a) added missing `rust/prost` entry (omitted from 2026-08-09 pass); (b) added missing `dotnet/Microsoft.AspNetCore.Authentication.Negotiate` entry (omitted from 2026-08-09 pass); (c) corrected `linux/openssl` description from "baseline stub" to "advisory-mapped" (page was upgraded on 2026-07-19 but master index was not updated); (d) updated page counts: Rust 32→34, .NET 10→11, Homebrew 6→7, total 250→254.

Rust index updated from 33 to 34 pages; Homebrew index updated from 6 to 7 pages; master index updated from 250 to 254 pages.

## [2026-08-09] advisory-review | prost (Rust/crates.io, new), Microsoft.AspNetCore.Authentication.Negotiate (.NET/NuGet, new)
Ran a public-information-only review pass targeting the Rust/crates.io and .NET/NuGet ecosystems. OSV.dev API blocked (HTTP 403); advisory content sourced from rustsec/advisory-db and github/advisory-database (via mcp__github__search_code and WebFetch on raw.githubusercontent.com). crates.io API accessible for prost download stats; nuget.org accessible for Negotiate package download stats. Evidence saved under `raw/advisory-review-20260809-0000/notes.md`.

`rust/prost` added as new advisory-mapped page with 1 confirmed advisory: RUSTSEC-2020-0002 / CVE-2020-35858 / GHSA-gv73-9mwv-fwgq (Critical CVSS 9.8 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H / CWE-787: stack overflow when decoding deeply nested / recursive protobuf messages from untrusted input — on x86 with stack probes this causes controlled DoS; on ARM and architectures lacking stack probes the overflow is unsound and can corrupt adjacent stack frames or heap metadata, enabling potential remote code execution; affects all prost versions < 0.6.1; fixed ≥ 0.6.1 published 2020-01-16; GHSA published 2021-08-25). prost is the dominant Rust protobuf library at ~122M/week (~524M total downloads, 2026-08-09) and is the foundation for the tonic gRPC framework (already covered at rust/tonic). Advisory search: 1 GHSA in github/advisory-database (GHSA-gv73-9mwv-fwgq, August 2021 path); 1 RUSTSEC in advisory-db (crates/prost/RUSTSEC-2020-0002.md); no additional advisories found. zip crate (initial candidate) has no RUSTSEC advisories — pivoted to prost.

`dotnet/Microsoft.AspNetCore.Authentication.Negotiate` added as new advisory-mapped page with 2 confirmed GHSA advisories: CVE-2026-47300 / GHSA-8prm-248r-h957 (High CVSS 8.8 AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H / CWE-303: elevation of privilege in the ASP.NET Core Negotiate authentication handler via improper validation in LDAP role retrieval; affects .NET 8.0.0–8.0.28, .NET 9.0.0–9.0.17, .NET 10.0.0–10.0.9; fixed .NET 8 → 8.0.29, .NET 9 → 9.0.18, .NET 10 → 10.0.10; published 2026-07-21) and CVE-2026-47303 / GHSA-2p3q-h3hg-jcqq (High CVSS 8.8 / same vector: elevation of privilege via improper parsing + LDAP injection — authentication bypass by assumed-immutable data manipulation; same affected ranges; same fixes; published 2026-07-21). Both advisories require only low privilege (authenticated domain user) to exploit. Package is a first-party Microsoft ASP.NET Core package enabling Windows/Kerberos/NTLM authentication; ~56.3M total NuGet downloads; current stable 10.0.10. GHSA search returned total_count: 2 for "Authentication.Negotiate" in github/advisory-database — all advisories captured. StackExchange.Redis (initial candidate) has no GHSA advisories; pivoted to Negotiate.

Rust index updated from 32 to 33 pages; .NET index updated from 10 to 11 pages; master index updated from 250 to 252 pages.

## [2026-08-08] advisory-review | apache2 (Linux, new), rocket (Rust/crates.io, new)
Ran a public-information-only review pass targeting the Linux and Rust/crates.io ecosystems. OSV.dev API blocked (HTTP 403); advisory content sourced from github/advisory-database and rustsec/advisory-db (via mcp__github__search_code and WebFetch on raw.githubusercontent.com). NVD used as primary source for Apache httpd CVEs where GHSA path was not directly confirmed. crates.io API accessible for rocket download stats. Evidence saved under `raw/advisory-review-20260808-0000/`.

`linux/apache2` added as new advisory-mapped page with 11 confirmed CVEs spanning 2017–2024.

`rust/rocket` added as new advisory-mapped page with 2 confirmed RustSec advisories: RUSTSEC-2020-0028 (Moderate: LocalRequest::clone reuses raw pointer creating aliased mutable references — undefined behaviour enabling data races/memory corruption; affects 0.4.0–0.4.4; fixed 0.4.5); RUSTSEC-2021-0044 (Low: uri::Formatter use-after-free — &str transmuted to &'static str and pushed to stack vec; panic in user callback creates dangling reference enabling UAF during unwind or catch_unwind; affects < 0.4.7; fixed 0.4.7). Neither advisory has a CVE assigned. Current stable 0.5.1 unaffected. Download stats: ~12.5M total, ~1.2M/week (crates.io, 2026-08-08).

Linux index updated from 13 to 14 pages; Rust index updated from 31 to 32 pages; master index updated from 248 to 250 pages.

## [2026-08-07] advisory-review | go-git (Go, new), nix (Rust/crates.io, new)
Ran a public-information-only review pass targeting the Go and Rust/crates.io ecosystems. OSV.dev API blocked (HTTP 403); advisory content sourced from github/advisory-database and rustsec/advisory-db (via mcp__github__search_code and WebFetch on raw.githubusercontent.com). pkg.go.dev and crates.io APIs accessible for download stats. Evidence saved under `raw/advisory-review-20260807-0000/`.

`go/github.com/go-git/go-git` added as new advisory-mapped page with 6 confirmed GHSA advisories.

`rust/nix` added as new advisory-mapped page with 1 confirmed RustSec advisory: RUSTSEC-2021-0119 / CVE-2021-45707 / GHSA-76w9-p8mg-j927 / GHSA-wgrg-5h56-jg27 (High: heap buffer overflow in nix::unistd::getgrouplist for users with >16 group memberships; affects Linux/FreeBSD/Android/NetBSD/DragonFly/OpenBSD/Fuchsia; NOT macOS; versions < 0.16.0 unaffected; patched ≥ 0.20.2, ≥ 0.21.2, ≥ 0.22.2, ≥ 0.23.0). crates.io stats: ~710M total, ~12.1M/week est. as of 2026-08-07; max_version 0.31.3.

Go index updated from 23 to 24 pages; Rust index updated from 30 to 31 pages; master index updated from 246 to 248 pages.

## [2026-08-05] advisory-review | sqlx (Rust/crates.io, new), tonic (Rust/crates.io, new)
Rust index updated from 28 to 30 pages; master index updated from 244 to 246 pages.

## [2026-08-03] advisory-review | vim (Linux, new), Duende.IdentityServer (NuGet, new)
Linux index updated from 12 to 13 pages; .NET index updated from 9 to 10 pages; master index updated from 242 to 244 pages.

## [2026-08-01] advisory-review | xstream (Maven, new), ed25519-dalek (Rust, new)
Rust index updated from 27 to 28 pages; Maven index updated from 29 to 30 pages; master index updated from 240 to 242 pages.

## [2026-07-31] advisory-review | struts2-core (Maven, new), shiro-core (Maven, new)
Maven index updated from 27 to 29 pages; master index updated from 238 to 240 pages.

## [2026-07-26] advisory-review | argo-cd (Kubernetes, new), curve25519-dalek (Rust, new)
Kubernetes index updated from 7 to 8 pages; Rust index updated from 26 to 27 pages; master index updated from 236 to 238 pages.

## [2026-07-25] advisory-review | wasmtime (Rust, new), tar (Rust, new)
Rust index updated from 24 to 26 pages; master index updated from 234 to 236 pages.

## [2026-07-22] advisory-review | ingress-nginx (Kubernetes, new), jackc/pgx (Go, new)
Go index updated from 22 to 23 pages; Kubernetes index updated from 6 to 7 pages; master index updated from 229 to 231 pages.

## [2026-07-20] advisory-review | systemd (Linux, new), kube-proxy (Kubernetes, new); index corrections for Go, Linux
Linux index updated from 9 to 10 pages; Kubernetes count updated 5→6; master index updated from 226 to 229 pages.

## [2026-07-19] advisory-review | openssl (Linux, upgrade to advisory-mapped), miekg/dns (Go, new), serde (Rust, stats refresh)
Go index updated from 21 to 22 pages; master index updated from 226 to 227 pages.

## [2026-07-14] advisory-review | quinn (Rust/crates.io), Microsoft.Data.SqlClient (NuGet), imagemagick (Homebrew)
Rust index updated from 23 to 24 pages; .NET index updated from 8 to 9 pages; Homebrew index updated from 4 to 5 pages; master index updated from 223 to 226 pages.

## [2026-07-13] advisory-review | commons-text (Maven), gjson (Go), mio (Rust/crates.io)
Maven index updated from 26 to 27 pages; Go index updated from 20 to 21 pages; Rust index updated from 22 to 23 pages; master index updated from 220 to 223 pages.

## [2026-07-11] advisory-review | com.h2database:h2 (Maven), curl (Homebrew), YamlDotNet (NuGet); master-index correction for RestSharp
.NET index updated from 6 to 8 pages; Maven index updated from 25 to 26 pages; Homebrew index updated from 3 to 4 pages; master index updated from 216 to 220 pages.
