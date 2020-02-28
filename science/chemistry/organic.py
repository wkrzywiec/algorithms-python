import unittest
import re

def is_alkane(formula):
    if (__is_hydrocarbon(formula)):
        carbons = __get_carbons(formula)
        hydrogens = __get_hydrogens(formula)
        if 2 * carbons + 2 == hydrogens:
            return True
        return False
    return False

def carbon_content(formula):
    weight = {'H': 1, 'C': 12, 'O': 16}
    carbons = __get_carbons(formula)
    hydrogens = __get_hydrogens(formula)
    oxygens = 0
    if not (re.search('O', formula) is None):
        oxygens = __get_oxygens(formula)
    return float(format(100.0 * carbons * weight.get('C') / (carbons * weight.get('C') + hydrogens * weight.get('H') + oxygens * weight.get('O')), '.1f'))

def __is_hydrocarbon(formula):
    pattern = 'C\\d*H\\d+'
    if re.match(pattern, formula):
        carbons_match = re.match('C\\d*', formula)
        hydrogens_match = re.search('(H\\d+)$', formula)
        if not (carbons_match is None) and not (hydrogens_match is None):
            return True
        return False
    return False

def __get_carbons(formula):
    return int(re.match('C\\d*', formula).group()[1:]) if re.match('C\\d+', formula) else 1

def __get_hydrogens(formula):
    return int(re.search('(H\\d+)', formula).group()[1:])

def __get_oxygens(formula):
    return int(re.search('(O\\d+)', formula).group()[1:]) if re.match('O\\d+', formula) else 1

class OrganicTest(unittest.TestCase):

    def test_is_not_alkane(self):
        self.assertFalse(is_alkane('SFDver0'))
        self.assertFalse(is_alkane('CH'))
        self.assertFalse(is_alkane('C2H'))
        self.assertFalse(is_alkane('C2H2'))
        self.assertFalse(is_alkane('CH4O'))

    def test_is_alkane(self):
        self.assertTrue(is_alkane('CH4'))
        self.assertTrue(is_alkane('C2H6'))
        self.assertTrue(is_alkane('C5H12'))
        self.assertTrue(is_alkane('C8H18'))
        self.assertTrue(is_alkane('C10H22'))

    def test_carbon_content(self):
        self.assertEqual(carbon_content('C2H6'), 80.0)
        self.assertEqual(carbon_content('C2H6O'), 52.2)


if __name__ == '__main__':
    unittest.main()