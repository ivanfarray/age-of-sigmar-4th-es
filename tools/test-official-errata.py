"""Regression checks for the official 23 September 2026 update.

Expected values come from Battle Profiles and Rules Updates, September 2026.
These checks inspect the catalogue; they do not emulate a roster-building client.
"""
import functools
import unittest
import xml.etree.ElementTree as ET


@functools.lru_cache(None)
def root(file):
    return ET.parse(file).getroot()


def by_id(file, id):
    return next(e for e in root(file).iter() if e.get('id') == id)


def named(file, name, path='{*}entryLinks/{*}entryLink'):
    return next(e for e in root(file).findall(path) if e.get('name') == name)


def values(profile):
    return {e.get('name'): e.text for e in profile.findall('{*}characteristics/{*}characteristic')}


class OfficialErrataTests(unittest.TestCase):
    def test_ogor_points_and_paid_formation(self):
        expected = {'Redd the Maw, High Slaughtermaster': 420,
                    'Morga the Mighty, Overtyrant': 420, 'Gluttons': 210,
                    'Hunters with Sabrefangs': 170, 'Maulbeast Raiders': 210}
        for name, cost in expected.items():
            with self.subTest(name=name):
                self.assertEqual(float(named('Ogor Mawtribes.cat', name)
                                       .find('{*}costs/{*}cost').get('value')), cost)
        formation = by_id('Ogor Mawtribes.cat', 'ae26-07a1-9b69-4549')
        self.assertEqual(formation.find('{*}costs/{*}cost').get('value'), '10')

    def test_single_model_stormdrakes_keep_separate_cost(self):
        file = 'Stormcast Eternals.cat'
        self.assertEqual(by_id(file, '33e3-dae2-fe70-22a7').find('{*}costs/{*}cost').get('value'), '290')
        self.assertEqual(by_id(file, '2ec3-5b38-8e3c-c9b4').find('{*}costs/{*}cost').get('value'), '150')

    def test_askurgan_reinforcement_has_sixteen_models(self):
        file = 'Soulblight Gravelords - Library.cat'
        unit = named(file, 'Askurgan Trueblades', '{*}sharedSelectionEntries/{*}selectionEntry')
        base, reinforced = 0, 0
        for model in unit.findall('{*}selectionEntries/{*}selectionEntry'):
            if model.get('type') != 'model':
                continue
            constraint = next(c for c in model.findall('{*}constraints/{*}constraint')
                              if c.get('type') == 'max' and c.get('scope') == 'parent')
            n = int(constraint.get('value'))
            modifiers = [m for m in model.findall('{*}modifiers/{*}modifier')
                         if m.get('field') == constraint.get('id')]
            self.assertEqual(len(modifiers), 1)
            self.assertEqual(modifiers[0].find('{*}repeats/{*}repeat').get('childId'),
                             '1b37-82b8-c062-eb82')
            base += n
            reinforced += n + int(modifiers[0].get('value'))
        self.assertEqual((base, reinforced), (8, 16))

    def test_reinforcement_does_not_duplicate_pyregheist_champion(self):
        champion = by_id('Nighthaunt - Library.cat', '1638-5e5b-b784-c160')
        cap = next(c for c in champion.findall('{*}constraints/{*}constraint')
                   if c.get('scope') == '5f08-4648-c0e8-e7d9')
        self.assertEqual(cap.get('value'), '1')
        self.assertFalse(champion.findall('{*}modifiers/{*}modifier'))

    def test_new_support_hero_requires_regimental_permission(self):
        butcher = named('Ogor Mawtribes.cat', 'Butcher')
        membership = [m for m in butcher.findall('{*}modifierGroups/{*}modifierGroup/{*}modifiers/{*}modifier')
                      if m.get('value') == 'bf4e-4b1b-7055-2ec8' and not m.get('affects')]
        self.assertEqual(len(membership), 1)
        hidden = next(m for m in butcher.findall('{*}modifiers/{*}modifier')
                      if m.get('field') == 'hidden')
        self.assertTrue(any(c.get('childId') == '8f4b-1fa6-3128-8405' and
                            c.get('type') == 'notInstanceOf' for c in hidden.iter()))

    def test_seraphon_support_choices_share_one_limit(self):
        # BSData 4ac427f: Favoured Spawning closes with a joining Starpriest or
        # Starseer under Kroak or a Slann, and the Starseer has its own 0-1 cap.
        file = 'Seraphon.cat'
        spawning = by_id(file, 'd252-534-cc7e-8040')
        blockers = {c.get('childId') for g in spawning.iter()
                    if g.tag.endswith('localConditionGroup') and g.get('type') == 'lessThan'
                    for c in g.iter() if c.tag.endswith('condition')}
        self.assertTrue({'4a6d-57cc-4f15-dd3a', '8b73-3877-1870-fce1'} <= blockers)
        starseer = by_id(file, '8b73-3877-1870-fce1')
        cap = starseer.find('{*}constraints/{*}constraint')
        self.assertEqual((cap.get('type'), cap.get('value')), ('max', '-1'))
        opened = next(m for m in starseer.findall('{*}modifiers/{*}modifier')
                      if m.get('field') == cap.get('id'))
        self.assertEqual(opened.get('value'), '1')
        leaders = {c.get('childId') for c in opened.iter() if c.tag.endswith('condition')}
        self.assertTrue({'b137-2ba4-aec4-ee33', '74bb-6987-d78-6035'} <= leaders)

    def test_aqshy_aggradon_still_joins_as_favoured_spawning(self):
        # Battle Profiles, September 2026, p. 18 keeps the note; BSData drops it.
        hero = by_id('Seraphon.cat', 'f43e-a514-0668-d66a')
        joins = [m for m in hero.findall('{*}modifierGroups/{*}modifierGroup/{*}modifiers/{*}modifier')
                 if m.get('value') == 'd252-534-cc7e-8040' and not m.get('affects')]
        self.assertEqual(len(joins), 1)

    def test_oracular_visions_changes_only_the_foot_hero(self):
        file = 'Slaves to Darkness - Library.cat'
        updated = values(by_id(file, '2f2c-ab67-f9b5-e2fe'))
        self.assertNotIn('roll a dice', updated['Declare'])
        self.assertIn('successfully cast a spell', updated['Effect'])
        self.assertIn('Ward (5+)', updated['Effect'])
        self.assertIn('Ward (6+)', updated['Effect'])
        self.assertIn('On a 3+', values(by_id(file, 'dc61-d4a6-5995-14aa'))['Effect'])

    def test_aqshy_gatebreaker_uses_new_profile(self):
        file = 'Sons of Behemat - Library.cat'
        unit = by_id(file, '87c2-9b68-f753-4b5c')
        stats = values(by_id(file, 'eedb-8155-f730-95f8'))
        self.assertEqual((stats['Health'], stats['Control']), ('25', '10'))
        weapons = {e.get('name'): values(e) for e in unit.iter()
                   if e.get('typeName') in ['Melee Weapon', 'Ranged Weapon']}
        self.assertEqual(set(weapons), {'Hurled Boulder', 'Fortcrusha Flail: Calamitous Sweep',
                                       'Fortcrusha Flail: Crushing Blow', 'Almighty Stomp'})
        self.assertEqual(weapons['Fortcrusha Flail: Calamitous Sweep']['Atk'], '16')
        self.assertEqual(weapons['Fortcrusha Flail: Crushing Blow']['Atk'], '6')
        self.assertEqual(weapons['Almighty Stomp']['Atk'], '3')
        self.assertEqual(weapons['Hurled Boulder']['Rnd'], '2')
        self.assertIn('BIG', [c.get('name') for c in unit.findall('{*}categoryLinks/{*}categoryLink')])
        self.assertEqual(values(by_id(file, 'cc15-3916-c7f2-cb9a'))['Timing'],
                         'Once Per Battle (Army), Your Hero Phase')
        self.assertFalse(unit.findall('{*}infoLinks/{*}infoLink'))


    def test_knight_zephyros_is_legends(self):
        # Moved to Warhammer Legends on 1 June 2025; BSData issue #1075 was
        # closed without the categoryLink ever being added.
        unit = by_id('Stormcast Eternals - Library.cat', 'f0d9-5cb2-345b-565e')
        self.assertIn('Legends', [c.get('name') for c in unit.findall('{*}categoryLinks/{*}categoryLink')])


if __name__ == '__main__':
    unittest.main()
