import unittest
import re

def is_alkane(formula):
    pattern = 'C\\d*H\\d+'
    if re.match(pattern, formula):
        carbons_match = re.match('C\\d*', formula)
        hydrogens_match = re.search('(H\\d+)$', formula)
        if not (carbons_match is None) and not (hydrogens_match is None):
            carbons = int(carbons_match.group()[1:]) if re.match('C\\d+', formula) else 1
            hydrogens = int(hydrogens_match.group()[1:])
            if 2 * carbons + 2 == hydrogens:
                return True
            return False
        return False
    return False

def carbon_content(formula):
    pass

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


if __name__ == '__main__':
    unittest.main()