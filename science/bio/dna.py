import unittest

def dna(sequence):
    dna = []
    dictionary = {'A': 'T', 'T':'A', 'G': 'C', 'C': 'G'}
    for n in sequence:
        dna.append(dictionary.get(n))
    return ''.join(dna)

class TestDna(unittest.TestCase):
    
    def test_complementary_dna(self):
        self.assertEqual(dna('ATTGC'), 'TAACG')
        self.assertEqual(dna('GTAT'), 'CATA')


if __name__ == '__main__':
    unittest.main()