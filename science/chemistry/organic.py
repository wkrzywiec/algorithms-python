import unittest
import re

def carbon_content(formula):
    """Get carbon mass concentration in the compound
    
    Arguments:
        formula {String} -- Formula of the organic compound (should include only C, H or O atoms) 
    
    Returns:
        float -- Carbon mass concentration ratio
    """
    weight = {'H': 1, 'C': 12, 'O': 16}
    carbons = __get_carbons(formula)
    hydrogens = __get_hydrogens(formula)
    oxygens = 0
    if not (re.search('O', formula) is None):
        oxygens = __get_oxygens(formula)
    return float(format(100.0 * carbons * weight.get('C') / (carbons * weight.get('C') + hydrogens * weight.get('H') + oxygens * weight.get('O')), '.1f'))

def hydrocarbon_class(formula):
    """Indicates if provided organic compound is a hydrocarbon
    
    Arguments:
        formula {String} -- Formula of the organic compound
    
    Returns:
        String -- Indicates what type of hydrocarbon is the compound (alkane/alkene/alkyne)
    """
    if __is_hydrocarbon(formula):
        hydrogens = __get_hydrogens(formula)
        carbons = __get_carbons(formula)
        if __is_alkane(carbons, hydrogens):
            return "%s is an alkane" % (formula)
        elif __is_alkene(carbons, hydrogens):
            return "%s is an alkene" % (formula)
        elif __is_alkyne(carbons, hydrogens):
            return "%s is an alkyne" % (formula)
    return "%s is not a hydrocarbon" % (formula)

def __is_hydrocarbon(formula):
    pattern = 'C\\d*H\\d+'
    if re.match(pattern, formula):
        carbons_match = re.match('C\\d*', formula)
        hydrogens_match = re.search('(H\\d+)$', formula)
        if not (carbons_match is None) and not (hydrogens_match is None):
            return True
        return False
    return False

def __is_alkane(carbons, hydrogens):
    if 2 * carbons + 2 == hydrogens:
        return True
    return False

def __is_alkene(carbons, hydrogens):
    if 2 * carbons == hydrogens:
        return True
    return False

def __is_alkyne(carbons, hydrogens):
    if 2 * carbons - 2 == hydrogens:
        return True
    return False

def __get_carbons(formula):
    return int(re.match('C\\d*', formula).group()[1:]) if re.match('C\\d+', formula) else 1

def __get_hydrogens(formula):
    return int(re.search('(H\\d+)', formula).group()[1:])

def __get_oxygens(formula):
    return int(re.search('(O\\d+)', formula).group()[1:]) if re.match('O\\d+', formula) else 1

class OrganicTest(unittest.TestCase):

    def test_carbon_content(self):
        self.assertEqual(carbon_content('C2H6'), 80.0)
        self.assertEqual(carbon_content('C2H6O'), 52.2)

    def test_hydrocarbon_class(self):
        self.assertEqual(hydrocarbon_class('DCax'), "DCax is not a hydrocarbon")
        self.assertEqual(hydrocarbon_class('CH'), "CH is not a hydrocarbon")
        self.assertEqual(hydrocarbon_class('C2H6'), "C2H6 is an alkane")
        self.assertEqual(hydrocarbon_class('C6H14'), "C6H14 is an alkane")
        self.assertEqual(hydrocarbon_class('C2H4'), "C2H4 is an alkene")
        self.assertEqual(hydrocarbon_class('C5H10'), "C5H10 is an alkene")
        self.assertEqual(hydrocarbon_class('C2H2'), "C2H2 is an alkyne")
        self.assertEqual(hydrocarbon_class('C8H14'), "C8H14 is an alkyne")


if __name__ == '__main__':
    unittest.main()