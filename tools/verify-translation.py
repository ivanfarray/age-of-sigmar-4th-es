# -*- coding: utf-8 -*-
"""Paso 3: demuestra que solo ha cambiado el texto descriptivo.

    python tools/verify-translation.py "Ogor Mawtribes.cat"

Compara "Ogor Mawtribes.cat" con "Ogor Mawtribes_es.cat" y falla (codigo de
salida 1) si algo mas ha cambiado. No es una revision "a ojo": vacia todos
los spans de texto de los dos ficheros y compara el resto byte a byte, ademas
de comprobar uno por uno todos los valores de atributo y la estructura.

Sin argumentos, verifica todos los pares *_es.cat / *_es.gst del directorio.
"""
import glob
import os
import re
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bscat  # noqa: E402

ATTR = re.compile(r'([A-Za-z_][\w.:-]*)\s*=\s*"([^"]*)"')
CRITICAL = ('id', 'name', 'typeId', 'targetId', 'type', 'field', 'entryId',
            'publicationId', 'gameSystemId', 'defaultSelectionEntryId', 'scope')


def check(source):
    translated = bscat.output_path(source)
    label = os.path.basename(translated)
    if not os.path.exists(translated):
        print('FALLO  %s: no existe (ejecuta apply-translation.py)' % label)
        return False

    original = bscat.read_source(source)
    spanish = bscat.read_source(translated)
    problems = []

    try:
        ET.parse(translated)
    except Exception as exc:
        problems.append('XML mal formado: %s' % exc)

    if bscat.strip_text(original) != bscat.strip_text(spanish):
        a, b = bscat.strip_text(original), bscat.strip_text(spanish)
        at = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]),
                  min(len(a), len(b)))
        problems.append('ha cambiado algo fuera del texto descriptivo, en el '
                        'offset %d:\n      original: %r\n      traducido: %r'
                        % (at, a[max(0, at - 70):at + 70], b[max(0, at - 70):at + 70]))

    va, vb = ATTR.findall(original), ATTR.findall(spanish)
    if va != vb:
        problems.append('los atributos no coinciden (%d vs %d)' % (len(va), len(vb)))
        for attr in CRITICAL:
            xa = [v for k, v in va if k == attr]
            xb = [v for k, v in vb if k == attr]
            if xa != xb:
                problems.append('  atributo %s alterado' % attr)

    try:
        ea = [e.tag for e in ET.parse(source).getroot().iter()]
        eb = [e.tag for e in ET.parse(translated).getroot().iter()]
        if ea != eb:
            problems.append('la estructura difiere (%d vs %d elementos)'
                            % (len(ea), len(eb)))
    except Exception:
        pass

    if problems:
        print('FALLO  %s' % label)
        for p in problems:
            print('    %s' % p)
        return False

    counts, _ = bscat.translatable(original)
    mapping = bscat.load_translations(bscat.json_path(source))
    done = sum(1 for k in counts if k in mapping)
    print('OK     %s  (%d/%d cadenas traducidas, %.1f%%; %d atributos intactos)'
          % (label, done, len(counts),
             100.0 * done / len(counts) if counts else 100.0, len(va)))
    return True


def main(argv):
    if argv:
        sources = argv
    else:
        sources = []
        for pattern in ('*_es.cat', '*_es.gst'):
            for translated in sorted(glob.glob(pattern)):
                root, ext = os.path.splitext(translated)
                candidate = root[:-3] + ext
                if os.path.exists(candidate):
                    sources.append(candidate)
        if not sources:
            print('No hay ningun fichero *_es.cat que verificar.')
            return 0

    ok = True
    for source in sources:
        if not os.path.exists(source):
            print('FALLO  no existe el fuente: %s' % source)
            ok = False
            continue
        ok = check(source) and ok
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
