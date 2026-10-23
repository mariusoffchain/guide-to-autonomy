# A Guide to Autonomy, tests of the source archive, the clean export and the credits.
# Copyright (C) 2026 the contributors of A Guide to Autonomy. AGPL-3.0-or-later, see LICENSE.
"""python3 -m unittest discover tests   (needs Python-Markdown for the build tests)"""

import argparse
import io
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import release  # noqa: E402

try:
    import build  # noqa: E402
except (ImportError, SystemExit):
    build = None

RIVERSIDE = ROOT / 'examples' / 'riverside-meetup' / 'edition.json'
HARBOUR = ROOT / 'examples' / 'harbour-circle' / 'edition.json'


def config(path):
    return build.load_config(path)[0]


def run_build(edition, out):
    return build.run(argparse.Namespace(edition=str(edition), out=str(out), check=False, update_actions=False))


class Isolation(unittest.TestCase):
    def test_outside_root_refused(self):
        with tempfile.TemporaryDirectory() as t:
            with self.assertRaises(release.ReleaseError):
                release.inside(Path(t).resolve(), ROOT / 'build.py', 'test')

    def test_symlink_refused(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t).resolve()
            (root / 'real.txt').write_text('x')
            (root / 'link.txt').symlink_to(root / 'real.txt')
            with self.assertRaises(release.ReleaseError):
                release.inside(root, root / 'link.txt', 'test')

    def test_font_without_notice_fails(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t).resolve()
            (root / 'assets' / 'fonts').mkdir(parents=True)
            (root / 'assets' / 'fonts' / 'custom.woff2').write_bytes(b'font')
            with self.assertRaises(release.ReleaseError):
                release.font_notices(root, root, {'file': 'assets/fonts/custom.woff2'}, 'fonts.body.files[0]')
            (root / 'assets' / 'fonts' / 'OFL.txt').write_text('licence')
            self.assertEqual([p.name for p in release.font_notices(root, root, {'file': 'assets/fonts/custom.woff2'}, 'f')], ['OFL.txt'])

    def test_zip_is_deterministic(self):
        entries = {'b.txt': b'2', 'a/c.py': b'1'}
        one, two = release.zip_bytes(entries), release.zip_bytes(dict(reversed(list(entries.items()))))
        self.assertEqual(one, two)
        infos = zipfile.ZipFile(io.BytesIO(one)).infolist()
        self.assertEqual([i.filename for i in infos], [release.ARCHIVE_DIR + '/a/c.py', release.ARCHIVE_DIR + '/b.txt'])
        self.assertTrue(all(i.date_time == release.ZIP_DATE for i in infos))
        with self.assertRaises(release.ReleaseError):
            release.zip_bytes({'../x': b''})


@unittest.skipIf(build is None, 'Python-Markdown is not installed')
class SourceArchive(unittest.TestCase):
    def test_root_edition_file_set(self):
        names = set(release.source_files(ROOT, ROOT / 'edition.json', config(ROOT / 'edition.json')))
        for name in ('build.py', 'release.py', 'requirements.txt', 'LICENSE', 'LICENSE-CONTENT', 'NOTICE', 'THIRD-PARTY.md',
                     'edition.json', 'theme/app.js', 'theme/styles.css', 'theme/sw.template.js', 'content/en/book.json',
                     'content/en/actions.json', 'content/en/strings.json', 'tests/test_release.py', 'docs/HOSTING.md'):
            self.assertIn(name, names)
        self.assertEqual(len([n for n in names if n.startswith('content/en/') and n.endswith('.md')]), 23)
        for n in names:
            self.assertFalse(n.startswith(('tools/', '.github/', '.git', 'dist', 'publish', 'examples/riverside', 'examples/harbour')), n)
            self.assertFalse(n.endswith('build-report.json'), n)

    def test_unreferenced_private_files_are_excluded(self):
        import shutil
        with tempfile.TemporaryDirectory() as t:
            root = Path(t).resolve()
            cfg = config(ROOT / 'edition.json')
            for rel, src in release.source_files(ROOT, ROOT / 'edition.json', cfg).items():
                dst = root / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)
            import uuid
            marker = uuid.uuid4().hex
            private = ['content/en/EDITOR-PROMPT.md', 'docs/private-notes.md', 'assets/private-note.txt']
            for rel in private:
                dst = root / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(marker)
            names = release.source_files(root, root / 'edition.json', cfg)
            self.assertTrue(all(rel not in names for rel in private))
            archive = zipfile.ZipFile(io.BytesIO(release.source_archive(root, root / 'edition.json', cfg)))
            self.assertTrue(all(marker.encode() not in archive.read(n) for n in archive.namelist()))

    def test_folder_edition_keeps_assets_and_font_notice(self):
        names = set(release.source_files(ROOT, RIVERSIDE, config(RIVERSIDE)))
        for name in ('examples/riverside-meetup/edition.json', 'examples/riverside-meetup/assets/logo.svg',
                     'examples/riverside-meetup/custom.css', 'examples/riverside-meetup/editions.json',
                     'theme/fonts/jetbrainsmono-latin.woff2', 'theme/fonts/OFL-JetBrainsMono.txt'):
            self.assertIn(name, names)
        self.assertFalse(any(n.startswith('examples/harbour-circle/') for n in names))

    def test_archive_is_deterministic_and_relative(self):
        cfg = config(RIVERSIDE)
        one = release.source_archive(ROOT, RIVERSIDE, cfg)
        self.assertEqual(one, release.source_archive(ROOT, RIVERSIDE, cfg))
        z = zipfile.ZipFile(io.BytesIO(one))
        self.assertIn(release.ARCHIVE_DIR + '/SOURCE-README.txt', z.namelist())
        readme = z.read(release.ARCHIVE_DIR + '/SOURCE-README.txt').decode('utf-8')
        self.assertIn('build.py --edition examples/riverside-meetup/edition.json', readme)
        self.assertNotIn(str(ROOT), readme)

    def test_rebuild_from_archive(self):
        """The README commands rebuild the edition from the archive alone, and give back the same archive."""
        with tempfile.TemporaryDirectory() as t:
            t = Path(t).resolve()
            out = t / 'dist-riverside'
            run_build(RIVERSIDE, out)
            data = (out / release.ARCHIVE_NAME).read_bytes()
            zipfile.ZipFile(io.BytesIO(data)).extractall(t / 'x')
            src = t / 'x' / release.ARCHIVE_DIR
            subprocess.run([sys.executable, 'build.py', '--edition', 'examples/riverside-meetup/edition.json', '--out', 'dist'],
                           cwd=str(src), check=True, stdout=subprocess.DEVNULL)
            self.assertEqual((src / 'dist' / release.ARCHIVE_NAME).read_bytes(), data)
            report = json.loads((src / 'dist.build-report.json').read_text(encoding='utf-8'))
            self.assertEqual((report['counts']['chapters'], report['counts']['actions']), (18, 90))

    def test_empty_repository_and_sub_folder(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t).resolve()
            out = t / 'dist-harbour'
            run_build(HARBOUR, out)
            zipfile.ZipFile(io.BytesIO((out / release.ARCHIVE_NAME).read_bytes())).extractall(t / 'x')
            src = t / 'x' / release.ARCHIVE_DIR
            path = src / 'examples' / 'harbour-circle' / 'edition.json'
            cfg = json.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(cfg['edition']['repository'], '')
            cfg['site']['base_path'] = '/guide/'
            path.write_text(json.dumps(cfg), encoding='utf-8')
            subprocess.run([sys.executable, 'build.py', '--edition', 'examples/harbour-circle/edition.json', '--out', 'dist-harbour'],
                           cwd=str(src), check=True, stdout=subprocess.DEVNULL)
            legal = (src / 'dist-harbour' / 'legal' / 'index.html').read_text(encoding='utf-8')
            self.assertIn('href="/guide/source/guide-to-autonomy-source.zip"', legal)
            self.assertIn('href="/guide/legal/LICENSE.txt"', legal)


@unittest.skipIf(build is None, 'Python-Markdown is not installed')
class BuiltEdition(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.t = Path(cls.tmp.name).resolve()
        cls.out = cls.t / 'dist-riverside'
        run_build(RIVERSIDE, cls.out)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_report_outside_output(self):
        self.assertFalse((self.out / 'build-report.json').exists())
        self.assertTrue((self.t / 'dist-riverside.build-report.json').is_file())

    def test_legal_files_shipped(self):
        for name in ('legal/index.html', 'legal/LICENSE.txt', 'legal/LICENSE-CONTENT.txt', 'legal/NOTICE.txt',
                     'legal/THIRD-PARTY.txt', 'legal/fonts/OFL-JetBrainsMono.txt', release.ARCHIVE_NAME, release.MANIFEST):
            self.assertTrue((self.out / name).is_file(), name)
        self.assertEqual((self.out / 'legal/LICENSE.txt').read_bytes(), (ROOT / 'LICENSE').read_bytes())
        self.assertEqual((self.out / 'legal/fonts/OFL-JetBrainsMono.txt').read_bytes(),
                         (ROOT / 'theme/fonts/OFL-JetBrainsMono.txt').read_bytes())

    def test_custom_edition_credits_original(self):
        page = (self.out / 'messages' / 'index.html').read_text(encoding='utf-8')
        self.assertIn('Riverside edition', page)
        self.assertIn('Cypher Baltics', page)
        self.assertIn('https://proofconference.com/book/en/', page)
        self.assertIn('href="/guide/legal/"', page)
        legal = (self.out / 'legal' / 'index.html').read_text(encoding='utf-8')
        self.assertIn('PROOF', legal)
        self.assertIn('Riverside Bitcoin Meetup', legal)
        self.assertIn('2026-10-22', legal)

    def test_manifest_and_service_worker(self):
        text = (self.out / release.MANIFEST).read_text(encoding='utf-8')
        self.assertNotIn(str(self.t), text)
        self.assertNotIn(str(ROOT), text)
        paths = [e['path'] for e in json.loads(text)['files']]
        self.assertEqual(paths, sorted(paths))
        self.assertTrue(all(release.safe_rel(p) for p in paths))
        sw = (self.out / 'sw.js').read_text(encoding='utf-8')
        self.assertIn('/guide/legal/LICENSE.txt', sw)
        self.assertNotIn('.zip', sw)

    def test_export_exact_file_set(self):
        out = self.t / 'dist-stale'
        run_build(RIVERSIDE, out)
        (out / 'stale-old-page.html').write_text('old')
        (out / 'build-report.json').write_text('{"edition": "/home/someone/x"}')  # left by an older build, kept
        dest = self.t / 'publish'
        copied, left = release.export(out, dest)
        expected = sorted(e['path'] for e in json.loads((out / release.MANIFEST).read_text(encoding='utf-8'))['files'])
        got = sorted(p.relative_to(dest).as_posix() for p in dest.rglob('*') if p.is_file())
        self.assertEqual(got, sorted(expected + [release.MANIFEST]))
        self.assertEqual(sorted(copied), got)
        self.assertEqual(left, ['build-report.json', 'stale-old-page.html'])
        self.assertTrue((out / 'build-report.json').is_file())
        with self.assertRaises(release.ReleaseError):
            release.export(out, dest)  # not empty any more

    def test_export_refuses_changed_file(self):
        out = self.t / 'dist-changed'
        run_build(RIVERSIDE, out)
        (out / 'legal' / 'NOTICE.txt').write_text('changed')
        with self.assertRaises(release.ReleaseError):
            release.export(out, self.t / 'publish-changed')
        self.assertFalse((self.t / 'publish-changed' / 'legal').exists())


if __name__ == '__main__':
    unittest.main()
