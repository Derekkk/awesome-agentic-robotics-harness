import importlib.util
import json
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('discover', ROOT/'scripts/discover.py')
discovery=importlib.util.module_from_spec(spec)
spec.loader.exec_module(discovery)

class IndexTests(unittest.TestCase):
    def test_curated_integrity(self):
        rows=json.loads((ROOT/'data/papers.json').read_text())
        cats=json.loads((ROOT/'data/categories.json').read_text())
        self.assertEqual(len(rows),len({p['id'] for p in rows}))
        for p in rows:
            self.assertRegex(p['id'],r'^\d{4}\.\d{4,5}$')
            self.assertTrue(set(p['tags'])<=set(cats))
            self.assertTrue(p['sources'])
            self.assertTrue((ROOT/'papers'/f'{p["id"]}.md').exists())
            self.assertIn(p['verification'],{'primary_abstract','official_project','primary_search_abstract','full_text'})

    def test_versions_dedup_and_review(self):
        known=[{'id':'2601.12345','version':2}]
        def entry(v): return dict(id='2601.12345',version=v,title='Fixture',updated='2026-09-20T00:00:00Z')
        rows=discovery.merge([], [entry(2),entry(3),entry(3)], known,'2026-09-22')
        self.assertEqual(len(rows),1)
        self.assertEqual(rows[0]['kind'],'revision')
        rows[0]['review_status']='rejected'
        self.assertEqual(discovery.merge(rows,[entry(3)],known,'2026-09-23')[0]['review_status'],'rejected')
        self.assertEqual(discovery.merge(rows,[entry(4)],known,'2026-09-23')[0]['review_status'],'pending')
        self.assertEqual(discovery.merge(rows,[entry(3)],[{'id':'2601.12345','version':3}],'2026-09-23'),[])

    def test_parse_and_fail_closed(self):
        rows,total=discovery.parse_feed((ROOT/'tests/fixture.xml').read_bytes())
        self.assertEqual(total,2)
        self.assertEqual(rows[0]['version'],3)
        with self.assertRaises(ValueError): discovery.parse_feed(b'<html>server failure</html>')
        with self.assertRaises(ValueError): discovery.parse_feed(b'<feed xmlns="http://www.w3.org/2005/Atom"><entry><id>http://arxiv.org/api/errors</id></entry></feed>')

    def test_relative_links(self):
        for path in ROOT.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
                if '://' in target or target.startswith('#'): continue
                self.assertTrue((path.parent/target.split('#')[0]).exists(),f'{path}: {target}')

if __name__=='__main__': unittest.main()
