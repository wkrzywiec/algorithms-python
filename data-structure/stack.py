import unittest

class Stack:
    """Simple Stack implementation - First In Last Out
    """

    def __init__(self):
        self.__data = []

    def push(self, text):
        """Push an item to a stack
        
        Arguments:
            text {string} -- Element that will be put on stack
        """
        self.__data.insert(0, text)

    def pop(self):
        """Get an element from a top of a stack 
        
        Returns:
            string -- element from a top of a stack
        """
        if len(self.__data) == 0:
            return None
        
        popped = self.__data[0]
        new_data = []
        for index in range(1, len(self.__data)):
            new_data.append(self.__data[index])
        self.__data = new_data
        return popped
        
    def peek(self):
        """Check what currently is at a top of a stack without taking it off
        
        Returns:
            string -- element from a top of a stack
        """
        return self.__data[0]


class StackTest(unittest.TestCase):

    def test_push_one_peek_one(self):
        stack = Stack()
        stack.push('one')
        self.assertEqual(stack.peek(), 'one', "Should be 'one'")

    def test_push_three_peek_last(self):
        stack = Stack()
        stack.push('one')
        stack.push('two')
        stack.push('three')
        self.assertEqual(stack.peek(), 'three', "Should be 'three'")

    def test_push_three_pop_one_peek_second(self):
        stack = Stack()
        stack.push('one')
        stack.push('two')
        stack.push('three')
        popped = stack.pop()
        self.assertEqual(popped, 'three', "Should be 'three'")
        self.assertEqual(stack.peek(), 'two', "Should be 'two'")

    def test_pop_empty_stack(self):
        stack = Stack()
        popped = stack.pop()
        self.assertIsNone(popped)


if __name__ == '__main__':
    unittest.main()