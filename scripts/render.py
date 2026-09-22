"""Generate Markdown and BibTeX from the curated records; Python 3.10+."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def cell(value):
    return str(value).replace('|', r'\|').replace('\n',' ')

def render():
    papers=json.loads((ROOT/'data/papers.json').read_text())
    categories=json.loads((ROOT/'data/categories.json').read_text())
    latest=max(p['checked_on'] for p in papers)
    lines=['# Awesome Agentic Robotics & Embodied Harness', '',
    '> From closed-loop execution to continual learning: a research index of papers, system mechanisms, evaluation, and open questions.', '',
    f'Latest manual review: **{latest}** · **{len(papers)} indexed papers** · See the unverified list for pending entries.', '',
    'This review primarily checked original abstracts and author project pages, rather than reproducing every paper in full. Each card states its verification scope; research questions and categories reflect maintainer analysis.', '',
    '## Navigation', '',
    '- [Research agenda and testable hypotheses](docs/research-agenda.md)',
    '- [Architecture comparison](docs/architecture-comparison.md)',
    '- [Initial review and corrections](reports/2026-09-22.md)',
    '- [Evaluation protocol](docs/evaluation-protocol.md) · [Evidence policy](docs/evidence-policy.md)',
    '- [Daily candidates](docs/inbox.md) · [Unverified leads](docs/unverified.md)',
    '- [Automated updates and publishing](docs/maintenance.md) · [Contributing](CONTRIBUTING.md)',
    '- [JSON data](data/papers.json) · [BibTeX](references.bib)', '',
    '## Source reconciliation', '', 'Coverage of 26 arXiv entries was checked against the original Notion page; see the [source mapping](docs/source-reconciliation.md). The original page and the uploaded attachment contain the same set of paper IDs.', '', '## Scope', '',
    'This index focuses on how large models make reliable robot decisions through tool interfaces, execution feedback, memory, verification, and learning. It covers frozen VLA orchestration, analytical tools and code-based control, semantic action interpreters, and trained dual-system architectures. General VLA architectures are included only when directly relevant.', '',
    'Execution, Learning, and Fleet are overlapping organizational perspectives. Multi-agent division of labor, multi-robot collaboration, and shared fleet learning are distinct concepts.', '',
    '## Categories', '', '| Area | Core question | Entries |', '|---|---|---:|']
    for tag,(name,question) in categories.items():
        lines.append(f'| [{name}](#{tag}) | {question} | {sum(tag in p["tags"] for p in papers)} |')
    lines += ['', '## Suggested reading', '',
    'Execution interfaces: Show-Harness → Harness VLA → CaP-X; accumulating experience: ViReSkill → ASPIRE → Zetta; memory: RoboMME → PonderPounce → MaP-WAM; data and training: RoboClaw → HALTER → TwinRL → LWD.', '',
    '## Paper index', '', 'Papers may appear in multiple categories. Dates indicate initial submission; new versions of the same arXiv ID are not counted again.']
    for tag,(name,question) in categories.items():
        lines += ['',f'<a id="{tag}"></a>', f'### {name}', '', question, '', '| Submitted | Work | Core mechanism |', '|---|---|---|']
        for p in papers:
            if tag in p['tags']:
                lines.append(f'| {p["published"]} | [{p["name"]}](papers/{p["id"]}.md) · [Paper]({p["paper_url"]}) | {cell(p["summary_en"])} |')
    lines += ['', '## Update status', '',
    'The repository includes daily arXiv candidate discovery and version checks, scheduled to run once the workflows are on the GitHub default branch and Actions is enabled. Discovery does not replace manual review; curated entries require verification before updates. Scheduled GitHub Actions runs may be delayed, and disabled workflows need attention.', '',
    '## Sources and licensing', '',
    'The initial topic came from research material dated 2026-09-08 supplied by the user. This repository reorganizes, verifies, and rewrites that material without including private Notion pages, original reports, or full papers. Code and original annotations use the MIT license; papers, abstracts, and third-party projects retain their respective licenses.', '']
    (ROOT/'README.md').write_text('\n'.join(lines))
    for p in papers:
        ver=f'v{p["version"]}' if p['version'] is not None else 'version pending verification'
        text=[f'# {p["name"]}', '', p['title'], '',
        f'- First submitted: {p["published"]}; reviewed version: {ver}; latest revision: {p["revised"] or "no additional revision recorded"}',
        f'- Reviewed on: {p["checked_on"]}; verification scope: `{p["verification"]}`',
        f'- Scope: {"general-purpose agents; robotics transfer remains unverified" if p["scope"]=="transfer" else "robotics"}',
        f'- Categories: {", ".join(p["tags"])}',f'- Interface / mechanism: {p["interface"]}',
        f'- [Paper]({p["paper_url"]})']
        for key,label in [('code_url','Official code'),('project_url','Author project page')]:
            if p[key]: text.append(f'- [{label}]({p[key]})')
        text += ['', '## Mechanism overview', '', p['summary_en'], '', '## Limitations and research questions', '',p['caveat_en'], '',
        '## Full-text verification checklist', '',
        '- Input observations, output interfaces, low-level controllers, and coordinate conventions.',
        '- Trainable and frozen modules, deployment-time updates, and persistence scope.',
        '- Training/adaptation/validation/test splits, privileged perception, and human-designed priors.',
        '- Success rates, costs, sample counts, uncertainty, ablations, and exact table references.', '',
        '## Verification sources', '']+[f'- {url}' for url in p['sources']]+['', '[Back to index](../README.md)', '']
        (ROOT/'papers'/f'{p["id"]}.md').write_text('\n'.join(text))
    bib=[]
    for p in papers:
        # Missing metadata stays missing rather than inventing author names.
        fields={'title':p['title'],'year':p['published'][:4],'eprint':p['id'],'archivePrefix':'arXiv','url':p['paper_url']}
        if p['authors']: fields['author']=' and '.join(p['authors'])
        bib += ['@misc{arxiv'+p['id'].replace('.','')+',']+[f'  {k} = {{{v}}},' for k,v in fields.items()]+['}', '']
    (ROOT/'references.bib').write_text('\n'.join(bib))
    unverified=json.loads((ROOT/'data/unverified.json').read_text())
    (ROOT/'docs/unverified.md').write_text('# Unverified leads\n\nFailure to access a primary source does not mean a paper does not exist. These entries are excluded from formal conclusions and rankings.\n\n'+ '\n'.join(f'- [{p["name"]}](https://arxiv.org/abs/{p["id"]}): {p["reason"]}' for p in unverified)+'\n')

if __name__=='__main__': render()
