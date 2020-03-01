import unittest

def dna(sequence):
    """Finds complementary DNA sequence
    
    Arguments:
        sequence {String} -- A DNA sequence, e.g `ATTGC`
    
    Returns:
        [Stringe] -- Complementatry DNA sequence to given one
    """
    dna = []
    dictionary = {'A': 'T', 'T':'A', 'G': 'C', 'C': 'G'}
    for n in sequence:
        dna.append(dictionary.get(n))
    return ''.join(dna)

def dna_location(dna, sub):
    """Finds all indexes of DNA sub sequence in bigger DNA sequence
    
    Arguments:
        dna {String} -- DNA sequence
        sub {String} -- DNA substring, to be found in bigger one
    
    Returns:
        list[integer] -- List of occurence indexes of DNA substring
    """
    check = True
    dna_locations = []
    index = 1
    sub_length = len(sub)
    while check:
        i = dna.find(sub)
        if i != -1:
            index += i
            dna_locations.append(index)
            dna = dna[i+sub_length:]
            index += sub_length
        else:
            check = False
    return dna_locations

def hamming_distance(first, second):
    """Calculate Hamming Distance, number of mismatched nucleotides in two DNA sequences
    
    Arguments:
        first {String} -- First DNA sequence
        second {String} -- Seconde DNA sequence
    
    Returns:
        integer -- Number of mismatches
    """
    sum = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            sum += 1
    return sum

class TestDna(unittest.TestCase):
    
    def test_complementary_dna(self):
        self.assertEqual(dna('ATTGC'), 'TAACG')
        self.assertEqual(dna('GTAT'), 'CATA')

    def test_substring_locations_in_dna(self):
        self.assertEqual(dna_location('AUGCUUCAGAAAGGUCUUACG', 'ATAT'), [])
        self.assertEqual(dna_location('AUGCUUCAGAAAGGUCUUACG', 'UGCU'), [2])
        self.assertEqual(dna_location('GATATATGCATATACTT', 'ATAT'), [2, 10])
        self.assertEqual(dna_location('AGCTTTTCATTCTGAGTGCAACGGGCAATAAGAGTGTCTGATGAGTATC', 'GAGT'), [14, 32, 43])

    def test_hamming_distance(self):
        self.assertEqual(hamming_distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'), 7)
        self.assertEqual(
            hamming_distance(
                'TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC',
                'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'), 50)


if __name__ == '__main__':
    unittest.main()