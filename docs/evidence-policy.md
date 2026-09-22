# Sources and evidence policy

## Verification scope

| verification | Meaning |
|---|---|
| primary_abstract | Original arXiv abstract and metadata read; does not claim a complete review of experiments |
| official_project | Author project page read; metadata such as version number may still be missing |
| primary_search_abstract | Search tools returned the original paper abstract; direct page access failed |
| full_text | Full paper read, with method and experiment locations recorded |
| needs_primary_verification | Only a lead or user-supplied material is available; primary-source verification is incomplete |

Entries in the last category are stored in `data/unverified.json` and excluded from the curated paper tables. Inclusion in the initial release indicates a relevant primary source, not independent reproduction of its conclusions.

## Source priority

Original papers take precedence over author projects and official code, followed by official conference records. Aggregators, social media, and reviews can identify leads but are not final evidence for technical mechanisms or numbers. Author claims such as “SOTA,” “first,” or “unique” are not automatically adopted as repository conclusions.

## Versions and dates

Deduplicate by arXiv ID. Record first-submission and last-revision dates; do not infer dates from the ID month. Preserve title-change notes, such as AgenticLab → PLanAR. Review new versions before updating manually curated fields.

## Limits of conclusions

- Distinguish author-reported results from reproductions; do not present correlation as causal proof.
- Distinguish design proposals, system prototypes, simulation validation, and real-robot validation.
- Distinguish external memory updates, code updates, and parameter learning.
- Distinguish multi-robot collaboration, state sharing, and shared learning.
- List general-purpose agent work separately as transfer leads, not as robotics experiments.
- An oracle gap may suggest a bottleneck, but does not prove that a single module explains the entire gap.

## Copyright and privacy

Retain links and write brief original summaries rather than mirroring full papers or images. Private Notion links are used only to locate sources during review and are excluded from the repository intended for publication. Automated discovery stores only title, date, and version metadata, not full abstracts.
