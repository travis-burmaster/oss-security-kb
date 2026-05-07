# OSS Security KB Page: Starlette (PyPI)

**Package:** [starlette](https://github.com/encode/starlette)
**Ecosystem:** PyPI

---

## Summary of Known Vulnerabilities

Starlette has five publicly documented security advisories, spanning denial-of-service (DoS) and path traversal issues. Below is an evidence-backed summary of each.

---

### 1. CVE-2025-54121 — Denial of Service via Blocking Event Loop on Large Multipart File Uploads
- **Advisory:** [GHSA-2c2j-9gv5-cj73](https://github.com/encode/starlette/security/advisories/GHSA-2c2j-9gv5-cj73)
- **Affected versions:** All versions prior to **0.47.2**
- **Fixed in:** 0.47.2 ([commit](https://github.com/encode/starlette/commit/9f7ec2eb512fcc3fe90b43cb9dd9e1d08696bec1))
- **Details:** When parsing multipart forms containing files larger than the default max spool size, `UploadFile` rolls the file over to disk synchronously, blocking the main asyncio event loop. This prevents the server from accepting new connections, enabling a denial-of-service condition.
- **Trigger condition:** Application must accept multipart form uploads (e.g., via `request.form()` or framework wrappers like FastAPI's `UploadFile`).

---

### 2. CVE-2023-30798 — MultipartParser DoS via Excessive Fields or Files
- **Advisory:** [GHSA-74m5-2c7w-9w3x](https://github.com/encode/starlette/security/advisories/GHSA-74m5-2c7w-9w3x)
- **Aliases:** PYSEC-2023-48
- **Affected versions:** All versions prior to **0.25.0**
- **Fixed in:** 0.25.0 ([commit](https://github.com/encode/starlette/commit/8c74c2c8dba7030154f8af18e016136bea1938fa))
- **Details:** The `MultipartParser` (using `python-multipart`) accepted an unlimited number of multipart parts. Sending many small form fields or empty files could cause high CPU and memory usage, potentially leading to OOM process kill.
- **Trigger condition:** `python-multipart` installed and application calls `request.form()` (directly or via frameworks like FastAPI).

---

### 3. CVE-2025-62727 — O(n²) DoS via Range Header Merging in FileResponse
- **Advisory:** [GHSA-7f5h-v6xp-fcq8](https://github.com/Kludex/starlette/security/advisories/GHSA-7f5h-v6xp-fcq8)
- **Affected versions:** **0.39.0** through versions prior to **0.49.1**
- **Fixed in:** 0.49.1 ([commits](https://github.com/Kludex/starlette/commit/4ea6e22b489ec388d6004cfbca52dd5b147127c5))
- **Details:** A crafted HTTP `Range` header with many range specifiers triggers quadratic-time processing in `FileResponse._parse_range_header()` due to an O(n²) merge algorithm. This enables CPU exhaustion on any endpoint serving files (e.g., `StaticFiles` or custom `FileResponse` usage). No authentication required.

---

### 4. CVE-2024-47874 — DoS via Unbounded Multipart Text Field Buffering
- **Advisory:** [GHSA-f96h-pmfr-66vw](https://github.com/encode/starlette/security/advisories/GHSA-f96h-pmfr-66vw)
- **Affected versions:** All versions prior to **0.40.0**
- **Fixed in:** 0.40.0 ([commit](https://github.com/encode/starlette/commit/fd038f3070c302bff17ef7d173dbb0b007617733))
- **Details:** Multipart form-data parts lacking a `filename` are treated as text fields and buffered in memory with no size limit. An attacker can upload arbitrarily large form fields, causing excessive memory allocation, memory copy operations, and eventual OOM or swap thrashing. Parallel requests can amplify impact even behind reverse proxies enforcing request size limits.

---

### 5. CVE-2023-29159 — Path Traversal in StaticFiles
- **Advisory:** [GHSA-v5gw-mw7f-84px](https://github.com/encode/starlette/security/advisories/GHSA-v5gw-mw7f-84px)
-
