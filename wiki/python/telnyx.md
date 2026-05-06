# telnyx (python)

**Registry:** PyPI
**Repository:** https://github.com/team-telnyx/telnyx-python
**Current Status:** advisory-mapped (incident-focused)

## Summary

In March 2026, two PyPI releases of `telnyx` were published containing credential-harvesting malware. Public reporting links this event to the same broader supply-chain campaign as the `litellm` incident, following an API token exposure associated with an exploited dependency in the Trivy ecosystem.

This page tracks the incident as a **supply-chain compromise** (malicious release), not a typical vulnerability in the upstream codebase.

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-06 | OpenClaw recurring review | incident identifier reconciliation | public-source curation (OSV.dev package query, PyPA advisory database, upstream GitHub Security Advisory / issue, PyPI incident report, public researcher write-ups, local Claude-compatible proxy used only as a drafting aid) | Reconciled the incident's public identifiers: OSV currently returns `PYSEC-2026-3`, `GHSA-955r-262c-33jc`, and malware marker `MAL-2026-2254` for the same affected `telnyx` PyPI releases. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities / Incidents

| ID | Severity | Description | Affected | Fixed / Mitigation | Sources |
|----|----------|-------------|----------|--------------------|---------|
| PYSEC-2026-3 / GHSA-955r-262c-33jc / MAL-2026-2254 | Critical (malicious release) | Malicious releases executed code when importing the `telnyx` module and downloaded follow-on stages from attacker-controlled infrastructure. Reporting describes credential-harvesting behavior; the PyPI advisory database notes that version 4.87.1 contained a typo preventing automated execution. `GHSA-955r-262c-33jc` is the upstream GitHub Security Advisory identifier and `MAL-2026-2254` is an OSV malware identifier for the same incident family. | `telnyx` 4.87.1 and 4.87.2 (per OSV / PyPI advisory database; the GHSA range is introduced 4.87.1 through last affected 4.87.2) | Treat any affected environment as compromised; revoke/rotate reachable credentials and isolate/analyze hosts. Prefer pinned/locked dependencies and avoid installing ultra-recent releases without review ("dependency cooldown" concept). | https://osv.dev/vulnerability/PYSEC-2026-3 ; https://osv.dev/vulnerability/GHSA-955r-262c-33jc ; https://osv.dev/vulnerability/MAL-2026-2254 ; https://raw.githubusercontent.com/pypa/advisory-database/main/vulns/telnyx/PYSEC-2026-3.yaml ; https://github.com/team-telnyx/telnyx-python/security/advisories/GHSA-955r-262c-33jc ; https://github.com/team-telnyx/telnyx-python/issues/235 ; https://blog.pypi.org/posts/2026-04-02-incident-report-litellm-telnyx-supply-chain-attack/ |

## Security Posture Notes (evidence-backed)

- This is best understood as a **malicious release / supply-chain compromise**, not a source-code vulnerability introduced through normal maintainer development.
- OSV currently exposes three package-scoped identifiers for this incident (`PYSEC-2026-3`, `GHSA-955r-262c-33jc`, and `MAL-2026-2254`). They should not be counted as three separate vulnerability classes without additional evidence; the KB treats them as aliases / parallel records for the same affected releases.
- The PyPI incident report provides ecosystem-level mitigations: locking dependencies with hashes, using dependency cooldowns, and vulnerability scanning while avoiding delays to legitimate security updates.

## Related Pages

- [[python/index]]

---
*Last updated: 2026-05-06 | Sources: OSV package query (PYSEC-2026-3, GHSA-955r-262c-33jc, MAL-2026-2254); PyPA advisory database; upstream GHSA / issue; PyPI incident report*
