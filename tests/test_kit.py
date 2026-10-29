# A Guide to Autonomy, tests of the reusable kit: stable ids, addresses, indexing, leaks, directory, recordings.
# Copyright (C) 2026 the contributors of A Guide to Autonomy. AGPL-3.0-or-later, see LICENSE.
"""python3 -m unittest discover tests   (needs Python-Markdown)"""

import argparse
import io
import json
import re
import shutil
import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
import sys  # noqa: E402
sys.path.insert(0, str(ROOT))
import release  # noqa: E402

try:
    import build  # noqa: E402
except (ImportError, SystemExit):
    build = None

RIVERSIDE = ROOT / 'examples' / 'riverside-meetup' / 'edition.json'
# The base edition as shipped, kept apart from edition.json, which every fork changes: these tests check the kit,
# not the choices of an edition.
BASE = ROOT / 'tests' / 'base-edition.json'


def run_build(edition, out, **kw):
    ns = dict(edition=str(edition), out=str(out), check=False, update_actions=False, site_url=None, base_path=None)
    ns.update(kw)
    return build.run(argparse.Namespace(**ns))


def clean_copy(dest):
    """A copy of the repository with only the files a fork receives (the source set of the root edition plus the
    examples), so that tests can add edition files without touching the repository."""
    cfg = build.load_config(BASE)[0]
    files = dict(release.source_files(ROOT, ROOT / 'edition.json', cfg))
    files.update({p.relative_to(ROOT).as_posix(): p for p in (ROOT / 'examples').rglob('*') if p.is_file()})
    for rel, src in files.items():
        (dest / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dest / rel)
    return dest


def build_in(copy, edition, out, *flags):
    """Runs build.py of a clean copy, as a user would. Returns (exit code, output)."""
    r = subprocess.run([sys.executable, 'build.py', '--edition', str(edition), '--out', str(out)] + list(flags),
                       cwd=str(copy), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    return r.returncode, r.stdout


def write_edition(folder, changes):
    """An edition file in folder/, from the root edition.json with changes applied (dotted keys)."""
    cfg = json.loads((BASE).read_text(encoding='utf-8'))
    for key, value in changes.items():
        node = cfg
        parts = key.split('.')
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = value
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / 'edition.json'
    path.write_text(json.dumps(cfg, ensure_ascii=False), encoding='utf-8')
    return path


def pages(out):
    return {p.relative_to(out).as_posix(): p.read_text(encoding='utf-8') for p in out.rglob('*.html')}


@unittest.skipIf(build is None, 'Python-Markdown is not installed')
class ReferenceIds(unittest.TestCase):
    """Readers' ticks are stored under these ids: a change would silently lose them."""

    def test_chapters_and_actions_unchanged(self):
        path = ROOT / 'tests' / 'reference-ids.json'
        if not path.is_file():
            self.skipTest('no tests/reference-ids.json in this edition')
        ref = json.loads(path.read_text(encoding='utf-8'))
        cfg = build.load_config(BASE)[0]
        content = build.Content(cfg)
        self.assertEqual([c['id'] for c in content.chapters], ref['chapters'])
        self.assertEqual([[c['id'], a['id']] for c in content.chapters for a in c['actions']], ref['actions'])

    def test_language_editions_keep_the_same_ids(self):
        """A language edition of the base (languages/<code>/edition.json) uses the same chapter and action ids."""
        path = ROOT / 'tests' / 'reference-ids.json'
        if not path.is_file():
            self.skipTest('no tests/reference-ids.json in this edition')
        ref = json.loads(path.read_text(encoding='utf-8'))
        for edition in sorted((ROOT / 'languages').glob('*/edition.json')):
            content = build.Content(build.load_config(edition)[0])
            self.assertEqual([c['id'] for c in content.chapters], ref['chapters'], edition)
            self.assertEqual([[c['id'], a['id']] for c in content.chapters for a in c['actions']], ref['actions'], edition)


@unittest.skipIf(build is None, 'Python-Markdown is not installed')
class Editions(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.t = Path(self.tmp.name).resolve()

    def tearDown(self):
        self.tmp.cleanup()

    def test_address_override_and_sub_path(self):
        out = self.t / 'dist'
        run_build(BASE, out, site_url='https://octocat.github.io', base_path='/guide-to-autonomy')
        html = pages(out)
        self.assertIn('<link rel="canonical" href="https://octocat.github.io/guide-to-autonomy/passwords/">', html['passwords/index.html'])
        for name, h in html.items():
            for href in re.findall(r'\s(?:href|src)="(/[^"]*)"', h):
                self.assertTrue(href.startswith('/guide-to-autonomy/'), (name, href))
        self.assertIn('https://octocat.github.io/guide-to-autonomy/sitemap.xml', (out / 'robots.txt').read_text())
        readme = zipfile.ZipFile(out / release.ARCHIVE_NAME).read(release.ARCHIVE_DIR + '/SOURCE-README.txt').decode()
        self.assertIn('--base-path /guide-to-autonomy/', readme)
        self.assertIn('--site-url https://octocat.github.io', readme)

    def test_site_url_with_folder_refused(self):
        with self.assertRaises(build.BuildError):
            build.load_config(BASE, site_url='https://octocat.github.io/repo')
        with self.assertRaises(build.BuildError):
            build.load_config(BASE, base_path='/a//b/')

    def test_draft_edition_is_not_indexed(self):
        copy = clean_copy(self.t / 'repo')
        write_edition(copy / 'draft', {'site.url': 'https://guide.example.org', 'site.indexing': False})
        out = self.t / 'dist-draft'
        code, log = build_in(copy, 'draft/edition.json', out)
        self.assertEqual(code, 0, log)
        for name, h in pages(out).items():
            self.assertIn('<meta name="robots" content="noindex">', h, name)
        self.assertEqual((out / 'robots.txt').read_text(), 'User-agent: *\nDisallow: /\n')
        self.assertFalse((out / 'sitemap.xml').exists())

    def test_customised_identity(self):
        self.copy = clean_copy(self.t / 'repo')
        write_edition(self.copy / 'mine', {
            'edition.name': 'Lakeside edition', 'edition.community': 'Lakeside Circle',
            'edition.contact': 'hello@lakeside.example.org', 'colors.scheme': 'dark', 'colors.background': '#0b1220',
            'colors.foreground': '#f4f1e8', 'layout.uppercase_headings': False, 'storage_key': 'guide-autonomy.lakeside.v1'})
        out = self.t / 'dist-mine'
        code, log = build_in(self.copy, 'mine/edition.json', out)
        self.assertEqual(code, 0, log)
        home = (out / 'index.html').read_text(encoding='utf-8')
        self.assertIn('Lakeside Circle', home)
        self.assertIn('mailto:hello@lakeside.example.org', home)
        css = next((out / 'assets').glob('guide.css')).read_text(encoding='utf-8')
        self.assertIn('--bg: #0b1220', css)
        self.assertIn('--caps: none', css)
        self.assertIn('"storageKey": "guide-autonomy.lakeside.v1"', (out / 'assets' / 'site-data.js').read_text())

    def test_progress_starts_at_zero(self):
        out = self.t / 'dist'
        run_build(BASE, out)
        for name, h in pages(out).items():
            for value in re.findall(r'data-stat="[^"]*"(?: data-ch="[^"]*")?>([^<]*)<', h):
                self.assertEqual(value, '0', name)
            self.assertNotRegex(h, r'<input[^>]*class="(?:action-cb|read-cb)"[^>]*\schecked', name)
            self.assertNotIn('--p:', h)

    def test_second_build_writes_nothing(self):
        out = self.t / 'dist'
        run_build(BASE, out)
        before = {p: p.read_bytes() for p in out.rglob('*') if p.is_file()}
        run_build(BASE, out)
        report = json.loads((self.t / 'dist.build-report.json').read_text())
        self.assertEqual(report['written'], [])
        self.assertEqual(before, {p: p.read_bytes() for p in out.rglob('*') if p.is_file()})

    def test_no_outside_resource_by_default(self):
        out = self.t / 'dist'
        run_build(BASE, out)
        for name, h in pages(out).items():
            self.assertEqual(build.external_resources(h), [], name)
            self.assertIn("frame-src 'none'", h)
            self.assertNotIn('media-src', h)
            self.assertNotIn('recordings.js', h)
        self.assertFalse((out / 'assets' / 'recordings.js').exists())

    def test_row_headers(self):
        out = self.t / 'dist'
        run_build(BASE, out)
        messages = (out / 'messages' / 'index.html').read_text(encoding='utf-8')
        self.assertIn('<th scope="row">', messages)
        total = sum(h.count('scope="row"') for h in pages(out).values())
        self.assertGreater(total, 100)


@unittest.skipIf(build is None, 'Python-Markdown is not installed')
class Guards(unittest.TestCase):
    def test_local_paths_detected(self):
        self.assertTrue(build.leaks(('see ' + '/Us' + 'ers/someone/x').encode(), 'x'))
        self.assertFalse(build.leaks(b'see /usr/share and https://example.org/Users', 'x'))

    def test_leak_stops_the_build(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t).resolve()
            copy = clean_copy(t / 'repo')
            write_edition(copy / 'leak', {'edition.changes': 'Built in ' + '/Us' + 'ers/someone/guide'})
            code, log = build_in(copy, 'leak/edition.json', t / 'out')
            self.assertNotEqual(code, 0)
            self.assertIn('Local paths would be published', log)
            self.assertFalse((t / 'out').exists())

    def test_external_resource_detection(self):
        self.assertTrue(build.external_resources('<img src="https://cdn.example.org/x.png">'))
        self.assertTrue(build.external_resources('<link rel="stylesheet" href="//fonts.example.org/a.css">'))
        self.assertFalse(build.external_resources('<link rel="canonical" href="https://example.org/">'))
        self.assertFalse(build.external_resources('<a href="https://example.org/">x</a>'))

    def test_unknown_start_chapter_is_named(self):
        cfg = build.load_config(BASE)[0]
        cfg['book']['start_chapter'] = 'intro'
        g = build.Guide(cfg, build.Content(cfg), {'editions': []})
        with self.assertRaises(build.BuildError) as e:
            g.view_home()
        self.assertIn('passwords', str(e.exception))

    def test_contrast_notes(self):
        cfg = build.load_config(BASE)[0]
        self.assertEqual(build.contrast_notes(cfg), [])
        cfg['colors']['parts'][0]['text'] = '#7dd3fc'
        self.assertEqual(len(build.contrast_notes(cfg)), 1)
        for path in sorted((ROOT / 'examples').glob('*/edition.json')):
            self.assertEqual(build.contrast_notes(build.load_config(path)[0]), [], path)

    def test_licence_texts_are_pinned(self):
        self.assertEqual(release.sha256((ROOT / 'LICENSE').read_bytes()), build.AGPL_SHA256)

    def test_directory_needs_consent_and_public_https(self):
        good = {'name': 'X', 'site': 'https://guide.example.org/', 'languages': ['en'],
                'consent': {'public_listing': True, 'date': '2026-10-23', 'reference': 'issue 1'}}
        build.check_directory({'editions': [good]}, 'editions.json')
        for bad in ({k: v for k, v in good.items() if k != 'consent'},
                    dict(good, site='http://guide.example.org/'),
                    dict(good, site='https://192.168.0.2/'),
                    dict(good, site='https://localhost/'),
                    dict(good, site='https://nas.local/')):
            with self.assertRaises(build.BuildError):
                build.check_directory({'editions': [bad]}, 'editions.json')
        with self.assertRaises(build.BuildError):
            build.check_directory({'editions': [good, dict(good, name='Y')]}, 'editions.json')
        build.check_directory(json.loads((ROOT / 'editions.json').read_text(encoding='utf-8')), 'editions.json')


@unittest.skipIf(build is None, 'Python-Markdown is not installed')
class Recordings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.t = Path(cls.tmp.name).resolve()
        cls.out = cls.t / 'dist-riverside'
        run_build(RIVERSIDE, cls.out)
        cls.home = (cls.out / 'index.html').read_text(encoding='utf-8')

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_cards_without_any_player_before_click(self):
        self.assertIn('id="recordings"', self.home)
        self.assertEqual(self.home.count('class="rp-item'), 2)
        for tag in ('<iframe', '<video', '<source'):
            self.assertNotIn(tag, self.home)
        self.assertIn('loading="lazy"', self.home)
        self.assertEqual(build.external_resources(self.home), [])

    def test_script_and_csp_only_on_the_cover(self):
        self.assertIn('recordings.js', self.home)
        self.assertIn('media-src \'self\' https://media.riverside-meetup.example.org', self.home)
        for name, h in pages(self.out).items():
            if name != 'index.html':
                self.assertNotIn('recordings.js', h, name)
                self.assertNotIn('media-src', h, name)

    def test_player_rules(self):
        js = (ROOT / 'theme' / 'recordings.js').read_text(encoding='utf-8')
        self.assertIn("'strict-origin-when-cross-origin'", js)
        self.assertIn('youtube-nocookie.com/embed/', js)
        self.assertIn("addEventListener('click'", js)

    def test_unknown_youtube_form_refused(self):
        with self.assertRaises(build.BuildError):
            build.prepare_recordings({'enabled': True, 'items': [{'title': 'T', 'video': 'https://www.youtube.com/watch?v=abc'}]})

    def test_youtube_opens_only_its_frame(self):
        cfg = {'enabled': True, 'items': [{'title': 'T', 'video': 'https://www.youtube.com/watch?v=abcdefghijk'}]}
        rec = build.prepare_recordings(cfg)
        self.assertEqual(rec, {'frame_origins': ['https://www.youtube-nocookie.com'], 'media_origins': []})

    def test_outside_poster_and_plain_http_refused(self):
        for item in ({'title': 'T', 'video': 'http://media.example.org/a.mp4'},
                     {'title': 'T', 'video': 'https://media.example.org/a.mp4', 'poster': 'https://img.example.org/a.jpg'},
                     {'title': ''}):
            with self.assertRaises(build.BuildError):
                build.prepare_recordings({'enabled': True, 'items': [item]})
        self.assertIsNone(build.prepare_recordings({'enabled': False, 'items': [{'title': 'T'}]}))

    def test_posters_in_archive_not_precached(self):
        names = zipfile.ZipFile(self.out / release.ARCHIVE_NAME).namelist()
        self.assertIn(release.ARCHIVE_DIR + '/examples/riverside-meetup/assets/talk-poster.svg', names)
        self.assertIn(release.ARCHIVE_DIR + '/theme/recordings.js', names)
        self.assertFalse(any(n.endswith(('.mp4', '.webm')) for n in names))
        sw = (self.out / 'sw.js').read_text(encoding='utf-8')
        self.assertNotIn('recordings', sw)


@unittest.skipIf(build is None, 'Python-Markdown is not installed')
class StoredArchive(unittest.TestCase):
    def test_archive_is_stored_and_clean(self):
        cfg = build.load_config(BASE)[0]
        z = zipfile.ZipFile(io.BytesIO(release.source_archive(ROOT, BASE, cfg)))
        self.assertTrue(all(i.compress_type == zipfile.ZIP_STORED for i in z.infolist()))
        for n in z.namelist():
            self.assertFalse(n.endswith('.html'), n)
            self.assertEqual(build.leaks(z.read(n), n), [], n)


if __name__ == '__main__':
    unittest.main()
