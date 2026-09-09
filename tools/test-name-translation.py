import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
import bscat


def module(name, file):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).parent / file)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


apply = module('apply_translation', 'apply-translation.py')
verify = module('verify_translation', 'verify-translation.py')
coverage = module('name_coverage', 'verify-name-coverage.py')


class NameTranslationTests(unittest.TestCase):
    def test_coverage_includes_abilities_rules_and_cross_file_aliases(self):
        old_cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as directory:
            try:
                os.chdir(directory)
                Path('Library.cat').write_text('<catalogue><profile id="p" name="Spell" typeName="Ability (Spell)"/><rule id="r" name="Swift"/><selectionEntry id="e" name="Trait"><infoLinks><infoLink targetId="p" name="Spell alias"/></infoLinks></selectionEntry></catalogue>', encoding='utf-8')
                Path('Army.cat').write_text('<catalogue><entryLink targetId="e" name="Trait alias"/><infoLink targetId="r" name="Rule alias"/></catalogue>', encoding='utf-8')
                Path('Army_es.cat').write_text('<catalogue><rule name="Ignored translated name"/></catalogue>', encoding='utf-8')
                self.assertEqual(set(coverage.required_names()), {'Spell', 'Swift', 'Trait', 'Spell alias', 'Trait alias', 'Rule alias'})
            finally:
                os.chdir(old_cwd)

    def test_only_display_names_change(self):
        xml = '<selectionEntry id="Sword" name="Sword" targetId="Sword"><profile name="Sword" typeId="Sword"/><characteristic name="Sword">Sword</characteristic><constraint field="Sword"/></selectionEntry>'
        result = bscat.localize_names(xml, {'Sword': 'Espada'})
        self.assertEqual(result, '<selectionEntry id="Sword" name="Espada" targetId="Sword"><profile name="Espada" typeId="Sword"/><characteristic name="Sword">Sword</characteristic><constraint field="Sword"/></selectionEntry>')

    def test_attribute_entities_and_single_quotes(self):
        result = bscat.localize_names("<entryLink name='Hunter &amp; Wolf' targetId='x'/>", {'Hunter & Wolf': 'Cazador "Lobo"'})
        self.assertEqual(result, "<entryLink name='Cazador &quot;Lobo&quot;' targetId='x'/>")

    def test_ability_rules_and_links_keep_technical_attributes(self):
        xml = '<rule id="Swift" name="Swift"><description>Swift</description></rule><infoLink name="Swift" targetId="Swift" type="rule"/><profile name="Swift" typeName="Ability (Passive)"/><characteristic name="Swift"/>'
        expected = '<rule id="Swift" name="Veloz"><description>Swift</description></rule><infoLink name="Veloz" targetId="Swift" type="rule"/><profile name="Veloz" typeName="Ability (Passive)"/><characteristic name="Swift"/>'
        self.assertEqual(bscat.localize_names(xml, {'Swift': 'Veloz'}), expected)

    def test_conditional_display_names_preserve_rules(self):
        xml = '<modifier type="set" field="name" value="Guard (1 model)"/><modifier type="increment" field="attacks" value="Guard (1 model)"/>'
        expected = '<modifier type="set" field="name" value="Guardia (1 miniatura)"/><modifier type="increment" field="attacks" value="Guard (1 model)"/>'
        self.assertEqual(bscat.localize_names(xml, {'Guard (1 model)': 'Guardia (1 miniatura)'}), expected)

    def test_references_use_longest_name_without_cascading(self):
        translate = bscat.reference_translator({'Hunter': 'Cazador', 'Ice Hunter': 'Hunter', 'Blade': 'Espada'})
        self.assertEqual(translate('**Ice\nHunter** and Hunter, Hunters, Blades, Blade.'), '**Hunter** and Cazador, Hunters, Blades, Espada.')

    def test_verifier_rejects_id_name_and_text_corruption(self):
        old_cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as directory:
            try:
                os.chdir(directory)
                Path('translations/names').mkdir(parents=True)
                Path('translations/names/test.json').write_text(json.dumps({'Sword': 'Espada'}), encoding='utf-8')
                Path('translations/Test.es.json').write_text(json.dumps({'Use Sword.': 'Usa Sword.'}), encoding='utf-8')
                Path('Test.cat').write_text('<catalogue><selectionEntry id="a" name="Sword"><description>Use Sword.</description></selectionEntry></catalogue>', encoding='utf-8')
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(apply.main(['Test.cat']), 0)
                    self.assertTrue(verify.check('Test.cat'))
                    valid = Path('Test_es.cat').read_text(encoding='utf-8')
                    self.assertIn('Usa Espada.', valid)
                    for before, after in [('id="a"', 'id="b"'), ('name="Espada"', 'name="Otra"'), ('Usa Espada.', 'Texto incorrecto.')]:
                        Path('Test_es.cat').write_text(valid.replace(before, after), encoding='utf-8')
                        self.assertFalse(verify.check('Test.cat'))
            finally:
                os.chdir(old_cwd)


if __name__ == '__main__':
    unittest.main()
