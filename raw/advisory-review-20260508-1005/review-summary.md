# Advisory review 2026-05-08 10:05 CT

Targets screened:
- PyPI `celery`: selected for a substantive KB page because OSV/GHSA has a compact direct advisory set with clear upstream fix evidence.
- PyPI `Django`: screened as a future high-value target; OSV query returned a large advisory history better suited to a dedicated deeper pass.
- PyPI `Pillow`: screened as a future high-value target; OSV query returned a large image-parser / memory-safety history better suited to a dedicated deeper pass.

Public sources gathered:
- OSV package queries for celery, Django, and Pillow.
- GitHub Advisory Database pages for `GHSA-q4xr-rc97-m4xx` and `GHSA-rpc6-h455-3rx5`.
- NVD pages for `CVE-2021-23727` and `CVE-2011-4356`.
- Upstream Celery 5.2.2 changelog and OSV-linked upstream fix commits.

Local proxy synthesis:
- `http://127.0.0.1:8319/v1/chat/completions` with model `claude-opus-4-6` succeeded.
- The response was used only as a drafting aid; final markdown was checked against OSV/GHSA/CVE/upstream evidence.
