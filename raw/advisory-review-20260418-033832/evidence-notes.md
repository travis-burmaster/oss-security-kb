# Advisory review evidence notes

## Candidate packages reviewed this pass
- cross-spawn — no current page in wiki/npm; very high weekly downloads (~173.8M); one published OSV/GHSA/CVE record.
- yargs-parser — no current page in wiki/npm; very high weekly downloads (~176.6M); one published OSV/GHSA/CVE record.
- braces — no current page in wiki/npm; very high weekly downloads (~143.0M); two published OSV/GHSA/CVE records, but fuller normalization deferred this pass.

## cross-spawn
- npm downloads API (last week): 173,814,017
- npm registry latest: 7.0.6
- GitHub Advisory DB JSON `GHSA-3xgq-45jj-v275`:
  - summary: ReDoS in cross-spawn
  - aliases: CVE-2024-21538
  - details: before 7.0.5 vulnerable due to improper input sanitization; crafted very large string can drive CPU usage / crash program
  - affected/fixed: `<6.0.6` and `>=7.0.0 <7.0.5`; fixed in `6.0.6` and `7.0.5`
  - references include issue #165, PR #160, commits `5ff3a07`, `640d391`, and `d35c865`
- OSV confirms affected ranges and fixes: all versions before 6.0.6; 7.0.0-7.0.4 fixed in 7.0.5.
- Upstream CHANGELOG:
  - 7.0.4: "fix: disable regexp backtracking (#160)"
  - 7.0.5: "fix: fix escaping bug introduced by backtracking"
  - 7.0.6: package-lock follow-up only
- Upstream commit summaries fetched from GitHub API match the changelog text.

## yargs-parser
- npm downloads API (last week): 176,636,757
- npm registry latest: 22.0.0
- GitHub Advisory DB JSON `GHSA-p9pc-299p-vxgp`:
  - summary: prototype pollution in yargs-parser
  - aliases: CVE-2020-7608
  - details: parsing attacker-controlled `--foo.__proto__.bar baz` can modify `Object.prototype`
  - recommendation / fixed versions: `5.0.1`, `13.1.2`, `15.0.1`, `18.1.1` or later depending on active major line
- OSV confirms fixed versions across those four maintained lines.
- Upstream CHANGELOG explicitly says for 18.1.1: `__proto__` will now be replaced with `___proto___` in parse, patching a potential prototype pollution vulnerability (#258), reported by Snyk Security Research Team.
- Commit summary fetched from GitHub API matches that changelog note.

## braces
- OSV package query returned 2 vulns (`GHSA-cwfw-4gq5-mrqx` / `CVE-2018-1109`, `GHSA-grv7-fg5c-xmjg` / `CVE-2024-4068`).
- Deferred because it deserves its own pass for release / fix normalization.
