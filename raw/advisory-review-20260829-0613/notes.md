# Advisory Review Pass — 2026-08-29 06:13 UTC

## Targets Selected

1. **go/github.com/gofiber/fiber** — Express-inspired Go web framework, 40,100+ GitHub stars, 30,850+ pkg.go.dev importers for v2. Not previously in the KB; strong advisory history.
2. **rust/lettre** — Dominant Rust email sending library, 16M+ total crates.io downloads. Not previously in the KB; 3 confirmed GHSA advisories.

## OSV.dev Status

`https://api.osv.dev` returned HTTP 403 (network policy block). All advisory data sourced from primary sources below.

## Sources Consulted

### go/github.com/gofiber/fiber

- GitHub advisory database search: `mcp__github__search_code` with `repo:github/advisory-database gofiber fiber` → 19 results
- WebFetch on raw.githubusercontent.com for each of the 19 GHSA JSON files:
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/02/GHSA-fmg4-x8pw-hjhg/GHSA-fmg4-x8pw-hjhg.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/05/GHSA-qjv7-627w-8qjv/GHSA-qjv7-627w-8qjv.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/02/GHSA-mrq8-rjmw-wpq3/GHSA-mrq8-rjmw-wpq3.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/07/GHSA-98j2-3j3p-fw2v/GHSA-98j2-3j3p-fw2v.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/02/GHSA-68rr-p4fp-j59v/GHSA-68rr-p4fp-j59v.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/02/GHSA-m3c2-496v-cw3v/GHSA-m3c2-496v-cw3v.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/08/GHSA-qx2q-88mx-vhg7/GHSA-qx2q-88mx-vhg7.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/05/GHSA-hg3g-gphw-5hhm/GHSA-hg3g-gphw-5hhm.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/09/GHSA-3q5p-3558-364f/GHSA-3q5p-3558-364f.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/04/GHSA-35hp-hqmv-8qg8/GHSA-35hp-hqmv-8qg8.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/01/GHSA-4mq2-gc4j-cmw6/GHSA-4mq2-gc4j-cmw6.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/07/GHSA-g5vh-55hw-rxm8/GHSA-g5vh-55hw-rxm8.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-927h-x4qj-r242/GHSA-927h-x4qj-r242.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/06/GHSA-9cx9-x2gp-9qvh/GHSA-9cx9-x2gp-9qvh.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/07/GHSA-gv83-gqw6-9j2c/GHSA-gv83-gqw6-9j2c.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/12/GHSA-m98w-cqp3-qcqr/GHSA-m98w-cqp3-qcqr.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/10/GHSA-94w9-97p3-p368/GHSA-94w9-97p3-p368.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/02/GHSA-2mr3-m5q5-wgp6/GHSA-2mr3-m5q5-wgp6.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/10/GHSA-mv73-f69x-444p/GHSA-mv73-f69x-444p.json
- pkg.go.dev/github.com/gofiber/fiber/v2 — importer count (30,850) and version (v2.52.15)
- pkg.go.dev/github.com/gofiber/fiber/v3 — importer count (1,480) and version (v3.5.0)
- github.com/gofiber/fiber — star count (40.1k) and security policy link
- github.com/gofiber/fiber/security/policy — disclosure contact and supported versions

### rust/lettre

- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/lettre/RUSTSEC-2021-0069.md — SMTP command injection advisory text
- mcp__github__search_code: `repo:github/advisory-database lettre` → 6 results (2 reviewed, 4 unreviewed)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/08/GHSA-vc2p-r46x-m3vx/GHSA-vc2p-r46x-m3vx.json — Sendmail argument injection
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/07/GHSA-qc36-q22q-cjw3/GHSA-qc36-q22q-cjw3.json — SMTP command injection
- github.com/lettre/lettre/security/advisories — GitHub security advisory listing (revealed GHSA-4pj9-g833-qx53)
- github.com/lettre/lettre/security/advisories/GHSA-4pj9-g833-qx53 — TLS hostname verification bypass (boring-tls backend)
- https://crates.io/api/v1/crates/lettre — download stats (16,047,511 total; 5,452,102 recent; stable 0.11.23)

## Advisory Counts

- gofiber/fiber: 19 GHSA advisories confirmed (all reviewed, from github/advisory-database). 17 on core fiber module; 2 on first-party companion packages (gofiber/template/django, gofiber/utils).
- lettre: 3 GHSA advisories confirmed (2 from github/advisory-database reviewed; 1 from lettre GitHub security advisory page). RUSTSEC-2021-0069 is the RustSec record for GHSA-qc36-q22q-cjw3.

## Excluded / Deferred

- gofiber/fiber: GHSA-4mq2-gc4j-cmw6 (CVE-2024-22199) affects `gofiber/template/django/v3`, not the core fiber module. Included in the page with clear attribution to the companion package.
- gofiber/fiber: GHSA-m98w-cqp3-qcqr (CVE-2025-66565) affects `gofiber/utils` and `gofiber/utils/v2`. Included in the page with clear attribution.
- lettre: GHSA-4229-qg79-m48h, GHSA-53xp-3w48-mgww, GHSA-xr84-8x72-rcj7 (unreviewed, 2022-05) and GHSA-7cmx-pq9m-76p5 (unreviewed, 2023-06) — not verified as applying to the lettre crate itself vs downstream consumers; noted as open question.
