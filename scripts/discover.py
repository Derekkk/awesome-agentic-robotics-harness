"""Discover arXiv candidates and revisions. No LLM, API key, or third-party package.

Never modifies curated papers.json. On any network/parse error, existing files
remain untouched and the command fails. Lookback uses updated, not published.
"""
import argparse
import datetime as dt
import json
import os
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
NS={'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}

def parse_feed(raw):
    root=ET.fromstring(raw)
    if root.tag!='{http://www.w3.org/2005/Atom}feed': raise ValueError('Expected Atom feed')
    rows=[]
    for e in root.findall('a:entry',NS):
        val=lambda key:' '.join((e.findtext('a:'+key,default='',namespaces=NS)).split())
        identity=val('id')
        m=re.search(r'/abs/(\d{4}\.\d{4,5})(?:v(\d+))?$',identity)
        if not m: raise ValueError('Invalid arXiv entry or API error: '+identity)
        published,updated=val('published'),val('updated')
        dt.datetime.fromisoformat(published.replace('Z','+00:00'))
        dt.datetime.fromisoformat(updated.replace('Z','+00:00'))
        rows.append(dict(id=m[1],version=int(m[2] or 1),title=val('title'),published=published,updated=updated,paper_url='https://arxiv.org/abs/'+m[1]))
    return rows,int(root.findtext('o:totalResults',default=str(len(rows)),namespaces=NS))

def fetch(params):
    url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode(params)
    for attempt in range(3):
        time.sleep(3.1 if attempt==0 else 6*(attempt+1))
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'AgenticRoboticsResearchIndex/1.0 (scholarly metadata only)'})
            with urllib.request.urlopen(req,timeout=60) as r: return parse_feed(r.read())
        except Exception:
            if attempt==2: raise

def merge(old, incoming, curated, discovered):
    byid={p['id']:dict(p) for p in old}
    known={p['id']:p for p in curated}
    for entry in incoming:
        aid=entry['id']
        k=known.get(aid)
        if k and k.get('version') is not None and entry['version']<=k['version']:
            # Remove a revision after its version has been manually reviewed.
            byid.pop(aid,None)
            continue
        previous=byid.get(aid,{})
        if previous.get('version',0)>entry['version']: continue
        status=previous.get('review_status','pending') if previous.get('version')==entry['version'] else 'pending'
        byid[aid]={**entry,'kind':'revision' if k else 'new_paper','review_status':status,'first_seen':previous.get('first_seen',discovered),'last_changed_seen':previous.get('last_changed_seen',discovered) if previous.get('version')==entry['version'] else discovered}
    return sorted(byid.values(),key=lambda x:(x['updated'],x['id']),reverse=True)

def markdown(rows):
    escape=lambda x:str(x).replace('|',r'\|').replace('\n',' ')
    lines=['# Daily candidates and revisions','','Automated discovery provides metadata only; relevance, conclusions, and categories require manual review. Excluded entries retain review_status=rejected to prevent repeated notifications.','','| Updated | Type | Paper | Status |','|---|---|---|---|']
    for p in rows:
        lines.append(f'| {p["updated"][:10]} | {p["kind"]} | [{escape(p["title"])}]({p["paper_url"]}) v{p["version"]} | {p["review_status"]} |')
    if not rows: lines+=['','No automated discovery results yet. Results will appear after publishing to GitHub and enabling the workflow; an empty list does not imply that no recent papers exist.']
    return '\n'.join(lines)+'\n'

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--days',type=int,default=14)
    parser.add_argument('--max-pages',type=int,default=10)
    parser.add_argument('--fixture',type=Path,help='Offline Atom fixture; writes only candidate output.')
    parser.add_argument('--output-dir',type=Path,default=ROOT)
    args=parser.parse_args()
    if args.days<1 or args.max_pages<1: parser.error('positive days/pages required')
    curated=json.loads((ROOT/'data/papers.json').read_text())
    cfg=json.loads((ROOT/'data/search_queries.json').read_text())
    now=dt.datetime.now(dt.timezone.utc)
    cutoff=now-dt.timedelta(days=args.days)
    incoming=[]
    coverage=[]
    if args.fixture:
        incoming,_=parse_feed(args.fixture.read_bytes())
        coverage=['offline-fixture']
    else:
        for query in cfg['queries']:
            exhausted=False
            for page in range(args.max_pages):
                rows,total=fetch(dict(search_query=query,start=page*100,max_results=100,sortBy='lastUpdatedDate',sortOrder='descending'))
                recent=[p for p in rows if dt.datetime.fromisoformat(p['updated'].replace('Z','+00:00'))>=cutoff]
                incoming+=recent
                if len(recent)<len(rows) or (page+1)*100>=total or not rows:
                    exhausted=True
                    break
            if not exhausted: raise RuntimeError('Pagination cap reached; increase --max-pages. No output changed.')
            coverage.append(query)
        # Existing records are checked even if their title/abstract stops matching keywords.
        for offset in range(0,len(curated),50):
            ids=[p['id'] for p in curated[offset:offset+50]]
            rows,_=fetch(dict(id_list=','.join(ids),max_results=len(ids)))
            if {p['id'] for p in rows}!=set(ids): raise RuntimeError('Incomplete ID lookup; no output changed')
            incoming+=rows
    out=args.output_dir
    candidate=out/'data/candidates.json'
    old=json.loads(candidate.read_text()) if candidate.exists() else []
    combined=merge(old,incoming,curated,now.date().isoformat())
    payloads={candidate:json.dumps(combined,ensure_ascii=False,indent=2)+'\n',out/'docs/inbox.md':markdown(combined),out/'data/discovery_status.json':json.dumps(dict(checked_at=now.isoformat(),mode='fixture' if args.fixture else 'live',days=args.days,queries=coverage,record_count=len(combined)),ensure_ascii=False,indent=2)+'\n'}
    for path,body in payloads.items():
        path.parent.mkdir(parents=True,exist_ok=True)
        temp=path.with_suffix(path.suffix+'.tmp')
        temp.write_text(body)
        os.replace(temp,path)
    print(f'{len(combined)} candidates/revisions. Curated index unchanged.')

if __name__=='__main__': main()
