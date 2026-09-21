# Advisory Review — 2026-09-21 09:00 UTC

## Targets

### 1. python/pyopenssl (PyPI)
**Selection rationale:** One of the most-downloaded Python TLS/SSL libraries; no existing KB page; PyCA-maintained; recent 2026 advisories in GitHub Advisory Database.

**Sources consulted:**
- GitHub Advisory Database search: `filename:GHSA pyopenssl repo:github/advisory-database` → 6 results; 5 confirmed as directly affecting pyOpenSSL, 1 (GHSA-v4w5-p2hg-8fh6 / CVE-2016-9015) confirmed as urllib3-affecting (urllib3+PyOpenSSL TLS config) — excluded from pyopenssl page.
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/03/GHSA-5pwr-322w-8jr4/GHSA-5pwr-322w-8jr4.json — CVE-2026-27459, High, buffer overflow in DTLS cookie callback, fixed 26.0.0
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-6748-36qp-fx6r/GHSA-6748-36qp-fx6r.json — CVE-2013-4314, High, X509Extension null byte in SAN, fixed 0.13.1
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2018/10/GHSA-2rcm-phc9-3945/GHSA-2rcm-phc9-3945.json — CVE-2018-1000808, High, PKCS#12 DoS, fixed 17.5.0
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2018/10/GHSA-p28m-34f6-967q/GHSA-p28m-34f6-967q.json — CVE-2018-1000807, High CVSS 9.0, X509 use-after-free, fixed 17.5.0
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/03/GHSA-vp96-hxj8-p424/GHSA-vp96-hxj8-p424.json — CVE-2026-27448, Low, SNI callback exception bypass, fixed 26.0.0
- https://pypi.org/pypi/pyopenssl/json — latest stable version 26.4.0 (2026-08-01), repository https://github.com/pyca/pyopenssl
- pypistats.org — blocked (HTTP 403); download stats not obtained

**Excluded:**
- GHSA-v4w5-p2hg-8fh6 / CVE-2016-9015 — affects urllib3 1.17–1.18 (not pyOpenSSL directly); the advisory is about urllib3's TLS validation when used with PyOpenSSL + OpenSSL 1.1.0; included in urllib3 page scope, not pyopenssl scope

**Result:** 5 GHSA advisories mapped; page created as advisory-mapped.

---

### 2. rust/jsonwebtoken (crates.io)
**Selection rationale:** Dominant Rust JWT library (~192M downloads); no existing KB page; recent 2026 GHSA advisory; security-critical authentication boundary.

**Sources consulted:**
- GitHub Advisory Database search: `jsonwebtoken crates.io repo:github/advisory-database path:advisories` → 3 results
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/02/GHSA-h395-gr6q-cpjc/GHSA-h395-gr6q-cpjc.json — CVE-2026-25537, Moderate CVSS 4.0, claim type confusion → auth bypass, fixed 10.3.0; **confirmed direct jsonwebtoken advisory**
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/07/GHSA-gw59-x2xr-wwvr/GHSA-gw59-x2xr-wwvr.json — CVE-2026-63761, affects surrealdb (downstream consumer); GHSA-gw59-x2xr-wwvr was withdrawn as duplicate of GHSA-fwg2-gr34-q3w8; **excluded (downstream consumer, withdrawn)**
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/07/GHSA-fwg2-gr34-q3w8/GHSA-fwg2-gr34-q3w8.json — CVE-2026-63761, affects surrealdb (ES512→ES384 silent downgrade due to jsonwebtoken's lack of P-521 support); not a vulnerability in jsonwebtoken itself; **excluded (downstream consumer SurrealDB advisory)**
- RustSec advisory-db search: `repo:rustsec/advisory-db path:crates/jsonwebtoken` → 0 results; no RustSec advisories found
- https://crates.io/api/v1/crates/jsonwebtoken — total downloads 192,627,378; recent 49,320,753 (~16.4M/week); latest stable 11.1.0; repo https://github.com/Keats/jsonwebtoken

**Result:** 1 direct GHSA advisory mapped; 2 downstream SurrealDB entries excluded; page created as advisory-mapped.

---

## Index Updates
- wiki/python/index.md: pyopenssl added (33 → 34 pages)
- wiki/rust/index.md: jsonwebtoken added (42 → 43 pages)
- wiki/index.md: header 293 → 295, date 2026-09-19 → 2026-09-21, Python 33 → 34, Rust 42 → 43
- wiki/log.md: 2026-09-21 entry prepended
