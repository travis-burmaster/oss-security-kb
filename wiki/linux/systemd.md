# systemd (Linux)

**Registry:** distro
**Weekly Downloads:** N/A — pre-installed on all major Linux distributions using systemd as init system (Ubuntu ≥ 15.04, RHEL / CentOS / Fedora ≥ 7/15, Debian ≥ 8, Arch Linux, openSUSE / SLES ≥ 12.1, and virtually all cloud base images)
**Repository:** https://github.com/systemd/systemd
**Security Contact:** security@systemd.io
**Disclosure Policy:** https://github.com/systemd/systemd/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2016-7796 / GHSA-cm6j-6m6x-hmjq | Moderate (CVSS 5.5 AV:L) | Denial of Service — `manager_dispatch_notify_fd` in systemd allows local users to hang the system via a zero-length message over a notify socket, disabling the notification handler entirely | ≥ 232 | [GHSA-cm6j-6m6x-hmjq](https://github.com/advisories/GHSA-cm6j-6m6x-hmjq) |
| CVE-2017-9445 / GHSA-42xm-66qf-5jj8 | High (CVSS 7.5 AV:N/AC:L/PR:N) | Out-of-bounds Write in systemd-resolved — `dns_packet_new` allocates a buffer that is too small for certain DNS response sizes; a malicious DNS server can send a crafted TCP payload causing arbitrary data to be written past the allocation boundary | ≥ 234 (affected: through 233) | [GHSA-42xm-66qf-5jj8](https://github.com/advisories/GHSA-42xm-66qf-5jj8) |
| CVE-2018-16864 / GHSA-h53q-m6g5-wfq9 | High (CVSS 7.8 AV:L/AC:L/PR:L) | Stack Clash in systemd-journald — unbounded `strdupa` / `alloca` allocation when a program with very long command-line arguments calls syslog; a local attacker can crash journald or escalate privileges | ≥ 241 (affected: through 240) | [GHSA-h53q-m6g5-wfq9](https://github.com/advisories/GHSA-h53q-m6g5-wfq9) |
| CVE-2021-33910 / GHSA-5337-wcgc-wcvp | Moderate (CVSS AV:L/AC:L/PR:L/A:H) | Stack Exhaustion / OS Crash — `unit-name.c` uses `strdupa` and `alloca` for a pathname controlled by a local attacker (e.g., via FUSE mount), exhausting the stack and crashing the OS | ≥ 249 (affected: 220 through 248) | [GHSA-5337-wcgc-wcvp](https://github.com/advisories/GHSA-5337-wcgc-wcvp) |
| CVE-2022-2526 / GHSA-f4r4-2gxf-88xj | Critical (CVSS 9.8 AV:N/AC:L/PR:N) | Use-After-Free in systemd-resolved — `on_stream_io()` and `dns_stream_complete()` in `resolved-dns-stream.c` fail to increment the `DnsStream` reference count, enabling remote callers to trigger use-after-free; full C/I/A impact | see upstream fix commit [d973d94](https://github.com/systemd/systemd/commit/d973d94dec349fb676fdd844f6fe2ada3538f27c) | [GHSA-f4r4-2gxf-88xj](https://github.com/advisories/GHSA-f4r4-2gxf-88xj) |
| CVE-2026-40225 / GHSA-396h-m3pm-fpm5 | Moderate (CVSS AV:P/AC:H/C:H/I:H/A:H) | Local Root via udev — unsanitized kernel output from malicious hardware devices can be used to achieve local root execution in udev; physical access to the machine is required | ≥ 260 (affected: < 260) | [GHSA-396h-m3pm-fpm5](https://github.com/advisories/GHSA-396h-m3pm-fpm5) / [GHSA-vpfq-8p5f-jcqx](https://github.com/systemd/systemd/security/advisories/GHSA-vpfq-8p5f-jcqx) |

*OSV live record: https://osv.dev/list?ecosystem=Linux&q=systemd*

## Security Posture Notes

systemd is the dominant init system and service manager for Linux, present on virtually every modern production Linux distribution and cloud base image. Its attack surface is unusually broad: it manages process lifecycle for the entire system and hosts over 50 component services that run as root or with elevated privileges, including systemd-resolved (network-facing DNS resolver on 127.0.0.53:53 by default), systemd-journald (syslog aggregator), systemd-networkd, systemd-logind, udev (hardware event processing), and systemd-tmpfiles.

**systemd-resolved (network-facing):** Both CVE-2017-9445 (remote OOB write via malicious DNS TCP response, affects systems querying attacker-controlled DNS servers) and CVE-2022-2526 (critical unauthenticated UAF, CVSS 9.8) target systemd-resolved. Systems that route DNS through systemd-resolved (the default on Ubuntu and many other distributions) are directly exposed if DNS traffic is handled by an attacker-controlled or untrusted resolver.

**systemd-journald (syslog consumer):** CVE-2018-16864 exploits journald's handling of syslog messages from processes with extremely long command lines. Since journald aggregates logs from all system services, the attack surface is reachable from any local process that can invoke syslog. The Qualys team published a detailed analysis (https://www.qualys.com/2019/01/09/system-down/system-down.txt).

**udev (hardware event processing):** CVE-2026-40225 demonstrates that the udev component — which processes kernel-supplied strings from hardware device metadata — must be treated as a trust boundary. Physical access to plug in a malicious device is sufficient to trigger root execution. This is particularly relevant for devices accessible in shared physical environments or via Thunderbolt/USB hot-plug.

**Disclosure policy:** The project uses coordinated disclosure via security@systemd.io and publishes security advisories on its GitHub security advisories page (https://github.com/systemd/systemd/security/advisories). Distro security teams (Red Hat, Ubuntu, Debian) typically handle backports; check distro-specific errata for patched package versions.

## Dependencies of Note

- `libsystemd` / `sd-bus` — the D-Bus IPC layer used by most systemd components; D-Bus privilege boundaries are a recurring security consideration in the ecosystem.
- `libudev` — userspace API for udev events; packages linking `libudev` are indirectly exposed to udev-side vulnerabilities.
- `polkit` — PolicyKit integrates with systemd-logind for privilege escalation decisions; polkit vulnerabilities (e.g., CVE-2021-3560, CVE-2021-4034 PwnKit) interact with the systemd privilege model.
- `linux/glibc` — glibc's `localtime_r` / environment variable mutation race (see RUSTSEC-2020-0159 / CVE-2020-26235 in the Rust chrono crate) originates from the same underlying OS interface that systemd's time and locale handling uses.

## Open Questions

- CVE-2018-16865 (companion stack-clash advisory to CVE-2018-16864): a second stack-based buffer overflow in journald via attacker-controlled log messages; GHSA entry GHSA-77qr-v44v-j2v3 returned 404 in the advisory database — verify current status in NVD or upstream.
- CVE-2022-2526 fixed version: the upstream fix commit (d973d94) is confirmed, but the specific release tag incorporating the fix is not stated in the GHSA record; a follow-up pass should confirm whether it was included in v251.x or v252.
- systemd-resolved DNSSEC validation: whether the DNSSEC processing path introduces additional parsing-boundary risks beyond what CVE-2022-2526 exposed.
- udev rule injection surface: whether the CVE-2026-40225 fix in v260 fully addresses all unsanitized kernel attribute paths or only the specifically reported device vector.

## Related Pages

- [[linux/glibc]] — libc underpinning most systemd component builds
- [[linux/openssh]] — relies on systemd socket activation in many distributions
- [[linux/index]]

---
*Last updated: 2026-07-20 | Sources: 6 (GHSA-cm6j-6m6x-hmjq, GHSA-42xm-66qf-5jj8, GHSA-h53q-m6g5-wfq9, GHSA-5337-wcgc-wcvp, GHSA-f4r4-2gxf-88xj, GHSA-396h-m3pm-fpm5)*
