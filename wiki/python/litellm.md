# litellm (python)

**Registry:** PyPI
**Repository:** https://github.com/BerriAI/litellm
**Current Status:** advisory-mapped (incident-focused)

## Summary

In March 2026, two PyPI releases of `litellm` were published containing credential-harvesting malware. Public reporting indicates the compromise was enabled by an API token exposure originating from an exploited dependency in the Trivy ecosystem, and resulted in malicious code executing on import and attempting persistence.

This page tracks the incident as a **supply-chain compromise** (malicious release), not a typical vulnerability in the upstream codebase.

## Known Vulnerabilities / Incidents

| ID | Severity | Description | Affected | Fixed / Mitigation | Sources |
|----|----------|-------------|----------|--------------------|---------|
| PYSEC-2026-2 | Critical (malicious release) | Malicious releases harvested sensitive files and credentials (e.g., SSH keys, tokens, dotenvs), attempted to acquire cloud metadata credentials, and exfiltrated data to attacker-controlled infrastructure. Reporting also describes persistence attempts via systemd unit creation and Kubernetes pod creation. | `litellm` 1.82.7 and 1.82.8 (OSV “introduced 1.82.7”, “last affected 1.82.8”) | Treat any affected environment as compromised; revoke/rotate reachable credentials. Prefer pinned/locked dependencies and avoid installing ultra-recent releases without review ("dependency cooldown" concept). | https://osv.dev/vulnerability/PYSEC-2026-2 ; https://blog.pypi.org/posts/2026-04-02-incident-report-litellm-telnyx-supply-chain-attack/ |

## Security Posture Notes (evidence-backed)

- **This was a malicious-package incident.** The published details describe malware behavior on import and credential/file harvesting, not just a logic bug.
- **Operational blast radius is large** for users who install unpinned latest versions: the PyPI incident report notes a high volume of downloads during the short exposure window and explicitly calls out unpinned installs as a key risk amplifier.
- Consider ecosystem hardening patterns discussed in the PyPI incident report: dependency pinning/locking (with hashes) and dependency cooldowns (excluding very recently uploaded distributions) to reduce exposure to rapid supply-chain events.

## Related Pages

- [[python/index]]

---
*Last updated: 2026-05-01 | Sources: OSV PYSEC-2026-2 entry; PyPI incident report (2026-04-02)*
