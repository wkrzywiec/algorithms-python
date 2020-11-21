import unittest

def reverse(text):
    """Returns a text in reversed order of characters
    
    Arguments:
        text {string} -- any kind of text
    
    Returns:
        string -- text with reversed order of characters
    """
    if text is None:
       return None 
    return ''.join(reversed(text))


class ReverseString(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse('coffee'), 'eeffoc', "Should be 'eeffoc'")

    def test_reverse_two_words(self):
        self.assertEqual(reverse('morning coffee'), 'eeffoc gninrom', "Should be 'eeffoc gninrom'")

    def test_reverse_empty_string(self):
        self.assertEqual(reverse(''), '')

    def test_reverse_none(self):
        self.assertEqual(reverse(None), None)

if __name__ == '__main__':
    unittest.main()
