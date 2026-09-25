"""Verify local official errata and optionally compare them with a fetched Git ref.

Run from the repository root:
    python tools/verify-official-errata.py
    python tools/verify-official-errata.py --upstream upstream/main --details

Read-only: never fetches, reapplies patches, or resolves conflicts automatically.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET


def fingerprint(element, attributes_only=False):
    if element is None:
        return None

    def node(e):
        return [e.tag.split('}')[-1], sorted(e.attrib.items()),
                ' '.join((e.text or '').split()), [node(c) for c in e]]

    value = sorted(element.attrib.items()) if attributes_only else node(element)
    return hashlib.sha256(json.dumps(value, ensure_ascii=False,
                                    separators=(',', ':')).encode('utf-8')).hexdigest()


def index(xml):
    root = ET.fromstring(xml)
    return {e.get('id'): e for e in root.iter() if e.get('id')}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', default='docs/erratas/2026-09-23.json')
    parser.add_argument('--upstream', help='Fetched Git ref to compare, e.g. upstream/main')
    parser.add_argument('--details', action='store_true')
    args = parser.parse_args(argv)
    manifest = json.loads(Path(args.manifest).read_text(encoding='utf-8'))
    local, remote = {}, {}
    failures = []
    status = Counter()
    for record in manifest['changes']:
        file = record['file']
        if file not in local:
            local[file] = index(Path(file).read_bytes())
        attrs = record.get('attributes_only', False)
        actual = fingerprint(local[file].get(record['id']), attrs)
        if actual != record['expected_sha256']:
            failures.append('%s: %s (%s)' % (file, record['label'], record['id']))
        if not args.upstream:
            continue
        if file not in remote:
            result = subprocess.run(['git', 'show', args.upstream + ':' + file],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode:
                print(result.stderr.decode('utf-8', errors='replace'), file=sys.stderr)
                return 2
            remote[file] = index(result.stdout)
        upstream_hash = fingerprint(remote[file].get(record['id']), attrs)
        if upstream_hash == record['expected_sha256']:
            state = 'coincide'
        elif upstream_hash == record['base_sha256']:
            state = 'pendiente'
        else:
            state = 'revisar'
        status[state] += 1
        if args.details:
            print('%-9s %s: %s [%s]' % (state, file, record['label'], record['id']))
    print('%d entradas locales verificadas; %d diferencias.' %
          (len(manifest['changes']), len(failures)))
    for failure in failures:
        print('REVISAR LOCAL: ' + failure)
    if args.upstream:
        print('Upstream %s: %d coinciden; %d pendientes; %d requieren revision.' %
              (args.upstream, status['coincide'], status['pendiente'], status['revisar']))
        print('Coincidir por ID y contenido no sustituye la revision de reglas ni '
              'autoriza a descartar cambios con IDs distintos.')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
