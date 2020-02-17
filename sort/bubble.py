import unittest

def bubble_sort(list):
    """Sort list using Bubble Sort algorithm
    
    Arguments:
        list {integer} -- Unsorted list
    
    Returns:
        list {integer} -- Sorted list
    """

    swap = True
    while swap:
        swap = False
        for n in range(len(list) - 1 ):
            if list[n] > list[n+1]:
                current = list[n]
                list[n] = list[n + 1]
                list[n + 1] = current
                swap = True
    return list

class TestBubbleSort(unittest.TestCase):

    def test_sort(self):
        self.assertListEqual(bubble_sort([1, 1]), [1, 1])
        self.assertListEqual(bubble_sort([1, 2]), [1, 2])
        self.assertListEqual(bubble_sort([2, 1]), [1, 2])
        self.assertListEqual(bubble_sort([6, 3, 9, 1, 43]), [1, 3, 6, 9, 43])
        self.assertListEqual(bubble_sort([14, 46, 43, 27, 57, 41, 45, 21, 70]), [14, 21, 27, 41, 43, 45, 46, 57, 70])

if __name__ == '__main__':
    unittest.main()

