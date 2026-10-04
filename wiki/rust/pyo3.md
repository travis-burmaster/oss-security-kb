# pyo3 (crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~10.5M/week estimated (63,140,744 recent 90-day downloads; 266,118,612 all-time as of 2026-10-04)
**Repository:** https://github.com/pyo3/pyo3
**Security Contact:** https://github.com/pyo3/pyo3/security (GitHub security advisories)
**Disclosure Policy:** https://github.com/pyo3/pyo3/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2026-0013 / GHSA-47qc-857f-7w7f | High | Type confusion in `abi3` feature with Python 3.12+: subclasses of `#[pyclass(extends=PyList)]` (and other native Python types) used the subclass type during data access memory operations instead of the parent class type, enabling memory corruption; affects 0.28.0–0.28.1 only | ≥ 0.28.2 | [RUSTSEC-2026-0013](https://rustsec.org/advisories/RUSTSEC-2026-0013.html) |
| RUSTSEC-2026-0177 | High | Missing `Sync` bound on `PyCFunction::new_closure`: accepted closures with only `Send + 'static`, omitting `Sync`, permitting data races when Python invokes the callable from multiple threads (critical in free-threaded / no-GIL CPython 3.13+); also exploitable via `Python::detach` under the GIL; affects `new_closure` ≥ 0.15.0, `new_closure_bound` 0.21.0–0.22.x | ≥ 0.29.0 | [RUSTSEC-2026-0177](https://rustsec.org/advisories/RUSTSEC-2026-0177.html) |

*OSV link: https://osv.dev/list?ecosystem=crates.io&q=pyo3*

## Security Posture Notes

`pyo3` is the dominant Rust–Python FFI bridge, used both to write Python extension modules in Rust (via `maturin`) and to embed the CPython interpreter in Rust applications. Maintained by the PyO3 organization under MIT OR Apache-2.0. Current stable version: 0.29.3 (released 2026-09-30); minimum Rust version: 1.83.

Download scale (~266M all-time, ~10.5M/week) reflects pervasive adoption across the Python ML/data-science ecosystem. Virtually every high-performance Python library wrapping a Rust core (e.g. `polars`, `cryptography`, `orjson`, `tantivy`, `ruff`) depends on pyo3. A soundness advisory in pyo3 therefore has wide downstream exposure.

Both confirmed public advisories relate to soundness failures at the Rust–CPython boundary:

- **RUSTSEC-2026-0013 (Feb 2026):** Type confusion in the `abi3` stable-ABI build path. Specifically affects code that subclasses native CPython types (`PyList`, `PyDict`, `PyTuple`, etc.) via `#[pyclass(extends=<NativeType>)]` on Python 3.12+. The low-level data accessor used the dynamic (subclass) type object rather than the expected supertype, enabling memory corruption. Fixed in 0.28.2 via corrected type selection in PR #5807.

- **RUSTSEC-2026-0177 (Jun 2026):** Unsound thread-safety for closures wrapped via `PyCFunction::new_closure`. The API accepted any `Send + 'static` closure without requiring `Sync`, but Python can invoke the callable from multiple threads concurrently. This is especially severe in free-threaded Python (CPython 3.13+ `--disable-gil`). Also exploitable under the standard GIL via `Python::detach`, which allows interleaved execution. Fixed in 0.29.0 by adding the `Sync` bound to the closure type parameter.

The broader security surface at the pyo3 boundary includes: reference-count management across Rust/Python ownership models, Python exception propagation safety, and the evolving GIL-removal landscape (PEP 703). The free-threading milestone makes FFI-level soundness increasingly important for the ecosystem.

## Dependencies of Note

- `pyo3-ffi` — low-level C FFI declarations for CPython; same workspace and version as pyo3
- `pyo3-macros` — proc-macro derive crate (`#[pyclass]`, `#[pyfunction]`, etc.); same workspace
- `inventory` — optional, for Python module initialization; no active RUSTSEC advisories

## Open Questions

- Are there additional soundness issues in the free-threaded (no-GIL) execution path beyond RUSTSEC-2026-0177?
- Has any published formal security review of the pyo3 FFI boundary been conducted?
- Does `pyo3-asyncio` / `pyo3-async-runtimes` maintain sound `Send`/`Sync` bounds throughout its executor bridge?

## Related Pages

- [[rust/serde_json]] (commonly combined in Python extensions that handle JSON)
- [[rust/index]]

---
*Last updated: 2026-10-04 | Sources: rustsec/advisory-db; crates.io API*
