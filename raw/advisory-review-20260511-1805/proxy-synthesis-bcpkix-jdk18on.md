# OSS KB Update Proposal: `org.bouncycastle:bcpkix-jdk18on`

## Recommended Page Status

**ACTIVE** — Package is actively maintained (latest release 1.84 as of 2026-04-14), with ongoing security fixes being published.

---

## Vulnerability Rows

| CVE / GHSA ID | Summary | Severity | Affected Versions (this artifact) | Fixed Version | Status in Latest (1.84) |
|---|---|---|---|---|---|
| **CVE-2023-33202** / GHSA-wjxj-5m7g-mg7q | DoS via crafted ASN.1 in `PEMParser` causing `OutOfMemoryError` | Medium (DoS) | 1.71 – 1.72 (artifact starts at 1.71) | 1.73 | ✅ Fixed |
| **CVE-2025-8916** / GHSA-4cx2-fc23-5wg6 | Excessive Allocation (no resource limits) in `PKIXCertPathReviewer` | Medium (DoS) | 1.71 – 1.78.1 (BC 1.44–1.78 range, artifact starts at 1.71) | 1.79 | ✅ Fixed |
| **CVE-2026-5588** / GHSA-wg6q-6289-32hp | CompositeVerifier accepts empty signature sequence as valid (broken crypto validation) | High (Signature bypass) | 1.71 – 1.83 (BC 1.49–1.83 range, artifact starts at 1.71) | 1.84 | ✅ Fixed |

### Notes on Affected Range Mapping
- The `bcpkix-jdk18on` artifact was first published at version **1.71**. OSV ranges that begin earlier (e.g., "from 1.44") are mapped to 1.71 as the effective lower bound for this specific artifact.
- All three CVEs are resolved in the current latest release **1.84**.

---

## Security Posture Notes

1. **Current posture (1.84): No known unpatched vulnerabilities.** All three OSV-listed CVEs are fixed at or before 1.84.
2. **Upgrade urgency:** Users on versions ≤ 1.83 should upgrade to **1.84** to address CVE-2026-5588 (empty composite signature acceptance — potentially high-severity signature bypass). Users on ≤ 1.78.1 are additionally exposed to CVE-2025-8916 (DoS). Users on ≤ 1.72 are additionally exposed to CVE-2023-33202 (DoS).
3. **Release cadence:** 16 releases from 1.71 to 1.84 since artifact inception, indicating active and regular maintenance.
4. **Uncertainty note:** CVE-2026-5588 has a future-dated CVE ID (2026), which is unusual. This is taken at face value from the OSV data; the fix commit and advisory reference exist in the bc-java repository. It may reflect a reserved ID or coordinated disclosure timeline.

---

## Recommended Minimum Safe Version

**1.84** — resolves all known CVEs for this artifact.

---

## Sources

| # | Source | URL |
|---|---|---|
| 1 | GHSA-wjxj-5m7g-mg7q (CVE-2023-33202) | https://github.com/advisories/GHSA-wjxj-5m7g-mg7q |
| 2 | GHSA-4cx2-fc23-5wg6 (CVE-2025-8916) | https://github.com/advisories/GHSA-4cx2-fc23-5wg6 |
| 3 | GHSA-wg6q-6289-32hp (CVE-2026-5588) | https://github.com/advisories/GHSA-wg6q-6289-32hp |
| 4 | Maven Central metadata | https://repo1.maven.org/maven2/org/bouncycastle/bcpkix-jdk18on/maven-metadata.xml |
| 5 | BC-Java CVE wiki (CVE-2023-33202) | https://github.com/bcgit/bc-java/wiki/CVE-2023-33202 |
| 6 | BC-Java CVE wiki (CVE-2025-8916) | https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902025%E2%80%908916 |
| 7 | BC-Java CVE wiki (CVE-2026-5588) | https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%905588