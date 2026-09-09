"""Comprueba nombres visibles de unidades, habilidades, menus y catalogos.

Ejecutar desde la raiz: python tools/verify-name-coverage.py
No modifica datos. Detecta nombres nuevos tras actualizar los originales.
"""
from pathlib import Path
import xml.etree.ElementTree as ET
import bscat

PROFILE_TYPES = {
    'Unit', 'Melee Weapon', 'Ranged Weapon', 'Manifestation',
    'Ability (Activated)', 'Ability (Passive)', 'Ability (Command)',
    'Ability (Spell)', 'Ability (Prayer)', 'Ability (Blood Tithe)',
    'Ability (Fate)', 'Battle Tactic Card',
}
MENU_NAME_TAGS = {
    'catalogue', 'catalogueLink', 'gameSystem', 'forceEntry', 'forceEntryLink',
    'selectionEntry', 'selectionEntryGroup', 'entryLink', 'infoLink',
}


def tag(element):
    return element.tag.rsplit('}', 1)[-1]


def required_names():
    trees = [(path, ET.parse(path).getroot())
             for ext in ('cat', 'gst') for path in sorted(Path('.').glob('*.' + ext))
             if not path.stem.endswith('_es')]
    profile_ids = {e.get('id') for _, root in trees for e in root.iter()
                   if (tag(e) == 'profile' and e.get('typeName') in PROFILE_TYPES)
                   or tag(e) == 'rule'}
    names, targets = {}, set(profile_ids)

    def record(name, source):
        if name:
            names.setdefault(name, set()).add(str(source))

    for source, root in trees:
        for e in root.iter():
            kind = tag(e)
            is_profile = (kind == 'profile' and e.get('typeName') in PROFILE_TYPES) or kind == 'rule'
            is_entry = kind == 'selectionEntry' and (
                e.get('type') in ('unit', 'model') or
                any(q.get('typeName') in PROFILE_TYPES for c in e
                    if tag(c) == 'profiles' for q in c) or
                any(tag(q) == 'rule' for c in e if tag(c) == 'rules' for q in c) or
                any(q.get('targetId') in profile_ids for c in e
                    if tag(c) == 'infoLinks' for q in c))
            if is_profile or is_entry or kind in MENU_NAME_TAGS:
                record(e.get('name'), source)
                targets.add(e.get('id'))
            if kind == 'modifier' and e.get('field') == 'name':
                record(e.get('value'), source)
    for source, root in trees:
        for e in root.iter():
            if tag(e) in ('entryLink', 'infoLink') and e.get('targetId') in targets:
                record(e.get('name'), source)
    return names


def main():
    required = required_names()
    names = bscat.load_names()
    missing = sorted(set(required) - set(names))
    for name in missing:
        print('PENDIENTE %r: %s' % (name, ', '.join(sorted(required[name]))))
    changed = sum(names.get(k, k) != k for k in required)
    print('%d nombres requeridos; %d con equivalencia; %d conservados; %d pendientes'
          % (len(required), changed, len(required) - changed - len(missing), len(missing)))
    return int(bool(missing))


if __name__ == '__main__':
    raise SystemExit(main())
