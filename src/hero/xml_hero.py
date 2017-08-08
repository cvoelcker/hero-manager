import xml.etree.ElementTree as ET
import pickle

class Hero():
    def __init__(self, xml):
        root = ET.fromstring(xml)
        
        hero = root.find('held')

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
        self.attributes = dict((attribute.attrib['name'], attribute.attrib['value']) for attribute in list(attributes))

        # get advantages and disadvantages
        self.adv = {}
        for adv in list(advantages):
            self.adv[adv.attrib['name']] = adv.attrib['value'] if 'value' in adv.keys() else None
        
        # get all special abilities
        self.special_abilities = [sf.attrib['name'] for sf in list(special_abilities)]

        # get all talents
        self.talents = dict((talent.attrib['name'], (talent.attrib['value'], talent.attrib['probe'])) for talent in list(talents))
        
        # get all spells
        self.spells = dict((spell.attrib['name'], (spell.attrib['value'], spell.attrib['probe'])) for spell in list(spells))

    def get_hero(self):
        return vars(self)

    def get_dump(self):
        return pickle.dumps(self, -1)

    def load_dump(string):
        return pickle.loads(string)
