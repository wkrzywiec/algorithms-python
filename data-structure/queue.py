import unittest

class Queue:
    """Simple Queue implementation - First in First Out
    """

    def __init__(self):
        self.__data = []

    def enqueue(self, text):
        """Add new element to queue
        
        Arguments:
            text {string} -- An element which needs to be added to an end of a queue
        """
        self.__data.append(text)

    def dequeue(self):
        """Gets a first element in a front of a queue
        
        Returns:
            string -- A first element in a front of a queue
        """
        if len(self.__data) == 0:
            return None
        taken = self.__data[0]
        new_queue = []
        for index in range(1, len(self.__data)):
            new_queue.append(self.__data[index])
        self.__data = new_queue
        return taken

    def front(self):
        """Checks a first element in a front of a queue
        
        Returns:
            string -- A first element in a front of a queue
        """
        if len(self.__data) == 0:
            return None
        return self.__data[0]

    def rear(self):
        """Checks a last element in a queue
        
        Returns:
            string -- A last element in a queue
        """
        if len(self.__data) == 0:
            return None
        return self.__data[-1]

class QueueTest(unittest.TestCase):
    
    def test_empty_queue(self):
        queue = Queue()
        self.assertIsNone(queue.front())
        self.assertIsNone(queue.rear())
        self.assertIsNone(queue.dequeue())

    def test_add_one(self):
        queue = Queue()
        queue.enqueue('one')
        self.assertEqual(queue.front(), 'one', "Should be 'one'")
        self.assertEqual(queue.rear(), 'one', "Should be 'one'")

    def test_add_three(self):
        queue = Queue()
        queue.enqueue('one')
        queue.enqueue('two')
        queue.enqueue('three')
        self.assertEqual(queue.front(), 'one', "Should be 'one'")
        self.assertEqual(queue.rear(), 'three', "Should be 'three'")

    def test_add_three_get_one(self):
        queue = Queue()
        queue.enqueue('one')
        queue.enqueue('two')
        queue.enqueue('three')
        taken = queue.dequeue()
        self.assertEqual(queue.front(), 'two', "Should be 'two'")
        self.assertEqual(queue.rear(), 'three', "Should be 'three'")
        self.assertEqual(taken, 'one', "Should be 'one'")

if __name__ == '__main__':
    unittest.main()