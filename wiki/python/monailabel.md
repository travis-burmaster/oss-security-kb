# MONAI Label (python)

**Registry:** PyPI (`monailabel`)
**Weekly Downloads:** unknown (pypistats.org did not respond from this environment) (as of 2026-11-24)
**Repository:** https://github.com/Project-MONAI/MONAILabel
**Security Contact:** GitHub private vulnerability reporting (https://github.com/Project-MONAI/MONAILabel/security)
**Disclosure Policy:** none found (no SECURITY.md on the `main` branch via raw.githubusercontent.com)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-11-24 | OSS Security KB | GHSA records naming MONAI / monailabel in github/advisory-database, PyPI release metadata, CISA KEV catalog 2026.11.23 | automated | 1 advisory (Critical, CISA KEV, exploited since September 2026) | [GHSA-2f43-rwqm-6h67](https://github.com/advisories/GHSA-2f43-rwqm-6h67), [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-133968) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-133968 / GHSA-qc22-rmgc-vg94 (GitHub DB record GHSA-2f43-rwqm-6h67) **CISA KEV** | Critical (CVSS 3.1 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, 9.8) | Directory traversal (CWE-24) through the `image` parameter of the `PUT /datastore/image` endpoint (CISA: unauthenticated remote attacker) lets an attacker write files outside the datastore, with resulting remote code execution. The record states it was exploited in the wild starting in September 2026. Affects through 0.8.5. Added to CISA KEV 2026-11-23 (due 2026-11-26; forensic triage required) | 0.8.6 (the record lists "through 0.8.5" and links the 0.8.6 release and PR #1915; 0.8.6 was published to PyPI 2026-11-22) | [GHSA-2f43-rwqm-6h67](https://github.com/advisories/GHSA-2f43-rwqm-6h67), [upstream GHSA-qc22-rmgc-vg94](https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94), [PR #1915](https://github.com/Project-MONAI/MONAILabel/pull/1915), [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-133968) |

Related record filed under the `monai` package: CVE-2026-48705 / GHSA-6hp3-vr39-rqw8 (Critical), a crafted-DICOM upload that crashes a MONAI Label server or silently corrupts inference, fixed in `monai` 1.6.1. See [[python/monai]].

## Security Posture Notes

- **Act now:** CVE-2026-133968 is exploited and on CISA KEV. Upgrade to 0.8.6. CISA's required action is "apply mitigations per vendor instructions", and it asks federal agencies to run forensic triage, so treat any internet-exposed MONAI Label server that ran 0.8.5 or older as possibly compromised.
- **Exposure:** MONAI Label runs as a FastAPI server (per its PyPI dependencies). CISA describes the attacker as unauthenticated and remote. The GHSA record references an AWS Security blog post saying AI agents run by a China-nexus actor found the bug on their own; that claim comes from the linked post's title and was not read here.
- **Patch timing:** the fix shipped on 2026-11-22. Secondary coverage (Rescana, 2026-11-21) said no fixed release existed at that time, so there was a window with exploitation and no patch.
- **Dependency on MONAI core:** `monailabel` 0.8.6 requires `monai>=1.4.0`, which permits `monai` versions affected by most of the advisories on [[python/monai]]. Using `monai>=1.6.1` avoids the ones with a stated fix.

## Dependencies of Note

- `monai>=1.4.0` (see [[python/monai]]; most MONAI advisories are fixed only in 1.6.0 or 1.6.1).
- `fastapi`, `uvicorn`, `pydicom`, `pyjwt`, `passlib`, `requests`, `urllib3` (see [[python/fastapi]], [[python/uvicorn]], [[python/pyjwt]], [[python/requests]], [[python/urllib3]]).

## Open Questions

- Read the upstream advisory GHSA-qc22-rmgc-vg94 and the 0.8.6 release notes when github.com HTML is reachable, to confirm 0.8.6 is the fixed release and to list any other fixes in it.
- Confirm whether authentication-enabled deployments are also exposed.
- Pull weekly download counts when pypistats.org is reachable.

## Related Pages

- [[python/monai]]
- [[python/fastapi]]
- [[python/index]]

---
*Last updated: 2026-11-24 | Sources: 3 (GHSA-2f43-rwqm-6h67, PyPI JSON metadata, CISA KEV catalog 2026.11.23)*
