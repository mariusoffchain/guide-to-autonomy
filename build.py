#!/usr/bin/env python3
# A Guide to Autonomy, static site generator.
# Copyright (C) 2026 the contributors of A Guide to Autonomy
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version. See LICENSE.
"""Build one edition of A Guide to Autonomy as a static website.

    python3 build.py                       build edition.json into dist/
    python3 build.py --serve               build, then preview on http://127.0.0.1:8000/
    python3 build.py --edition examples/riverside-meetup/edition.json --out dist-riverside
    python3 build.py --check               render and check everything, write nothing
    python3 build.py --update-actions      give IDs to new checklist actions, retire removed ones

Everything an edition changes lives in its edition.json (see docs/CONFIGURATION.md).
The text lives in content/<language>/*.md with its manifest book.json, its UI
strings strings.json and its action registry actions.json. The look lives in
theme/. The output is static HTML and CSS plus JavaScript that runs in the
reader's browser: no server code, no database, no external request. Every
edition also gets a page of licences, credits and source (legal/), the full
licence and notice texts, and a ZIP of its own source (source/, see release.py).
Only Python 3.9+ and Python-Markdown are needed.

The build never deletes a file. It writes only inside the output folder, and
only the files whose content changed, plus an internal build report next to
that folder (<out>.build-report.json), never inside it. release-manifest.json
lists the files of the current build; release.py exports exactly those.
"""

import argparse
import hashlib
import html
import io
import json
import re
import shutil
import sys
import unicodedata
import zipfile
import xml.etree.ElementTree as ET
from html.entities import name2codepoint
from pathlib import Path
from urllib.parse import quote, urlsplit

try:
    import markdown
except ImportError:
    sys.exit('Python-Markdown is missing. Install it with:  python3 -m pip install -r requirements.txt')

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import release  # noqa: E402  (source archive and notices, next to this file)

THEME = ROOT / 'theme'
# Version of the base (generator, theme and reference text). Each release is described in CHANGELOG.md.
VERSION = '1.2.0'
# The original work, credited in every edition whatever its own name and branding.
ORIGINAL = {'title': 'A Guide to Autonomy', 'project': 'PROOF', 'initiative': 'Cypher Baltics',
            'url': 'https://proofconference.com/book/en/'}
# The licence texts are shipped unchanged: the official AGPL v3 text, byte for byte, and the CC BY-SA 4.0 legal code.
AGPL_SHA256 = '0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0'
LEGAL_TEXTS = [('LICENSE', 'legal/LICENSE.txt'), ('LICENSE-CONTENT', 'legal/LICENSE-CONTENT.txt'),
               ('NOTICE', 'legal/NOTICE.txt'), ('THIRD-PARTY.md', 'legal/THIRD-PARTY.txt')]
EXTENSIONS = ['tables', 'toc', 'fenced_code', 'sane_lists', 'attr_list']

DEFAULTS = {
    'edition': {'name': 'Community edition', 'label': '', 'community': 'your community', 'community_url': '',
                'contact': '', 'repository': '', 'wordmark': '', 'logo': {'file': '', 'cover_file': '', 'alt': ''},
                'changes': '', 'modified': ''},
    'book': {'title': 'A Guide to Autonomy', 'title_lines': [], 'outlined_line': -1, 'kicker': 'A learning book',
             'intro': [], 'start_chapter': '', 'start_paths': [], 'search_suggestions': []},
    'language': {'code': 'en', 'name': 'English', 'direction': 'ltr', 'content_dir': 'content/en', 'locale': 'en_US'},
    'other_editions': [],
    'colors': {'scheme': 'light', 'background': '#ffffff', 'foreground': '#141414',
               'parts': [{'accent': '#0f766e', 'text': '#0f766e'}, {'accent': '#4f46e5', 'text': '#4f46e5'},
                         {'accent': '#b45309', 'text': '#b45309'}]},
    'fonts': {'heading': {'family': '', 'fallback': 'system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
                          'weight': '700', 'files': []},
              'body': {'family': '', 'fallback': 'system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
                       'files': []}},
    'layout': {'reading_width': '42rem', 'page_toc': True, 'uppercase_headings': True, 'cover_part_bars': True,
               'show_progress': True, 'show_search': True},
    'site': {'url': '', 'base_path': '/', 'offline': False, 'sitemap': True, 'indexing': True, 'og_image': '', 'favicon': ''},
    'storage_key': 'guide-autonomy.v1',
    'directory': {'enabled': False, 'file': 'editions.json'},
    # Optional recordings of talks on the cover. Off and empty by default; no video is shipped with the base.
    'recordings': {'enabled': False, 'kicker': '', 'title': '', 'intro': '', 'media_origins': [], 'items': []},
    'licence': {'content': {'label': 'CC BY-SA 4.0', 'url': 'https://creativecommons.org/licenses/by-sa/4.0/'},
                'code': {'label': 'AGPL-3.0-or-later', 'url': 'https://www.gnu.org/licenses/agpl-3.0.html'}},
}

CSP = ("default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; "
       "font-src 'self'; connect-src 'none'; frame-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'")
YOUTUBE = re.compile(r'^https://(?:www\.)?(?:youtube\.com/(?:watch\?v=|embed/|shorts/)|youtu\.be/)([A-Za-z0-9_-]{6,})')
YOUTUBE_EMBED = 'https://www.youtube-nocookie.com'


def origin_of(url):
    parts = urlsplit(url)
    return '%s://%s' % (parts.scheme, parts.netloc)


def csp(cfg, key=''):
    """Content-Security-Policy of a page. Only the cover of an edition with recordings may load a player, and only
    from the addresses of its own recordings (frame-src for YouTube, media-src for video files)."""
    rec = cfg.get('_recordings')
    if key != 'home/' or not rec:
        return CSP
    frame = ' '.join(rec['frame_origins']) or "'none'"
    media = ' '.join(["'self'"] + rec['media_origins'])
    return CSP.replace("frame-src 'none'", 'frame-src ' + frame) + '; media-src ' + media


NOSCRIPT_CSS = ('@media (max-width: 1023px) { .toc-toggle { display: none; } .toc-aside { position: static; } '
                '.page-toc, .page-toc .toc-title { display: block; } .page-toc { position: static; max-height: none; box-shadow: none; } }')
KIND_BY_ID = {'in-brief': 'brief', 'step-by-step': 'steps', 'mistakes-to-avoid': 'pitfalls',
              'go-further': 'further', 'sources': 'sources', 'your-checklist': 'checklist'}
TICK = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath "
        "d='M3 8.4l3.3 3.2L13 4.6' fill='none' stroke='%23{hex}' stroke-width='2.4'/%3E%3C/svg%3E\")")


class BuildError(Exception):
    pass


# ---------- small helpers ----------

def sha256(data):
    return hashlib.sha256(data).hexdigest()


def esc(s):
    return html.escape(str(s), quote=True)


def squash(s):
    return ' '.join(str(s).split())


def pad(n):
    return '%02d' % n


def fold(s):
    return ''.join(ch for ch in unicodedata.normalize('NFD', s) if not '\u0300' <= ch <= '\u036f').lower()


def slugify(s):
    return re.sub(r'^-|-$', '', re.sub(r'[^a-z0-9]+', '-', fold(s)))


def host_of(url):
    try:
        host = urlsplit(url).hostname
    except ValueError:
        return url
    if not host:
        return url
    return host[4:] if host.startswith('www.') else host


def merge(base, over, path=''):
    """Deep merge of the user's configuration over the defaults. Unknown keys are reported."""
    out = dict(base)
    for k, v in (over or {}).items():
        if k.startswith('$') or k == 'about':
            continue
        if k not in base:
            raise BuildError('edition.json: unknown key "%s%s". See docs/CONFIGURATION.md.' % (path, k))
        if isinstance(base[k], dict) and isinstance(v, dict):
            out[k] = merge(base[k], v, path + k + '.')
        else:
            out[k] = v
    return out


def hex_rgb(value, what):
    m = re.fullmatch(r'#?([0-9a-fA-F]{6})', str(value).strip())
    if not m:
        raise BuildError('%s must be a 6-digit hex colour such as #1a2b3c, found %r.' % (what, value))
    h = m.group(1)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgba(rgb, a):
    return 'rgba(%d, %d, %d, %s)' % (rgb[0], rgb[1], rgb[2], ('%.2f' % a).rstrip('0').rstrip('.'))


def mix(a, b, t):
    """Colour a mixed into b by fraction t (0 = b, 1 = a)."""
    return '#%02x%02x%02x' % tuple(round(b[i] + (a[i] - b[i]) * t) for i in range(3))


class Strings:
    """UI strings of the language, with {placeholders} and _one/_many plurals."""

    def __init__(self, data):
        self.data = data

    def __call__(self, key, **kw):
        if key not in self.data:
            raise BuildError('strings.json: missing key "%s".' % key)
        value = self.data[key]
        if not isinstance(value, str):
            return value
        return value.format(**kw) if kw else value

    def opt(self, key, default, **kw):
        """A string that a language may translate in strings.json; the English default otherwise."""
        value = self.data.get(key, default)
        return value.format(**kw) if kw else value

    def n(self, key, n, **kw):
        return self(key + ('_one' if n == 1 else '_many'), n=n, **kw)

    def join(self, items):
        if len(items) > 1:
            return self('list_comma').join(items[:-1]) + self('list_and') + items[-1]
        return ''.join(items)

    def runtime(self):
        keys = ['search_try', 'search_none', 'search_results_one', 'search_results_many', 'search_first_shown',
                'search_loading', 'search_error', 'results_label', 'storage_unavailable', 'read_mark', 'marked_as_read',
                'confirm_clear', 'press_again', 'progress_cleared', 'continue_reading', 'chapter_n',
                'offline_ready', 'offline_saving', 'offline_failed', 'offline_none']
        return {k: self.data[k] for k in keys}


# ---------- content: Markdown, checklists, action registry ----------

TAG = re.compile(r'<[^>]+>')
EFFORT = re.compile(r'\s*\(([^()<>]+)\)\s*$')
CHECK_MD = re.compile(r'^- \[ \] ', re.M)
CHECK_LI = re.compile(r'<li>\[ \] (.*?)</li>')
H1_HTML = re.compile(r'<h1 id="[^"]*">.*?</h1>\n?')
QUOTES = str.maketrans({'\u2018': "'", '\u2019': "'", '\u201c': '"', '\u201d': '"'})
STOPWORDS = {'a', 'an', 'the', 'and', 'or', 'of', 'to', 'on', 'in', 'at', 'for', 'with', 'from',
             'by', 'it', 'its', 'is', 'that', 'this', 'your', 'you', 'any', 'every', 'then'}
PLACEHOLDER = re.compile(r'\{\{\s*([a-z_]+)\s*\}\}')


def plain(fragment):
    return ' '.join(html.unescape(TAG.sub('', fragment)).split())


def normalize(text):
    text = unicodedata.normalize('NFKC', plain(text)).translate(QUOTES)
    return ' '.join(text.casefold().split())


def split_effort(fragment):
    m = EFFORT.search(fragment)
    return (fragment[:m.start()], m.group(1).strip()) if m else (fragment, '')


def mint_id(chapter, text, taken):
    words = [w for w in re.findall(r'[a-z0-9]+', normalize(text)) if w not in STOPWORDS][:4]
    base = '-'.join([chapter] + (words or ['action']))
    new, k = base, 2
    while new in taken:
        new, k = '%s-%d' % (base, k), k + 1
    return new


def render_markdown(name, text, expected_h1):
    first = text.lstrip('\n').split('\n', 1)[0]
    if first != '# ' + expected_h1:
        raise BuildError('%s: expected the title "# %s" on the first line, found "%s". Titles in book.json and in the '
                         'Markdown files must match.' % (name, expected_h1, first))
    md = markdown.Markdown(extensions=EXTENSIONS)
    body = md.convert(text)
    m = H1_HTML.match(body)
    if not m:
        raise BuildError('%s: the rendered page does not start with its title.' % name)
    body = body[m.end():]
    if '<h1' in body:
        raise BuildError('%s: only 1 top-level title (# ...) is allowed per file.' % name)
    tokens = md.toc_tokens
    if len(tokens) != 1 or tokens[0]['level'] != 1:
        raise BuildError('%s: unexpected heading structure (sections must be ## headings under the single # title).' % name)
    return body, tokens[0]['children']


def checklist_items(name, text, body):
    md_count = len(CHECK_MD.findall(text))
    items = CHECK_LI.findall(body)
    if md_count != len(items):
        raise BuildError('%s: %d "- [ ]" lines in the source but %d rendered as checklist items. Keep every action on '
                         'its own "- [ ] " line inside the "Your checklist" section.' % (name, md_count, len(items)))
    out = []
    for item in items:
        text_html, effort = split_effort(item)
        out.append({'html': item, 'text': plain(text_html), 'effort': effort})
    return out


class Content:
    """The Markdown of one language: manifest, chapters, other pages, action IDs, UI strings, tool links."""

    def __init__(self, cfg, update_registry=False):
        self.dir = (ROOT / cfg['language']['content_dir']).resolve()
        if not self.dir.is_dir():
            raise BuildError('Content folder not found: %s (language.content_dir in edition.json).' % self.dir)
        self.manifest = self.read_json('book.json')
        self.strings = Strings(self.read_json('strings.json'))
        self.links = self.read_json('links.json') if (self.dir / 'links.json').is_file() else {}
        self.registry_path = self.dir / 'actions.json'
        self.registry = self.read_json('actions.json') if self.registry_path.is_file() else {'about': '', 'actions': []}
        self.slugs = dict({'start': 'start', 'actions': 'actions', 'editions': 'editions', 'legal': 'legal'},
                          **self.manifest.get('slugs', {}))
        self.vars = {
            'community': cfg['edition']['community'], 'edition_name': cfg['edition']['name'],
            'contact': cfg['edition']['contact'] or cfg['edition']['community_url'] or cfg['edition']['community'],
            'community_url': cfg['edition']['community_url'], 'book_title': cfg['book']['title'],
        }
        self.sources, self.chapters, self.pages = [], [], []
        self.load(update_registry)

    def read_json(self, name):
        path = self.dir / name
        if not path.is_file():
            raise BuildError('Missing %s in %s.' % (name, self.dir))
        try:
            return json.loads(path.read_text(encoding='utf-8'))
        except ValueError as e:
            raise BuildError('%s is not valid JSON: %s' % (path, e))

    def read_markdown(self, name):
        path = self.dir / name
        if not path.is_file():
            raise BuildError('Source file not found: %s (listed in book.json).' % path)
        raw = path.read_bytes()
        text = raw.decode('utf-8-sig').replace('\r\n', '\n')
        text = PLACEHOLDER.sub(lambda m: self.vars.get(m.group(1), m.group(0)), text)
        return raw, text

    def load(self, update_registry):
        M = self.manifest
        parts = {p['number']: p for p in M['parts']}
        for name_key in ('introduction', 'glossary'):
            if M.get(name_key):
                self.add_page(M[name_key], name_key, None)
        for p in M['parts']:
            self.add_page(p, 'part', p['number'], h1_prefix=self.strings('part_prefix', n=p['number']))
        numbers = set()
        for c in M['chapters']:
            if c['number'] in numbers:
                raise BuildError('book.json: chapter number %d is listed twice.' % c['number'])
            numbers.add(c['number'])
            if c['part'] not in parts:
                raise BuildError('book.json: chapter %d refers to part %d, which is not declared.' % (c['number'], c['part']))
            raw, text = self.read_markdown(c['file'])
            h1 = self.strings('chapter_prefix', n=c['number']) + c['title']
            body, toc = render_markdown(c['file'], text, h1)
            actions = checklist_items(c['file'], text, body)
            if actions:
                first_h2, first_item = body.find('<h2 '), body.find('<li>[ ] ')
                if first_h2 == -1 or first_item < first_h2:
                    raise BuildError('%s: checklist actions must sit under a "## Your checklist" section, not before the first section.' % c['file'])
            self.sources.append({'file': c['file'], 'kind': 'chapter', 'id': c['id'], 'sha256': sha256(raw)})
            self.chapters.append({'number': c['number'], 'id': c['id'], 'title': c['title'], 'part': c['part'],
                                  'source': c['file'], 'html': body, 'headings': toc, 'actions': actions, 'markdown': text})
        self.chapters.sort(key=lambda c: c['number'])
        ids = [c['id'] for c in self.chapters]
        if len(set(ids)) != len(ids):
            raise BuildError('book.json: 2 chapters share the same id.')
        if not self.chapters:
            raise BuildError('book.json lists no chapter.')
        self.assign_action_ids(update_registry)

    def add_page(self, entry, kind, part, h1_prefix=''):
        raw, text = self.read_markdown(entry['file'])
        body, toc = render_markdown(entry['file'], text, h1_prefix + entry['title'])
        if checklist_items(entry['file'], text, body):
            raise BuildError('%s: only chapters may contain checklist actions.' % entry['file'])
        self.sources.append({'file': entry['file'], 'kind': kind, 'id': entry['id'], 'sha256': sha256(raw)})
        self.pages.append({'id': entry['id'], 'kind': kind, 'title': entry['title'], 'part': part, 'slug': entry['slug'],
                           'source': entry['file'], 'html': body, 'headings': toc, 'markdown': text})

    def assign_action_ids(self, update):
        entries = self.registry.setdefault('actions', [])
        seen = set()
        for e in entries:
            if e['id'] in seen:
                raise BuildError('actions.json: ID %s is listed twice.' % e['id'])
            seen.add(e['id'])
        taken = set(seen)
        added, retired, problems = [], [], []
        for ch in self.chapters:
            cid = ch['id']
            pool = {normalize(e['text']): e for e in entries if e['chapter'] == cid}
            for e in [e for e in entries if e['chapter'] == cid]:
                for t in e.get('previous_texts', []):
                    pool.setdefault(normalize(t), e)
            keys = [normalize(a['text']) for a in ch['actions']]
            if len(set(keys)) != len(keys):
                raise BuildError('%s: 2 checklist actions have the same text.' % ch['source'])
            matched = set()
            for a, key in zip(ch['actions'], keys):
                e = pool.get(key)
                if e is not None and not e.get('retired'):
                    a['id'] = e['id']
                    matched.add(e['id'])
                elif e is not None and update:
                    e.pop('retired', None)
                    a['id'] = e['id']
                    matched.add(e['id'])
                    added.append({'id': e['id'], 'chapter': cid, 'text': a['text'], 'reactivated': True})
                elif update:
                    new = {'id': mint_id(cid, a['text'], taken), 'chapter': cid, 'text': a['text']}
                    taken.add(new['id'])
                    entries.append(new)
                    a['id'] = new['id']
                    matched.add(new['id'])
                    added.append({'id': new['id'], 'chapter': cid, 'text': a['text']})
                else:
                    problems.append('%s: no entry in actions.json for "%s"%s' % (cid, a['text'], ' (its entry is retired)' if e is not None else ''))
            for e in entries:
                if e['chapter'] == cid and not e.get('retired') and e['id'] not in matched:
                    if update:
                        e['retired'] = True
                        retired.append({'id': e['id'], 'chapter': cid, 'text': e['text']})
                    else:
                        problems.append('%s: entry %s of actions.json is not in the checklist any more: "%s"' % (cid, e['id'], e['text']))
        known = {e['chapter'] for e in entries}
        for cid in known - {c['id'] for c in self.chapters}:
            for e in entries:
                if e['chapter'] == cid and not e.get('retired'):
                    if update:
                        e['retired'] = True
                        retired.append({'id': e['id'], 'chapter': cid, 'text': e['text']})
                    else:
                        problems.append('%s: chapter not in book.json but entry %s is still active in actions.json' % (cid, e['id']))
        if problems:
            raise BuildError('The checklists do not match %s:\n  - ' % self.registry_path.relative_to(ROOT)
                             + '\n  - '.join(problems)
                             + '\nIf an action was only reworded, update its "text" in actions.json (or add the old wording to '
                               '"previous_texts") to keep its ID and the ticks saved under it. If it is really new or removed, '
                               'run again with --update-actions: new actions get new IDs, removed ones are marked retired.')
        ids = [a['id'] for c in self.chapters for a in c['actions']]
        if len(set(ids)) != len(ids):
            raise BuildError('2 actions received the same ID.')
        self.added, self.retired = added, retired
        if update and (added or retired):
            self.write_registry()

    def write_registry(self):
        head = {k: v for k, v in self.registry.items() if k != 'actions'}
        lines = ['{']
        for k, v in head.items():
            lines.append('  %s: %s,' % (json.dumps(k), json.dumps(v, ensure_ascii=False)))
        lines.append('  "actions": [')
        lines.append(',\n'.join('    ' + json.dumps(e, ensure_ascii=False) for e in self.registry['actions']))
        lines.append('  ]')
        lines.append('}')
        self.registry_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


# ---------- autolinks: tool names in tables, bare domains ----------

class Linker:
    DOMAIN = re.compile(r'(?<![\w@/.-])((?:[a-z0-9-]+\.)+[a-z]{2,}(?:/[\w\-./%#?=&]*[\w/])?)')

    def __init__(self, links):
        self.links = links
        self.tool = (re.compile(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(links, key=len, reverse=True)) + r')(?![\w-])')
                     if links else None)

    def __call__(self, h):
        out, in_a, in_td, seen = [], 0, 0, set()
        for tok in re.split(r'(<[^>]+>)', h):
            if tok.startswith('<'):
                low = tok.lower()
                if low.startswith('<a'):
                    in_a += 1
                elif low.startswith('</a'):
                    in_a = max(0, in_a - 1)
                elif low.startswith('<tr'):
                    seen = set()
                elif low.startswith('<td'):
                    in_td += 1
                elif low.startswith('</td'):
                    in_td = max(0, in_td - 1)
                out.append(tok)
                continue
            if in_a or not tok.strip():
                out.append(tok)
                continue
            slots = []

            def keep(piece):
                slots.append(piece)
                return '\x00%d\x00' % (len(slots) - 1)
            tok = self.DOMAIN.sub(lambda m: keep('<a href="https://%s">%s</a>' % (m.group(1), m.group(1))), tok)
            if in_td and self.tool:
                def tool(m):
                    name = m.group(1)
                    after = m.string[m.end():m.end() + 8].lower()
                    if name in seen or after.startswith(' server'):
                        return name
                    seen.add(name)
                    return keep('<a href="%s">%s</a>' % (self.links[name], name))
                tok = self.tool.sub(tool, tok)
            out.append(re.sub(r'\x00(\d+)\x00', lambda m: slots[int(m.group(1))], tok))
        return ''.join(out)


def summary(text, limit=160):
    """Meta description: the start of the first paragraphs, whole sentences while they fit."""
    paras = [p for p in re.split(r'\n\s*\n', text) if p.strip() and not p.lstrip().startswith('#')][:2]
    if len(paras) > 1 and re.match(r'\s*(\*\*|[-|*]|\d+\.)', paras[1]):
        paras = paras[:1]
    para = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', ' '.join(paras)).replace('**', '').replace('`', '')
    para = ' '.join(para.split())
    out = ''
    for sentence in re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-ÝĀ-Ž„“"])', para):
        if len(out) + 1 + len(sentence) <= limit:
            out = ('%s %s' % (out, sentence)).strip()
            if len(out) >= 120:
                break
            continue
        if len(out) < 110:
            room = limit - 2 - len(out)
            out = ('%s %s…' % (out, sentence[:room].rsplit(' ', 1)[0].rstrip(',;:'))).strip()
        break
    return out


# ---------- HTML trees ----------

_ENTITY = re.compile(r'&([A-Za-z][A-Za-z0-9]*);')


def parse(fragment, where):
    def numeric(m):
        name = m.group(1)
        if name in ('amp', 'lt', 'gt', 'quot', 'apos') or name not in name2codepoint:
            return m.group(0)
        return '&#%d;' % name2codepoint[name]
    try:
        return ET.fromstring('<div>' + _ENTITY.sub(numeric, fragment) + '</div>')
    except ET.ParseError as e:
        raise BuildError('%s: the HTML is not well-formed (%s). Check unclosed inline HTML in the Markdown.' % (where, e))


def inner(el, method='html'):
    return html.escape(el.text or '', quote=False) + ''.join(ET.tostring(c, encoding='unicode', method=method) for c in el)


def text_of(el, skip=None):
    parts = []

    def walk(e):
        if e.text:
            parts.append(e.text)
        for c in e:
            if not (skip and skip(c)):
                walk(c)
            if c.tail:
                parts.append(c.tail)
    walk(el)
    return ''.join(parts)


def classes(el):
    return (el.get('class') or '').split()


def add_class(el, c):
    if c not in classes(el):
        el.set('class', ' '.join(classes(el) + [c]))


def parent_map(root):
    return {c: p for p in root.iter() for c in p}


def replace(parents, old, new):
    p = parents[old]
    i = list(p).index(old)
    new.tail, old.tail = old.tail, None
    p.remove(old)
    p.insert(i, new)
    parents[new] = p


def is_todo(li):
    return re.match(r'\s*\[ \]', text_of(li)) is not None


# ---------- the book ----------

class Guide:
    def __init__(self, cfg, content, directory):
        self.cfg = cfg
        self.S = content.strings
        self.content = content
        self.E, self.B, self.L = cfg['edition'], cfg['book'], cfg['layout']
        self.BASE = cfg['site']['base_path']
        self.slugs = content.slugs
        self.link = Linker(content.links)
        self.row_header_columns = {str(x).casefold() for x in self.S.opt('row_header_columns', [])}
        self.directory = directory
        self.PARTS = []
        for p in content.manifest['parts']:
            self.PARTS.append({'number': p['number'], 'name': p.get('short_title') or p['title'], 'title': p['title']})
        self.chapters = content.chapters
        self.pages = content.pages
        self.by_id = {c['id']: c for c in self.chapters}
        self.page_by_id = {p['id']: p for p in self.pages}
        self.tool_links = 0
        self.built = {c['id']: self.build_doc(c, True) for c in self.chapters}
        self.built_pages = {p['id']: self.build_doc(p, False) for p in self.pages}
        self.total_actions = sum(len(b['actions']) for b in self.built.values())
        self.intro = self.page_of('introduction')
        self.glossary = self.page_of('glossary')
        self.part_pages = [p for p in (self.part_page(x['number']) for x in self.PARTS) if p]
        self.term_count = sum(1 for e in self.built_pages[self.glossary['id']]['index'] if e['type'] == 'term') if self.glossary else 0
        self.show_actions = bool(self.total_actions) and self.L['show_progress']
        self.sequence = ([self.nav_page(self.intro)] if self.intro else []) + [
            item for p in self.PARTS for item in
            ([self.nav_page(self.part_page(p['number']))] if self.part_page(p['number']) else [])
            + [self.nav_chapter(c) for c in self.part_chapters(p['number'])]
        ] + ([self.nav_actions()] if self.show_actions else []) + ([self.nav_page(self.glossary)] if self.glossary else [])
        self.language_name = cfg['language']['name']
        self.release = {'files': {}, 'fonts': [], 'archive': None}  # filled by legal_files() before rendering

    # addresses
    @staticmethod
    def at(path, section=None):
        return path + ('#' + quote(section, safe='-_.~') if section else '')

    def chapter_href(self, cid, section=None):
        return self.at(self.BASE + cid + '/', section)

    def page_href(self, pid, section=None):
        return self.at(self.BASE + self.page_by_id[pid]['slug'] + '/', section)

    def actions_href(self, section=None):
        return self.at(self.BASE + self.slugs['actions'] + '/', section)

    def start_href(self, section=None):
        return self.at(self.BASE + self.slugs['start'] + '/', section)

    def editions_href(self, section=None):
        return self.at(self.BASE + self.slugs['editions'] + '/', section)

    def home_href(self, section=None):
        return self.at(self.BASE, section)

    def legal_href(self, section=None):
        return self.at(self.BASE + self.slugs['legal'] + '/', section)

    # lookups
    def part_of(self, n):
        return next((p for p in self.PARTS if p['number'] == n), {'number': n, 'name': self.S('part_n', n=n)})

    def part_chapters(self, n):
        return [c for c in self.chapters if c['part'] == n]

    def page_of(self, kind, part=None):
        return next((p for p in self.pages if p['kind'] == kind and (part is None or p['part'] == part)), None)

    def part_page(self, n):
        return self.page_of('part', n)

    def actions_of(self, chapters):
        return sum(len(self.built[c['id']]['actions']) for c in chapters)

    def kind_label(self, kind):
        return '' if kind == 'brief' else self.S('kind_' + kind)

    # ----- page building -----
    def build_doc(self, doc, is_chapter):
        S = self.S
        where = doc['source']
        marked = re.sub(r'<a href=', '<a data-src="" href=', doc['html'])
        tpl = parse(self.link(marked), where)
        root = ET.Element('div')
        root.text = tpl.text
        sec, count = None, 0
        for node in list(tpl):
            if node.tag == 'h2':
                count += 1
                sec = ET.SubElement(root, 'section', {'class': 'sec', 'data-no': pad(count)})
            (sec if sec is not None else root).append(node)
        for a in root.iter('a'):
            if 'data-src' in a.attrib:
                del a.attrib['data-src']
            else:
                add_class(a, 'tool-link')
                self.tool_links += 1
            if re.match(r'https?://', a.get('href', ''), re.I):
                add_class(a, 'ext')
                a.set('rel', 'noopener noreferrer')

        href = (lambda s=None: self.chapter_href(doc['id'], s)) if is_chapter else (lambda s=None: self.page_href(doc['id'], s))
        label = S('chapter_short', n=doc['number']) if is_chapter else (
            S('part_opening', n=doc['part']) if doc['kind'] == 'part' else doc['title'])
        ctx = {'doc': doc, 'chapter': is_chapter, 'href': href, 'label': label, 'actions': [], 'index': [],
               'ids': {e.get('id') for e in root.iter() if e.get('id')}, 'steps': 0, 'checklist_id': None, 'where': where}

        for s in [e for e in root if e.tag == 'section']:
            h2 = s[0]
            hid = h2.get('id')
            kind = self.section_kind(s, hid, ctx)
            title = squash(text_of(h2))
            add_class(s, 'sec--' + kind)
            s.set('aria-labelledby', hid)
            h2.set('tabindex', '-1')
            kicker = ET.Element('p', {'class': 'sec-kicker'})
            ET.SubElement(kicker, 'span', {'class': 'sec-no'}).text = s.get('data-no')
            if self.kind_label(kind):
                ET.SubElement(kicker, 'span', {'class': 'sec-kind'}).text = self.kind_label(kind)
            s.insert(0, kicker)
            self.index_subsections(s, title, ctx)
            if kind == 'explain':
                self.add_cited(s)
            if kind == 'compare' or (not is_chapter and s.find('.//table') is not None):
                self.wrap_tables(s, title, ctx, kind == 'compare')
            if kind == 'steps':
                self.mark_steps(s, title, ctx)
            if kind == 'checklist':
                self.build_checklist(s, ctx)
                ctx['checklist_id'] = hid
            if kind == 'glossary':
                self.mark_terms(s, title, ctx)
            if kind in ('sources', 'further'):
                for ul in s.iter('ul'):
                    add_class(ul, 'refs')
            skip = lambda e: (e.tag in ('h2', 'noscript') or bool(set(classes(e)) & {
                'sec-kicker', 'compare-cap', 'sec-cited', 'cl-head', 'cl-hint', 'effort'}))
            ctx['index'].append({'type': 'section', 'part': doc['part'], 'title': title,
                                 'kicker': label + ' · ' + (self.kind_label(kind) or S('kind_brief')) if is_chapter else label,
                                 'text': squash(text_of(s, skip)), 'href': href(hid)})

        def toc_map(items):
            out = []
            for i, h in enumerate(items or []):
                el = root.find(".//*[@id='%s']" % h['id'])
                out.append({'id': h['id'], 'no': pad(i + 1) if h['level'] == 2 else '',
                            'label': squash(text_of(el)) if el is not None else h['name'],
                            'href': href(h['id']), 'children': toc_map(h['children'])})
            return out
        toc = toc_map(doc['headings'])
        first = {'type': 'chapter', 'part': doc['part'], 'title': doc['title'],
                 'kicker': S('chapter_n', n=doc['number']) + ' · ' + self.part_of(doc['part'])['name']} if is_chapter else {
            'type': 'page', 'part': doc['part'], 'title': doc['title'],
            'kicker': (S('part_n', n=doc['part']) + ' · ' + self.part_of(doc['part'])['name'] + ' · ' + S('opening_essay')
                       if doc['kind'] == 'part' else S('book'))}
        first.update(text=' · '.join(t['label'] for t in toc), href=href())
        ctx['index'].insert(0, first)
        return {'html': inner(root), 'actions': ctx['actions'], 'index': ctx['index'], 'toc': toc,
                'checklist_id': ctx['checklist_id'], 'ids': ctx['ids']}

    @staticmethod
    def section_kind(sec, hid, ctx):
        if not ctx['chapter']:
            if hid == 'sources':
                return 'sources'
            return 'glossary' if ctx['doc']['kind'] == 'glossary' else 'explain'
        if any(is_todo(li) for li in sec.iter('li')):
            return 'checklist'
        if hid in KIND_BY_ID:
            return KIND_BY_ID[hid]
        if sec.find('.//table') is not None:
            return 'compare'
        return 'explain'

    @staticmethod
    def claim(ctx, base):
        new, k = base, 2
        while new in ctx['ids']:
            new, k = '%s-%d' % (base, k), k + 1
        ctx['ids'].add(new)
        return new

    def index_subsections(self, sec, parent_title, ctx):
        parents = parent_map(sec)
        for h3 in [e for e in sec.iter('h3') if e.get('id')]:
            h3.set('tabindex', '-1')
            sibs = list(parents[h3])
            text = []
            for n in sibs[sibs.index(h3) + 1:]:
                if n.tag in ('h2', 'h3'):
                    break
                text.append(text_of(n))
            ctx['index'].append({'type': 'section', 'part': ctx['doc']['part'], 'title': squash(text_of(h3)),
                                 'kicker': ctx['label'] + ' · ' + parent_title, 'text': squash(' '.join(text)),
                                 'href': ctx['href'](h3.get('id'))})

    def add_cited(self, sec):
        urls = []
        for a in sec.iter('a'):
            if 'ext' in classes(a) and 'tool-link' not in classes(a) and a.get('href') not in urls:
                urls.append(a.get('href'))
        if not urls:
            return
        box = ET.SubElement(sec, 'div', {'class': 'sec-cited'})
        ET.SubElement(box, 'p', {'class': 'sec-cited-label'}).text = self.S('cited_in_section')
        ul = ET.SubElement(box, 'ul')
        seen = {}
        for url in urls:
            host = host_of(url)
            seen[host] = seen.get(host, 0) + 1
            a = ET.SubElement(ET.SubElement(ul, 'li'), 'a', {'class': 'ext', 'rel': 'noopener noreferrer', 'href': url})
            a.text = host + (' (%d)' % seen[host] if seen[host] > 1 else '')

    def wrap_tables(self, sec, title, ctx, index_rows):
        S = self.S
        tables = list(sec.iter('table'))
        parents = parent_map(sec)
        for i, table in enumerate(tables):
            tbody, thead = table.find('tbody'), table.find('thead')
            rows = tbody.findall('tr') if tbody is not None else []
            head_row = thead.find('tr') if thead is not None else None
            heads = [squash(text_of(c)) for c in head_row] if head_row is not None else []
            for th in (thead.iter('th') if thead is not None else []):
                th.set('scope', 'col')
            # Tables whose first column names the compared things (strings.json, row_header_columns): its cells
            # become row headers, so a screen reader announces "Signal" with every cell of that row.
            if heads and heads[0].casefold() in self.row_header_columns:
                for tr in rows:
                    cell = next(iter(tr), None)
                    if cell is not None and squash(text_of(cell)):
                        cell.tag = 'th'
                        cell.set('scope', 'row')
            fig = ET.Element('figure', {'class': 'compare'})
            cap = ET.SubElement(fig, 'figcaption', {'class': 'compare-cap'})
            ET.SubElement(cap, 'span').text = (S.n('options', len(rows)) if index_rows else S.n('rows', len(rows))) + ' · ' + S.n('columns', len(heads))
            ET.SubElement(cap, 'span', {'class': 'compare-hint', 'aria-hidden': 'true'}).text = S('scroll_sideways')
            label = (S('comparison_table', title=title) if index_rows else S('table', title=title)) + (
                S('table_n_of', i=i + 1, n=len(tables)) if len(tables) > 1 else '')
            scroller = ET.SubElement(fig, 'div', {'class': 'table-scroll', 'role': 'region', 'tabindex': '0', 'aria-label': label})
            replace(parents, table, fig)
            scroller.append(table)
            if not index_rows:
                continue
            for tr in rows:
                cells = list(tr)
                name = squash(text_of(cells[0]))
                tr.set('id', self.claim(ctx, 'row-' + (slugify(name) or 'item')))
                ctx['index'].append({
                    'type': 'tool', 'part': ctx['doc']['part'], 'title': name,
                    'kicker': ctx['label'] + ' · ' + S('kind_compare') + ' · ' + title,
                    'text': ' · '.join((heads[j + 1] + ': ' if j + 1 < len(heads) and heads[j + 1] else '')
                                       + squash(text_of(c)) for j, c in enumerate(cells[1:])),
                    'href': ctx['href'](tr.get('id'))})

    def mark_steps(self, sec, title, ctx):
        for ol in list(sec.iter('ol')):
            ctx['steps'] += 1
            prefix = 'step-' if ctx['steps'] == 1 else 'step-%d-' % ctx['steps']
            add_class(ol, 'steps')
            for i, li in enumerate([c for c in ol if c.tag == 'li']):
                li.set('id', self.claim(ctx, prefix + str(i + 1)))
                lead = next(li.iter('strong'), None)
                name = re.sub(r'[.:]$', '', squash(text_of(lead) if lead is not None else text_of(li)[:64]))
                ctx['index'].append({'type': 'step', 'part': ctx['doc']['part'], 'title': self.S('step_n', n=i + 1, name=name),
                                     'kicker': ctx['label'] + ' · ' + title, 'text': squash(text_of(li)),
                                     'href': ctx['href'](li.get('id'))})

    def mark_terms(self, sec, group, ctx):
        for p in list(sec.iter('p')):
            if p.text or not len(p) or p[0].tag != 'strong':
                continue
            lead = text_of(p[0])
            term = re.sub(r'[.:]$', '', squash(lead))
            p.set('id', self.claim(ctx, 'term-' + (slugify(term) or 'item')))
            add_class(p, 'term')
            ctx['index'].append({'type': 'term', 'part': None, 'title': term, 'kicker': ctx['label'] + ' · ' + group,
                                 'text': squash(text_of(p)[len(lead):]), 'href': ctx['href'](p.get('id'))})

    def build_checklist(self, sec, ctx):
        S = self.S
        items = [li for li in sec.iter('li') if is_todo(li)]
        if not items:
            return
        ch = ctx['doc']
        known = ch['actions']
        if len(known) != len(items):
            raise BuildError('%s: %d checklist items rendered, %d actions found in the source.' % (ctx['where'], len(items), len(known)))
        parents = parent_map(sec)
        list_el = parents[items[0]]
        for i, li in enumerate(items):
            h = re.sub(r'^\s*\[ \]\s*', '', inner(li, 'xml'))
            effort = ''
            m = re.search(r'\s*\(([^()<>]+)\)\s*$', h)
            if m:
                effort, h = m.group(1).strip(), h[:m.start()]
            text = squash(html.unescape(re.sub(r'<[^>]+>', '', h)))
            aid = known[i]['id']
            ctx['actions'].append({'id': aid, 'text': text, 'effort': effort, 'html': h})
            ctx['index'].append({'type': 'action', 'part': ch['part'], 'title': text,
                                 'kicker': ctx['label'] + ' · ' + S('checklist_action') + (', ' + effort if effort else ''),
                                 'text': '', 'href': self.chapter_href(ch['id'], 'action-' + aid)})
        if not self.L['show_progress']:
            # Plain list, no tick boxes: the actions stay readable.
            add_class(list_el, 'actions-plain')
            for li in items:
                li_html = re.sub(r'^\s*\[ \]\s*', '', inner(li, 'xml'))
                new = parse('<li>' + li_html + '</li>', ctx['where'])[0]
                replace(parents, li, new)
            return
        wrap = parse('<div class="checklist">' + self.checklist_head(ch['id'], len(items))
                     + '<ul class="actions">' + ''.join(self.action_item(a) for a in ctx['actions']) + '</ul>'
                     + '<p class="cl-hint">' + esc(S('one_action_at_a_time')) + ' ' + esc(S('storage_sentence'))
                     + ' <a href="' + esc(self.actions_href()) + '">' + esc(S('see_all_actions')) + '</a>.</p>'
                     + '<noscript><p class="cl-hint">' + esc(S('missing_js_ticks')) + '</p></noscript></div>', ctx['where'])[0]
        replace(parents, list_el, wrap)
        for a in ctx['actions']:
            a['html'] = inner(parse(a['html'], ctx['where']))

    def checklist_head(self, cid, total):
        done = '<strong data-stat="ch-done" data-ch="%s">0</strong>' % cid
        return ('<div class="cl-head"><p class="cl-count">%s</p><span class="bar" data-bar="ch" data-ch="%s" aria-hidden="true"><i></i></span></div>'
                % (self.S('actions_done_of', done=done, total=total), cid))

    def action_item(self, a):
        return ('<li class="action" id="action-%s"><label class="action-row">'
                '<input type="checkbox" class="action-cb" data-action="%s" disabled="disabled" />'
                '<span class="action-text">%s</span>%s</label></li>'
                % (esc(a['id']), esc(a['id']), a['html'],
                   '<span class="effort"><span class="sr-only">%s</span>%s</span>' % (esc(self.S('effort_sr')), esc(a['effort'])) if a['effort'] else ''))

    # ----- sequence -----
    def nav_chapter(self, c):
        return {'key': 'chapter/' + c['id'], 'href': self.chapter_href(c['id']), 'dir': self.S('chapter_n', n=c['number']),
                'title': c['title'], 'part': c['part']}

    def nav_page(self, p):
        return {'key': 'page/' + p['id'], 'href': self.page_href(p['id']), 'title': p['title'], 'part': p['part'],
                'dir': self.S('part_opening', n=p['part']) if p['kind'] == 'part'
                else self.S('reference') if p['kind'] == 'glossary' else self.S('before_chapters')}

    def nav_actions(self):
        return {'key': 'actions/', 'href': self.actions_href(), 'dir': self.S('global_checklist'), 'title': self.S('all_actions'), 'part': None}

    def nav_cover(self):
        return {'key': 'home/', 'href': self.home_href(), 'dir': self.S('cover'), 'title': self.S('back_to_cover'), 'part': None}

    def neighbours(self, key):
        i = next(k for k, s in enumerate(self.sequence) if s['key'] == key)
        return (self.sequence[i - 1] if i > 0 else self.nav_cover(),
                self.sequence[i + 1] if i + 1 < len(self.sequence) else self.nav_cover())

    # ----- shared fragments -----
    def progress_sub(self, ch):
        if not self.L['show_progress']:
            return self.S.n('actions', len(self.built[ch['id']]['actions']))
        done = '<span data-stat="ch-done" data-ch="%s">0</span>' % ch['id']
        return self.S('actions_done_of', done=done, total=len(self.built[ch['id']]['actions'])) + '<span data-read-label="%s"></span>' % ch['id']

    def chapter_item(self, ch, current=None):
        return ('<li class="ch-item part-%d" data-ch-item="%s"><a class="ch-row" href="%s"%s><span class="ch-n">%s</span>'
                '<span class="ch-t">%s</span><span class="ch-s">%s</span></a></li>'
                % (ch['part'], ch['id'], self.chapter_href(ch['id']), ' aria-current="page"' if ch['id'] == current else '',
                   pad(ch['number']), esc(ch['title']), self.progress_sub(ch)))

    def extra_item(self, key, current=None):
        S = self.S
        part = None
        if key == 'actions':
            no, title, href = '✓', S('all_actions'), self.actions_href()
            sub = S('actions_done_of', done='<span data-stat="actions-done">0</span>', total=self.total_actions)
        else:
            p = self.page_by_id[key]
            href, title = self.page_href(p['id']), p['title']
            if p['kind'] == 'part':
                no, part, sub = '··', p['part'], S('opening_essay_of', n=p['part'])
            elif p['kind'] == 'glossary':
                no, sub = 'Az', S.n('terms', self.term_count)
            else:
                no, sub = '00', S('before_chapters')
        return ('<li class="ch-item%s"><a class="ch-row" href="%s"%s><span class="ch-n">%s</span><span class="ch-t">%s</span>'
                '<span class="ch-s">%s</span></a></li>'
                % (' part-%d' % part if part else '', href, ' aria-current="page"' if key == current else '', no, esc(title), sub))

    def before_keys(self):
        return [self.intro['id']] if self.intro else []

    def after_keys(self):
        return (['actions'] if self.show_actions else []) + ([self.glossary['id']] if self.glossary else [])

    def extra_list(self, keys, current=None, cls=''):
        return ('<ol class="ch-list%s">%s</ol>' % (' ' + cls if cls else '', ''.join(self.extra_item(k, current) for k in keys)) if keys else '')

    def part_list(self, n, current=None):
        pp = self.part_page(n)
        return ('<ol class="ch-list">' + (self.extra_item(pp['id'], current) if pp else '')
                + ''.join(self.chapter_item(c, current) for c in self.part_chapters(n)) + '</ol>')

    def toc_block(self, items):
        if not items or not self.L['page_toc']:
            return ''
        return ('<div class="toc-aside"><button type="button" class="toc-toggle" aria-expanded="false" aria-controls="page-toc">'
                '<span class="toc-toggle-label">%s</span><span class="toc-current" aria-hidden="true"></span>'
                '<span class="toc-chevron" aria-hidden="true"></span></button>'
                '<nav class="page-toc" id="page-toc" aria-labelledby="page-toc-title">'
                '<p class="toc-title" id="page-toc-title">%s</p>%s</nav></div>' % (esc(self.S('on_this_page')), esc(self.S('on_this_page')), self.toc_list(items, 0)))

    def toc_list(self, items, depth):
        return ('<ol class="toc-list%s">' % (' toc-sub' if depth else '') + ''.join(
            '<li><a href="%s" data-target="%s">%s<span class="toc-label">%s</span></a>%s</li>'
            % (it['href'], esc(it['id']), '<span class="toc-no">%s</span>' % it['no'] if it.get('no') else '', esc(it['label']),
               self.toc_list(it['children'], depth + 1) if it.get('children') else '') for it in items) + '</ol>')

    def layout(self, items, main, extra=''):
        has_toc = bool(items) and self.L['page_toc']
        return ('<div class="page-layout%s%s">' % ('' if has_toc else ' no-toc', ' ' + extra if extra else '')
                + self.toc_block(items) + '<div class="page-main">' + main + '</div></div>')

    @staticmethod
    def stat(value, total, label, bar=None):
        return ('<div class="stat"><p class="stat-n">%s<small> / %d</small></p><p class="stat-l">%s</p>%s</div>'
                % (value, total, esc(label), '<span class="bar" data-bar="%s" aria-hidden="true"><i></i></span>' % bar if bar else ''))

    def pager(self, prev, nxt, label):
        def link(it, d, cls):
            return ('<a class="%s%s" href="%s"><span class="pager-dir">%s · %s</span><span class="pager-title">%s</span></a>'
                    % (cls, ' part-%d' % it['part'] if it.get('part') else '', it['href'], esc(d), esc(it['dir']), esc(it['title'])))
        return '<nav class="pager" aria-label="%s">%s%s</nav>' % (esc(label), link(prev, self.S('previous'), 'pager-prev'), link(nxt, self.S('next'), 'pager-next'))

    def extras_sentence(self):
        S = self.S
        parts = []
        if self.intro:
            parts.append(S('the_introduction'))
        if self.part_pages:
            parts.append(S.n('part_openings', len(self.part_pages)))
        if self.glossary:
            parts.append(S('the_glossary'))
        return S.join(parts)

    def range_label(self, chapters):
        nums = [c['number'] for c in chapters]
        if not nums:
            return ''
        if len(nums) == 1:
            return self.S('chapter_range_one', a=nums[0])
        if all(i == 0 or n == nums[i - 1] + 1 for i, n in enumerate(nums)):
            return self.S('chapter_range', a=nums[0], b=nums[-1])
        return self.S('chapter_range_list', list=', '.join(map(str, nums)))

    def logo_html(self, cls):
        logo = self.cfg.get('_logo')
        if not logo:
            return ''
        url = logo.get('cover') if cls == 'cover-logo' and logo.get('cover') else logo['url']
        return '<img class="%s" src="%s" alt="%s">' % (cls, esc(url), esc(self.E['logo'].get('alt') or self.E['community']))

    def licence_links(self):
        L = self.cfg['licence']
        lic = lambda x: '<a class="ext" rel="noopener noreferrer" href="%s">%s</a>' % (esc(x['url']), esc(x['label']))
        return self.S('licence_line', content=lic(L['content']), code=lic(L['code']))

    def original_credit(self):
        O = self.S.opt
        title = '<a class="ext" rel="noopener noreferrer" href="%s">%s</a>' % (esc(ORIGINAL['url']), esc(ORIGINAL['title']))
        return O('original_credit', 'Based on {title}, originally written for {project}, an initiative of {initiative}. '
                 'Adapted and published by {community}.', title=title, project=esc(ORIGINAL['project']),
                 initiative=esc(ORIGINAL['initiative']), community=esc(self.E['community']))

    def legal_link(self):
        return '<a href="%s">%s</a>' % (self.legal_href(), esc(self.S.opt('legal_link', 'Licences, credits and source')))

    def community_link(self):
        if self.E['community_url']:
            return '<a class="ext" rel="noopener noreferrer" href="%s">%s</a>' % (esc(self.E['community_url']), esc(self.E['community']))
        return esc(self.E['community'])

    def contact_link(self):
        c = self.E['contact']
        if not c:
            return ''
        if '@' in c and not c.startswith(('http://', 'https://')):
            return '<a href="mailto:%s">%s</a>' % (esc(c), esc(c))
        if c.startswith(('http://', 'https://')):
            return '<a class="ext" rel="noopener noreferrer" href="%s">%s</a>' % (esc(c), esc(host_of(c) if host_of(c) != c else c))
        return esc(c)

    def start_chapter(self):
        """Chapter opened by "Start reading": book.start_chapter when it names a chapter. Otherwise None when there is
        an introduction (the button opens it), else the first chapter."""
        sc = self.B['start_chapter']
        if sc and sc not in self.by_id:
            raise BuildError('book.start_chapter: unknown chapter id "%s". Leave it empty to open the introduction, or use 1 of: %s.'
                             % (sc, ', '.join(self.by_id)))
        return self.by_id.get(sc) or (None if self.intro else self.chapters[0])

    def in_this_guide(self):
        return self.S.opt('in_this_guide', 'In this guide')

    def coverage_facts(self):
        """What the book contains, for "In this guide": counts of content, never of the reader's ticks."""
        S, O = self.S, self.S.opt
        extras = self.extras_sentence()
        values = {'chapters': S.n('chapters', len(self.chapters)),
                  'extras': S('coverage_extras', extras=extras) if extras else ''}
        n = self.total_actions
        if not n:
            return O('coverage_facts_no_actions', '{chapters}{extras}.', **values)
        actions = O('checklist_actions_one', '{n} checklist action', n=n) if n == 1 else \
            O('checklist_actions_many', '{n} checklist actions', n=n)
        return O('coverage_facts', '{chapters} with {actions}{extras}.', actions=actions, **values)

    # ----- views -----
    def recordings_title(self):
        return self.cfg['recordings']['title'] or self.S.opt('recordings_title', 'Talk recordings')

    def recordings_block(self):
        """Cover section of talk recordings (edition.json, recordings). Plain links without JavaScript; with it, the
        player is created only when the reader clicks, so nothing is requested from another site before."""
        S, O, R = self.S, self.S.opt, self.cfg['recordings']
        items = []
        for i, it in enumerate(R['items']):
            chapters = it.get('chapters', [])
            missing = [c for c in chapters if c not in self.by_id and c not in self.page_by_id]
            if missing:
                raise BuildError('recordings.items[%d]: unknown chapter id %s. Valid ids: %s.'
                                 % (i, ', '.join(missing), ', '.join(list(self.by_id) + list(self.page_by_id))))
            part = it.get('part') or next((self.by_id[c]['part'] for c in chapters if c in self.by_id), 0)
            video, sd = it.get('video', ''), it.get('video_sd', '')
            title_id = 'rec-%d-title' % (i + 1)
            text = []
            if it.get('kicker'):
                text.append('<p class="rp-kicker">%s</p>' % esc(it['kicker']))
            text.append('<p class="rp-title" id="%s">%s</p>' % (title_id, esc(it['title'])))
            who = ' · '.join(x for x in (it.get('speaker', ''), it.get('note', '')) if x)
            if who:
                text.append('<p class="rp-spk">%s</p>' % esc(who))
            if it.get('links'):
                text.append('<p class="rp-alt">%s %s</p>' % (esc(O('recordings_also_on', 'Also on:')), ' · '.join(
                    '<a class="ext" rel="noopener noreferrer" href="%s">%s</a>' % (esc(l['href']), esc(l['label'])) for l in it['links'])))
            if chapters:
                links = []
                for c in chapters:
                    if c in self.by_id:
                        ch = self.by_id[c]
                        links.append('<a href="%s">%s</a>' % (self.chapter_href(c), esc(S('chapter_n', n=ch['number']) + ' · ' + ch['title'])))
                    else:
                        links.append('<a href="%s">%s</a>' % (self.page_href(c), esc(self.page_by_id[c]['title'])))
                text.append('<p class="rp-alt">%s %s</p>' % (esc(O('recordings_in_the_book', 'In the book:')), ' · '.join(links)))
            attrs, side = '', ''
            if video:
                text.append('<a class="rp-play" href="%s" aria-describedby="%s">%s</a>'
                            % (esc(sd or video), title_id, esc(O('recordings_watch', 'Watch the recording'))))
                attrs = ' data-video="%s"' % esc(video)
                for key, attr in (('video_type', 'data-video-type'), ('video_sd', 'data-video-sd'), ('video_sd_type', 'data-video-sd-type')):
                    if it.get(key):
                        attrs += ' %s="%s"' % (attr, esc(it[key]))
                poster = self.cfg.get('_posters', {}).get(it.get('poster', ''))
                if poster:
                    side = ('<a class="rp-thumb" href="%s" tabindex="-1" aria-hidden="true"><img src="%s" alt="" width="1280" '
                            'height="720" loading="lazy" decoding="async"></a>' % (esc(sd or video), esc(poster)))
            elif it.get('badge'):
                side = '<span class="rp-badge">%s</span>' % esc(it['badge'])
            items.append('<li class="rp-item%s%s%s"%s><div class="rp-text">%s</div>%s</li>'
                         % (' part-%d' % part if part else '', ' rp-closing' if it.get('kicker') else '',
                            ' rp-has-video' if video and side else '', attrs, ''.join(text), side))
        note = O('recordings_note', 'The recordings are hosted by other sites and need a connection. Nothing is loaded from '
                 'those sites until you play a recording; that site then receives your request like any visit. '
                 'The recordings keep the rights of their authors and are not covered by the licences of this book.')
        return ('<section class="block" aria-labelledby="recordings"><p class="block-kicker">%s</p>'
                '<h2 id="recordings" tabindex="-1">%s</h2><div class="block-text">%s<p class="rp-note">%s</p></div>'
                '<div class="guide-recordings"><ul class="rp-list">%s</ul></div></section>'
                % (esc(R['kicker'] or O('recordings_kicker', 'Talks')), esc(self.recordings_title()),
                   '<p>%s</p>' % esc(R['intro']) if R['intro'] else '', esc(note), ''.join(items)))

    def view_home(self):
        S, B, E = self.S, self.B, self.E
        start = self.start_chapter()
        first = self.chapters[0]
        # "Open a checklist" always opens a chapter checklist: the start chapter, or the first chapter.
        checklist_ch = start or first
        title_lines = B['title_lines'] or [B['title']]
        lines = ' '.join('<span class="cover-line%s">%s</span>' % (' is-outlined' if i == B['outlined_line'] else '', esc(l))
                         for i, l in enumerate(title_lines))
        # Every part gets the same small colour marker (theme/styles.css): nothing on the cover is sized by a count.
        cover_parts = ''.join(
            '<li class="part-%d"><span class="cp-no">%s</span><span class="cp-name">%s</span><span class="cp-range">%s</span></li>'
            % (p['number'], esc(S('part_n', n=p['number'])), esc(p['name']), esc(self.range_label(self.part_chapters(p['number']))))
            for p in self.PARTS)
        if start:
            href, sub = self.chapter_href(start['id']), esc(S('chapter_n', n=start['number'])) + ' · ' + esc(start['title'])
        else:
            href, sub = self.page_href(self.intro['id']), esc(self.intro['title'])
        actions = ('<a class="btn btn--dark" href="%s"><span class="btn-main">%s <span aria-hidden="true">→</span></span>'
                   '<span class="btn-sub">%s</span></a>' % (href, esc(S('start_reading')), sub))
        alt = []
        if self.intro and start:
            alt.append('<a href="%s">%s</a>' % (self.page_href(self.intro['id']), esc(S('read_the_introduction'))))
        if not start or first['id'] != start['id']:
            alt.append('<a href="%s">%s</a>' % (self.chapter_href(first['id']), esc(S('or_begin_with', n=first['number']))))
        alt.append('<a href="%s">%s</a>' % (self.home_href('contents'), esc(S('see_all_chapters', n=len(self.chapters)))))
        mark = self.logo_html('cover-logo') or ('<p class="wordmark"><span class="wm-big">%s</span></p>' % esc(E['wordmark'] or E['community']))
        edition_line = ' · '.join(x for x in (esc(E['label']), esc(E['name'])) if x)
        cover = ('<section class="cover" aria-labelledby="page-title"><div class="cover-main">'
                 '<p class="cover-kicker">%s</p><h1 class="cover-title" id="page-title" tabindex="-1">%s</h1>'
                 '<ol class="cover-parts" aria-label="%s">%s</ol></div>'
                 '<div class="cover-side"><div class="edition">%s'
                 '<p class="edition-line">%s</p><p class="edition-by">%s</p></div>'
                 '<div class="cover-intro">%s</div>'
                 '<div class="cover-actions">%s<a class="btn btn--line" href="%s">%s</a></div>'
                 '<p class="cover-alt">%s</p><p class="cover-alt cover-resume" data-resume hidden></p></div></section>'
                 % (esc(B['kicker']), lines, esc(S('parts_label', n=len(self.PARTS))), cover_parts, mark, edition_line,
                    S('an_edition_of', community=self.community_link()),
                    ''.join('<p>%s</p>' % esc(p) for p in B['intro']), actions, self.start_href(), esc(S('where_to_start')),
                    '<span aria-hidden="true"> · </span>'.join(alt)))

        parts = ''.join('<section class="part-col part-%d" aria-labelledby="part-%d"><h3 id="part-%d" tabindex="-1">'
                        '<span class="part-no">%s</span><span class="part-name">%s</span></h3>%s</section>'
                        % (p['number'], p['number'], p['number'], esc(S('part_n', n=p['number'])), esc(p['name']), self.part_list(p['number']))
                        for p in self.PARTS)
        extras = self.extras_sentence()
        n_ch, n_act = len(self.chapters), self.total_actions
        lead = S('contents_lead', chapters=S.n('chapters', n_ch), parts=len(self.PARTS),
                 extras=S('contents_lead_extras', extras=extras) if extras else '',
                 actions=S('contents_lead_actions', n=n_act) if self.show_actions else '')
        main = ('<section class="block" aria-labelledby="contents"><p class="block-kicker">%s</p>'
                '<h2 id="contents" tabindex="-1">%s</h2><p class="block-lead">%s</p>%s<div class="parts-grid">%s</div>%s</section>'
                % (esc(S('general_contents')), esc(S('contents')), esc(lead),
                   self.extra_list(self.before_keys(), None, 'contents-extra'), parts, self.extra_list(self.after_keys(), None, 'contents-extra')))
        toc = [{'id': 'contents', 'label': S('contents'), 'href': self.home_href('contents'),
                'children': [{'id': 'part-%d' % p['number'], 'label': S('part_n', n=p['number']) + ' · ' + p['name'],
                              'href': self.home_href('part-%d' % p['number'])} for p in self.PARTS]}]
        # #preview keeps its anchor. Plain facts about the content: no score, fraction or bar, which would read as the
        # reader's progress (that is the next section).
        main += ('<section class="block" aria-labelledby="preview"><p class="block-kicker">%s</p>'
                 '<h2 id="preview" tabindex="-1">%s</h2><div class="block-text"><p>%s</p><p>%s%s</p></div></section>'
                 % (esc(S.opt('coverage_kicker', 'Overview')), esc(self.in_this_guide()), esc(self.coverage_facts()),
                    esc(S('coverage_language', language=self.language_name)),
                    ' ' + esc(S('coverage_other_editions')) if self.cfg['other_editions'] else ''))
        toc.append({'id': 'preview', 'label': self.in_this_guide(), 'href': self.home_href('preview')})
        if self.cfg.get('_recordings'):
            main += self.recordings_block()
            toc.append({'id': 'recordings', 'label': self.recordings_title(), 'href': self.home_href('recordings')})
        if self.show_actions:
            main += ('<section class="block" aria-labelledby="progress"><p class="block-kicker">%s</p>'
                     '<h2 id="progress" tabindex="-1">%s</h2><div class="stats">%s%s</div>'
                     '<div class="block-text"><p>%s</p><p><a class="btn" href="%s">%s</a></p><p><a href="%s">%s</a></p><p>%s %s</p>'
                     '<p><button type="button" class="btn-quiet" data-reset data-js-only hidden>%s</button></p>'
                     '<p class="sr-only" id="progress-status" aria-live="polite"></p></div></section>'
                     % (esc(S('in_this_browser')), esc(S('your_progress')),
                        self.stat('<span data-stat="actions-done">0</span>', n_act, S('actions_done'), 'actions'),
                        self.stat('<span data-stat="chapters-read">0</span>', n_ch, S('chapters_read'), 'read'),
                        esc(S('progress_help')), self.chapter_href(checklist_ch['id'], self.built[checklist_ch['id']]['checklist_id']), esc(S('open_a_checklist')),
                        self.actions_href(), esc(S('see_all_n_actions', n=n_act)), esc(S('storage_sentence')), esc(S('ticks_removable')),
                        esc(S('clear_progress'))))
            toc.append({'id': 'progress', 'label': S('your_progress'), 'href': self.home_href('progress')})
        about = ['<p>%s</p>' % S('about_text', edition=esc(E['name']), title=esc(B['title']), community=self.community_link())]
        if E['contact']:
            about.append('<p>%s</p>' % S('about_contact', community=esc(E['community']), contact=self.contact_link()))
        about.append('<p>%s</p>' % esc(S('about_no_ads')))
        if E['repository']:
            about.append('<p>%s</p>' % S('about_source', repository='<a class="ext" rel="noopener noreferrer" href="%s">%s</a>' % (esc(E['repository']), esc(E['repository']))))
        about.append('<p>%s %s</p>' % (self.licence_links(), esc(S('licence_note'))))
        # The credit to the original work lives on the page "Licences, credits and source", linked here and in every footer.
        about.append('<p>%s</p>' % self.S.opt('about_credits', 'Original work, credits, licences and source: {link}.', link=self.legal_link()))
        if self.cfg['site']['offline']:
            about.append('<p class="offline-state" data-offline hidden></p>')
        main += ('<section class="block" aria-labelledby="edition"><p class="block-kicker">%s</p>'
                 '<h2 id="edition" tabindex="-1">%s</h2><div class="block-text">%s</div></section>'
                 % (esc(S('colophon')), esc(S('about_this_edition')), ''.join(about)))
        toc.append({'id': 'edition', 'label': S('about_this_edition'), 'href': self.home_href('edition')})
        return cover + self.layout(toc, main, 'is-home')

    def view_start(self):
        S = self.S
        paths = self.B['start_paths']
        out = []
        for i, p in enumerate(paths):
            main = [self.by_id[c] for c in p.get('chapters', []) if c in self.by_id]
            deeper = [self.by_id[c] for c in p.get('deeper', []) if c in self.by_id]
            missing = [c for c in p.get('chapters', []) + p.get('deeper', []) if c not in self.by_id]
            if missing:
                raise BuildError('book.start_paths "%s": unknown chapter id %s. Valid ids: %s.' % (p.get('id'), ', '.join(missing), ', '.join(self.by_id)))
            if not main:
                raise BuildError('edition.json, start_paths "%s": at least 1 chapter is needed.' % p.get('id'))
            part = main[0]['part']
            pid = p.get('id') or 'path-' + str(i + 1)
            out.append(
                '<section class="path part-%d" aria-labelledby="%s"><p class="path-no">%s</p>'
                '<h2 id="%s" tabindex="-1">%s</h2><p class="path-desc">%s</p><ol class="ch-list">%s</ol>%s'
                '<p class="path-avail">%s · %s</p></section>'
                % (part, esc(pid), esc(S('path_n', n=pad(i + 1))), esc(pid), esc(p['title']), esc(p.get('text', '')),
                   ''.join(self.chapter_item(c) for c in main),
                   '<h3 class="path-sub">%s</h3><ol class="ch-list">%s</ol>' % (esc(p.get('deeper_title') or S('to_go_deeper')),
                                                                                ''.join(self.chapter_item(c) for c in deeper)) if deeper else '',
                   S.n('chapters', len(main + deeper)), S.n('actions', self.actions_of(main + deeper))))
        guides = []
        if self.intro:
            guides.append(S('guide_intro', href=self.page_href(self.intro['id'])))
        if self.part_pages:
            guides.append(S('guide_parts', links=', '.join('<a href="%s">%s</a>' % (self.page_href(p['id']), esc(p['title'])) for p in self.part_pages)))
        if self.glossary:
            guides.append(S('guide_glossary', href=self.page_href(self.glossary['id'])))
        if self.show_actions:
            guides.append(S('guide_actions', n=self.total_actions, href=self.actions_href()))
        anatomy = ''.join('<li><span class="an-no">%s</span><span class="an-t">%s</span><span class="an-d">%s</span></li>'
                          % (pad(i + 1), esc(a['title']), esc(a['text'])) for i, a in enumerate(S('anatomy')))
        main = ('<header class="page-head"><p class="block-kicker">%s</p>'
                '<h1 id="page-title" class="page-title" tabindex="-1">%s</h1>'
                '<div class="start-lead"><p>%s</p><p>%s</p></div></header>'
                '<div class="paths">%s</div>'
                '<section class="block" aria-labelledby="how-chapters-work"><p class="block-kicker">%s</p>'
                '<h2 id="how-chapters-work" tabindex="-1">%s</h2><ol class="anatomy">%s</ol><div class="block-text"><p>%s %s</p>%s</div></section>'
                % (esc(S('orientation')), esc(S('where_to_start')), esc(S('start_lead_1')), esc(S('start_lead_2')), ''.join(out),
                   esc(S('method')), esc(S('how_chapters_work')), anatomy, esc(S('checklist_explained')),
                   esc(S('storage_sentence')) if self.show_actions else '', '<p>%s</p>' % ' '.join(guides) if guides else ''))
        toc = [{'id': p.get('id') or 'path-' + str(i + 1), 'no': pad(i + 1), 'label': p['title'],
                'href': self.start_href(p.get('id') or 'path-' + str(i + 1))} for i, p in enumerate(paths)]
        toc.append({'id': 'how-chapters-work', 'label': S('how_chapters_work'), 'href': self.start_href('how-chapters-work')})
        return self.layout(toc, main, 'is-start')

    def view_chapter(self, ch):
        S = self.S
        b = self.built[ch['id']]
        part = self.part_of(ch['part'])
        i = self.chapters.index(ch)
        seq_prev, seq_next = self.neighbours('chapter/' + ch['id'])
        prev_ch = self.chapters[i - 1] if i > 0 else None
        next_ch = self.chapters[i + 1] if i + 1 < len(self.chapters) else None
        prev = self.nav_chapter(prev_ch) if prev_ch else seq_prev
        nxt = self.nav_chapter(next_ch) if next_ch else seq_next
        opening = self.part_page(ch['part'])
        next_opening = self.part_page(next_ch['part']) if next_ch and next_ch['part'] != ch['part'] else None
        part_label = esc(S('part_n', n=part['number'])) + ' · ' + esc(part['name'])
        meta = '<span>%s</span>' % esc(S('chapter_of', n=ch['number'], total=len(self.chapters)))
        if b['checklist_id'] and self.L['show_progress']:
            done = '<span data-stat="ch-done" data-ch="%s">0</span>' % ch['id']
            meta += '<a href="%s">%s</a>' % (self.chapter_href(ch['id'], b['checklist_id']), S('actions_done_of', done=done, total=len(b['actions'])))
        meta += '<span class="ch-readstate" data-read-state="%s"></span>' % ch['id']
        read_row = ('<label class="read-row"><input type="checkbox" class="read-cb" data-read="%s" disabled><span>%s</span></label>'
                    % (ch['id'], esc(S('i_have_read')))) if self.L['show_progress'] else ''
        main = ('<article class="chapter part-%d" aria-labelledby="page-title"><header class="chapter-head">'
                '<p class="ch-kicker">%s</p>'
                '<h1 class="ch-title" id="page-title" tabindex="-1"><span class="sr-only">%s</span>%s</h1>'
                '<p class="ch-bignum" aria-hidden="true">%s</p><div class="ch-meta">%s</div></header>'
                '<div class="prose">%s</div><footer class="chapter-end">%s%s%s</footer></article>'
                % (ch['part'], '<a href="%s">%s</a>' % (self.page_href(opening['id']), part_label) if opening else part_label,
                   esc(S('chapter_prefix', n=ch['number'])), esc(ch['title']), pad(ch['number']), meta, b['html'], read_row,
                   self.pager(prev, nxt, S('chapters_nav')),
                   '<p class="pager-note">%s</p>' % S('next_part_essay', n=next_opening['part'], href=self.page_href(next_opening['id']),
                                                      title=esc(next_opening['title'])) if next_opening else ''))
        return self.layout(b['toc'], main, 'is-chapter part-%d' % ch['part'])

    def view_page(self, p):
        S = self.S
        b = self.built_pages[p['id']]
        is_part = p['kind'] == 'part'
        chapters = self.part_chapters(p['part']) if is_part else []
        prev, nxt = self.neighbours('page/' + p['id'])
        if is_part:
            part = self.part_of(p['part'])
            kicker = esc(S('part_n', n=part['number'])) + ' · ' + esc(part['name']) + ' · ' + esc(S('opening_essay'))
            meta = S.n('chapters', len(chapters)) + ' · ' + S.n('actions', self.actions_of(chapters))
        elif p['kind'] == 'glossary':
            kicker, meta = esc(S('reference')), S.n('terms', self.term_count)
        else:
            kicker, meta = esc(S('before_chapters')), S('contents_lead', chapters=S.n('chapters', len(self.chapters)), parts=len(self.PARTS), extras='', actions='')
        block = ('<section class="block" aria-labelledby="part-chapters"><p class="block-kicker">%s</p>'
                 '<h2 id="part-chapters" tabindex="-1">%s</h2><ol class="ch-list">%s</ol></section>'
                 % (esc(S('part_n', n=p['part'])), esc(S('part_chapters')), ''.join(self.chapter_item(c) for c in chapters))) if is_part else ''
        main = ('<article class="chapter page-doc%s" aria-labelledby="page-title"><header class="chapter-head">'
                '<p class="ch-kicker">%s</p><h1 class="ch-title" id="page-title" tabindex="-1">%s%s</h1>'
                '<div class="ch-meta"><span>%s</span></div></header><div class="prose">%s</div>%s'
                '<footer class="chapter-end">%s</footer></article>'
                % (' part-%d' % p['part'] if is_part else '', kicker,
                   '<span class="sr-only">%s</span>' % esc(S('part_prefix', n=p['part'])) if is_part else '', esc(p['title']), esc(meta), b['html'],
                   block, self.pager(prev, nxt, S('pages_nav'))))
        toc = b['toc'] + ([{'id': 'part-chapters', 'label': S('part_chapters'), 'href': self.page_href(p['id'], 'part-chapters')}] if is_part else [])
        return self.layout(toc, main, 'is-chapter is-page' + (' part-%d' % p['part'] if is_part else ''))

    def view_actions(self):
        S = self.S
        prev, nxt = self.neighbours('actions/')
        groups = []
        for p in self.PARTS:
            chapters = self.part_chapters(p['number'])
            if not chapters:
                continue
            groups.append(
                '<section class="sec part-%d" aria-labelledby="actions-part-%d"><p class="sec-kicker"><span class="sec-no">%s</span>'
                '<span class="sec-kind">%s</span></p><h2 id="actions-part-%d" tabindex="-1">%s</h2>%s</section>'
                % (p['number'], p['number'], esc(S('part_n', n=p['number'])), S.n('actions', self.actions_of(chapters)),
                   p['number'], esc(p['name']), ''.join(
                       '<div class="checklist" id="actions-%s" tabindex="-1"><h3 class="cl-title"><a href="%s">'
                       '<span class="cl-title-n">%s</span>%s</a></h3>%s<ul class="actions">%s</ul></div>'
                       % (c['id'], self.chapter_href(c['id']), pad(c['number']), esc(c['title']),
                          self.checklist_head(c['id'], len(self.built[c['id']]['actions'])),
                          ''.join(self.action_item(a) for a in self.built[c['id']]['actions']))
                       for c in chapters)))
        n_ch, n_act = len(self.chapters), self.total_actions
        main = ('<header class="page-head"><p class="block-kicker">%s</p>'
                '<h1 id="page-title" class="page-title page-title--md" tabindex="-1">%s</h1>'
                '<div class="block-text"><p>%s</p><p>%s</p><noscript><p>%s</p></noscript></div><div class="stats">%s%s</div></header>'
                '<div class="prose">%s</div><footer class="chapter-end">%s</footer>'
                % (esc(S('global_checklist')), esc(S('all_actions')), esc(S('actions_page_lead', actions=n_act, chapters=n_ch)),
                   esc(S('storage_sentence')), esc(S('missing_js_ticks')),
                   self.stat('<span data-stat="actions-done">0</span>', n_act, S('actions_done'), 'actions'),
                   self.stat('<span data-stat="chapters-read">0</span>', n_ch, S('chapters_read'), 'read'),
                   ''.join(groups), self.pager(prev, nxt, S('pages_nav'))))
        toc = [{'id': 'actions-part-%d' % p['number'], 'label': S('part_n', n=p['number']) + ' · ' + p['name'],
                'href': self.actions_href('actions-part-%d' % p['number']),
                'children': [{'id': 'actions-' + c['id'], 'no': pad(c['number']), 'label': c['title'],
                              'href': self.actions_href('actions-' + c['id'])} for c in self.part_chapters(p['number'])]}
               for p in self.PARTS if self.part_chapters(p['number'])]
        return self.layout(toc, main, 'is-actions')

    def view_directory(self):
        S = self.S
        entries = self.directory.get('editions', [])
        items = []
        for e in entries:
            rows = []
            if e.get('languages'):
                rows.append('<p class="dir-row"><span class="dir-k">%s</span> %s</p>' % (esc(S('directory_languages')), esc(', '.join(e['languages']))))
            if e.get('site'):
                rows.append('<p class="dir-row"><span class="dir-k">%s</span> <a class="ext" rel="noopener noreferrer" href="%s">%s</a></p>'
                            % (esc(S('directory_site')), esc(e['site']), esc(host_of(e['site']))))
            if e.get('repository'):
                rows.append('<p class="dir-row"><span class="dir-k">%s</span> <a class="ext" rel="noopener noreferrer" href="%s">%s</a></p>'
                            % (esc(S('directory_repository')), esc(e['repository']), esc(e['repository'])))
            items.append('<li class="dir-item" id="%s"><h2 tabindex="-1">%s</h2><p class="dir-community">%s</p>%s%s</li>'
                         % (esc('edition-' + slugify(e['name'])), esc(e['name']), esc(e.get('community', '')),
                            '<p>%s</p>' % esc(e['description']) if e.get('description') else '', ''.join(rows)))
        body = '<ul class="directory">%s</ul>' % ''.join(items) if items else '<p class="block-lead">%s</p>' % esc(S('directory_empty'))
        main = ('<header class="page-head"><p class="block-kicker">%s</p>'
                '<h1 id="page-title" class="page-title page-title--md" tabindex="-1">%s</h1>'
                '<div class="block-text"><p>%s</p></div></header><div class="prose">%s</div>'
                '<footer class="chapter-end">%s</footer>'
                % (esc(S('directory_kicker')), esc(S('directory_title')), esc(S('directory_lead')), body,
                   self.pager(self.nav_cover(), self.sequence[0] if self.sequence else self.nav_cover(), S('pages_nav'))))
        toc = [{'id': 'edition-' + slugify(e['name']), 'label': e['name'], 'href': self.editions_href('edition-' + slugify(e['name']))} for e in entries]
        return self.layout(toc, main, 'is-directory')

    def view_legal(self):
        S, E, R, O = self.S, self.E, self.release, self.S.opt
        L = self.cfg['licence']
        ext = lambda url, label: '<a class="ext" rel="noopener noreferrer" href="%s">%s</a>' % (esc(url), esc(label))
        local = lambda path, label: '<a href="%s">%s</a>' % (esc(self.BASE + path), esc(label))
        sections = []

        def section(sid, title, paras):
            sections.append('<section class="block" aria-labelledby="%s"><h2 id="%s" tabindex="-1">%s</h2>'
                            '<div class="block-text">%s</div></section>' % (sid, sid, esc(title), ''.join(paras)))

        section('original', O('legal_original_title', 'Original work'), [
            '<p>%s</p>' % O('legal_original', 'The original work is {title}, written for {project}, an initiative of {initiative}, '
                            'for its first conference (Vilnius, 2026). Original publication: {link}. That address is the reference '
                            'of the original work, not the source of this edition: the source of this edition is offered below.',
                            title='<cite>%s</cite>' % esc(ORIGINAL['title']), project=esc(ORIGINAL['project']),
                            initiative=esc(ORIGINAL['initiative']), link=ext(ORIGINAL['url'], ORIGINAL['url'])),
            '<p>%s</p>' % esc(O('legal_no_endorsement', 'This credit does not mean that {project} or {initiative} endorse this edition.',
                                project=ORIGINAL['project'], initiative=ORIGINAL['initiative']))])
        paras = ['<p>%s</p>' % O('legal_edition', '{edition} is an adapted edition of the original work, published by {community}. '
                                 'Its name, look, configuration, text and code may differ from the original.',
                                 edition=esc(E['name']), community=self.community_link())]
        if E['changes']:
            paras.append('<p>%s</p>' % O('legal_changes', 'Changes in this edition: {changes}', changes=esc(E['changes'])))
        else:
            paras.append('<p>%s</p>' % esc(O('legal_changes_unstated', 'The publisher of this edition has not described its changes here. '
                                              'The source archive below shows exactly what this edition is built from.')))
        paras.append('<p>%s</p>' % (esc(O('legal_modified', 'Last modified: {date}.', date=E['modified'])) if E['modified'] else
                                    esc(O('legal_modified_unstated', 'Modification date: not stated by the publisher of this edition.'))))
        if E['contact']:
            paras.append('<p>%s</p>' % S('about_contact', community=esc(E['community']), contact=self.contact_link()))
        section('this-edition', O('legal_edition_title', 'This edition'), paras)

        section('licences', O('legal_licences_title', 'Licences'), [
            '<p>%s</p>' % O('legal_text_licence', 'The text of the book is under {licence}. Full text: {local}.',
                            licence=ext(L['content']['url'], L['content']['label']), local=local('legal/LICENSE-CONTENT.txt', 'LICENSE-CONTENT.txt')),
            '<p>%s</p>' % O('legal_code_licence', 'The code is under {licence}: the generator, the stylesheet, and the scripts that '
                            'run in your browser (guide.js, and sw.js when the offline copy is on). Full text: {local}.',
                            licence=ext(L['code']['url'], L['code']['label']), local=local('legal/LICENSE.txt', 'LICENSE.txt')),
            '<p>%s</p>' % esc(O('legal_layers', 'These pages combine both: the book text stays under its licence and the code under '
                                'its own; putting them on the same page does not relicense either.')),
            '<p>%s</p>' % O('legal_notices', 'Notices: {notice} and {third}.', notice=local('legal/NOTICE.txt', 'NOTICE.txt'),
                            third=local('legal/THIRD-PARTY.txt', 'THIRD-PARTY.txt'))])

        if R['fonts']:
            items = ''.join('<li>%s: %s</li>' % (esc(f['family']), local(f['path'], f['path'].rsplit('/', 1)[-1])) for f in R['fonts'])
            section('fonts', O('legal_fonts_title', 'Fonts'), [
                '<p>%s</p>' % esc(O('legal_fonts', 'This edition serves the following fonts. They keep their own licence; '
                                    'the full notice of each is linked here and included in the source archive.')),
                '<ul>%s</ul>' % items])
        else:
            section('fonts', O('legal_fonts_title', 'Fonts'), [
                '<p>%s</p>' % esc(O('legal_no_fonts', 'This edition serves no font file: it uses the fonts of your device.'))])

        arc = R['archive']
        paras = []
        if arc:
            paras.append('<p>%s</p>' % O('legal_source', 'Source of this edition, as used to build these pages: {link} '
                                         '({kb} KB, SHA-256 <code>{sha}</code>). It contains the generator, the theme, the text, '
                                         'the configuration and assets of this edition, the licences and notices, and the build '
                                         'commands in SOURCE-README.txt.',
                                         link=local(arc['path'], arc['path'].rsplit('/', 1)[-1]), kb=max(1, round(arc['bytes'] / 1024)),
                                         sha=arc['sha256']))
        if E['repository']:
            paras.append('<p>%s</p>' % O('legal_repository', 'The publisher also keeps a source repository: {link}. It may hold a '
                                         'newer or older version than the archive above.', link=ext(E['repository'], E['repository'])))
        section('source', O('legal_source_title', 'Source'), paras)
        section('names', O('legal_names_title', 'Names and logos'), [
            '<p>%s</p>' % esc(O('legal_names', 'Neither licence grants rights to the names or logos of {project}, {initiative}, '
                                '{community}, or of the tools and organisations named in the book.',
                                project=ORIGINAL['project'], initiative=ORIGINAL['initiative'], community=E['community']))])

        main = ('<header class="page-head"><p class="block-kicker">%s</p>'
                '<h1 id="page-title" class="page-title page-title--md" tabindex="-1">%s</h1></header>%s'
                '<footer class="chapter-end">%s</footer>'
                % (esc(S('colophon')), esc(O('legal_title', 'Licences, credits and source')), ''.join(sections),
                   self.pager(self.nav_cover(), self.sequence[0] if self.sequence else self.nav_cover(), S('pages_nav'))))
        toc = [{'id': sid, 'label': label, 'href': self.legal_href(sid)} for sid, label in (
            ('original', O('legal_original_title', 'Original work')), ('this-edition', O('legal_edition_title', 'This edition')),
            ('licences', O('legal_licences_title', 'Licences')), ('fonts', O('legal_fonts_title', 'Fonts')),
            ('source', O('legal_source_title', 'Source')), ('names', O('legal_names_title', 'Names and logos')))]
        return self.layout(toc, main, 'is-directory')

    def view_not_found(self):
        S = self.S
        main = ('<header class="page-head"><p class="block-kicker">404</p>'
                '<h1 id="page-title" class="page-title page-title--md" tabindex="-1">%s</h1>'
                '<div class="block-text"><p>%s</p><p><a href="%s">%s</a> · <a href="%s">%s</a></p></div></header>'
                % (esc(S('not_found_title')), esc(S('not_found_text')), self.home_href(), esc(S('cover')), self.start_href(), esc(S('where_to_start'))))
        return self.layout([], main, 'is-notice')

    def contents_html(self, current):
        S = self.S
        links = ['<li><a href="%s">%s</a></li>' % (self.home_href(), esc(S('cover'))),
                 '<li><a href="%s">%s</a></li>' % (self.start_href(), esc(S('where_to_start')))]
        if self.show_actions:
            links.append('<li><a href="%s">%s</a></li>' % (self.home_href('progress'), esc(S('your_progress'))))
        if self.cfg['directory']['enabled']:
            links.append('<li><a href="%s">%s</a></li>' % (self.editions_href(), esc(S('editions_directory'))))
        links.append('<li>%s</li>' % self.legal_link())
        return ('<nav class="drawer" aria-label="%s"><ul class="drawer-links">%s</ul>' % (esc(S('book_contents')), ''.join(links))
                + self.extra_list(self.before_keys(), current)
                + ''.join('<section class="drawer-part part-%d" aria-labelledby="dp-%d"><h3 class="drawer-part-title" id="dp-%d">'
                          '<span>%s</span> %s</h3>%s</section>'
                          % (p['number'], p['number'], p['number'], esc(S('part_n', n=p['number'])), esc(p['name']), self.part_list(p['number'], current))
                          for p in self.PARTS)
                + '<div class="drawer-part">' + self.extra_list(self.after_keys(), current) + '</div>'
                + '<p class="drawer-scope">%s</p></nav>' % esc(S('drawer_scope', chapters=len(self.chapters), actions=self.total_actions, language=self.language_name)))

    def footer_html(self):
        S, E = self.S, self.E
        links = []
        if E['community_url']:
            links.append(self.community_link())
        if E['contact']:
            links.append(self.contact_link())
        if E['repository']:
            links.append('<a class="ext" rel="noopener noreferrer" href="%s">%s</a>' % (esc(E['repository']), esc(host_of(E['repository']))))
        for o in self.cfg['other_editions']:
            links.append('<a href="%s" hreflang="%s" lang="%s">%s</a>' % (esc(o['url']), esc(o['code']), esc(o['code']), esc(o['name'])))
        links.append(self.legal_link())
        return ('<div class="footer-inner"><p class="footer-mark">%s</p><p>%s</p><p>%s %s</p>%s%s</div>'
                % (esc(self.B['title']) + (' · ' + esc(E['name']) if E['name'] else ''),
                   esc(S('footer_counts', edition=E['name'], community=E['community'], chapters=len(self.chapters), actions=self.total_actions)),
                   self.licence_links(), esc(S('licence_note')),
                   '<p>%s</p>' % esc(S('storage_sentence')) if self.show_actions else '',
                   '<p class="footer-links">%s</p>' % ' · '.join(links) if links else ''))

    def lang_panel_html(self):
        S = self.S
        others = self.cfg['other_editions']
        if not others:
            return ''
        cur = self.cfg['language']
        items = ['<li class="lang-item is-current" aria-current="true"><span class="lang-code" aria-hidden="true">%s</span>'
                 '<span class="lang-body"><span class="lang-name" lang="%s">%s</span><span class="lang-state">%s</span></span></li>'
                 % (esc(cur['code'].upper()), esc(cur['code']), esc(cur['name']), esc(S('this_one')))]
        for o in others:
            items.append('<li class="lang-item"><span class="lang-code" aria-hidden="true">%s</span><span class="lang-body">'
                         '<a class="lang-name" href="%s" hreflang="%s" lang="%s">%s</a>%s</span></li>'
                         % (esc(o['code'].upper()), esc(o['url']), esc(o['code']), esc(o['code']), esc(o['name']),
                            '<span class="lang-note">%s</span>' % esc(o['note']) if o.get('note') else ''))
        return ('<div class="lang"><button type="button" class="hbtn hbtn--lang" id="lang-btn" aria-expanded="false" aria-controls="lang-panel">'
                '<span class="sr-only">%s</span>%s</button><div class="lang-panel" id="lang-panel" hidden>'
                '<p class="lang-title">%s</p><ul class="lang-list">%s</ul></div></div>'
                % (esc(S('language_button_label')), esc(cur['code'].upper()), esc(S('other_editions')), ''.join(items)))

    def search_index(self):
        S = self.S
        out = []
        if self.intro:
            out += self.built_pages[self.intro['id']]['index']
        for p in self.PARTS:
            pp = self.part_page(p['number'])
            if pp:
                out += self.built_pages[pp['id']]['index']
            for c in self.part_chapters(p['number']):
                out += self.built[c['id']]['index']
        if self.glossary:
            out += self.built_pages[self.glossary['id']]['index']
        n_ch, n_act = len(self.chapters), self.total_actions
        out += [
            {'type': 'page', 'title': S('contents'), 'kicker': S('cover'), 'href': self.home_href('contents'),
             'text': ' · '.join([c['title'] for c in self.chapters] + [p['title'] for p in self.pages])},
            {'type': 'page', 'title': self.in_this_guide(), 'kicker': S('cover'), 'href': self.home_href('preview'),
             'text': self.coverage_facts() + ' ' + S('coverage_language', language=self.language_name)},
            {'type': 'page', 'title': S('about_this_edition'), 'kicker': S('cover'), 'href': self.home_href('edition'),
             'text': plain(S('about_text', edition=self.E['name'], title=self.B['title'], community=self.E['community']))},
            {'type': 'page', 'title': S.opt('legal_title', 'Licences, credits and source'), 'kicker': S('colophon'),
             'href': self.legal_href(), 'text': plain(self.original_credit())},
            {'type': 'page', 'title': S('where_to_start'), 'kicker': S('orientation'), 'href': self.start_href(),
             'text': S('start_lead_1') + ' ' + S('start_lead_2')},
            {'type': 'page', 'title': S('how_chapters_work'), 'kicker': S('where_to_start'), 'href': self.start_href('how-chapters-work'),
             'text': ' · '.join(a['title'] + ': ' + a['text'] for a in S('anatomy'))},
        ]
        if self.show_actions:
            out.append({'type': 'page', 'title': S('your_progress'), 'kicker': S('cover'), 'href': self.home_href('progress'),
                        'text': plain(S('progress_help'))})
            out.append({'type': 'page', 'title': S('all_actions'), 'kicker': S('global_checklist'), 'href': self.actions_href(),
                        'text': S('actions_page_lead', actions=n_act, chapters=n_ch)})
        if self.cfg.get('_recordings'):
            out.append({'type': 'page', 'title': self.recordings_title(), 'kicker': S('cover'), 'href': self.home_href('recordings'),
                        'text': ' · '.join(' '.join(x for x in (it['title'], it.get('speaker', ''), it.get('note', '')) if x)
                                           for it in self.cfg['recordings']['items'])})
        if self.cfg['directory']['enabled']:
            out.append({'type': 'page', 'title': S('directory_title'), 'kicker': S('directory_kicker'), 'href': self.editions_href(),
                        'text': ' · '.join(e['name'] for e in self.directory.get('editions', []))})
        for i, p in enumerate(self.B['start_paths']):
            titles = [self.by_id[c]['title'] for c in p.get('chapters', []) + p.get('deeper', []) if c in self.by_id]
            out.append({'type': 'page', 'title': p['title'], 'kicker': S('where_to_start') + ' · ' + S('path_n', n=pad(i + 1)),
                        'text': p.get('text', '') + ' ' + ' · '.join(titles), 'href': self.start_href(p.get('id') or 'path-' + str(i + 1))})
        return [{'type': e['type'], 'part': e.get('part'), 'title': e['title'], 'kicker': e['kicker'],
                 'text': e.get('text', ''), 'href': e['href']} for e in out]


# ---------- pages ----------

def description(markdown_text):
    rest = markdown_text.lstrip('\n')
    return summary(rest.split('\n', 1)[1] if '\n' in rest else '')


def page_list(g):
    S, t = g.S, g.B['title']
    sep = S('title_separator')
    out = [{'path': '', 'key': 'home/', 'current': None, 'title': t + (sep + g.E['name'] if g.E['name'] else ''),
            'desc': S('meta_cover_description', title=t, edition=g.E['name'] or g.E['community']), 'og': 'website',
            'part': None, 'reading': False, 'html': g.view_home}]
    if g.intro:
        p = g.intro
        out.append({'path': p['slug'] + '/', 'key': 'page/' + p['id'], 'current': p['id'], 'title': p['title'] + sep + t,
                    'desc': description(p['markdown']), 'og': 'article', 'part': None, 'reading': True, 'html': (lambda p=p: g.view_page(p))})
    for part in g.PARTS:
        pp = g.part_page(part['number'])
        if pp:
            out.append({'path': pp['slug'] + '/', 'key': 'page/' + pp['id'], 'current': pp['id'],
                        'title': S('part_prefix', n=pp['part']) + pp['title'] + sep + t, 'desc': description(pp['markdown']),
                        'og': 'article', 'part': pp['part'], 'reading': True, 'html': (lambda p=pp: g.view_page(p))})
        for c in g.part_chapters(part['number']):
            out.append({'path': c['id'] + '/', 'key': 'chapter/' + c['id'], 'current': c['id'], 'title': c['title'] + sep + t,
                        'desc': description(c['markdown']), 'og': 'article', 'part': c['part'], 'reading': True, 'html': (lambda c=c: g.view_chapter(c))})
    if g.show_actions:
        out.append({'path': g.slugs['actions'] + '/', 'key': 'actions/', 'current': 'actions', 'title': S('all_actions') + sep + t,
                    'desc': summary(S('meta_actions_description', actions=g.total_actions, chapters=len(g.chapters), title=t)),
                    'og': 'article', 'part': None, 'reading': False, 'html': g.view_actions})
    if g.glossary:
        p = g.glossary
        out.append({'path': p['slug'] + '/', 'key': 'page/' + p['id'], 'current': p['id'], 'title': p['title'] + sep + t,
                    'desc': description(p['markdown']), 'og': 'article', 'part': None, 'reading': True, 'html': (lambda p=p: g.view_page(p))})
    paths = g.B['start_paths']
    out.append({'path': g.slugs['start'] + '/', 'key': 'start/', 'current': None, 'title': S('where_to_start') + sep + t,
                'desc': summary(S('meta_start_description', n=len(paths), title=t, paths='; '.join(p['title'] for p in paths))),
                'og': 'article', 'part': None, 'reading': False, 'html': g.view_start})
    if g.cfg['directory']['enabled']:
        out.append({'path': g.slugs['editions'] + '/', 'key': 'editions/', 'current': None, 'title': S('directory_title') + sep + t,
                    'desc': S('meta_directory_description', title=t), 'og': 'article', 'part': None, 'reading': False, 'html': g.view_directory})
    out.append({'path': g.slugs['legal'] + '/', 'key': 'legal/', 'current': None,
                'title': S.opt('legal_title', 'Licences, credits and source') + sep + t,
                'desc': S.opt('meta_legal_description', 'Licences, original work, credits, font notices and the source archive of this edition of {title}.', title=t),
                'og': 'article', 'part': None, 'reading': False, 'html': g.view_legal})
    return out


def head_html(g, page, assets, not_found=False):
    cfg = g.cfg
    site_url = cfg['site']['url'].rstrip('/')
    url = site_url + g.BASE + page['path'] if site_url else ''
    title, desc = esc(page['title']), esc(page['desc'])
    canonical = '<link rel="canonical" href="%s">\n' % url if url and not not_found else ''
    alternates = ''
    if url and cfg['other_editions'] and page['key'] in ('home/',):
        alternates = ''.join('<link rel="alternate" hreflang="%s" href="%s">\n' % (esc(o['code']), esc(o['url'])) for o in cfg['other_editions'])
        alternates += '<link rel="alternate" hreflang="%s" href="%s">\n' % (esc(cfg['language']['code']), url)
    og = ''
    if url:
        og = ('<meta property="og:type" content="%s">\n<meta property="og:site_name" content="%s">\n'
              '<meta property="og:title" content="%s">\n<meta property="og:description" content="%s">\n'
              '<meta property="og:url" content="%s">\n<meta property="og:locale" content="%s">\n'
              % (page['og'], esc(g.B['title']), title, desc, url, esc(cfg['language']['locale'])))
        if assets.get('og_image'):
            og += ('<meta property="og:image" content="%s">\n<meta name="twitter:card" content="summary_large_image">\n'
                   '<meta name="twitter:image" content="%s">\n' % (site_url + assets['og_image'], site_url + assets['og_image']))
    preload = ''.join('<link rel="preload" href="%s" as="font" type="font/woff2" crossorigin>\n' % u for u in assets['preload_fonts'])
    favicon = '<link rel="icon" href="%s">\n' % assets['favicon'] if assets.get('favicon') else ''
    robots = '<meta name="robots" content="noindex">\n' if not_found or not cfg['site']['indexing'] else ''
    return ('<!doctype html>\n<html lang="%s" dir="%s">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<meta name="referrer" content="no-referrer">\n'
            '<meta name="generator" content="A Guide to Autonomy %s">\n'
            '<meta http-equiv="Content-Security-Policy" content="%s">\n'
            '<meta name="color-scheme" content="%s">\n'
            '<title>%s</title>\n<meta name="description" content="%s">\n%s%s%s%s%s%s'
            '<link rel="stylesheet" href="%s">\n'
            '<noscript><style>%s</style></noscript>\n'
            '<script defer src="%s"></script>\n<script defer src="%s"></script>\n%s'
            '</head>\n'
            % (esc(cfg['language']['code']), esc(cfg['language']['direction']), VERSION, csp(cfg, page['key']), esc(cfg['colors']['scheme']), title, desc,
               robots, canonical, alternates, favicon, og, preload, assets['guide.css'], NOSCRIPT_CSS, assets['site-data.js'], assets['guide.js'],
               '<script defer src="%s"></script>\n' % assets['recordings.js'] if page['key'] == 'home/' and assets.get('recordings.js') else ''))


def page_html(g, page, assets, not_found=False):
    S, E = g.S, g.E
    part_cls = ' part-%d' % page['part'] if page['part'] else ''
    brand = g.logo_html('brand-logo') + ('<span class="brand-text"><span class="brand-title">%s</span>%s</span>'
                                          % (esc(g.B['title']), '<span class="brand-sub">%s</span>' % esc(E['name']) if E['name'] else ''))
    search_btn = ('<button type="button" class="hbtn" data-open="search" aria-haspopup="dialog" aria-keyshortcuts="/ Control+K Meta+K" data-js-only hidden>'
                  '<svg class="hbtn-icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="8.5" cy="8.5" r="5.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12.6 12.6 17 17" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'
                  '<span class="hbtn-label">%s</span><kbd class="hbtn-kbd" aria-hidden="true">/</kbd></button>' % esc(S('search'))) if g.L['show_search'] else ''
    search_dialog = ('<dialog class="dialog dialog--search" id="search-dialog" aria-labelledby="search-title"><div class="dialog-box">'
                     '<div class="dialog-head"><h2 class="dialog-title" id="search-title">%s</h2>'
                     '<button type="button" class="dialog-close" data-close>%s <span class="dialog-esc" aria-hidden="true">%s</span></button></div>'
                     '<form class="search-form" role="search" id="search-form"><label class="search-label" for="search-input">%s</label>'
                     '<input class="search-input" id="search-input" type="search" autocomplete="off" spellcheck="false" aria-describedby="search-scope" aria-controls="search-results">'
                     '<p class="search-scope" id="search-scope">%s</p></form>'
                     '<p class="sr-only" id="search-status" aria-live="polite"></p><div class="dialog-scroll search-results" id="search-results"></div></div></dialog>\n'
                     % (esc(S('search_title')), esc(S('close')), esc(S('esc')), esc(S('search_label')), esc(S('search_scope')))) if g.L['show_search'] else ''
    return (head_html(g, page, assets, not_found)
            + '<body>\n<a class="skip-link" href="#main">%s</a>\n' % esc(S('skip_to_content'))
            + '<header class="site-header"><div class="header-inner">'
            '<a class="brand" href="%s">%s</a><div class="header-actions">'
            '<a class="hbtn" href="%s" data-open="contents" aria-haspopup="dialog">'
            '<svg class="hbtn-icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M3 5h14M3 10h14M3 15h9" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'
            '<span class="hbtn-label">%s</span></a>%s%s</div></div></header>\n'
            '<div class="read-progress%s" id="read-progress" aria-hidden="true"%s><i></i></div>\n'
            '<main id="main" tabindex="-1" data-page="%s">%s</main>\n'
            '<footer class="site-footer" id="site-footer">%s</footer>\n%s'
            '<dialog class="dialog dialog--drawer" id="contents-dialog" aria-labelledby="contents-title"><div class="dialog-box">'
            '<div class="dialog-head"><h2 class="dialog-title" id="contents-title">%s</h2>'
            '<button type="button" class="dialog-close" data-close>%s <span class="dialog-esc" aria-hidden="true">%s</span></button></div>'
            '<div class="dialog-scroll" id="contents-body">%s</div></div></dialog>\n'
            '</body>\n</html>\n'
            % (g.home_href(), brand, g.home_href('contents'), esc(S('contents')), search_btn, g.lang_panel_html(),
               part_cls, '' if page['reading'] else ' hidden', page['key'], page['html'](), g.footer_html(), search_dialog,
               esc(S('contents')), esc(S('close')), esc(S('esc')), g.contents_html(page['current'])))


# ---------- theme: CSS variables from the configuration, fonts, logo ----------

def theme_css(cfg, font_urls, tick_hex):
    C, F, L = cfg['colors'], cfg['fonts'], cfg['layout']
    bg, fg = hex_rgb(C['background'], 'colors.background'), hex_rgb(C['foreground'], 'colors.foreground')
    faces = []
    for role in ('heading', 'body'):
        for f in F[role]['files']:
            faces.append('@font-face { font-family: %s; font-style: %s; font-weight: %s; font-display: swap; src: url(%s) format("woff2");%s }' % (
                json.dumps(F[role]['family']), f.get('style', 'normal'), f.get('weight', '400'), json.dumps(font_urls[f['file']]),
                ' unicode-range: %s;' % f['unicode_range'] if f.get('unicode_range') else ''))
    heading = (json.dumps(F['heading']['family']) + ', ' if F['heading']['family'] else '') + F['heading']['fallback']
    body = (json.dumps(F['body']['family']) + ', ' if F['body']['family'] else '') + F['body']['fallback']
    parts = []
    for i, p in enumerate(C['parts'], 1):
        hex_rgb(p['accent'], 'colors.parts[%d].accent' % (i - 1))
        parts.append('  --part-%d: %s; --part-%d-text: %s;' % (i, p['accent'], i, p.get('text') or p['accent']))
    tokens = [
        '  --bg: %s; --fg: %s;' % (C['background'], C['foreground']),
        '  --text: %s; --muted: %s; --line: %s; --line-strong: %s;' % (rgba(fg, .86), rgba(fg, .64), rgba(fg, .12), rgba(fg, .28)),
        '  --fg-70: %s; --fg-60: %s; --fg-35: %s; --fg-20: %s; --fg-10: %s; --fg-05: %s; --fg-04: %s;' % (
            rgba(fg, .7), rgba(fg, .6), rgba(fg, .35), rgba(fg, .2), rgba(fg, .1), rgba(fg, .05), rgba(fg, .04)),
        '  --bg-97: %s; --bg-96: %s; --bg-86: %s; --bg-78: %s; --bg-72: %s; --bg-70: %s; --bg-68: %s; --bg-16: %s;' % (
            rgba(bg, .97), rgba(bg, .96), rgba(bg, .86), rgba(bg, .78), rgba(bg, .72), rgba(bg, .7), rgba(bg, .68), rgba(bg, .16)),
        '  --raised: %s; --sunk: %s; --surface-5: %s; --surface-6: %s; --surface-9: %s;' % (
            mix(fg, bg, .03), mix(fg, bg, .015), mix(fg, bg, .05), mix(fg, bg, .06), mix(fg, bg, .09)),
        '  --shadow: rgba(0, 0, 0, %s); --backdrop: rgba(0, 0, 0, 0.6);' % ('0.5' if C['scheme'] == 'dark' else '0.25'),
        '\n'.join(parts),
        '  --heading: %s; --heading-weight: %s; --body: %s;' % (heading, F['heading']['weight'] if F['heading']['family'] or F['heading']['weight'] else '700', body),
        '  --caps: %s;' % ('uppercase' if L['uppercase_headings'] else 'none'),
        '  --measure: %s;' % L['reading_width'],
        '  color-scheme: %s;' % C['scheme'],
    ]
    tick = TICK.format(hex=tick_hex)
    return ('/* Generated by build.py from edition.json. Edit edition.json, not this block. */\n'
            + '\n'.join(faces) + ('\n' if faces else '')
            + ':root {\n' + '\n'.join(tokens) + '\n}\n'
            + '.action-cb:checked, .read-row .read-cb:checked { background-image: %s; }\n' % tick)


def resolve_asset(cfg, edition_dir, rel, what):
    for base in (edition_dir, ROOT):
        p = (base / rel).resolve()
        if p.is_file():
            return p
    raise BuildError('%s: file not found: %s (looked in %s and in the repository root).' % (what, rel, edition_dir))


def build_assets(g, cfg, edition_dir):
    """Every file under <base>/assets/, with its versioned address."""
    files, urls = {}, {}
    asset_base = g.BASE + 'assets/'

    def add(name, data):
        files[name] = data
        urls[name] = asset_base + name + '?v=' + sha256(data)[:12]

    font_urls, preload = {}, []
    for role in ('heading', 'body'):
        for f in cfg['fonts'][role]['files']:
            p = resolve_asset(cfg, edition_dir, f['file'], 'fonts.%s.files' % role)
            name = 'fonts/' + p.name
            if name not in files:
                add(name, p.read_bytes())
            font_urls[f['file']] = urls[name][len(asset_base):]
            if f.get('preload') and urls[name] not in preload:
                preload.append(urls[name])
    bg = hex_rgb(cfg['colors']['background'], 'colors.background')
    css = (THEME / 'styles.css').read_text(encoding='utf-8')
    extra = (edition_dir / 'custom.css')
    custom = ('\n\n/* custom.css of this edition */\n' + extra.read_text(encoding='utf-8')) if extra.is_file() else ''
    add('guide.css', (theme_css(cfg, font_urls, '%02x%02x%02x' % bg) + '\n' + css.rstrip('\n') + custom + '\n').encode('utf-8'))
    add('guide.js', (THEME / 'app.js').read_bytes())
    assets = {'preload_fonts': preload}
    cfg['_posters'] = {}
    if cfg.get('_recordings'):
        add('recordings.js', (THEME / 'recordings.js').read_bytes())
        assets['recordings.js'] = urls['recordings.js']
        for i, it in enumerate(cfg['recordings']['items']):
            if it.get('poster') and it['poster'] not in cfg['_posters']:
                p = resolve_asset(cfg, edition_dir, it['poster'], 'recordings.items[%d].poster' % i)
                name = 'recordings/%d-%s' % (i + 1, re.sub(r'[^a-z0-9.-]+', '-', p.name.lower()))
                add(name, p.read_bytes())
                cfg['_posters'][it['poster']] = urls[name]
    logo = cfg['edition']['logo']
    if logo.get('file'):
        p = resolve_asset(cfg, edition_dir, logo['file'], 'edition.logo.file')
        add('logo' + p.suffix.lower(), p.read_bytes())
        cfg['_logo'] = {'url': urls['logo' + p.suffix.lower()]}
        if logo.get('cover_file'):
            p = resolve_asset(cfg, edition_dir, logo['cover_file'], 'edition.logo.cover_file')
            add('logo-cover' + p.suffix.lower(), p.read_bytes())
            cfg['_logo']['cover'] = urls['logo-cover' + p.suffix.lower()]
    for key, label in (('favicon', 'site.favicon'), ('og_image', 'site.og_image')):
        if cfg['site'][key]:
            p = resolve_asset(cfg, edition_dir, cfg['site'][key], label)
            add(key + p.suffix.lower(), p.read_bytes())
            assets[key] = urls[key + p.suffix.lower()]
    search = ('/* Generated by build.py: search index of every page. */\nwindow.GUIDE_SEARCH = %s;\n'
              % json.dumps(g.search_index(), ensure_ascii=True, separators=(',', ':')))
    add('search-index.js', search.encode('utf-8'))
    site = {
        'base': g.BASE, 'search': urls['search-index.js'] if g.L['show_search'] else None,
        'sw': g.BASE + 'sw.js' if cfg['site']['offline'] else None, 'swScope': g.BASE,
        'storageKey': cfg['storage_key'], 'progress': g.L['show_progress'],
        'chapters': [{'id': c['id'], 'number': c['number'], 'part': c['part'], 'title': c['title'],
                      'actions': [a['id'] for a in g.built[c['id']]['actions']]} for c in g.chapters],
        'routes': {'home': g.BASE, 'chapter': {c['id']: g.BASE + c['id'] + '/' for c in g.chapters}},
        'strings': g.S.runtime(),
    }
    add('site-data.js', ('/* Generated by build.py: addresses, actions and interface strings. */\nwindow.GUIDE_SITE = %s;\n'
                         % json.dumps(site, ensure_ascii=True, indent=1)).encode('utf-8'))
    assets.update({k: urls[k] for k in ('guide.css', 'guide.js', 'site-data.js')})
    return files, urls, assets


def legal_files(g, cfg, edition_file, out_dir):
    """Licence and notice texts, font notices and the source ZIP, as {path in the output: bytes}."""
    files = {}
    for src, dst in LEGAL_TEXTS:
        p = ROOT / src
        if not p.is_file():
            raise BuildError('%s is missing. Every edition ships it; restore it from the base repository.' % src)
        files[dst] = p.read_bytes()
    if sha256(files['legal/LICENSE.txt']) != AGPL_SHA256:
        raise BuildError('LICENSE is not the official text of the GNU AGPL v3. Restore it from the base repository; '
                         'the code stays under AGPL-3.0-or-later in every edition.')
    if b'Attribution-ShareAlike 4.0 International' not in files['legal/LICENSE-CONTENT.txt']:
        raise BuildError('LICENSE-CONTENT is not the CC BY-SA 4.0 legal code. Restore it from the base repository.')
    fonts = []
    try:
        for role, i, f in release.configured_fonts(cfg):
            for notice in release.font_notices(ROOT, edition_file.parent, f, 'fonts.%s.files[%d]' % (role, i)):
                path, data = 'legal/fonts/' + notice.name, notice.read_bytes()
                if files.get(path, data) != data:
                    raise BuildError('2 different font notices are both named %s. Rename one of them.' % notice.name)
                files[path] = data
                entry = {'family': cfg['fonts'][role]['family'] or notice.stem, 'path': path}
                if entry not in fonts:
                    fonts.append(entry)
        archive = release.source_archive(ROOT, edition_file, cfg, exclude=[out_dir])
    except release.ReleaseError as e:
        raise BuildError(str(e))
    files[release.ARCHIVE_NAME] = archive
    g.release = {'files': files, 'fonts': fonts,
                 'archive': {'path': release.ARCHIVE_NAME, 'bytes': len(archive), 'sha256': sha256(archive)}}
    return files


def service_worker(g, outputs, urls, cfg, extra=None):
    """extra: small files outside assets/ to precache (the legal texts). The source ZIP is not precached."""
    extra = extra or {}
    tpl = (THEME / 'sw.template.js').read_text(encoding='utf-8')
    # The player and posters of recordings are not precached: that section needs a connection anyway.
    online = {u for k, u in urls.items() if k.startswith('recordings')}
    core = sorted(set([u for u in urls.values() if u not in online] + [g.BASE + p for p in outputs] + [g.BASE + p for p in extra]))
    h = hashlib.sha256('\n'.join(core).encode('utf-8'))
    for p in sorted(outputs):
        h.update(outputs[p])
    for p in sorted(extra):
        h.update(extra[p])
    h.update(tpl.encode('utf-8'))
    prefix = re.sub(r'[^a-z0-9-]+', '-', cfg['storage_key'].lower()).strip('-') or 'guide'
    return tpl.replace('__PREFIX__', prefix).replace('__VERSION__', h.hexdigest()[:8]).replace(
        '__CORE__', ',\n  '.join(json.dumps(u) for u in core)).encode('utf-8')


# ---------- checks ----------

_ID = re.compile(r'\sid="([^"]*)"')
_HREF = re.compile(r'\shref="([^"]*)"')


_EMBED = re.compile(r'<(?:script|img|iframe|video|audio|source|embed|object)\b[^>]*?\s(?:src|data|srcset|poster)="\s*(?:https?:)?//[^"]*"[^>]*>', re.I)
_LINK = re.compile(r'<link\b[^>]*>', re.I)
# Local paths of the computer that built the edition must never reach the pages or the source archive.
# The fragments are split so that this file, which ships in every source archive, does not match itself.
LEAKS = tuple(a + b for a, b in (('/Us', 'ers/'), ('/home/', 'runner/'), ('C:\\', 'Users\\'), ('C:/', 'Users/'), ('fi', 'le://'),
                                  ('/private/', 'tmp/'), ('/private/', 'var/folders/'), ('.co', 'dex/')))


def external_resources(h):
    """Tags that would make the reader's browser fetch something from another site when the page loads."""
    found = _EMBED.findall(h)
    for tag in _LINK.findall(h):
        rel = re.search(r'\srel="([^"]*)"', tag)
        href = re.search(r'\shref="([^"]*)"', tag)
        if rel and href and rel.group(1) not in ('canonical', 'alternate') and re.match(r'\s*(?:https?:)?//', href.group(1)):
            found.append(tag)
    return found


def leaks(data, where):
    """Local paths found in a built file, as messages."""
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError:
        return []
    return ['%s: contains the local path fragment %r; remove it from the source' % (where, x) for x in LEAKS if x in text]


def check_pages(g, outputs, files, cfg, extra=()):
    base = g.BASE
    ids = {p: _ID.findall(h.decode('utf-8')) for p, h in outputs.items()}
    problems, links = [], 0
    site_url = cfg['site']['url'].rstrip('/')
    for path, data in outputs.items():
        h = data.decode('utf-8')
        where = base + path
        dup = sorted({i for i in ids[path] if ids[path].count(i) > 1})
        if dup:
            problems.append('%s: duplicate IDs %s' % (where, ', '.join(dup[:8])))
        if site_url and h.count('<link rel="canonical" href="%s">' % (site_url + where)) != 1:
            problems.append('%s: canonical link' % where)
        if not re.search(r'<title>[^<]+</title>', h) or not re.search(r'<meta name="description" content="[^"]{30,}">', h):
            problems.append('%s: title or description too short' % where)
        if h.count('<h1') != 1:
            problems.append('%s: %d <h1>' % (where, h.count('<h1')))
        for tag in external_resources(h):
            problems.append('%s: loaded from another site, which the pages never do: %s' % (where, tag[:120]))
        if PLACEHOLDER.search(html.unescape(h)):
            problems.append('%s: an unfilled {{placeholder}} remains in the text' % where)
        for href in _HREF.findall(h):
            href = html.unescape(href)
            if href.startswith(('http://', 'https://', 'mailto:')):
                continue
            links += 1
            target, _, frag = href.partition('#')
            target = target.split('?')[0]
            if not target:
                target = where
            if target.startswith(base + 'assets/'):
                if target[len(base) + 7:] not in files:
                    problems.append('%s: asset %s not built' % (where, href))
            elif target.startswith(base) and target[len(base):] in extra:
                pass
            elif target.startswith(base) and target.endswith('/'):
                rel = target[len(base):]
                if rel not in outputs:
                    problems.append('%s: link to %s, not a page of the book' % (where, href))
                elif frag and frag not in ids[rel]:
                    problems.append('%s: link to %s, no such ID' % (where, href))
            else:
                problems.append('%s: unexpected link %s' % (where, href))
    if problems:
        raise BuildError('Checks of the generated pages failed:\n  - ' + '\n  - '.join(problems[:60]))
    return {'pages': len(outputs), 'internal_links_checked': links, 'ids': sum(len(v) for v in ids.values())}


# ---------- main ----------

def load_config(path, site_url=None, base_path=None):
    """site_url and base_path, when given (build.py --site-url / --base-path), replace the values of
    edition.json for this build only; the source archive records them (see release.source_readme)."""
    path = Path(path).resolve()
    if not path.is_file():
        raise BuildError('Edition file not found: %s' % path)
    try:
        user = json.loads(path.read_text(encoding='utf-8'))
    except ValueError as e:
        raise BuildError('%s is not valid JSON: %s\nTip: JSON needs double quotes and no trailing comma after the last item; the mistake is '
                         'often at the end of the line before the one named.' % (path, e))
    try:
        cfg = merge(DEFAULTS, user)
    except BuildError as e:
        raise BuildError(str(e).replace('edition.json:', path.name + ':', 1))
    overrides = {}
    if site_url is not None:
        overrides['site_url'] = cfg['site']['url'] = site_url.strip()
    if base_path is not None:
        overrides['base_path'] = cfg['site']['base_path'] = base_path.strip()
    bp = cfg['site']['base_path'] or '/'
    if not bp.startswith('/'):
        bp = '/' + bp
    if not bp.endswith('/'):
        bp += '/'
    if '//' in bp or any(c in bp for c in ' ?#\\'):
        raise BuildError('site.base_path must be a folder such as / or /guide/, found %r.' % bp)
    cfg['site']['base_path'] = bp
    url = cfg['site']['url']
    if url and not url.startswith(('http://', 'https://')):
        raise BuildError('site.url must start with https:// (or be empty while you have no address yet).')
    if url:
        parts = urlsplit(url)
        if not parts.hostname or parts.path.strip('/') or parts.query or parts.fragment:
            raise BuildError('site.url must be the address of the site only, such as https://example.org, without a folder: '
                             'found %r. Put the folder in site.base_path (for example "/guide/").' % url)
        cfg['site']['url'] = '%s://%s' % (parts.scheme, parts.netloc)
    cfg['_overrides'] = {k: cfg['site']['url'] if k == 'site_url' else bp for k in overrides}
    for i, p in enumerate(cfg['colors']['parts']):
        if 'accent' not in p:
            raise BuildError('colors.parts[%d] needs an "accent" colour.' % i)
    cfg['_recordings'] = prepare_recordings(cfg['recordings'])
    return cfg, path.parent


def prepare_recordings(R):
    """Checks recordings.items and lists the outside addresses the cover may contact after a click.
    None when the section is off or empty."""
    if not R.get('enabled') or not R.get('items'):
        return None
    frames, media, problems = set(), set(), []
    for o in R.get('media_origins', []):
        if not str(o).startswith('https://') or origin_of(o) != str(o).rstrip('/'):
            problems.append('recordings.media_origins: %r must be an origin such as https://cdn.example.org' % o)
        else:
            media.add(origin_of(o))
    for i, it in enumerate(R['items']):
        where = 'recordings.items[%d]' % i
        if not isinstance(it, dict) or not str(it.get('title', '')).strip():
            problems.append(where + ': "title" is required')
            continue
        for key in ('video', 'video_sd'):
            url = it.get(key, '')
            if not url:
                continue
            if not url.startswith('https://'):
                problems.append('%s.%s must start with https://' % (where, key))
            elif YOUTUBE.match(url):
                frames.add(YOUTUBE_EMBED)
            elif re.match(r'https://(?:[a-z0-9-]+\.)?(?:youtube\.com|youtu\.be)/', url):
                problems.append('%s.%s is a YouTube address the player does not recognise; use the form '
                                'https://www.youtube.com/watch?v=<id> or https://youtu.be/<id>' % (where, key))
            else:
                media.add(origin_of(url))
        for j, link in enumerate(it.get('links', [])):
            if not str(link.get('href', '')).startswith('https://') or not link.get('label'):
                problems.append('%s.links[%d] needs a "label" and an https address' % (where, j))
        poster = it.get('poster', '')
        if poster and (poster.startswith(('http://', 'https://', '/')) or '..' in poster.split('/')):
            problems.append('%s.poster must be an image file next to edition.json (for example assets/talk-1.jpg), '
                            'never an outside address: the cover loads nothing from another site before a click' % where)
    if problems:
        raise BuildError('edition.json, recordings:\n  - ' + '\n  - '.join(problems))
    return {'frame_origins': sorted(frames), 'media_origins': sorted(media)}


def public_https(url):
    """True for an https address on a public domain name (no IP address, localhost or local network name)."""
    try:
        parts = urlsplit(url)
        host = (parts.hostname or '').lower()
    except ValueError:
        return False
    if parts.scheme != 'https' or '.' not in host or parts.username or parts.password:
        return False
    if re.fullmatch(r'[0-9.]+', host) or ':' in host:
        return False
    return not host.endswith(('.local', '.localhost', '.internal', '.lan', '.home', '.test', '.invalid'))


def check_directory(directory, name):
    """The optional list of other editions: every entry public, consented and unique."""
    problems, seen = [], set()
    entries = directory.get('editions')
    if not isinstance(entries, list):
        raise BuildError('%s: "editions" must be a list (it may be empty).' % name)
    for i, e in enumerate(entries):
        where = '%s, editions[%d] (%s)' % (name, i, e.get('name', 'no name') if isinstance(e, dict) else '?')
        if not isinstance(e, dict) or not str(e.get('name', '')).strip():
            problems.append(where + ': "name" is required')
            continue
        for key in ('site', 'repository'):
            if e.get(key) and not public_https(e[key]):
                problems.append(where + ': "%s" must be an https address on a public domain name' % key)
        if not e.get('site'):
            problems.append(where + ': "site" is required')
        elif e['site'].rstrip('/') in seen:
            problems.append(where + ': the same site is listed twice')
        seen.add(str(e.get('site', '')).rstrip('/'))
        if not isinstance(e.get('languages', []), list):
            problems.append(where + ': "languages" must be a list such as ["en"]')
        consent = e.get('consent')
        if not (isinstance(consent, dict) and consent.get('public_listing') is True and consent.get('date')):
            problems.append(where + ': "consent" must say {"public_listing": true, "date": "YYYY-MM-DD", "reference": "..."}: '
                            'an edition is listed only when its maintainers asked for it')
    if problems:
        raise BuildError('The directory of editions is not valid:\n  - ' + '\n  - '.join(problems))


def contrast(a, b):
    """WCAG contrast ratio of 2 colours given as (r, g, b)."""
    def lum(c):
        ch = [v / 255 for v in c]
        ch = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in ch]
        return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]
    hi, lo = sorted((lum(a), lum(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def contrast_notes(cfg):
    """Readability notes (never errors): text colours under 4.5:1 on the page background."""
    C = cfg['colors']
    bg = hex_rgb(C['background'], 'colors.background')
    pairs = [('colors.foreground', C['foreground'])] + [('colors.parts[%d].text' % i, p.get('text') or p['accent'])
                                                        for i, p in enumerate(C['parts'])]
    notes = []
    for key, value in pairs:
        r = contrast(hex_rgb(value, key), bg)
        if r < 4.5:
            notes.append('Note: %s %s has a contrast of %.1f:1 on the background %s; 4.5:1 or more reads well. '
                         'See the palettes in docs/CONFIGURATION.md.' % (key, value, r, C['background']))
    return notes


def run(args):
    cfg, edition_dir = load_config(args.edition, getattr(args, 'site_url', None), getattr(args, 'base_path', None))
    out_dir = Path(args.out).resolve()
    if out_dir == ROOT or ROOT in out_dir.parents and out_dir.name in ('content', 'theme', 'docs', 'examples'):
        raise BuildError('Refusing to write into %s.' % out_dir)
    content = Content(cfg, update_registry=args.update_actions)
    if len(cfg['colors']['parts']) < len(content.manifest['parts']):
        raise BuildError('edition.json: colors.parts has %d entries, book.json declares %d parts.' % (len(cfg['colors']['parts']), len(content.manifest['parts'])))
    directory = {'editions': []}
    if cfg['directory']['enabled']:
        dpath = edition_dir / cfg['directory']['file']
        if not dpath.is_file():
            dpath = ROOT / cfg['directory']['file']
        if not dpath.is_file():
            raise BuildError('directory.enabled is true but %s was not found.' % cfg['directory']['file'])
        try:
            directory = json.loads(dpath.read_text(encoding='utf-8'))
        except ValueError as e:
            raise BuildError('%s is not valid JSON: %s' % (dpath, e))
        check_directory(directory, dpath.name)
    g = Guide(cfg, content, directory)
    edition_file = release.edition_path(args.edition)
    legal = legal_files(g, cfg, edition_file, out_dir)
    files, urls, assets = build_assets(g, cfg, edition_dir)
    pages = page_list(g)
    outputs = {p['path']: page_html(g, p, assets).encode('utf-8') for p in pages}
    not_found = {'path': '404.html', 'key': 'not-found/', 'current': None, 'title': g.S('not_found_title') + g.S('title_separator') + g.B['title'],
                 'desc': g.S('not_found_text') + ' ' + g.S('meta_cover_description', title=g.B['title'], edition=g.E['name'] or g.E['community']),
                 'og': 'website', 'part': None, 'reading': False, 'html': g.view_not_found}
    checks = check_pages(g, outputs, files, cfg, extra=set(legal))
    outputs['404.html'] = page_html(g, not_found, assets, not_found=True).encode('utf-8')

    writes = {}
    for p, data in outputs.items():
        writes[out_dir / (p if p.endswith('.html') else p + 'index.html')] = data
    for name, data in files.items():
        writes[out_dir / 'assets' / Path(name)] = data
    for name, data in legal.items():
        writes[out_dir / Path(name)] = data
    if cfg['site']['offline']:
        small = {k: v for k, v in legal.items() if k != release.ARCHIVE_NAME}
        writes[out_dir / 'sw.js'] = service_worker(g, {k: v for k, v in outputs.items() if not k.endswith('.html')}, urls, cfg, small)
    site_url = cfg['site']['url'].rstrip('/')
    if not cfg['site']['indexing']:
        # Draft or private edition: every page says noindex, and crawlers are asked to stay away.
        writes[out_dir / 'robots.txt'] = b'User-agent: *\nDisallow: /\n'
    elif site_url and cfg['site']['sitemap']:
        locs = ''.join('  <url><loc>%s</loc></url>\n' % esc(site_url + g.BASE + p['path']) for p in pages)
        writes[out_dir / 'sitemap.xml'] = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % locs).encode('utf-8')
        writes[out_dir / 'robots.txt'] = ('User-agent: *\nAllow: /\nSitemap: %s\n' % (site_url + g.BASE + 'sitemap.xml')).encode('utf-8')
    # Public list of the files of this build: relative paths, sizes, SHA-256. release.py exports exactly these.
    manifest = {'about': 'Files of this build of the edition, with their SHA-256. Upload these files and nothing else '
                         '(python3 release.py --dest <new folder> does it). Paths are relative to the base path.',
                'files': [{'path': p.relative_to(out_dir).as_posix(), 'bytes': len(d), 'sha256': sha256(d)}
                          for p, d in sorted(writes.items(), key=lambda w: w[0].relative_to(out_dir).as_posix())]}
    writes[out_dir / release.MANIFEST] = (json.dumps(manifest, ensure_ascii=False, indent=1) + '\n').encode('utf-8')
    for path in writes:
        if out_dir not in path.resolve().parents:
            raise BuildError('Refusing to write outside the output folder: %s' % path)
    found = []
    for path, data in writes.items():
        rel = path.relative_to(out_dir).as_posix()
        if rel.endswith('.zip'):
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                for name in z.namelist():
                    found += leaks(z.read(name), rel + ':' + name)
        else:
            found += leaks(data, rel)
    if found:
        raise BuildError('Local paths would be published:\n  - ' + '\n  - '.join(found[:20]))

    written, unchanged = [], []
    for path, data in sorted(writes.items()):
        rel = path.relative_to(out_dir).as_posix()
        if path.is_file() and path.read_bytes() == data:
            unchanged.append(rel)
        elif args.check:
            written.append(rel)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            written.append(rel)

    report = {
        'generator': 'build.py', 'version': VERSION, 'python_markdown': markdown.__version__,
        'edition': edition_file.relative_to(ROOT).as_posix() if ROOT in edition_file.parents else edition_file.name,
        'counts': {'chapters': len(g.chapters), 'other_pages': len(g.pages), 'actions': g.total_actions, 'pages_written': len(outputs),
                   'parts': len(g.PARTS), 'tool_links_added': g.tool_links, 'search_entries': len(g.search_index())},
        'sources': content.sources,
        'routes': [{'url': g.BASE + p['path'], 'title': p['title'], 'description': p['desc']} for p in pages],
        'assets': {name: {'url': urls[name], 'bytes': len(data)} for name, data in files.items()},
        'actions': [{'chapter': c['id'], 'position': i + 1, 'id': a['id'], 'text': a['text'], 'effort': a['effort']}
                    for c in g.chapters for i, a in enumerate(g.built[c['id']]['actions'])],
        'registry': {'added': content.added, 'retired': content.retired},
        'checks': checks, 'written': written, 'unchanged': unchanged,
    }
    if not args.check:
        # Internal report, next to the output folder and never inside it, so it is not published with the site.
        # A build-report.json left inside the folder by an older version is not removed; release.py does not export it.
        report_path = out_dir.parent / (out_dir.name + '.build-report.json')
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    verb = 'Would write' if args.check else 'Wrote'
    print('%s %d files, %d already up to date -> %s (edition: %s)' % (verb, len(written), len(unchanged), out_dir, Path(args.edition).resolve().relative_to(ROOT) if ROOT in Path(args.edition).resolve().parents else args.edition))
    print('%d pages: %d chapters in %d parts, %d other pages, %d actions, %d internal links checked'
          % (len(outputs), len(g.chapters), len(g.PARTS), len(g.pages), g.total_actions, checks['internal_links_checked']))
    for note in contrast_notes(cfg):
        print(note)
    if cfg['_overrides']:
        print('Address for this build only (not saved in %s): %s%s' % (Path(args.edition).name, cfg['site']['url'] or '(no site.url)', cfg['site']['base_path']))
    if content.added or content.retired:
        print('actions.json updated: %d added, %d retired' % (len(content.added), len(content.retired)))
    if not markdown.__version__.startswith('3.'):
        print('Note: Python-Markdown %s; the project is tested with 3.9.' % markdown.__version__)
    return out_dir, cfg


def serve(out_dir, cfg, port):
    import http.server
    import functools
    base = cfg['site']['base_path']
    root = out_dir
    if base != '/':
        # Mirror the base path so that absolute links work: serve out_dir at /<base>/.
        root = Path(str(out_dir) + '-serve')
        root.mkdir(exist_ok=True)
        target = root / base.strip('/')
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.symlink_to(out_dir, target_is_directory=True)
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root))
    httpd = http.server.ThreadingHTTPServer(('127.0.0.1', port), handler)
    print('Preview on http://127.0.0.1:%d%s (this computer only). Press Ctrl+C to stop.' % (port, base))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nStopped.')


def main(argv=None):
    p = argparse.ArgumentParser(description='Build an edition of A Guide to Autonomy.')
    p.add_argument('--edition', default=str(ROOT / 'edition.json'), help='edition file (default: edition.json)')
    p.add_argument('--out', default=str(ROOT / 'dist'), help='output folder (default: dist/)')
    p.add_argument('--check', action='store_true', help='render and check everything, write nothing (combines with --edition and --out)')
    p.add_argument('--update-actions', action='store_true', help='give IDs to new checklist actions, retire removed ones')
    p.add_argument('--serve', action='store_true', help='after building, preview on http://127.0.0.1:PORT/')
    p.add_argument('--port', type=int, default=8000, help='port of the preview (default: 8000)')
    p.add_argument('--site-url', default=None, help='use this address instead of site.url, for this build only (https://example.org, no folder)')
    p.add_argument('--base-path', default=None, help='use this folder instead of site.base_path, for this build only (/ or /guide/)')
    args = p.parse_args(argv)
    try:
        out_dir, cfg = run(args)
    except BuildError as e:
        sys.exit('Build stopped, nothing was written.\n' + str(e))
    if args.serve and not args.check:
        serve(out_dir, cfg, args.port)


if __name__ == '__main__':
    main()
