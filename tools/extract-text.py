# -*- coding: utf-8 -*-
"""Paso 1: saca a un JSON las cadenas descriptivas que hay que traducir.

    python tools/extract-text.py "Ogor Mawtribes.cat"

Escribe translations/Ogor Mawtribes.es.json con una entrada por cadena:

    "Pick a visible enemy unit to be the target.": ""

Rellena el valor en espanol y pasa al paso 2 (apply-translation.py). Un valor
vacio significa "dejar en ingles", asi que se puede traducir por tandas.

Si el JSON ya existe, se conserva lo ya traducido: solo se anaden las cadenas
nuevas y se avisa de las que han desaparecido del fichero fuente (util cuando
BSData actualiza el .cat).
"""
import collections
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bscat  # noqa: E402

NOTE = ('Traduccion al espanol del contenido descriptivo. La clave es la cadena '
        'inglesa exacta; no la edites. Valor vacio = se deja en ingles. Las claves '
        'que empiezan por "_" son metadatos. Dentro del texto, deja en ingles los '
        'nombres propios: unidades, armas, habilidades citadas entre comillas, '
        'palabras clave (**^^Hero^^**) y nombres de caracteristicas (Health, '
        'Attacks, Rend).')


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 2
    source = argv[0]
    if not os.path.exists(source):
        print('No existe: %s' % source)
        return 1

    xml = bscat.read_source(source)
    counts, skipped = bscat.translatable(xml)

    target = bscat.json_path(source)
    existing = {}
    meta = {}
    if os.path.exists(target):
        raw = json.load(io.open(target, encoding='utf-8'))
        for key, value in raw.items():
            if key.startswith('_'):
                meta[key] = value
            else:
                existing[key] = value

    gone = [k for k in existing if k not in counts]
    added = [k for k in counts if k not in existing]

    # Primero las cortas y despues las largas: las cortas son etiquetas y
    # momentos, se traducen rapido y se ven en muchos sitios.
    order = sorted(counts.items(), key=lambda kv: (len(kv[0]), kv[0]))

    out = collections.OrderedDict()
    out['_note'] = NOTE
    out['_source'] = os.path.basename(source)
    for key, value in meta.items():
        if key not in ('_note', '_source', '_unused'):
            out[key] = value
    for key, _count in order:
        out[key] = existing.get(key, '')

    # Las cadenas que ya no aparecen en el fuente no se borran: se guardan
    # aparte para no perder trabajo si BSData vuelve a cambiar la redaccion.
    kept = {k: existing[k] for k in gone if existing[k].strip()}
    if kept:
        out['_unused'] = kept

    os.makedirs(bscat.TRANSLATIONS_DIR, exist_ok=True)
    io.open(target, 'w', encoding='utf-8', newline='\n').write(
        json.dumps(out, indent=2, ensure_ascii=False) + '\n')

    done = sum(1 for k, _ in order if existing.get(k, '').strip())
    print('%s' % source)
    print('  spans de texto        : %d' % sum(counts.values()))
    print('  cadenas distintas     : %d' % len(counts))
    print('  descartadas como datos: %d' % skipped)
    print('  ya traducidas         : %d (%.1f%%)'
          % (done, 100.0 * done / len(counts) if counts else 100.0))
    print('  nuevas en esta pasada : %d' % len(added))
    if gone:
        print('  AVISO: %d cadenas del JSON ya no estan en el fuente '
              '(movidas a "_unused"):' % len(gone))
        for key in gone[:10]:
            print('    %s' % json.dumps(key[:90], ensure_ascii=False))
    print('  escrito -> %s' % target)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
