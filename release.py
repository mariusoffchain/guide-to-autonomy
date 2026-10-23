#!/usr/bin/env python3
# A Guide to Autonomy, source archive and clean export of an edition.
# Copyright (C) 2026 the contributors of A Guide to Autonomy
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version. See LICENSE.
"""Source archive and clean export of one edition.

    python3 release.py --edition edition.json --out dist --dest publish
        build the edition into dist/, then copy into publish/ only the files listed in
        dist/release-manifest.json. publish/ must not exist or must be empty. Upload publish/.
    python3 release.py --out dist --dest publish --no-build
        export the last build of dist/ without building again.

build.py uses source_files() and zip_bytes() to put source/guide-to-autonomy-source.zip into
every edition. The archive is made from an explicit list of inputs, never from the whole
folder: the generator, this file, the theme, the documents listed in book.json, the explicit public docs,
the licences and notices, the chosen edition file and every asset the
configuration references. No Git data, CI workflow, internal report, built output or other
edition. Entries are sorted and carry a fixed date, so the same inputs give the same bytes.
Python standard library only.
"""

import argparse
import hashlib
import io
import json
import os
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ARCHIVE_DIR = 'guide-to-autonomy-source'
ARCHIVE_NAME = 'source/guide-to-autonomy-source.zip'
MANIFEST = 'release-manifest.json'
ZIP_DATE = (1980, 1, 1, 0, 0, 0)

REQUIRED_FILES = ['build.py', 'release.py', 'requirements.txt', 'LICENSE', 'LICENSE-CONTENT', 'NOTICE',
                  'theme/styles.css', 'theme/app.js', 'theme/recordings.js', 'theme/sw.template.js']
OPTIONAL_FILES = ['README.md', 'THIRD-PARTY.md', 'AGENTS.md', 'CLAUDE.md', 'CONTRIBUTING.md', 'CHANGELOG.md', 'edition.json',
                  'editions.json', 'examples/README.md', 'theme/fonts/README.md']
PUBLIC_SUPPORT = ['docs/CONFIGURATION.md', 'docs/CUSTOMIZING.md', 'docs/HOSTING.md',
                  'docs/TRANSLATING.md', 'docs/UPDATING.md', 'docs/RELEASING.md', 'tests/test_release.py',
                  'tests/test_kit.py', 'tests/test_progress_ux.py', 'tests/reference-ids.json', 'tests/base-edition.json',
                  'theme/fonts/jetbrainsmono-latin.woff2', 'theme/fonts/jetbrainsmono-latin-ext.woff2',
                  'theme/fonts/righteous-latin.woff2', 'theme/fonts/righteous-latin-ext.woff2',
                  'theme/fonts/OFL-JetBrainsMono.txt', 'theme/fonts/OFL-Righteous.txt']
EDITION_EXTRAS = ['custom.css', 'editions.json']

# Full licence notices of the fonts bundled in theme/fonts/, byte-identical to the official files
# (google/fonts, ofl/<family>/OFL.txt). The build refuses a notice whose bytes differ.
BUNDLED_FONT_NOTICES = {
    'jetbrainsmono': ('theme/fonts/OFL-JetBrainsMono.txt', 'b2fe5e8987594e9ffd1d2ca52a2f5d73eb8335243893c5d6254b5ad69269591d'),
    'righteous': ('theme/fonts/OFL-Righteous.txt', '1c5bc055869d5e9151ec7774082727db720ec4293c65be67f91a4bdcaeb02998'),
}
NOTICE_PREFIXES = ('ofl', 'license', 'licence', 'copying', 'notice')


class ReleaseError(Exception):
    pass


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def inside(root, path, what):
    """Path relative to root (posix string). Refuses anything outside root and any symlink on the way."""
    root = Path(root)
    p = Path(os.path.normpath(str(path if Path(path).is_absolute() else root / path)))
    try:
        rel = p.relative_to(root)
    except ValueError:
        raise ReleaseError('%s: %s is outside the repository folder. Move it inside (for example into examples/<name>/) '
                           'and build again: the source archive of an edition only takes files from the repository.' % (what, path))
    cur = root
    for part in rel.parts:
        cur = cur / part
        if cur.is_symlink():
            raise ReleaseError('%s: %s is a symbolic link. Replace it with the real file so that the source archive is complete.'
                               % (what, rel.as_posix()))
    if root.resolve() != p.resolve() and root.resolve() not in p.resolve().parents:
        raise ReleaseError('%s: %s resolves outside the repository.' % (what, rel.as_posix()))
    return rel.as_posix()


def locate(root, edition_dir, rel, what):
    """Same lookup as build.py: next to edition.json first, then the repository root."""
    for base in (edition_dir, root):
        cand = Path(os.path.normpath(str(base / rel)))
        if cand.is_file():
            return cand
    raise ReleaseError('%s: file not found: %s.' % (what, rel))


def font_notices(root, edition_dir, entry, what):
    """The licence notice files of 1 configured font file. A font without a notice stops the build."""
    root = Path(root)
    if entry.get('license'):
        return [locate(root, edition_dir, entry['license'], what + '.license')]
    font = locate(root, edition_dir, entry['file'], what)
    if font.parent == root / 'theme' / 'fonts':
        for prefix, (notice, digest) in sorted(BUNDLED_FONT_NOTICES.items()):
            if font.name.lower().startswith(prefix):
                path = root / notice
                if not path.is_file():
                    raise ReleaseError('%s: the licence notice %s is missing.' % (what, notice))
                if sha256(path.read_bytes()) != digest:
                    raise ReleaseError('%s: %s is not the official licence text of the font (SHA-256 differs).' % (what, notice))
                return [path]
    family = font.name.lower().split('-')[0].split('.')[0]
    found = sorted(p for p in font.parent.iterdir() if p.is_file() and p.name.lower().startswith(NOTICE_PREFIXES))
    matching = [p for p in found if family in p.name.lower()]
    if matching:
        return matching
    if len(found) == 1:
        return found
    raise ReleaseError('%s: %s licence notice found for %s. Put the font\'s licence file (for example OFL.txt) next to it, '
                       'or name it in "license" in the same entry of edition.json.'
                       % (what, 'more than 1 possible' if found else 'no', entry['file']))


def edition_path(path):
    """Absolute path of the edition file, with its folder resolved (the file itself may not be a link)."""
    path = Path(path).absolute()
    return path.parent.resolve() / path.name


def configured_fonts(cfg):
    return [(role, i, f) for role in ('heading', 'body') for i, f in enumerate(cfg['fonts'][role]['files'])]


def source_files(root, edition_file, cfg, exclude=()):
    """{archive path: file} of everything needed to rebuild this edition, and nothing else."""
    root = Path(root).resolve()
    edition_file = edition_path(edition_file)
    exclude = [Path(x).resolve() for x in exclude]
    files = {}

    def add(path, what, required=True):
        rel = inside(root, path, what)
        full = root / rel
        if not full.is_file():
            if required:
                raise ReleaseError('%s: %s not found.' % (what, rel))
            return
        if any(x == full.resolve() or x in full.resolve().parents for x in exclude):
            return
        files[rel] = full

    for name in REQUIRED_FILES:
        add(root / name, 'base file')
    for name in OPTIONAL_FILES:
        add(root / name, 'base file', required=False)
    for name in PUBLIC_SUPPORT:
        add(root / name, 'public support file', required=False)
    content = root / cfg['language']['content_dir']
    inside(root, content, 'language.content_dir')
    for name in ('book.json', 'strings.json', 'actions.json', 'links.json'):
        add(content / name, 'content metadata', required=name != 'links.json')
    book = json.loads((content / 'book.json').read_text(encoding='utf-8'))
    documents = book.get('parts', []) + book.get('chapters', [])
    documents += [book[k] for k in ('introduction', 'glossary') if book.get(k)]
    for document in documents:
        add(content / document['file'], 'book document')

    edition_dir = edition_file.parent
    add(edition_file, 'edition file')
    for name in EDITION_EXTRAS:
        if (edition_dir / name).exists():
            add(edition_dir / name, 'edition folder')
    # Only configured assets are build inputs. Unreferenced files beside them remain private.

    logo = cfg['edition']['logo']
    for key, value in (('edition.logo.file', logo.get('file')), ('edition.logo.cover_file', logo.get('cover_file')),
                       ('site.favicon', cfg['site']['favicon']), ('site.og_image', cfg['site']['og_image'])):
        if value:
            add(locate(root, edition_dir, value, key), key)
    for role, i, f in configured_fonts(cfg):
        what = 'fonts.%s.files[%d]' % (role, i)
        add(locate(root, edition_dir, f['file'], what), what)
        for notice in font_notices(root, edition_dir, f, what):
            add(notice, what + ' licence notice')
    for i, it in enumerate(cfg['recordings']['items'] if cfg['recordings'].get('enabled') else []):
        if it.get('poster'):
            what = 'recordings.items[%d].poster' % i
            add(locate(root, edition_dir, it['poster'], what), what)
    if cfg['directory']['enabled']:
        d = edition_dir / cfg['directory']['file']
        add(d if d.is_file() else root / cfg['directory']['file'], 'directory.file')
    return dict(sorted(files.items()))


def source_readme(cfg, edition_rel, files):
    base = cfg['site']['base_path']
    over = cfg.get('_overrides') or {}
    flags = ''.join(' --%s %s' % (k.replace('_', '-'), v or '""') for k, v in sorted(over.items()))
    lines = [
        'A Guide to Autonomy: source of the edition "%s"' % cfg['edition']['name'],
        '',
        'This archive holds the files used to build this edition: the generator (build.py), the',
        'packager (release.py), the theme, the text, the configuration and assets of the edition,',
        'the licences and the notices. It was made by release.py from an explicit list of inputs.',
        'It contains no Git history, CI workflow, internal report or built website.',
        '',
        'Original work: A Guide to Autonomy, written for PROOF, an initiative of Cypher Baltics.',
        'Licences: text CC BY-SA 4.0 (LICENSE-CONTENT), code AGPL-3.0-or-later (LICENSE).',
        'See NOTICE and THIRD-PARTY.md. Font notices are in theme/fonts/ or next to the fonts.',
        '',
        'Rebuild the edition (Python 3.9 or newer):',
        '',
        '  python3 -m pip install -r requirements.txt',
        '  python3 build.py --edition %s --out dist%s' % (edition_rel, flags),
        '  python3 build.py --edition %s --out dist%s --serve' % (edition_rel, flags),
        '',
    ]
    if over:
        lines += [
            'These pages were built with an address given on the command line instead of the',
            'one in the edition file (%s): %s%s.' % (edition_rel, cfg['site']['url'] or 'no site.url', base),
            '',
        ]
    lines += [
        'The preview opens on http://127.0.0.1:8000%s. To get a folder to upload, with only the' % base,
        'files of this build:',
        '',
        '  python3 release.py --edition %s --out dist --dest publish%s' % (edition_rel, flags),
        '',
        'Files (SHA-256):',
        '',
    ]
    lines += ['%s  %s' % (sha256(files[rel].read_bytes()), rel) for rel in sorted(files)]
    return ('\n'.join(lines) + '\n').encode('utf-8')


def zip_bytes(entries):
    """Deterministic ZIP: sorted names under 1 folder, fixed date and modes, no absolute path."""
    buf = io.BytesIO()
    # Stored, not compressed: the bytes then depend only on the inputs, not on the zlib version of the machine.
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_STORED) as z:
        for name in sorted(entries):
            if name.startswith('/') or '..' in name.split('/') or '\\' in name:
                raise ReleaseError('Refusing the archive path %r.' % name)
            info = zipfile.ZipInfo(ARCHIVE_DIR + '/' + name, ZIP_DATE)
            info.compress_type = zipfile.ZIP_STORED
            info.create_system = 3
            info.external_attr = (0o100755 if name.endswith('.py') else 0o100644) << 16
            z.writestr(info, entries[name])
    return buf.getvalue()


def source_archive(root, edition_file, cfg, exclude=()):
    """Bytes of the source ZIP of the edition."""
    root = Path(root).resolve()
    files = source_files(root, edition_file, cfg, exclude)
    edition_rel = inside(root, edition_path(edition_file), 'edition file')
    entries = {rel: path.read_bytes() for rel, path in files.items()}
    entries['SOURCE-README.txt'] = source_readme(cfg, edition_rel, files)
    return zip_bytes(entries)


# ---------- clean export of a build ----------

def safe_rel(rel):
    parts = rel.split('/')
    return bool(rel) and not rel.startswith('/') and '\\' not in rel and '..' not in parts and '' not in parts and ':' not in parts[0]


def export(out_dir, dest):
    """Copy into dest exactly the files listed in out_dir/release-manifest.json, after checking their hashes."""
    out_dir, dest = Path(out_dir).resolve(), Path(dest).absolute()
    if dest.is_symlink():
        raise ReleaseError('Refusing to export into a symbolic link: %s' % dest)
    dest = dest.resolve()
    if dest == out_dir or out_dir in dest.parents or dest in out_dir.parents or dest == ROOT or dest in ROOT.parents:
        raise ReleaseError('Choose a destination outside the build folder and not the repository itself: %s' % dest)
    if dest.exists() and (not dest.is_dir() or any(dest.iterdir())):
        raise ReleaseError('The destination %s already exists and is not empty. Nothing was copied or removed. '
                           'Choose a new folder (or empty this one yourself).' % dest)
    mpath = out_dir / MANIFEST
    if not mpath.is_file():
        raise ReleaseError('No %s in %s. Build the edition first with build.py.' % (MANIFEST, out_dir))
    manifest = json.loads(mpath.read_text(encoding='utf-8'))
    copies = []
    for e in manifest['files']:
        rel = e['path']
        if not safe_rel(rel) or rel == MANIFEST:
            raise ReleaseError('%s: unexpected path %r.' % (MANIFEST, rel))
        inside(out_dir, out_dir / rel, MANIFEST)
        src = out_dir / rel
        if not src.is_file():
            raise ReleaseError('%s lists %s, which is missing. Build again.' % (MANIFEST, rel))
        data = src.read_bytes()
        if sha256(data) != e['sha256']:
            raise ReleaseError('%s changed since the build (SHA-256 differs). Build again.' % rel)
        copies.append((rel, data))
    listed = {rel for rel, _ in copies} | {MANIFEST}
    left = sorted(p.relative_to(out_dir).as_posix() for p in out_dir.rglob('*')
                  if p.is_file() and p.relative_to(out_dir).as_posix() not in listed)
    for rel, data in copies + [(MANIFEST, mpath.read_bytes())]:
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    return [rel for rel, _ in copies] + [MANIFEST], left


def main(argv=None):
    p = argparse.ArgumentParser(description='Build an edition, then export only the files of that build into a new folder.')
    p.add_argument('--edition', default='edition.json', help='edition file (default: edition.json)')
    p.add_argument('--out', default='dist', help='build folder (default: dist/)')
    p.add_argument('--dest', required=True, help='new or empty folder that receives the files to upload')
    p.add_argument('--no-build', action='store_true', help='export the last build of --out without building again')
    p.add_argument('--site-url', default=None, help='passed to build.py: address of the site for this build only')
    p.add_argument('--base-path', default=None, help='passed to build.py: folder of the site for this build only')
    args = p.parse_args(argv)
    if not args.no_build:
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        import build
        try:
            build.run(argparse.Namespace(edition=args.edition, out=args.out, check=False, update_actions=False,
                                         site_url=args.site_url, base_path=args.base_path))
        except build.BuildError as e:
            sys.exit('Build stopped, nothing was exported.\n' + str(e))
    try:
        copied, left = export(args.out, args.dest)
    except (ReleaseError, ValueError, KeyError) as e:
        sys.exit('Export stopped.\n' + str(e))
    print('Exported %d files -> %s. Upload this folder, nothing else.' % (len(copied), Path(args.dest).resolve()))
    if left:
        print('Left out %d file(s) of %s that are not part of this build (older builds, reports): %s%s'
              % (len(left), args.out, ', '.join(left[:8]), ' …' if len(left) > 8 else ''))


if __name__ == '__main__':
    main()
