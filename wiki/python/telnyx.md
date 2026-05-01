# telnyx (python)

**Registry:** PyPI
**Repository:** https://github.com/team-telnyx/telnyx-python
**Current Status:** advisory-mapped (incident-focused)

## Summary

In March 2026, two PyPI releases of `telnyx` were published containing credential-harvesting malware. Public reporting links this event to the same broader supply-chain campaign as the `litellm` incident, following an API token exposure associated with an exploited dependency in the Trivy ecosystem.

This page tracks the incident as a **supply-chain compromise** (malicious release), not a typical vulnerability in the upstream codebase.

## Known Vulnerabilities / Incidents

| ID | Severity | Description | Affected | Fixed / Mitigation | Sources |
|----|----------|-------------|----------|--------------------|---------|
| PYSEC-2026-3 | Critical (malicious release) | Malicious releases executed code when importing the `telnyx` module and downloaded follow-on stages from attacker-controlled infrastructure. Reporting describes persistence behavior on Windows via Startup folder placement, and exfiltration of generated artifacts. One affected version is described as having a typo that prevented automated execution. | OSV entry: affected versions (see OSV record) | Treat any affected environment as compromised; revoke/rotate reachable credentials and isolate/analyze hosts. Prefer pinned/locked dependencies and avoid installing ultra-recent releases without review ("dependency cooldown" concept). | https://osv.dev/vulnerability/PYSEC-2026-3 ; https://blog.pypi.org/posts/2026-04-02-incident-report-litellm-telnyx-supply-chain-attack/ |

## Security Posture Notes (evidence-backed)

- As with the `litellm` event, this is best understood as a **malicious release / supply-chain compromise**.
- The PyPI incident report provides ecosystem-level mitigations (locking dependencies with hashes, using dependency cooldowns, vulnerability scanning to avoid delaying security updates).

## Related Pages

- [[python/index]]

---
*Last updated: 2026-05-01 | Sources: OSV PYSEC-2026-3 entry; PyPI incident report (2026-04-02)*
