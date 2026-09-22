# Contributing and updating

1. Pick a lead from `data/candidates.json` or `data/unverified.json` and check for duplicates by arXiv ID.
2. Read the original paper or author project page. Record dates, version, title, relevant categories, and verification scope.
3. Add or revise the entry in `data/papers.json`. Write English summaries in your own words rather than copying long passages.
4. Record specific experimental numbers in `metrics`, with the paper version and table or section location. Use `null` for missing conditions.
5. Run `python3 scripts/render.py`, followed by `python3 -m unittest discover -s tests -v`.
6. Record additions, title changes, corrected conclusions, and unresolved items in `reports/YYYY-MM-DD.md` and `CHANGELOG.md`.

## Minimum entry

Follow the existing records in `data/papers.json`. Use the unversioned arXiv ID for `id` and store `version` separately. Set `scope` to `robotics` or `transfer`. Write the mechanism summary in `summary_en` and limitations in `caveat_en`. Do not guess unverified `code_url` values.

Generate `README.md`, `papers/*.md`, `docs/unverified.md`, and `references.bib` with the script. Keep manual full-text reading notes in `docs/` or `reports/` and link them to the relevant card so regeneration does not erase them.
