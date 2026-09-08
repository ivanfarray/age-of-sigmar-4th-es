# -*- coding: utf-8 -*-
"""Paso 2: genera el fichero traducido.

    python tools/apply-translation.py "Ogor Mawtribes.cat"

Lee translations/Ogor Mawtribes.es.json y escribe "Ogor Mawtribes_es.cat".

El fichero de salida es un artefacto generado: no se edita a mano nunca. Si
algo esta mal traducido, se corrige el JSON y se vuelve a ejecutar.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bscat  # noqa: E402


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 2
    source = argv[0]
    if not os.path.exists(source):
        print('No existe: %s' % source)
        return 1

    mapping = bscat.load_translations(bscat.json_path(source))
    names = bscat.load_names()
    translate_references = bscat.reference_translator(names)
    xml = bscat.read_source(source)
    counts, _ = bscat.translatable(xml)
    if not mapping and counts:
        print('No hay traducciones en %s. Ejecuta primero extract-text.py y '
              'rellena el JSON.' % bscat.json_path(source))
        return 1
    eol = bscat.eol_of(xml)
    used = set()

    def replace(match):
        text = bscat.decode(match.group(3))
        target = mapping.get(text)
        if target is None:
            target = text
        else:
            used.add(text)
        target = translate_references(target)
        if target == text and text not in mapping:
            return match.group(0)
        # Los saltos de linea del JSON se escriben con el mismo fin de linea
        # que use el fichero fuente.
        body = bscat.encode(target.replace('\r\n', '\n').replace('\n', eol))
        return match.group(1) + body + match.group(4)

    out = bscat.TEXT_SPAN.sub(replace, xml)
    out = bscat.localize_names(out, names)
    target_path = bscat.output_path(source)
    with open(target_path, 'w', encoding='utf-8', newline='') as handle:
        handle.write(out)

    unused = sorted(set(mapping) - used)
    total = len(counts)
    print('%s -> %s' % (source, target_path))
    print('  cadenas traducidas: %d de %d (%.1f%%)'
          % (len(used), total, 100.0 * len(used) / total if total else 100.0))
    print('  sin traducir      : %d' % (total - len(used)))
    if unused:
        print('  AVISO: %d entradas del JSON no encajan con ninguna cadena del '
              'fuente (revisa si la clave tiene un cambio de redaccion):' % len(unused))
        for key in unused[:10]:
            print('    %r' % key[:90])
    print('  Ahora: python tools/verify-translation.py "%s"' % source)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
