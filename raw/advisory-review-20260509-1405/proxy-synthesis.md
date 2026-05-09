# OSS Security KB Update Review

## Summary

All three candidates have substantive, evidence-backed vulnerability data suitable for KB inclusion. Below is the per-package analysis.

---

## 1. crates.io `h2` — **Safe to add (Substantive)**

Three confirmed advisories, all Denial of Service class:

| Advisory | CVE / RUSTSEC | Class | Affected | Fixed |
|---|---|---|---|---|
| GHSA-8r5v-vm4m-4g25 | RUSTSEC-2024-0003 | Resource exhaustion → DoS | all < 0.3.24 | **0.3.24** |
| GHSA-f8vr-r385-rh5r | CVE-2023-26964 / RUSTSEC-2023-0034 | DoS (stream count handling) | all < 0.3.17 | **0.3.17** |
| GHSA-q6cp-qfwq-4gcv | RUSTSEC-2024-0332 | HTTP/2 CONTINUATION Flood → DoS | all < 0.3.26 | **0.3.26** |

**Key vulnerability class:** HTTP/2 protocol-level Denial of Service. The CONTINUATION flood (RUSTSEC-2024-0332) is part of the cross-ecosystem VU#421644 multi-vendor disclosure. All three are corroborated by upstream commits and RUSTSEC entries.

**Recommended minimum safe version:** **0.3.26**

---

## 2. npm `koa` — **Safe to add (Substantive)**

Five confirmed advisories spanning multiple vulnerability classes:

| Advisory | CVE | Class | Affected Range | Fixed |
|---|---|---|---|---|
| GHSA-593f-38f6-jp5m | CVE-2025-25200 | ReDoS (Inefficient Regex) | 2.0.0 – 2.15.3 | **2.15.4** |
| GHSA-7gcc-r8m5-44qm | CVE-2026-27959 | Host Header Injection | 3.0.0 – 3.1.1 | **3.1.2** |
| GHSA-g8mr-fgfg-5qpc | CVE-2025-62595 | Open Redirect (trailing `//`) | 3.0.1 – 3.0.2 | **3.0.3** |
| GHSA-jgmv-j7ww-jx2x | CVE-2025-8129 | Open Redirect (Referrer header) | 2.0.0 – 2.16.1 | **2.16.2** |
| GHSA-x2rg-q646-7m2v | CVE-2025-32379 | Reflected XSS (`ctx.redirect()`) | all < 2.16.1 | **2.16.1** |

**Key vulnerability classes:** ReDoS, Host Header Injection, Open Redirect, Cross-Site Scripting (XSS). Note the split across the 2.x and 3.x major lines — both require separate minimum-safe-version tracking.

**Recommended minimum safe versions:** **2.x → 2.16.2**, **3.x → 3.1.2**

> ⚠️ **Note on CVE-2026-27959:** The "2026" year prefix in the CVE is unusual and may indicate a reservation anomaly or future-dated assignment. The advisory itself (GHSA-7gcc-r8m5-44qm) is real, published by koajs, with a fix commit — safe to include but worth flagging the CVE ID as potentially atypical.

---

## 3. Go `github.com/go-chi/chi/v5` — **Safe to add (Substantive, but note incomplete fix)**

| Advisory | CVE / Alias | Class | Affected | Fixed |
|---|---|---|---|---|
| GHSA-vrw8-fxc6-2r93 | GO-2025-3770 | Host Header Injection → Open Redirect (`RedirectSlashes`) | all < 5.2.2 | **5.2.2** |
| GO-2026-4316 | CVE-2025-69725 / GHSA-mqqf-5wvp-8fh8 | Open Redirect (`RedirectSlashes`) | all (no fixed version listed) | **Unfixed / pending** |

**Key vulnerability class:** Open Redirect via `RedirectSlashes` middleware, exploitable through Host header manipulation.

**Critical observation:** GO-2026-4316 appears to be a **bypass or incomplete fix** of GHSA-vrw8-fxc6-2r93. The event data shows `{'introduced': '0'}` with **no `fixed` entry**, and a separate commit (`6eb35881...`)