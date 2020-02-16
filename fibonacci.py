import unittest

def fib(n):
    """Returns a Fibonacii element by its index
    
    Arguments:
        n {integer} -- An index number
    
    Returns:
        integer -- A Fibonacci number at given index
    """
    
    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return n

def fib_seq(n):
    """Returns a Fibonacci sequence
    
    Arguments:
        n {integer} -- Number of elements to be returned
    
    Returns:
        string -- The Fibonacci sequence
    """

    list = []
    for i in range(n):
        list.append(str(fib(i)))
    return ' '.join(list)


## TEST cases of the Fibonacci sequence
class TestFibonacci(unittest.TestCase):

    def test_fib_value_in_position(self):
        self.assertEqual(fib(0), 0, "Should be 0")
        self.assertEqual(fib(1), 1, "Should be 1")
        self.assertEqual(fib(2), 1, "Should be 1")
        self.assertEqual(fib(3), 2, "Should be 2")
        self.assertEqual(fib(4), 3, "Should be 3")
        self.assertEqual(fib(5), 5, "Should be 5")
        self.assertEqual(fib(6), 8, "Should be 8")
        self.assertEqual(fib(7), 13, "Should be 13")
        self.assertEqual(fib(8), 21, "Should be 21")
        self.assertEqual(fib(9), 34, "Should be 34")
        self.assertEqual(fib(10), 55, "Should be 55")

    def test_print_fib_sequence(self):
        self.assertEqual(fib_seq(1), "0")
        self.assertEqual(fib_seq(2), "0 1")
        self.assertEqual(fib_seq(9), "0 1 1 2 3 5 8 13 21")


if __name__ == '__main__':
    unittest.main()