# Advisory Review — 2026-07-20 06:00 UTC

## Pass Summary

Targets: `linux/systemd` (new), `kubernetes/kube-proxy` (new); index corrections for Go (miekg/dns), Linux (sudo, cve-2026-31431-copy-fail).

OSV.dev API blocked (HTTP 403). All advisory content sourced from github/advisory-database via mcp__github__search_code + WebFetch on raw.githubusercontent.com.

## linux/systemd

### Sources consulted

| URL | Status | Notes |
|-----|--------|-------|
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-cm6j-6m6x-hmjq/GHSA-cm6j-6m6x-hmjq.json | 200 OK | CVE-2016-7796, systemd notify socket DoS |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-42xm-66qf-5jj8/GHSA-42xm-66qf-5jj8.json | 200 OK | CVE-2017-9445, systemd-resolved OOB write |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-h53q-m6g5-wfq9/GHSA-h53q-m6g5-wfq9.json | 200 OK | CVE-2018-16864, journald stack clash |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-5337-wcgc-wcvp/GHSA-5337-wcgc-wcvp.json | 200 OK | CVE-2021-33910, unit-name.c stack exhaustion |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/09/GHSA-f4r4-2gxf-88xj/GHSA-f4r4-2gxf-88xj.json | 200 OK | CVE-2022-2526, systemd-resolved UAF (Critical) |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/04/GHSA-396h-m3pm-fpm5/GHSA-396h-m3pm-fpm5.json | 200 OK | CVE-2026-40225, udev local root execution |
| GHSA-77qr-v44v-j2v3 (CVE-2018-16865) | 404 NOT FOUND | Companion journald stack-clash advisory not in database; noted in Open Questions |
| mcp__github__search_code: "systemd repo:github/advisory-database path:advisories" | 198 results | Filtered to systemd-specific records; most results were incidental mentions in other package advisories |

### Key findings

- CVE-2022-2526 (GHSA-f4r4-2gxf-88xj): CRITICAL CVSS 9.8, AV:N/AC:L/PR:N — the highest-severity confirmed systemd advisory in this pass. Network-exploitable UAF in systemd-resolved with full C/I/A impact. Fix commit d973d94dec349fb676fdd844f6fe2ada3538f27c confirmed via GHSA reference.
- CVE-2017-9445 (GHSA-42xm-66qf-5jj8): High CVSS 7.5 AV:N — also network-exploitable, systemd-resolved OOB write via malicious DNS TCP response. Affected through v233.
- CVE-2018-16864 (GHSA-h53q-m6g5-wfq9): High CVSS 7.8 AV:L — local privilege escalation in journald via long syslog command line. Qualys detailed write-up at https://www.qualys.com/2019/01/09/system-down/system-down.txt.
- CVE-2021-33910 (GHSA-5337-wcgc-wcvp): Moderate — stack exhaustion OS crash via unit-name.c strdupa/alloca. Affects 220–248.
- CVE-2016-7796 (GHSA-cm6j-6m6x-hmjq): Moderate — system hang via zero-length notify socket message.
- CVE-2026-40225 (GHSA-396h-m3pm-fpm5): Moderate (physical AV) — udev local root via malicious hardware. Fixed in v260.

### Not mapped (out of scope for this pass)

- CVE-2018-16865: Companion journald stack-clash; GHSA not found in database. Requires follow-up via NVD.
- CVE-2020-1712: TOCTOU race with D-Bus; deferred to future pass.
- Numerous distro-specific backport advisories (RHSA, DSA, USN) — upstream version-based fix data used instead.

## kubernetes/kube-proxy

### Sources consulted

| URL | Status | Notes |
|-----|--------|-------|
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/02/GHSA-wqv3-8cm6-h6wg/GHSA-wqv3-8cm6-h6wg.json | 200 OK | CVE-2020-8558, loopback adjacent-network bypass (reviewed) |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/10/GHSA-35c7-w35f-xwgh/GHSA-35c7-w35f-xwgh.json | 200 OK | CVE-2021-25736, Windows LoadBalancer forwarding bypass (reviewed) |
| mcp__github__search_code: "kube-proxy repo:github/advisory-database path:advisories" | 4 results | Only 2 were directly kube-proxy advisories; GHSA-8fg8-jh2h-f2hc (Cilium IPv6 interaction) and GHSA-m38g-vww2-mvgx (Talos/copy.fail) were noted as context/posture but not mapped as direct kube-proxy vulnerabilities |
| https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/05/GHSA-m38g-vww2-mvgx/GHSA-m38g-vww2-mvgx.json | 200 OK | CVE-2026-31431 (copy.fail) Talos Linux advisory; kube-proxy named as exploitation vector but is not the vulnerable component |

### Key findings

- Only 2 direct kube-proxy public advisories confirmed: CVE-2020-8558 (shared with kubelet, already in [[kubernetes/kubelet]]) and CVE-2021-25736 (Windows-only).
- The copy.fail / CVE-2026-31431 exploitation chain (GHSA-m38g-vww2-mvgx) specifically names kube-proxy as a privileged process whose executable can be poisoned via overlayfs page-cache; documented in Security Posture Notes as a kernel-level risk, not a kube-proxy code defect.
- Very sparse advisory history for kube-proxy compared to other Kubernetes components; this likely reflects both its relatively constrained code surface (primarily iptables/ipvs/nftables rule management) and the tendency for cross-component vulnerabilities to be filed against k8s.io/kubernetes as a whole.

## Index corrections discovered

- `wiki/index.md` shows `Go (21)` but `wiki/go/github.com/miekg/dns.md` exists on disk (created 2026-07-19 pass); master index was not updated at that time.
- `wiki/linux/index.md` lists only 7 pages but 9 exist on disk: `linux/sudo` and `linux/cve-2026-31431-copy-fail` were absent from the ecosystem index.

## Files changed this pass

- wiki/linux/systemd.md (new)
- wiki/kubernetes/kube-proxy.md (new)
- wiki/linux/index.md (add sudo, cve-2026-31431-copy-fail, systemd)
- wiki/kubernetes/index.md (add kube-proxy, remove from future targets)
- wiki/index.md (Go 21→22, Linux 9→10, Kubernetes 5→6, total 226→229, date 2026-07-14→2026-07-20)
- wiki/log.md (prepend entry)
