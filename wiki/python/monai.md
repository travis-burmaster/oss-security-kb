# MONAI (python)

**Registry:** PyPI (`monai`)
**Weekly Downloads:** unknown (pypistats.org did not respond from this environment) (as of 2026-11-24)
**Repository:** https://github.com/Project-MONAI/MONAI
**Security Contact:** GitHub private vulnerability reporting (https://github.com/Project-MONAI/MONAI/security)
**Disclosure Policy:** https://github.com/Project-MONAI/MONAI/security/policy (not fetched this pass; github.com HTML is blocked from this environment)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-11-24 | OSS Security KB | All GHSA records naming MONAI in github/advisory-database (reviewed and unreviewed), PyPI release metadata, CISA KEV catalog 2026.11.23 | automated | 17 distinct advisories (2025-09 to 2026-10); 1 Critical, 15 High, 1 Moderate; none on CISA KEV | [github/advisory-database](https://github.com/github/advisory-database), [PyPI](https://pypi.org/project/monai/) |

## Known Vulnerabilities

MONAI (Medical Open Network for AI) is the PyTorch-based medical imaging framework from Project MONAI. Several upstream GHSA records have a second, unreviewed GHSA record created from the CVE (NVD/VulnCheck) feed; each row lists both IDs and counts once. Severity is the GHSA label; CVSS 3.1 base scores are computed from each record's vector string. "Fixed in" follows the reviewed record's patched version, or the CVE record's "before X" wording. Where a record only says "through 1.6.0" the fixed version is left as not stated: MONAI 1.6.1 was published to PyPI on 2026-09-27, the same day those records appeared, but no record says it fixes them.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-118683 / GHSA-wvpx-5qmp-46g3 (dup GHSA-475h-4rfw-9899) | High (CVSS 3.1 8.8) | `ConfigWorkflow.__init__` passes a bundle's `configs/logging.conf` to `logging.config.fileConfig`, which evaluates handler class and args fields; a malicious bundle runs code when loaded or run. Affects 1.2.0 to before 1.6.1 | 1.6.1 | [GHSA-475h-4rfw-9899](https://github.com/advisories/GHSA-475h-4rfw-9899), [upstream GHSA-wvpx-5qmp-46g3](https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-wvpx-5qmp-46g3) |
| CVE-2026-118684 / GHSA-hhh4-h52m-fqh6 (dup GHSA-59gw-w64r-2mg7) | High (CVSS 3.1 5.9) | `check_hash()` returns True when no hash is supplied, with MD5 as the default; bundles, datasets or model archives downloaded without hashes can be substituted by a man-in-the-middle or registry compromise | 1.6.1 | [GHSA-59gw-w64r-2mg7](https://github.com/advisories/GHSA-59gw-w64r-2mg7), [upstream GHSA-hhh4-h52m-fqh6](https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-hhh4-h52m-fqh6) |
| CVE-2026-119578 / GHSA-2wx3-8x3w-r8qv (dup GHSA-rx25-w8hq-hr3g) | High (CVSS 3.1 7.8) | Auto3DSeg `algo_from_json()` imports and instantiates a `_target_` from a crafted work directory's `algo_object.json`, running attacker code via `AutoRunner` or `import_bundle_algo_history`. Affects 1.6.0 | 1.6.1 | [GHSA-rx25-w8hq-hr3g](https://github.com/advisories/GHSA-rx25-w8hq-hr3g), [upstream GHSA-2wx3-8x3w-r8qv](https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-2wx3-8x3w-r8qv) |
| CVE-2026-48705 / GHSA-6hp3-vr39-rqw8 | Critical (CVSS 3.1 9.3) | Crafted DICOM upload to a MONAI Label server crashes it or silently corrupts inference results: pydicom does not validate DS/IS value representations, so NaN and infinity values reach MONAI transforms | 1.6.1 | [GHSA-6hp3-vr39-rqw8](https://github.com/advisories/GHSA-6hp3-vr39-rqw8) |
| CVE-2026-109361 / GHSA-8f32-8649-rv87 (dup GHSA-7hmf-j253-4p2j) | High (CVSS 3.1 7.3) | `nnUNetV2Runner` unpickles the `postprocessing_file` path from `inference_information.json` without confining it to the results directory. Affects 1.2.0 to before 1.6.1 | 1.6.1 | [GHSA-7hmf-j253-4p2j](https://github.com/advisories/GHSA-7hmf-j253-4p2j), [upstream GHSA-8f32-8649-rv87](https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-8f32-8649-rv87) |
| CVE-2026-109360 / GHSA-vm9c-7j6g-c7mm (dup GHSA-fvr7-75wp-4566) | High (CVSS 3.1 7.5) | SENet pretrained weights are fetched over plaintext HTTP and unpickled without `weights_only=True`; an on-path attacker can substitute a `.pth` file. Affects 0.4.0 to before 1.6.1 | 1.6.1 | [GHSA-fvr7-75wp-4566](https://github.com/advisories/GHSA-fvr7-75wp-4566), [upstream GHSA-vm9c-7j6g-c7mm](https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-vm9c-7j6g-c7mm) |
| CVE-2026-100840 / GHSA-873f-pvrv-4x83 (dup GHSA-8jxj-xq3g-hvm2) | High (CVSS 3.1 7.8) | Bundle configuration engine resolves `_target_` values to any importable callable and passes `$` expressions to `eval()`; a malicious bundle runs code on `monai.bundle.load()` or `run()`. Affects through 1.6.0 | Not stated in record | [GHSA-8jxj-xq3g-hvm2](https://github.com/advisories/GHSA-8jxj-xq3g-hvm2), [upstream GHSA-873f-pvrv-4x83](https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-873f-pvrv-4x83) |
| CVE-2026-100842 / GHSA-h89g-r5pc-wxfm (dup GHSA-j335-cfj5-2fw8) | High (CVSS 3.1 7.0) | `_get_fake_spatial_shape()` eval allowlist only inspects `ast.Name` nodes, so attribute-chain expressions in bundle metadata escape it (non-default `verify_net_in_out` flow). Affects through 1.6.0 | Not stated in record | [GHSA-j335-cfj5-2fw8](https://github.com/advisories/GHSA-j335-cfj5-2fw8), [upstream GHSA-h89g-r5pc-wxfm](https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-h89g-r5pc-wxfm) |
| CVE-2026-100841 / GHSA-636w-j999-g7x5 (dup GHSA-wfpp-6gx5-h8xr) | High (CVSS 3.1 7.8) | `PersistentDataset` forces `torch.load(weights_only=False)` when caching MetaTensors, and cache helpers call `pickle.loads`; a local user with write access to a shared `cache_dir` can run code as another user. Record says all released versions affected, no patch at publication (2026-09-27) | Not stated in record (no patch at publication) | [GHSA-wfpp-6gx5-h8xr](https://github.com/advisories/GHSA-wfpp-6gx5-h8xr), [upstream GHSA-636w-j999-g7x5](https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-636w-j999-g7x5) |
| CVE-2026-100845 / GHSA-wg9g-w2j2-8pgr (dup GHSA-4jj3-3266-2688) | High (CVSS 3.1 7.8) | `NumpyReader` hard-codes `np.load(allow_pickle=True)`, so a crafted `.npy` / `.npz` file runs code through the standard data pipeline | 1.6.0 | [GHSA-wg9g-w2j2-8pgr](https://github.com/advisories/GHSA-wg9g-w2j2-8pgr), [GHSA-4jj3-3266-2688](https://github.com/advisories/GHSA-4jj3-3266-2688) |
| CVE-2026-100844 / GHSA-rghg-q7wp-9767 (dup GHSA-x7wh-49x3-6748) | High (CVSS 3.1 8.4 on GHSA-x7wh-49x3-6748; reviewed record gives a CVSS 4.0 vector only) | OS command injection in `nnUNetV2Runner`: `dataset_name_or_id` and CLI/kwargs values are concatenated into a `shell=True` command (reported via JPCERT/CC) | 1.6.0 | [GHSA-rghg-q7wp-9767](https://github.com/advisories/GHSA-rghg-q7wp-9767), [GHSA-x7wh-49x3-6748](https://github.com/advisories/GHSA-x7wh-49x3-6748) |
| CVE-2026-100843 / GHSA-qxq5-qhx6-94qw (dup GHSA-m8hq-fmc4-c3v2) | High (CVSS 3.1 7.8) | Incomplete fix: `algo_from_pickle()` `pickle.loads()` RCE was still present in 1.5.2 even though GHSA-89gg-p5r5-q6r4 said it was patched | 1.6.0 | [GHSA-qxq5-qhx6-94qw](https://github.com/advisories/GHSA-qxq5-qhx6-94qw), [GHSA-m8hq-fmc4-c3v2](https://github.com/advisories/GHSA-m8hq-fmc4-c3v2) |
| CVE-2026-100846 / GHSA-89gg-p5r5-q6r4 (dup GHSA-cvqf-4876-w239) | High (CVSS 3.1 7.6) | `algo_from_pickle()` in `monai/auto3dseg/utils.py` passes file contents to `pickle.loads` without validation | 1.6.0 per reviewed record (CVE record says "before 1.5.2"; see GHSA-qxq5-qhx6-94qw) | [GHSA-89gg-p5r5-q6r4](https://github.com/advisories/GHSA-89gg-p5r5-q6r4), [GHSA-cvqf-4876-w239](https://github.com/advisories/GHSA-cvqf-4876-w239) |
| CVE-2026-21851 / GHSA-9rg3-9pvr-6p27 | Moderate (CVSS 3.1 5.3) | Zip Slip path traversal in `_download_from_ngc_private()`, which calls `extractall()` without the project's `safe_extract_member()` | 1.5.2 | [GHSA-9rg3-9pvr-6p27](https://github.com/advisories/GHSA-9rg3-9pvr-6p27) |
| CVE-2025-58756 / GHSA-6vm5-6jv9-rjpj (PYSEC-2025-141) | High (CVSS 3.1 8.8) | Unsafe `torch.load` without `weights_only=True` when loading checkpoints | 1.5.1 | [GHSA-6vm5-6jv9-rjpj](https://github.com/advisories/GHSA-6vm5-6jv9-rjpj) |
| CVE-2025-58757 / GHSA-p8cm-mm2v-gwjm (PYSEC-2025-142) | High (CVSS 3.1 8.8) | Unsafe pickle deserialization may lead to RCE | 1.5.1 | [GHSA-p8cm-mm2v-gwjm](https://github.com/advisories/GHSA-p8cm-mm2v-gwjm) |
| CVE-2025-58755 / GHSA-x6ww-pf9m-m73m (PYSEC-2025-140) | High (CVSS 3.1 8.8) | `zip_file.extractall()` used without path checks across the project, allowing arbitrary file writes from malicious archives | 1.5.1 | [GHSA-x6ww-pf9m-m73m](https://github.com/advisories/GHSA-x6ww-pf9m-m73m) |

Excluded search hits: GHSA-jvr6-pc69-7w54 (CVE-2020-15914, EA Origin client; matched a researcher handle) and GHSA-rrfp-vv85-pxq9 (CVE-2024-7390, WordPress plugin).

## Security Posture Notes

- **Dominant class:** 13 of 17 advisories are code execution through untrusted model, bundle, cache or config files (pickle, `torch.load`, `eval`, `_target_` imports). MONAI bundles and checkpoints should be treated as code, not data.
- **Fix train:** 1.5.1 (2025-09-22), 1.5.2 (2026-01-27), 1.6.0 (2026-06-22) and 1.6.1 (2026-09-27) each closed advisories; 1.6.2 was published 2026-11-18. The 1.5.2 fix for `algo_from_pickle` was incomplete (GHSA-qxq5-qhx6-94qw).
- **Disclosure lag:** JPCERT/CC noted on GHSA-rghg-q7wp-9767 that its February and March 2026 reports had gone unanswered before publication.
- **Downstream exposure:** MONAI Label (`monailabel`) depends on `monai>=1.4.0`; CVE-2026-48705 is filed under `monai` but describes a MONAI Label server attack. The KEV-listed MONAI Label path traversal is on [[python/monailabel]].

## Dependencies of Note

- PyTorch (`torch.load` deserialization behavior) and pydicom (DS/IS validation gap behind CVE-2026-48705).

## Open Questions

- Confirm whether 1.6.1 or 1.6.2 fixes CVE-2026-100840, CVE-2026-100841 and CVE-2026-100842 (records say "through 1.6.0" or "no patch").
- Pull weekly download counts when pypistats.org is reachable.

## Related Pages

- [[python/monailabel]]
- [[python/litellm]]
- [[python/index]]

---
*Last updated: 2026-11-24 | Sources: 26 (24 GHSA records from github/advisory-database search, PyPI JSON metadata, CISA KEV catalog 2026.11.23)*
