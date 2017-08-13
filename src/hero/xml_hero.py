import xml.etree.ElementTree as ET
import pickle


class XMLNotSupportedException(Exception):
    def __init__(self, rule_version):
        self.rule_version = rule_version


class SettingNotSupportedException(Exception):
    def __init__(self, rule_version):
        self.rule_version = rule_version


class Hero:
    name = ""

    def __init__(self, xml):
        self.root = ET.fromstring(xml)


class DSA4Hero(Hero):
    def __init__(self, xml):
        Hero.__init__(self, xml)
        hero = self.root.find('held')

        self.name = hero.attrib['name']

        # get all parts of the xml for easy reuse
        basis = hero.find('basis')
        attributes = hero.find('eigenschaften')
        advantages = hero.find('vt')
        disadvantages = hero.find('nt')
        talents = hero.find('talentliste')
        spells = hero.find('zauberliste')
        fighting_talents = hero.find('kampf')
        special_abilities = hero.find('sf')

        # get all information about R/K/P and body
        self.gender = basis.find('geschlecht').attrib['name']
        race = basis.find('rasse')
        self.species = race.attrib['string']
        self.height = race.find('groesse').attrib['value']
        looks = race.find('aussehen')
        self.age = looks.attrib['alter']
        self.culture = basis.find('kultur').attrib['string']
        education = list(basis.find('ausbildungen'))
        self.education = [item.attrib['string'] for item in education]
        self.free_ap = basis.find('abenteuerpunkte').attrib['value']

        # get attributes
        self.attributes = [
            (attribute.attrib['name'], attribute.attrib['value']) for attribute
            in list(attributes)]

        # get advantages and disadvantages
        self.adv = [(adv.attrib['name'], adv.attrib[
            'value'] if 'value' in adv.keys() else None) for adv in
                    list(advantages)]

        # get all special abilities
        self.special_abilities = [sf.attrib['name'] for sf in
                                  list(special_abilities)]

        # get all talents
        self.talents = [(talent.attrib['name'], talent.attrib['probe'],
                         talent.attrib['value'])
                        for talent in list(talents)]

        # get all spells
        self.spells = [(spell.attrib['name'], spell.attrib['probe'],
                        spell.attrib['value']) for
                       spell in list(spells)]

    def get_hero(self):
        return vars(self)


RULES_SUPPORTED = (
    ('DSA4', 'Das Schwarze Auge, v4.1'),
    ('SPLITTERMOND', 'Splittermond'),
    ('GENERAL', 'Generic setting'),
)


def has_charsheet(rule_version):
    if rule_version in ['DSA4']:
        return True
    elif rule_version in ['SPLITTERMOND', 'GENERAL']:
        return False
    else:
        raise SettingNotSupportedException(rule_version)


def get_hero(rule_version, xml):
    if rule_version == 'DSA4':
        return DSA4Hero(xml).get_hero()
    elif rule_version == 'SPLITTERMOND':
        raise XMLNotSupportedException(rule_version)
    elif rule_version == 'GENERAL':
        raise XMLNotSupportedException(rule_version)
    else:
        raise SettingNotSupportedException(rule_version)
