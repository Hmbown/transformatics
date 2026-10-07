#!/usr/bin/env python3
"""Build the reviewed Markdown learning notes; validate its navigation and claim graph.

Requires the pinned package in notes/requirements.txt. No network at build time.
Writes notes/_site; --update-claim-index also refreshes notes/claims.md.
Run from any working directory.
"""
from pathlib import Path
from html import escape
from html.parser import HTMLParser
import json
import argparse
import hashlib
import re
import shutil
from urllib.parse import urlsplit, unquote
import markdown

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / 'notes'
OUT = BOOK / '_site'
META = json.loads((BOOK / 'notes.json').read_text())
REGISTRY = json.loads((BOOK / 'claims.json').read_text())
COURSE = json.loads((BOOK / 'course-outline.json').read_text())
CHAPTERS = META['chapters']
ASSET_URLS = {
    name: f'assets/{name}?v={hashlib.sha256((BOOK / "assets" / name).read_bytes()).hexdigest()[:12]}'
    for name in ('book.css', 'book.js')
}



def claim_markdown():
    """A GitHub-readable view of the same claim registry used by the website."""
    lines = ['# Claim register', '',
             'Generated from [claims.json](claims.json); edit that source and run '
             '`python scripts/build_notes.py --update-claim-index`. The '
             'linked source records state the scope of each result.', '']
    lines += [REGISTRY['review_semantics'], '']
    lines += [REGISTRY['verification_label_semantics'], '']
    for c in REGISTRY['claims']:
        lines += [f'<a id="{c["id"]}"></a>', f'## {c["title"]}', '',
                  f'**Evidence record — {c.get("verification_label", c["status"])}.**', '',
                  c['scope'], '',
                  f'**Boundary.** {c["excludes"]}', '']
        if c['depends_on']:
            lines += ['**Prior inputs:** ' + ', '.join(f'[{d}](#{d})' for d in c['depends_on']) + '.', '']
        if c.get('evidence'):
            for key, value in c['evidence'].items():
                text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
                lines += [f'- **{key.replace("_", " ").capitalize()}:** {text}']
            lines += ['']
        lines += ['**Sources:** ' + ' · '.join(f'[{s}](../{s})' for s in c['sources']), '']
    return '\n'.join(lines)


def rewrite_links(source, transform):
    """Rewrite explicit Markdown and HTML URLs without altering the math or prose."""
    source = re.sub(r'\]\(([^\s)]+)\)', lambda m: '](' + transform(m[1]) + ')', source)
    return re.sub(r'\b(href|src)="([^"]+)"', lambda m: m[1] + '="' + transform(m[2]) + '"', source)


def chapter_site_source(source, slug, source_paths):
    """Canonical Markdown links resolve in GitHub; generated links resolve in the site."""
    def target(url):
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return url
        path = (BOOK/'chapters'/unquote(parsed.path)).resolve()
        assert path.is_relative_to(ROOT) and path.is_file(), f'{slug}.md: broken source link {url}'
        if path.parent == BOOK/'chapters' and path.stem in {s for s, _ in CHAPTERS}:
            route = path.stem + '.html'
        elif path == BOOK/'claims.md':
            route = 'claims.html'
        elif path == BOOK/'claims.json':
            route = 'claims.json'
        elif path.is_relative_to(BOOK/'assets'):
            route = str(path.relative_to(BOOK))
        else:
            relative = str(path.relative_to(ROOT))
            source_paths.add(relative)
            route = 'source/' + relative
        return route + ('?' + parsed.query if parsed.query else '') + ('#' + parsed.fragment if parsed.fragment else '')
    return rewrite_links(source, target)


def render_md(source, slug='chapter'):
    # Keep canonical chapter math readable in GitHub. Normalize its delimiters
    # before stashing so Python-Markdown cannot consume TeX escapes.
    source = re.sub(r'\$\$(.*?)\$\$', lambda m: r'\[' + m[1] + r'\]', source, flags=re.S)
    source = re.sub(r'(?<!\\)\$([^$]+?)(?<!\\)\$', lambda m: r'\(' + m[1] + r'\)', source)
    # Python-Markdown otherwise consumes TeX backslashes and underscores.
    math = []
    def stash(match):
        math.append(match.group())
        return f'TEXPLACEHOLDER{len(math)-1}END'
    source = re.sub(r'\\\[.*?\\\]|\\\(.*?\\\)', stash, source, flags=re.S)
    renderer = markdown.Markdown(
        extensions=['tables', 'fenced_code', 'md_in_html', 'toc'],
        extension_configs={'toc': {'toc_depth': '2-2'}},
    )
    result = renderer.convert(source)
    sections = renderer.toc_tokens
    if sections:
        items = ''.join(
            f'<li><a href="#{escape(section["id"], quote=True)}">{section["name"]}</a></li>'
            for section in sections
        )
        outline = ('<details class="chapter-outline"><summary>In this chapter</summary>'
                   f'<nav aria-label="In this chapter"><ul>{items}</ul></nav></details>')
        result = re.sub(r'(</h1>)', lambda m: m[0] + outline, result, count=1)
    for i, expression in enumerate(math):
        result = result.replace(f'TEXPLACEHOLDER{i}END', escape(expression))
    solution_number = 0
    def solution_anchor(match):
        nonlocal solution_number
        if 'solution' not in match[2].lower():
            return match[0]
        solution_number += 1
        attrs = match[1]
        if not re.search(r'\bid=', attrs):
            attrs += f' id="solution-{slug}-{solution_number}"'
        return f'<details{attrs}><summary>{match[2]}</summary>'
    result = re.sub(r'<details([^>]*)>\s*<summary>(.*?)</summary>', solution_anchor, result, flags=re.S)
    return result


def page(slug, title, content, index=None):
    links = []
    for n, (key, name) in enumerate(CHAPTERS):
        group = META.get('parts', {}).get(key)
        if group:
            links.append(f'<li class="part-title">{escape(group)}</li>')
        selected = ' aria-current="page"' if key == slug else ''
        links.append(f'<li><a href="{key}.html"{selected}><span>{n:02d}</span>{escape(name)}</a></li>')
    selected = ' aria-current="page"' if slug == 'claims' else ''
    links.append(f'<li><a href="claims.html"{selected}><span>↗</span>Claim register</a></li>')
    pager = ''
    if index is not None:
        prev = CHAPTERS[index-1] if index else None
        nxt = CHAPTERS[index+1] if index+1 < len(CHAPTERS) else None
        pager = '<div class="nextprev" aria-label="Chapter navigation">'
        pager += f'<a href="{prev[0]}.html">← {escape(prev[1])}</a>' if prev else '<span></span>'
        pager += f'<a href="{nxt[0]}.html">{escape(nxt[1])} →</a>' if nxt else '<a href="claims.html">Inspect the claim register →</a>'
        pager += '</div>'
    source_link = f'<a href="chapters/{slug}.md">Chapter Markdown</a>' if index is not None else '<a href="claims.json">Machine-readable JSON</a>'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} · Transformatics</title><link rel="icon" href="data:,"><meta name="description" content="{escape(META['subtitle'])}. Definitions, proofs, worked examples, exercises, and a three-dimensional fluid laboratory.">
<link rel="stylesheet" href="{ASSET_URLS['book.css']}"><script defer src="{ASSET_URLS['book.js']}"></script>
<script>window.MathJax={{tex:{{inlineMath:[['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']]}},options:{{skipHtmlTags:['script','noscript','style','textarea','pre','code']}}}};</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js"></script>
</head><body><a class="skip" href="#main">Skip to chapter</a>
<header class="site-header"><p><a class="brand" href="index.html">Transformatics</a></p>
<nav class="site-links" aria-label="Site navigation"><a href="index.html">Home</a><a href="search.html">Search</a><a href="simulator.html">3D fluid lab</a><a href="glossary.html">Glossary</a><a href="claims.html">Claims</a><button class="theme" type="button">Change appearance</button></nav>
<details class="book-contents" id="contents"><summary>All chapters</summary><nav aria-label="Learning notes contents"><ol>{''.join(links)}</ol></nav></details></header>
<div class="layout"><div class="masthead">{source_link} · <span class="edition">{escape(META['edition'])}</span></div><main id="main" tabindex="-1"><article>{content}</article>{pager}</main><footer><a href="credits.html">Authors and credits</a> · <a href="references.html">References</a> · <a href="course.json">Course JSON</a> · <a href="all-chapters.md">Complete Markdown</a> · <a href="LICENSE.txt">License</a><br>Equations use MathJax 3.2.2; the source notation remains readable offline. Print includes exercise solutions.</footer></div>
</body></html>'''


def claim_html():
    parts = ['<h1>A register of claims</h1>', '<p><a href="claims.json">Download the machine-readable register and source hashes</a> · <a href="source/docs/STATUS.md">Canonical research status</a></p>']
    parts.append(f'<p>{escape(REGISTRY["review_semantics"])}</p>')
    parts.append(f'<p>{escape(REGISTRY["verification_label_semantics"])}</p>')
    for c in REGISTRY['claims']:
        dependencies = ', '.join(f'<a href="#{escape(d)}">{escape(d)}</a>' for d in c['depends_on']) or 'No dependencies asserted by this editorial index.'
        sources = ' · '.join(f'<a href="source/{escape(s)}">{escape(s)}</a>' for s in c['sources'])
        def field_text(value):
            if isinstance(value,list): return '; '.join(map(str,value))
            if isinstance(value,dict): return json.dumps(value,ensure_ascii=False)
            return str(value)
        details = ''
        for group, label in [('evidence','Provenance and verification'),('contract','Assumptions, norms and coordinates')]:
            if c.get(group):
                rows=''.join(f'<dt>{escape(k.replace("_"," ").capitalize())}</dt><dd>{escape(field_text(v))}</dd>' for k,v in c[group].items())
                details += f'<details><summary>{label}</summary><dl>{rows}</dl></details>'
        parts.append(f'<section class="claim" id="{escape(c["id"])}"><h2>{escape(c["title"])}</h2><span class="tag">{escape(c.get("verification_label", c["status"]))}</span><p>{escape(c["scope"])}</p><dl><dt>Boundary</dt><dd>{escape(c["excludes"])}</dd><dt>Dependencies / prior inputs</dt><dd>{dependencies}</dd></dl>{details}<p class="source-links">{sources}</p></section>')
    return ''.join(parts)


class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.targets=[]; self.ids=set()
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        key = 'href' if tag == 'a' else 'src' if tag in ('script','img') else None
        if tag == 'link': key = 'href'
        if key and attrs.get(key): self.targets.append(attrs[key])


class Catalogue(HTMLParser):
    def __init__(self):
        super().__init__(); self.sections=[]; self.solutions=[]; self.words=[]; self.heading=None; self.skip=0
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag in ('script','style'): self.skip += 1
        if re.fullmatch(r'h[1-6]', tag): self.heading={'id':attrs.get('id',''),'title':'','level':int(tag[1])}
        if tag=='details' and attrs.get('id','').startswith('solution-'):
            self.solutions.append({'id':attrs['id'],'section':self.sections[-1]['id'] if self.sections else ''})
    def handle_data(self, data):
        if not self.skip: self.words.append(data)
        if self.heading is not None: self.heading['title'] += data
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.skip=max(0,self.skip-1)
        if re.fullmatch(r'h[1-6]',tag) and self.heading is not None:
            self.sections.append(self.heading); self.heading=None


def build(update_claim_index=False):
    index = BOOK/'claims.md'
    expected_index = claim_markdown()
    if update_claim_index:
        index.write_text(expected_index)
    assert index.is_file() and index.read_text() == expected_index, 'Refresh the readable claim register with --update-claim-index.'
    ids = [c['id'] for c in REGISTRY['claims']]
    assert len(ids) == len(set(ids)), 'Duplicate claim identifier'
    for c in REGISTRY['claims']:
        assert set(c['depends_on']) <= set(ids), f'Unknown dependency in {c["id"]}'
        assert c['status'] in {'OPEN','DEAD','PROVED','IMPORTED','WITHDRAWN','NUMERICAL','VERIFIED','CERTIFIED','KERNEL-CHECKED','UNDER REVIEW'}
        if 'evidence' in c:
            assert set(c['evidence']) == {'provenance','proof_status','review','formalization'}, f'Incomplete evidence axes: {c["id"]}'
    for relative, digest in REGISTRY.get('source_sha256', {}).items():
        assert hashlib.sha256((ROOT/relative).read_bytes()).hexdigest() == digest, f'Stale primary-source hash: {relative}; review and refresh the editable register snapshot.'
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copytree(BOOK/'assets', OUT/'assets', dirs_exist_ok=True)
    (OUT/'chapters').mkdir(exist_ok=True)
    (OUT/'claims.json').write_text(json.dumps(REGISTRY, ensure_ascii=False, indent=2)+'\n')
    (OUT/'.nojekyll').touch()
    source_paths = {s for c in REGISTRY['claims'] for s in c['sources']}
    course = dict(COURSE); course.update(title=META['title'],edition=META['edition'],chapters=[])
    search=[]; complete=[]
    chapter_ids={s for s,_ in CHAPTERS}
    for i, (slug, title) in enumerate(CHAPTERS):
        source = (BOOK/'chapters'/f'{slug}.md').read_text()
        info=COURSE['chapters'][slug]
        assert set(info['prerequisites']) <= chapter_ids, f'Unknown prerequisite for {slug}'
        site_source = chapter_site_source(source, slug, source_paths)
        downloadable = rewrite_links(site_source, lambda url: url if urlsplit(url).scheme or urlsplit(url).netloc or url.startswith('#') else '../' + url)
        (OUT/'chapters'/f'{slug}.md').write_text(downloadable)
        rendered=render_md(site_source,slug)
        (OUT/f'{slug}.html').write_text(page(slug,title,rendered,i))
        catalog=Catalogue(); catalog.feed(rendered)
        row=dict(info,id=slug,title=title,html=f'{slug}.html',markdown=f'chapters/{slug}.md',
                 source_sha256=hashlib.sha256(source.encode()).hexdigest(),download_sha256=hashlib.sha256(downloadable.encode()).hexdigest(),
                 sections=catalog.sections,solutions=catalog.solutions,word_count=len(source.split()))
        course['chapters'].append(row)
        search.append({'title':title,'url':f'{slug}.html','text':' '.join(catalog.words),'sections':catalog.sections})
        complete.append(site_source)
    (OUT/'course.json').write_text(json.dumps(course,ensure_ascii=False,indent=2)+'\n')
    (OUT/'search-index.json').write_text(json.dumps(search,ensure_ascii=False)+'\n')
    (OUT/'all-chapters.md').write_text('\n\n---\n\n'.join(complete))
    shutil.copy2(ROOT/'LICENSE', OUT/'LICENSE.txt')
    if (ROOT/'CITATION.cff').is_file(): shutil.copy2(ROOT/'CITATION.cff', OUT/'CITATION.cff')
    (OUT/'llms.txt').write_text('# Transformatics\n\nOpen learning notes: finite change, evolution, and transfer between models.\n\n- [Course, prerequisites, objectives, sections, solutions and source hashes](course.json)\n- [All chapters in Markdown](all-chapters.md)\n- [Scoped research claims and source hashes](claims.json)\n- [Attribution and provenance](credits.html)\n- [References](references.html)\n\nThe course manifest is a reading index, not a proof certificate. Imported external results and this project\'s finite research claims have separate evidence records.\n')
    (OUT/'search.html').write_text(page('search','Search the learning notes','''<h1>Search the learning notes</h1><p>Find a definition, example or exercise. Search runs in your browser.</p><label for="book-search">Words or a phrase</label><input id="book-search" type="search" placeholder="e.g. pressure, finite difference, smooth force" style="display:block;width:100%;margin:10px 0;padding:8px"><p id="search-status" role="status">Enter a search term.</p><ol id="search-results"></ol><noscript><p>Search requires JavaScript. Use <a href="glossary.html">the glossary</a> or your browser's Find command in <a href="all-chapters.md">the complete Markdown notes</a>.</p></noscript>'''))
    (OUT/'claims.html').write_text(page('claims','A register of claims',claim_html()))
    # Snapshot the primary reading sources, preserving their repository-relative paths.
    # Linked companion pins are included so the Markdown stays useful after download.
    queue = list(source_paths); copied = set()
    while queue:
        relative = queue.pop()
        source = (ROOT/relative).resolve()
        if source in copied: continue
        if not source.is_relative_to(ROOT): continue
        if not source.is_file():
            raise FileNotFoundError(f'Missing learning notes source: {relative}')
        target = OUT/'source'/source.relative_to(ROOT)
        target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(source,target); copied.add(source)
        if source.suffix == '.md':
            for url in re.findall(r'\]\(([^\s)]+)\)', source.read_text()):
                parsed=urlsplit(url)
                if parsed.scheme or not parsed.path: continue
                candidate=(source.parent/unquote(parsed.path)).resolve()
                if candidate.is_relative_to(ROOT) and candidate.is_file() and candidate.suffix in {'.md','.py','.json','.txt','.lean','.toml','.yml','.yaml'}:
                    queue.append(str(candidate.relative_to(ROOT)))
    snapshot = dict(REGISTRY)
    snapshot['source_root'] = 'source/'
    snapshot['source_hash_scope'] = 'Complete linked source snapshot for this generated edition; the editable register pins its primary sources separately.'
    snapshot['source_sha256'] = {str(p.relative_to(ROOT)): hashlib.sha256((OUT/'source'/p.relative_to(ROOT)).read_bytes()).hexdigest() for p in sorted(copied)}
    (OUT/'claims.json').write_text(json.dumps(snapshot, ensure_ascii=False, indent=2)+'\n')
    parsed_pages={}
    for path in OUT.glob('*.html'):
        parser=Links(); parser.feed(path.read_text()); parsed_pages[path.resolve()]=parser
    for path, parser in parsed_pages.items():
        for url in parser.targets:
            parsed=urlsplit(url)
            if parsed.scheme or parsed.netloc: continue
            target=(path.parent/unquote(parsed.path)).resolve() if parsed.path else path
            assert target.is_relative_to(OUT.resolve()) and target.is_file(), f'{path.name}: broken link {url}'
            if parsed.fragment and target in parsed_pages:
                assert unquote(parsed.fragment) in parsed_pages[target].ids, f'{path.name}: broken anchor {url}'
    print(f'Built {len(parsed_pages)} pages; validated all HTML local links and claim dependencies; copied {len(copied)} source files.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--update-claim-index', action='store_true', help='Refresh the committed GitHub-readable claim register from claims.json.')
    build(parser.parse_args().update_claim_index)
