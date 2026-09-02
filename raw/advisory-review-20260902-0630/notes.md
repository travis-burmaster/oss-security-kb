# Advisory Review — 2026-09-02 (0630 UTC)

## Targets

- `linux/bind9` — BIND 9 DNS server (ISC)
- `homebrew/python` — Homebrew Python formula (CPython)

## Sources Consulted

### BIND 9

| URL | Purpose |
|-----|----------|
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/05/GHSA-cqgq-ff3f-rj7r/GHSA-cqgq-ff3f-rj7r.json | CVE-2026-5946 DNS non-Internet class assertion failures |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/03/GHSA-vwv5-298p-pw28/GHSA-vwv5-298p-pw28.json | CVE-2026-3104 memory leak via crafted domain |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/05/GHSA-p65f-mhrm-vhrc/GHSA-p65f-mhrm-vhrc.json | CVE-2026-3039 TKEY/GSS-API memory exhaustion |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/07/GHSA-89q8-qc36-7m58/GHSA-89q8-qc36-7m58.json | CVE-2026-13204 DNSSEC NSEC/NSEC3 assertion DoS |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/07/GHSA-qhh7-j7w3-xfxq/GHSA-qhh7-j7w3-xfxq.json | CVE-2026-11605 excessive RRSIG validation CPU exhaustion |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/07/GHSA-8p39-mp4q-99c8/GHSA-8p39-mp4q-99c8.json | CVE-2026-11331 RPZ wildcard CNAME NAMETOOLONG crash |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/05/GHSA-63mj-2fw3-4w3h/GHSA-63mj-2fw3-4w3h.json | CVE-2026-3592 resolver resource exhaustion |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/07/GHSA-4fw4-hmvf-4www/GHSA-4fw4-hmvf-4www.json | CVE-2026-10723 NSEC3 NXDOMAIN forgery |
| mcp__github__search_code: `bind9 isc repo:github/advisory-database path:advisories` | Initial advisory discovery (31 total results) |

### CPython / homebrew/python

| URL | Purpose |
|-----|----------|
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/06/GHSA-9mc4-rqmq-h467/GHSA-9mc4-rqmq-h467.json | CVE-2026-11940 tarfile hardlink→symlink traversal |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2024/12/GHSA-ph84-rcj2-fxxm/GHSA-ph84-rcj2-fxxm.json | CVE-2024-12254 asyncio writelines() OOM |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/03/GHSA-rm92-fj5q-mpj5/GHSA-rm92-fj5q-mpj5.json | CVE-2026-4519 webbrowser.open() leading-dash CLI injection |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/04/GHSA-8r9f-h969-mm4m/GHSA-8r9f-h969-mm4m.json | CVE-2026-3446 base64 silent truncation |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2024/07/GHSA-r8h6-cwxj-rv5j/GHSA-r8h6-cwxj-rv5j.json | CVE-2024-3219 socket.socketpair() race on Windows |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/08/GHSA-2345-wr3r-cxf2/GHSA-2345-wr3r-cxf2.json | CVE-2026-18503 csv.Sniffer ReDoS |
| mcp__github__search_code: `python cpython repo:github/advisory-database path:advisories` | Initial advisory discovery (138 total results) |

## Blocked Endpoints

- `https://api.osv.dev` — HTTP 403 (network policy)
- `https://formulae.brew.sh/api/formula/python@3.13.json` — blocked by egress proxy

## Findings Summary

- BIND 9: 8 confirmed 2026 GHSA advisories mapped; historical ISC archive not included in GHSA database search results
- CPython/homebrew/python: 6 confirmed GHSA advisories from 2024–2026 mapped; 138 total GHSA records exist for CPython — only the most recent non-superseded advisories captured in this pass
