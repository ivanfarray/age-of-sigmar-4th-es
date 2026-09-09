# -*- coding: utf-8 -*-
"""Utilidades compartidas para traducir ficheros BattleScribe (.cat / .gst).

Idea central: NO se parsea y vuelve a serializar el XML. Se sustituyen rangos
de texto descriptivo y nombres autorizados por los diccionarios, incluidos
los valores de modificadores de nombre. Los atributos tecnicos permanecen intactos.

El texto descriptivo es el contenido de <description> y <characteristic>.
Solo se permiten nombres registrados de entradas, perfiles, reglas y enlaces visibles.
Los atributos id, targetId, typeId y type nunca se traducen.
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
    with io.open(path, encoding='utf-8', newline='') as handle:
        return handle.read()


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
    with io.open(path, encoding='utf-8') as handle:
        raw = json.load(handle)
    out = {}
    for key, value in raw.items():
        if key.startswith('_'):
            continue
        if not isinstance(value, str):
            raise SystemExit('%s: el valor de %r no es texto' % (path, key[:60]))
        if value.strip():
            out[key] = value
    return out


NAME_TAG = re.compile(r'<(?:selectionEntry|selectionEntryGroup|profile|entryLink|infoLink|rule)\b(?:"[^"]*"|\x27[^\x27]*\x27|[^\x27">])*>')
NAME_ATTR = re.compile(r'(\sname\s*=\s*)(["\x27])(.*?)\2')
MODIFIER_TAG = re.compile(r'<modifier\b(?:"[^"]*"|\x27[^\x27]*\x27|[^\x27">])*>')
VALUE_ATTR = re.compile(r'(\svalue\s*=\s*)(["\x27])(.*?)\2')
NAME_FIELD = re.compile(r'\sfield\s*=\s*(["\x27])name\1')


def load_names():
    """Load reviewed display-name mappings, separate from descriptive text."""
    import glob
    mapping = {}
    for path in sorted(glob.glob(os.path.join(TRANSLATIONS_DIR, 'names', '*.json'))):
        for key, value in load_translations(path).items():
            if key in mapping and mapping[key] != value:
                raise ValueError('Conflicting name translation: %r' % key)
            mapping[key] = value
    return mapping


def localize_names(xml, mapping):
    """Translate approved display names and conditional name-modifier values."""
    def tag_replace(tag):
        def attr_replace(attr):
            name = decode(attr.group(3))
            value = mapping.get(name, name)
            if value == name:
                return attr.group(0)
            value = encode(value).replace('"', '&quot;')
            return attr.group(1) + attr.group(2) + value + attr.group(2)
        return NAME_ATTR.sub(attr_replace, tag.group(0))
    result = NAME_TAG.sub(tag_replace, xml)
    def modifier_replace(tag):
        if not NAME_FIELD.search(tag.group(0)):
            return tag.group(0)
        def value_replace(attr):
            name = decode(attr.group(3))
            value = mapping.get(name, name)
            if value == name:
                return attr.group(0)
            return attr.group(1) + attr.group(2) + encode(value).replace('"', '&quot;') + attr.group(2)
        return VALUE_ATTR.sub(value_replace, tag.group(0))
    return MODIFIER_TAG.sub(modifier_replace, result)


def reference_translator(mapping):
    """Replace whole name references once, longest first, retaining whitespace."""
    changed = {k: v for k, v in mapping.items() if k != v}
    if not changed:
        return lambda text: text
    normalized = {re.sub(r'\s+', ' ', k): v for k, v in changed.items()}
    alternatives = [r'\s+'.join(re.escape(part) for part in name.split(' '))
                    for name in sorted(normalized, key=len, reverse=True)]
    pattern = re.compile(r'(?<![\w])(?:' + '|'.join(alternatives) + r')(?![\w])')
    return lambda text: pattern.sub(
        lambda match: normalized[re.sub(r'\s+', ' ', match.group(0))], text)
