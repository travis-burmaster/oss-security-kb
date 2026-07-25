# wasmtime (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~582K/week est. (7.57M 90-day; as of 2026-07-25)
**Repository:** https://github.com/bytecodealliance/wasmtime
**Security Contact:** https://github.com/bytecodealliance/wasmtime/security
**Disclosure Policy:** https://github.com/bytecodealliance/wasmtime/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-07-25 | OSS Security KB (nightly pass) | public advisory database mapping | automated lookup (RustSec advisory-db + GHSA) | 16 advisory records mapped | [rustsec/advisory-db](https://github.com/rustsec/advisory-db/tree/main/crates/wasmtime) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2021-0110 / CVE-2021-39216, CVE-2021-39218, CVE-2021-39219 | High (CVSS:3.1 AV:L/AC:H/PR:L I:H/A:H) | Three memory safety bugs: UAF in `Store::gc()`, OOB R/W in externref GC callbacks, type confusion in `Linker::func_wrap`/`func_new`. All exploitable by malicious WASM guests. | ≥ 0.30.0 | [GHSA-v4cp-h94r-m7xf](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-v4cp-h94r-m7xf) |
| RUSTSEC-2022-0016/0099 / CVE-2022-24791 | High | Use-after-free when both epoch interruption and externrefs are enabled; epoch interrupt can drop externrefs still in use by a WASM call. | ≥ 0.34.2 or ≥ 0.35.2 | [GHSA-gwc9-348x-qwv2](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-gwc9-348x-qwv2) |
| RUSTSEC-2022-0096 / CVE-2022-23636, CVE-2022-31169 | High | Invalid drop of `VMExternRef` from partially-initialized instances in the pooling allocator, enabling memory corruption. | ≥ 0.33.1 or ≥ 0.34.1 | [GHSA-88xq-w8cq-xfg7](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-88xq-w8cq-xfg7) |
| RUSTSEC-2022-0076 / CVE-2022-39392 | High (CVSS:3.1 AV:N C:H/I:H) | OOB read/write in pooling allocator when `instance_memory_pages` is set to 0; guest WASM can escape the linear-memory sandbox. | ≥ 1.0.2 or ≥ 2.0.2 | [GHSA-44mr-8vmm-wjhg](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-44mr-8vmm-wjhg) |
| RUSTSEC-2022-0095 / CVE-2022-31104 | Moderate | Miscompilation of `i8x16.swizzle` and `select` with v128 inputs on x86_64 — incorrect code generation produces wrong results or potential integrity violations. | ≥ 0.38.1 | [GHSA-jqwc-c49r-4w2x](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-jqwc-c49r-4w2x) |
| RUSTSEC-2022-0100 / CVE-2022-31146 | High | Use-after-free when externrefs are used inside async stores; UAF reachable by guest WASM. | ≥ 0.38.2 | [GHSA-5fhj-g3p3-pq9g](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-5fhj-g3p3-pq9g) |
| RUSTSEC-2022-0097 / CVE-2022-39394 | Low (CVSS:3.1 AV:L/AC:H) | OOB write in the `wasmtime_trap_code` C API function when trap code value exceeds expected range; limited exploitation potential (high-privilege attacker). | ≥ 1.0.2 or ≥ 2.0.2 | [GHSA-h84q-m8rr-3v9q](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-h84q-m8rr-3v9q) |
| RUSTSEC-2023-0090 / CVE-2023-26489 | **Critical (CVSS:3.1 9.9 AV:N/AC:L/PR:L S:C/C:H/I:H/A:H)** | Guest-controlled OOB read/write on x86_64: a Cranelift miscompilation allows malicious WASM to read/write arbitrary host memory outside the sandbox. Unauthenticated from the WASM perspective. | ≥ 4.0.1, ≥ 5.0.1, ≥ 6.0.1 | [GHSA-ff4p-7xrq-q5r8](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-ff4p-7xrq-q5r8) |
| RUSTSEC-2023-0093 / CVE-2023-27477 | Low (CVSS:3.1 3.1) | Miscompilation of `i8x16.select` when both inputs are identical on x86_64; integrity/correctness violation only. | ≥ 4.0.1, ≥ 5.0.1, ≥ 6.0.1 | [GHSA-xm67-587q-r2vw](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-xm67-587q-r2vw) |
| RUSTSEC-2024-0439 / CVE-2024-47813 | Low (CVSS:3.1 3.1 AV:L/AC:H) | Race condition under concurrent WASM execution allowing a guest to violate CFI and type safety guarantees. Requires multi-threaded embedding. | ≥ 21.0.2, ≥ 22.0.1, ≥ 23.0.3, ≥ 24.0.1, ≥ 25.0.2 | [GHSA-7qmx-3fpx-r45m](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-7qmx-3fpx-r45m) |
| RUSTSEC-2025-0046 / GHSA-fm79-3f68-h2fc | Low | WASIp1 `fd_renumber` syscall causes host-side panic (DoS); any guest calling fd_renumber with certain arguments can crash the host process. | ≥ 24.0.4, ≥ 33.0.2, ≥ 34.0.2 | [GHSA-fm79-3f68-h2fc](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-fm79-3f68-h2fc) |
| RUSTSEC-2025-0118 / CVE-2025-64345 | Low (CVSS:3.1 AV:L/PR:H) | Unsound Rust API when accessing WebAssembly shared linear memory; soundness violation can produce undefined behavior under specific high-privilege conditions. | ≥ 24.0.5, ≥ 36.0.3, ≥ 37.0.3, ≥ 38.0.4 | [GHSA-hc7m-r6v8-hg9q](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-hc7m-r6v8-hg9q) |
| RUSTSEC-2026-0020 / CVE-2026-27204 | Moderate | Guest-controlled resource exhaustion via WASI implementation; untrusted guest code can exhaust host resources and cause availability loss. | ≥ 24.0.6, ≥ 36.0.6, ≥ 40.0.4, ≥ 41.0.4 | [GHSA-852m-cvvp-9p4w](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-852m-cvvp-9p4w) |
| RUSTSEC-2026-0085 / CVE-2026-34943 | High (CVSS:4.0 VA:H) | Panic when lifting a `flags` Component Model value; any guest calling the Component Model flags API triggers a host process panic (DoS). | ≥ 24.0.7, ≥ 36.0.7, ≥ 42.0.2, ≥ 43.0.1 | [GHSA-m758-wjhj-p3jq](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-m758-wjhj-p3jq) |
| RUSTSEC-2026-0087 / CVE-2026-34944 | Low | Cranelift x86-64 miscompilation of `f64x2.splat` SIMD instruction can produce a host segfault or an out-of-sandbox memory load. | ≥ 24.0.7, ≥ 36.0.7, ≥ 42.0.2, ≥ 43.0.1 | [GHSA-qqfj-4vcm-26hv](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-qqfj-4vcm-26hv) |
| RUSTSEC-2026-0088 / CVE-2026-34988 | Low | Pooling allocator data leakage: one WASM instance can read stale memory from a previously-recycled slot belonging to a different instance. | ≥ 36.0.7, ≥ 42.0.2, ≥ 43.0.1 | [GHSA-6wgr-89rj-399p](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-6wgr-89rj-399p) |
| RUSTSEC-2026-0089 / CVE-2026-34946 | High (CVSS:4.0 VA:H AV:N) | Winch baseline compiler panics on `table.fill` instruction; guest-triggered host DoS. Affects only the optional Winch compiler path. | ≥ 36.0.7, ≥ 42.0.2, ≥ 43.0.1 | [GHSA-q49f-xg75-m9xw](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-q49f-xg75-m9xw) |

## Security Posture Notes

Wasmtime is the BytecodeAlliance's production Rust WebAssembly runtime, used as the WASM engine in Fastly Compute, Fermyon Spin, and many cloud sandbox platforms. It underpins `wasmtime-wasi`, the Component Model host runtime, and the Cranelift compiler backend.

BytecodeAlliance maintains a formal `SECURITY.md` with a GitHub security-advisory disclosure workflow and a coordinated-disclosure SLA. Security advisories are routinely back-ported to supported stable branches (e.g., the 24.x LTS line and recent majors). The advisory cadence is high relative to most crates (16 mapped here across 5 years), reflecting both the attack surface of a sandbox runtime and the project's diligent disclosure posture.

**Vulnerability pattern analysis:**
- **Cranelift miscompilations** (2022–2026): Incorrect code generation for SIMD/vector instructions (`i8x16.swizzle`, `i8x16.select`, `f64x2.splat`) periodically enables incorrect memory access or sandbox escape. x86-64 is consistently the affected architecture.
- **Externref / GC safety** (2021–2022): Multiple UAF and invalid-drop issues when `externref` type is combined with epoch interruption or the pooling allocator. All fixed in the 0.33–0.38 range; the externref GC model was subsequently redesigned.
- **Guest-controlled host panics** (2025–2026): Increasingly, guest WASM can cause host-process panics via WASI syscalls (`fd_renumber`) or Component Model operations (`flags` lifting, Winch `table.fill`). These are DoS-category but security-relevant in multi-tenant hosting.
- **Pooling allocator boundary** (2022, 2026): The pooling instance allocator has produced both OOB-write sandbox escapes (2022) and cross-instance data leakage (2026). Security-sensitive deployments using the pooling allocator should audit their version chain carefully.

The worst single advisory is **RUSTSEC-2023-0090 / CVE-2023-26489 (CVSS 9.9 Critical)**: a Cranelift miscompilation allowing arbitrary host memory read/write from guest WASM on x86_64. Any service that accepted untrusted WASM for execution on wasmtime < 4.0.1 / < 5.0.1 / < 6.0.1 was fully compromised.

Current stable: **wasmtime 47.0.2** (crates.io). All known advisories fixed in current release.

## Dependencies of Note

- **cranelift-codegen**: The Cranelift compiler backend is the root cause of several miscompilation advisories; it is a sibling crate, not a transitive dep in the traditional sense, but its version must track wasmtime exactly.
- **wasmtime-wasi**: Companion crate; RUSTSEC-2026-0182 / GHSA-3p27-qvp9-27qf (2026-06-15) affects `wasmtime-wasi` independently — advisory not mapped here as it targets the sibling crate.
- **wasmtime-jit-debug**: RUSTSEC-2024-0442 (unsoundness in JIT debug helper, 2024-07-06) affects the sibling crate; not mapped here.

## Open Questions

- Confirm exact CVE for RUSTSEC-2025-0046 (GHSA-fm79-3f68-h2fc has no CVE listed in the advisory DB at the time of this pass).
- Track wasmtime-wasi RUSTSEC-2026-0182 / GHSA-3p27-qvp9-27qf: guest-controlled host panic via WASI preview2 path — should be mapped on a separate `rust/wasmtime-wasi` page or noted here.
- Monitor Cranelift miscompilation frequency; the pattern suggests an ongoing need for fuzzing investment in code-generation paths.
- Verify current stable version (47.0.2) against any advisories published after 2026-07-25.

## Related Pages

- [[rust/index]]
- [[rust/h2]]
- [[rust/hyper]]
- [[rust/axum]]

---
*Last updated: 2026-07-25 | Sources: rustsec/advisory-db (16 advisories mapped), crates.io metadata*
