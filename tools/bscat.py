# -*- coding: utf-8 -*-
"""Utilidades compartidas para traducir ficheros BattleScribe (.cat / .gst).

Idea central: NO se parsea y vuelve a serializar el XML. Se localizan los
rangos de bytes que contienen texto descriptivo y se sustituyen solo esos.
Todo lo demas (ids, atributos, orden de atributos, comillas, indentacion,
saltos de linea) queda intacto por construccion.

El texto descriptivo es el contenido de <description> y <characteristic>.
Los atributos NUNCA se tocan: eso deja fuera name=, id=, targetId=, typeId=
y type=, que es exactamente lo que no se debe traducir.
"""
import io
import os
import re

# El contenido de texto de estos elementos no puede contener elementos hijos
# en los datos de BSData, asi que [^<]* delimita el span de forma exacta.
TEXT_SPAN = re.compile(r'(<(description|characteristic)\b[^>]*>)([^<]*)(</\2>)')

# Cadenas que son datos, no prosa: valores de perfil, dados, tamanos de peana.
# No se ofrecen para traducir.
DATA_ONLY = re.compile(
    r'^(?:'
    r'[0-9]+(?:\.[0-9]+)?(?:mm|")?'
    r'|[0-9]+x[0-9]+mm'
    r'|[0-9]+(?:mm|") (?:Round|Oval|Square)'
    r'|[0-9]+\+'
    r'|[0-9]*D[36](?:\+[0-9]+)?'
    r'|[0-9]+D[36]'
    r'|-|N/A|\*+'
    r')$'
)

ENTITIES = {'amp': '&', 'lt': '<', 'gt': '>', 'quot': '"', 'apos': "'"}
_ENT_RE = re.compile(r'&(#x?[0-9a-fA-F]+|[a-z]+);')

TRANSLATIONS_DIR = 'translations'


def decode(text):
    """Entidades XML -> caracteres."""
    def one(m):
        ent = m.group(1)
        if ent.startswith('#'):
            base = 16 if ent[1] in 'xX' else 10
            return chr(int(ent[2:], base) if base == 16 else int(ent[1:]))
        return ENTITIES.get(ent, m.group(0))
    return _ENT_RE.sub(one, text)


def encode(text):
    """Caracteres -> entidades XML, para contenido de texto."""
    return (text.replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace("'", '&apos;'))


def read_source(path):
    """Lee el fichero sin normalizar saltos de linea."""
    return io.open(path, encoding='utf-8', newline='').read()


def eol_of(text):
    return '\r\n' if '\r\n' in text else '\n'


def iter_spans(xml):
    """Genera (texto_decodificado, match) por cada span de texto descriptivo."""
    for match in TEXT_SPAN.finditer(xml):
        text = decode(match.group(3))
        if not text.strip():
            continue
        yield text, match


def translatable(xml):
    """Cadenas distintas que merece la pena traducir, con su numero de usos."""
    counts = {}
    skipped = 0
    for text, _ in iter_spans(xml):
        if DATA_ONLY.match(text.strip()):
            skipped += 1
            continue
        counts[text] = counts.get(text, 0) + 1
    return counts, skipped


def json_path(source_path):
    """'Ogor Mawtribes.cat' -> 'translations/Ogor Mawtribes.es.json'"""
    base = os.path.basename(source_path)
    stem = re.sub(r'\.(cat|gst)$', '', base, flags=re.I)
    return os.path.join(TRANSLATIONS_DIR, stem + '.es.json')


def output_path(source_path):
    """'Ogor Mawtribes.cat' -> 'Ogor Mawtribes_es.cat'"""
    root, ext = os.path.splitext(source_path)
    return root + '_es' + ext


def strip_text(xml):
    """Vacia todos los spans de texto: lo que queda debe ser identico entre
    el fichero original y el traducido."""
    return TEXT_SPAN.sub(lambda m: m.group(1) + m.group(4), xml)


def load_translations(path):
    """Mapa {ingles: espanol} de un fichero .es.json, sin las claves de
    metadatos (las que empiezan por '_') ni los valores vacios."""
    import json
    if not os.path.exists(path):
        return {}
    raw = json.load(io.open(path, encoding='utf-8'))
    out = {}
    for key, value in raw.items():
        if key.startswith('_'):
            continue
        if not isinstance(value, str):
            raise SystemExit('%s: el valor de %r no es texto' % (path, key[:60]))
        if value.strip():
            out[key] = value
    return out
