import unittest

def is_anagram(first, second):
    """Check if two strings are anagrams
    
    Arguments:
        first {string} -- First word
        second {string} -- Second word
    
    Returns:
        [boolean] -- Returns True is both strings are anagrams, returns False if they're not
    """
    return sorted(first.lower()) == sorted(second.lower())

class TestAnagram(unittest.TestCase):

    def test_anagrams(self):
        self.assertTrue(is_anagram("Buckethead", "DeathCubeK"))
        self.assertTrue(is_anagram('Creative', 'Reactive'))
        self.assertTrue(is_anagram('foefet', 'toffee'))
        self.assertTrue(is_anagram('Twoo', 'WooT'))

    def test_not_anagrams(self):
        self.assertFalse(is_anagram('chemistry', 'physics'), 'Different words')
        self.assertFalse(is_anagram('ython', 'python'), 'Missing one letter')
        self.assertFalse(is_anagram('book', 'bok'), 'Same letters, but different count')

if __name__ == '__main__':
    unittest.main()