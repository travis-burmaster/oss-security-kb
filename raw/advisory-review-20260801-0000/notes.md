# Advisory Review Notes — 2026-08-01

## Pass scope

Targets: `maven/com.thoughtworks.xstream/xstream`, `rust/ed25519-dalek`
Methodology: Public advisory database mapping only. No source-code review.
OSV.dev: blocked (HTTP 403) — not used.

---

## XStream (com.thoughtworks.xstream:xstream)

### Sources consulted

- `mcp__github__search_code` query: `xstream repo:github/advisory-database path:advisories` — 88 total results returned, 20 items shown.
- Individual GHSA JSON files fetched via WebFetch on `raw.githubusercontent.com/github/advisory-database/main/advisories/...`:

**2020:**
- `advisories/github-reviewed/2020/11/GHSA-mw36-7c6c-q4q2/GHSA-mw36-7c6c-q4q2.json` — CVE-2020-26217 RCE, fixed 1.4.14
- `advisories/github-reviewed/2020/12/GHSA-4cch-wxpw-8p28/GHSA-4cch-wxpw-8p28.json` — CVE-2020-26258 SSRF, fixed 1.4.15
- `advisories/github-reviewed/2020/12/GHSA-jfvx-7wrx-43fh/GHSA-jfvx-7wrx-43fh.json` — CVE-2020-26259 Arbitrary File Deletion, fixed 1.4.15

**March 2021 batch (fixed 1.4.16):**
- `advisories/github-reviewed/2021/03/GHSA-2p3x-qw9c-25hh/GHSA-2p3x-qw9c-25hh.json` — CVE-2021-21341 DoS
- `advisories/github-reviewed/2021/03/GHSA-hvv8-336g-rx3m/GHSA-hvv8-336g-rx3m.json` — CVE-2021-21342 SSRF
- `advisories/github-reviewed/2021/03/GHSA-74cv-f58x-f9wf/GHSA-74cv-f58x-f9wf.json` — CVE-2021-21343 file deletion
- `advisories/github-reviewed/2021/03/GHSA-59jw-jqf4-3wq3/GHSA-59jw-jqf4-3wq3.json` — CVE-2021-21344 ACE
- `advisories/github-reviewed/2021/03/GHSA-hwpc-8xqv-jvj4/GHSA-hwpc-8xqv-jvj4.json` — CVE-2021-21345 RCE (privileged)
- `advisories/github-reviewed/2021/03/GHSA-4hrm-m67v-5cxr/GHSA-4hrm-m67v-5cxr.json` — CVE-2021-21346 ACE
- `advisories/github-reviewed/2021/03/GHSA-qpfq-ph7r-qv6f/GHSA-qpfq-ph7r-qv6f.json` — CVE-2021-21347 ACE
- `advisories/github-reviewed/2021/03/GHSA-56p8-3fh9-4cvq/GHSA-56p8-3fh9-4cvq.json` — CVE-2021-21348 ReDoS
- `advisories/github-reviewed/2021/03/GHSA-f6hm-88x3-mfjv/GHSA-f6hm-88x3-mfjv.json` — CVE-2021-21349 SSRF
- `advisories/github-reviewed/2021/03/GHSA-43gc-mjxg-gvrq/GHSA-43gc-mjxg-gvrq.json` — CVE-2021-21350 ACE
- `advisories/github-reviewed/2021/03/GHSA-hrcp-8f3q-4w2c/GHSA-hrcp-8f3q-4w2c.json` — CVE-2021-21351 ACE (admin)

**Standalone (fixed 1.4.17):**
- `advisories/github-reviewed/2021/05/GHSA-7chv-rrw6-w6fc/GHSA-7chv-rrw6-w6fc.json` — CVE-2021-29505 RCE

**August 2021 batch (fixed 1.4.18):**
- `advisories/github-reviewed/2021/08/GHSA-64xx-cq4q-mf44/GHSA-64xx-cq4q-mf44.json` — CVE-2021-39139
- `advisories/github-reviewed/2021/08/GHSA-6wf9-jmg9-vxcc/GHSA-6wf9-jmg9-vxcc.json` — CVE-2021-39140
- `advisories/github-reviewed/2021/08/GHSA-g5w6-mrj7-75h2/GHSA-g5w6-mrj7-75h2.json` — CVE-2021-39141
- `advisories/github-reviewed/2021/08/GHSA-j9h8-phrw-h4fh/GHSA-j9h8-phrw-h4fh.json` — CVE-2021-39144
- `advisories/github-reviewed/2021/08/GHSA-8jrj-525p-826v/GHSA-8jrj-525p-826v.json` — CVE-2021-39145
- `advisories/github-reviewed/2021/08/GHSA-p8pq-r894-fm8f/GHSA-p8pq-r894-fm8f.json` — CVE-2021-39146
- `advisories/github-reviewed/2021/08/GHSA-h7v4-7xg3-hxcc/GHSA-h7v4-7xg3-hxcc.json` — CVE-2021-39147
- `advisories/github-reviewed/2021/08/GHSA-qrx8-8545-4wg2/GHSA-qrx8-8545-4wg2.json` — CVE-2021-39148
- `advisories/github-reviewed/2021/08/GHSA-3ccq-5vw3-2p6x/GHSA-3ccq-5vw3-2p6x.json` — CVE-2021-39149
- `advisories/github-reviewed/2021/08/GHSA-cxfm-5m4g-x7xp/GHSA-cxfm-5m4g-x7xp.json` — CVE-2021-39150
- `advisories/github-reviewed/2021/08/GHSA-hph2-m3g5-xxv4/GHSA-hph2-m3g5-xxv4.json` — CVE-2021-39151
- `advisories/github-reviewed/2021/08/GHSA-xw4p-crpj-vjx2/GHSA-xw4p-crpj-vjx2.json` — CVE-2021-39152
- `advisories/github-reviewed/2021/08/GHSA-2q8x-2p7f-574v/GHSA-2q8x-2p7f-574v.json` — CVE-2021-39153
- `advisories/github-reviewed/2021/08/GHSA-6w62-hx7r-mw68/GHSA-6w62-hx7r-mw68.json` — CVE-2021-39154

**2022:**
- `advisories/github-reviewed/2022/02/GHSA-rmr5-cpv2-vgjf/GHSA-rmr5-cpv2-vgjf.json` — CVE-2021-43859 DoS, fixed 1.4.19
- `advisories/github-reviewed/2022/12/GHSA-f8cc-g7j8-xxpm/GHSA-f8cc-g7j8-xxpm.json` — CVE-2022-40151 stack-overflow DoS, fixed 1.4.20

### Notes

- GHSA-9fwf-46g9-45rx confirmed to be woodstox-core (not xstream)
- GHSA-45rg-g72w-r393 confirmed to be jenkins-core (not xstream)
- GHSA-vwxj-6m5m-rrvh confirmed to be struts2-rest-plugin (uses xstream but not xstream itself)
- GHSA-hm5r-7fxm-9mrv confirmed to be Airtel Xstream Fiber IoT firmware (unrelated)
- CVE-2021-39142 and CVE-2021-39143 have no corresponding GHSA in the database (gap in sequence)
- CVE-2022-41966 (stack overflow via XmlReaderWrapper, reportedly fixed 1.4.21) not confirmed in database in this pass; noted as open question

---

## ed25519-dalek (Rust/crates.io)

### Sources consulted

- `mcp__github__search_code` query: `ed25519-dalek repo:rustsec/advisory-db path:crates` — 3 results, only 1 for ed25519-dalek itself
- Raw advisory: `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/ed25519-dalek/RUSTSEC-2022-0093.md` — fetched successfully
- crates.io API: `https://crates.io/api/v1/crates/ed25519-dalek` — returned: downloads=179,090,151, max_version=3.0.0, repository=github.com/dalek-cryptography/curve25519-dalek/tree/main/ed25519-dalek
- MystenLabs write-up: https://github.com/MystenLabs/ed25519-unsafe-libs (referenced in RUSTSEC)

### Notes

- Only 1 RUSTSEC advisory exists for ed25519-dalek: RUSTSEC-2022-0093
- The other 2 results from the search (RUSTSEC-2016-0005 for rust-crypto, RUSTSEC-2021-0137 for sodiumoxide) are different crates
- GHSA-w5vr-6qhr-36cc is the GitHub Advisory Database alias; JSON fetch was blocked in one attempt but content confirmed via RUSTSEC toml aliases field
- ed25519-dalek is now part of the dalek-cryptography monorepo under curve25519-dalek (merged since v2.0)
- The RUSTSEC advisory is dated 2022-06-11; patched = [">= 2"]; the vulnerability was discovered as part of the MystenLabs analysis of unsafe Ed25519 library APIs
