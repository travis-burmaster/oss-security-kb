# Advisory review evidence summary: PyPI paramiko

Reviewed candidates:
- PyPI `paramiko`: no existing KB page; OSV returned 10 records including duplicate PYSEC/GHSA aliases, normalizing to six public vulnerability groups. Selected for substantive update.
- PyPI `httpx`: no existing KB page; OSV returned two records, good future compact page.
- Maven `org.apache.commons:commons-lang3`: no existing KB page; OSV returned one record, good future compact page.
- Maven `org.apache.zookeeper:zookeeper`: no existing KB page; OSV returned nine records, good future page.
- npm `passport`: existing page already present; OSV returned one record.

Sources saved in this directory:
- `pypi-paramiko-osv-query.json` from OSV.dev package query.
- `GHSA-*.json` / `GHSA-*.html` public GitHub Advisory Database records.
- `CVE-*.json` from cveawg.mitre.org public CVE records.
- `paramiko-changelog.html` / text snippets from upstream public changelog.
- `paramiko-pypi.json` from PyPI metadata; latest release 5.0.0.
- `paramiko-github-security-policy.html` public GitHub security policy page.
- `paramiko-ostif-audit.pdf` public OSTIF audit referenced by GHSA-r374-rxx8-8654 / CVE-2026-44405.
- PyPIStats weekly download API returned HTTP 429 during this run, so no download count should be fabricated.

Normalized Paramiko advisory groups:
1. GHSA-wqmm-q65g-2hqr / CVE-2008-0299 / PYSEC-2008-8 — unsafe randomness / RandomPool state reuse could allow sensitive information exposure. GitHub advisory severity high. Fixed ranges vary between GHSA and PyPA records (`1.7.1-3` distro-style vs `1.7.2` upstream-ish); represent cautiously as early 1.7.x fixed/backported.
2. GHSA-232r-66cg-79px / CVE-2018-7750 / PYSEC-2018-19 — server-mode auth-check bypass before processing channel-open and related post-auth requests. GitHub advisory severity critical. Fixed across 1.17.6, 1.18.5, 2.0.8, 2.1.5, 2.2.3, 2.3.2, 2.4.1. Upstream changelog explicitly says server mode, not client use.
3. GHSA-f2j6-wrhh-v25m / CVE-2018-1000805 / PYSEC-2018-69 — server-mode auth bypass / hostile clients could make server think they were authenticated. GitHub advisory severity high; description mentions RCE risk. Fixed across 2.0.9, 2.1.6, 2.2.4, 2.3.3, 2.4.2. Upstream changelog says server mode, not client mode, and references separating client/server message handling tables.
4. GHSA-f8q4-jwww-x3wv / CVE-2022-24302 / PYSEC-2022-166 — race between private-key file creation and chmod in `PKey.write_private_key_file` could expose key files to local attackers. GitHub advisory severity high. Fixed in 2.9.3 and 2.10.1. Upstream changelog says patched using `os.open` / `os.fdopen` to set mode at file creation.
5. GHSA-45x7-px36-x8w8 / CVE-2023-48795 — SSH Terrapin prefix truncation attack against strict SSH channel integrity. GitHub advisory severity medium for Paramiko; fixed in 3.4.0 for Paramiko range >=2.5.0,<3.4.0. Upstream changelog states impact is on encrypt-then-MAC with CBC in Paramiko's implemented algorithm set, and notes `disabled_algorithms` mitigation plus strict-kex cooperation.
6. GHSA-r374-rxx8-8654 / CVE-2026-44405 — public advisory says Paramiko through 4.0.0 before commit `a4489456...` allows SHA-1 algorithm in `rsakey.py`. GitHub advisory severity low; public references include OSTIF audit PDF and fixing commit. PyPI latest 5.0.0 was released 2026-05-09 after this public advisory.

Posture notes:
- Paramiko is an SSH2 protocol library; server-mode deployments and key-management paths carry different risk from ordinary SSH client use.
- The 2018 auth-bypass records are separate but adjacent server-mode message-ordering/auth-state bugs and should not be collapsed into one issue.
- Terrapin is a protocol-level SSH issue where mitigation depends on both sides supporting strict key exchange; deployment configs can temporarily disable affected algorithms if immediate upgrade is blocked.
- The 2026 SHA-1 record is recent, public, and low severity; avoid claiming exploitation or impact beyond advisory wording and public audit/fix references.
