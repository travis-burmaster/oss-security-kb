# Advisory Review Notes — 2026-06-21-0000

## Targets

- **rust/rustls** (crates.io) — 2 RUSTSEC advisories
- **rust/chrono** (crates.io) — 1 RUSTSEC advisory
- **kubernetes/containerd** (GHSA) — 21 GHSA advisories

## Sources Consulted

### rustsec/advisory-db (via raw.githubusercontent.com + GitHub MCP code search)
- `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/rustls/RUSTSEC-2024-0336.md`
- `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/rustls/RUSTSEC-2024-0399.md`
- `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/chrono/RUSTSEC-2020-0159.md`

### github/advisory-database (via raw.githubusercontent.com)
- `GHSA-36xw-fx78-c5r4` — CVE-2020-15257 — containerd-shim API exposed to host-network containers
- `GHSA-6g2q-w5j3-fwh4` — CVE-2021-21334 — environment variable leak between containers
- `GHSA-c72p-9xmj-rx3w` — CVE-2021-32760 — archive chmod outside unpack target
- `GHSA-c2h3-6mxw-7mvq` — CVE-2021-41103 — insufficiently restricted plugin directory permissions
- `GHSA-mvff-h3cj-wj9c` — CVE-2021-43816 — hostPath SELinux LSM bypass
- `GHSA-crp2-qrr5-8pq7` — CVE-2022-23648 — insecure image volume handling in CRI (High CVSS 9.1)
- `GHSA-c9cp-9c75-9v8c` — non-empty inheritable Linux process capabilities (Low)
- `GHSA-5ffw-gxpp-mxpf` — CVE-2022-31030 — ExecSync host memory exhaustion
- `GHSA-2qjp-425j-52j9` — CVE-2022-23471 — CRI stream server goroutine leak
- `GHSA-hmfx-3pcx-653p` — CVE-2023-25173 — supplementary groups not set up properly
- `GHSA-7ww5-4wqc-m92c` — RAPL side-channel exposure
- `GHSA-pwhc-rpq9-4c8w` — CVE-2024-25621 — broad directory permissions, local privilege escalation
- `GHSA-265r-hfxg-fhmg` — CVE-2024-40635 — UID integer overflow; container runs as root
- `GHSA-cm76-qm8v-3j95` — CVE-2025-47290 — TOCTOU in image unpacking (High)
- `GHSA-cxfp-7pvr-95ff` — CVE-2025-47291 — user-namespaced pods outside k8s cgroup hierarchy
- `GHSA-m6hq-p25p-ffr2` — CVE-2025-64329 — CRI Attach goroutine leak memory exhaustion
- `GHSA-fqw6-gf59-qr4w` — CVE-2026-46680 — oversized UID parsed as username; runAsNonRoot bypass
- `GHSA-cvxm-645q-p574` — CVE-2026-50195 — CRI checkpoint import local image tag poisoning
- `GHSA-xhf5-7wjv-pqxp` — CVE-2026-53488 — image LABEL → restart-monitor binary logger (host RCE)
- `GHSA-rgh6-rfwx-v388` — CVE-2026-53489 — symlink log-file read via checkpoint restore
- `GHSA-33vj-92qq-66hc` — CVE-2026-53492 — CDI annotation smuggling via checkpoint restore

### crates.io API
- `https://crates.io/api/v1/crates/rustls` — total: 719,178,289; recent_downloads: 165,008,339; latest: 0.23.40
- `https://crates.io/api/v1/crates/chrono` — total: 635,453,111; recent_downloads: 125,700,595; latest: 0.4.45

### GitHub MCP code search
- `repo:rustsec/advisory-db rustls path:crates` — 14 results; 2 direct rustls advisories identified
- `repo:rustsec/advisory-db chrono path:crates` — 7 results; 1 direct chrono advisory (RUSTSEC-2020-0159)
- `repo:github/advisory-database containerd GHSA path:advisories` — 33 results; 21 containerd/containerd advisories confirmed

## OSV.dev
Blocked by network policy (HTTP 403). All advisory content sourced from rustsec/advisory-db and github/advisory-database directly.

## Scope Decisions
- GHSA-8v99-48m9-c8pm excluded: belongs to `containerd/imgcrypt`, not `containerd/containerd`.
- GHSA-5j5w-g665-5m35 and GHSA-742w-89gc-8m9c appeared in search results but were not fetched; excluded from this pass to maintain source-citation integrity (no citation without fetched content).
- rustls-webpki advisories (RUSTSEC-2023-0053, RUSTSEC-2026-0049, -0098, -0099, -0104) noted in rustls Dependencies of Note section but not expanded into separate pages in this pass.
- RUSTSEC-2020-0071 (`time` crate advisory) mentioned in chrono notes section as related background but not listed as a chrono package-level advisory.
