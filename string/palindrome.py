import unittest

def is_palindrome(word):
    """Checks if given word is a palindrome.
    
    Arguments:
        word {string} -- Word that you want to check if it's a palindrome
    
    Returns:
        boolean -- True if it's palindrome, False if it's not.
    """
    lowered = str(word).lower()
    lowered = ''.join(l for l in lowered if l.isalnum())
    return lowered == lowered[::-1]

class TestPalindrome(unittest.TestCase):

    def test_None_input(self):
        self.assertFalse(is_palindrome(None))

    def test_word_palindromes(self):
        self.assertTrue(is_palindrome('madam'))
        self.assertTrue(is_palindrome('raCecaR'))
        self.assertTrue(is_palindrome('123454321'))
        self.assertTrue(is_palindrome('12 321'))
        self.assertFalse(is_palindrome('test'))

    def test_sentence_palindromes(self):
        self.assertTrue(is_palindrome('A man, a plan, a canal, Panama!'))
        self.assertTrue(is_palindrome('Was it a car or a cat I saw?'))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))
        self.assertTrue(is_palindrome('Amor, Roma'))

if __name__ == '__main__':
    unittest.main()