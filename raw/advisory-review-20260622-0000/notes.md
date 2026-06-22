# Advisory Review — 2026-06-22

## Pass metadata
- Date: 2026-06-22
- Ecosystems targeted: Kubernetes (runc), Go (golang.org/x/text), Linux (nginx)
- Primary source: github/advisory-database via GitHub MCP code search + raw.githubusercontent.com WebFetch
- OSV.dev API: blocked (HTTP 403) — not used
- Pages added: 3 (wiki/kubernetes/runc.md, wiki/go/golang.org-x-text.md, wiki/linux/nginx.md)

## Target selection rationale
- `runc` explicitly listed as a future target in wiki/kubernetes/index.md with CVE-2019-5736 and CVE-2024-21626 noted; Kubernetes ecosystem had only 3 pages
- `golang.org/x/text` foundational Go module (used by virtually every Go web app); Go ecosystem had 15 pages with this key transitive dep missing
- `nginx` critical Linux web server / reverse proxy, default Kubernetes Ingress Controller; Linux ecosystem had only 5 pages

## URLs consulted

### runc
- https://github.com/advisories/GHSA-gxmr-w5mj-v8hh (CVE-2019-5736 — /proc/self/exe container escape)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-gxmr-w5mj-v8hh/GHSA-gxmr-w5mj-v8hh.json
- https://github.com/advisories/GHSA-c3xm-pvg7-gh7r (CVE-2021-30465 — TOCTOU symlink mount race)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/05/GHSA-c3xm-pvg7-gh7r/GHSA-c3xm-pvg7-gh7r.json
- https://github.com/advisories/GHSA-f3fp-gc8g-vw66 (CVE-2022-29162 — inheritable capabilities)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-f3fp-gc8g-vw66/GHSA-f3fp-gc8g-vw66.json
- https://github.com/advisories/GHSA-vpvm-3wq2-2wvm (CVE-2023-27561 — access-control regression)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/03/GHSA-vpvm-3wq2-2wvm/GHSA-vpvm-3wq2-2wvm.json
- https://github.com/advisories/GHSA-g2j6-57v7-gm8c (CVE-2023-28642 — AppArmor/SELinux bypass)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/03/GHSA-g2j6-57v7-gm8c/GHSA-g2j6-57v7-gm8c.json
- https://github.com/advisories/GHSA-xr7r-f8xq-vfvv (CVE-2024-21626 — fd-leak container breakout)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/01/GHSA-xr7r-f8xq-vfvv/GHSA-xr7r-f8xq-vfvv.json
- https://pkg.go.dev/github.com/opencontainers/runc (version: v1.5.0 as of 2026-06-19)

### golang.org/x/text
- https://github.com/advisories/GHSA-5rcv-m4m3-hfh7 (CVE-2020-14040 — UTF-16 infinite loop)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/05/GHSA-5rcv-m4m3-hfh7/GHSA-5rcv-m4m3-hfh7.json
- https://github.com/advisories/GHSA-ppp9-7jff-5vj2 (CVE-2021-38561 — BCP 47 OOB read panic)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/12/GHSA-ppp9-7jff-5vj2/GHSA-ppp9-7jff-5vj2.json
- https://github.com/advisories/GHSA-69ch-w2m2-3vjp (CVE-2022-32149 — ParseAcceptLanguage DoS)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/10/GHSA-69ch-w2m2-3vjp/GHSA-69ch-w2m2-3vjp.json
- https://pkg.go.dev/golang.org/x/text (version: v0.38.0 as of 2026-06-08)
- Also noted (downstream misuse, not x/text advisories): GHSA-3g8v-8r37-cgjm (FrankenPHP CVE-2026-45062), GHSA-m675-2p33-xv9g (Caddy CVE-2026-45135)

### nginx
- https://github.com/advisories/GHSA-85mj-h68w-w736 (CVE-2017-7529 — range filter integer overflow)
- https://github.com/advisories/GHSA-c9vh-3f9g-f2xf (CVE-2019-20372 — HTTP request smuggling)
- https://github.com/advisories/GHSA-83p9-mcpm-374v (CVE-2021-23017 — DNS resolver off-by-one)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-83p9-mcpm-374v/GHSA-83p9-mcpm-374v.json
- https://github.com/advisories/GHSA-3v5h-538g-pr7g (CVE-2022-41741 — mp4 module memory corruption)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/10/GHSA-3v5h-538g-pr7g/GHSA-3v5h-538g-pr7g.json
- https://github.com/advisories/GHSA-wj45-j4gh-fm3x (CVE-2022-41742 — mp4 module memory disclosure)
- https://github.com/advisories/GHSA-3r23-64c4-mj87 (CVE-2024-7347 — mp4 module memory over-read)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2024/08/GHSA-3r23-64c4-mj87/GHSA-3r23-64c4-mj87.json
- nginx.org/en/security_advisories.html (referenced as primary disclosure location)
