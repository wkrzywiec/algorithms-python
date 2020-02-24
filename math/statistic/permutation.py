import unittest

# https://www.codewars.com/kata/5254ca2719453dcc0b00027d
def all_permutations(string):
    count = permutations_number(string.count())
    pass


def permutations_number(count):
    if count > 1:
        return count * permutations_number(count - 1)
    return 1

class TestPermutation(unittest.TestCase):

    def test_permutations(self):
        self.assertEqual(all_permutations('a'), ['a'])
        self.assertEqual(all_permutations('ab'), ['ab', 'ba'])
        self.assertEqual(all_permutations('aabb'), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])

    def test_permutations_number(self):
        self.assertEqual(permutations_number(1), 1)
        self.assertEqual(permutations_number(2), 2)
        self.assertEqual(permutations_number(3), 6)
        self.assertEqual(permutations_number(4), 24)
        self.assertEqual(permutations_number(5), 120)
        self.assertEqual(permutations_number(6), 720)
        self.assertEqual(permutations_number(7), 5040)


if __name__ == '__main__':
    unittest.main()