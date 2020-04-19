import unittest

class BinaryTree:

    def __init__(self):
        self.root_node = None
        self.tree = []

    def insert(self, data):
        if self.root_node is None:
            self.root_node = Node(data)
        else:
            node = self.root_node
            while True:
                if data >= node.data:
                    if node.right is None:
                        node.right = Node(data)
                        break
                    node = node.right
                else: 
                    if node.left is None:
                        node.left = Node(data)
                        break
                    node = node.left

    def remove(self, data):
        pass

    def get_tree(self):
        if self.root_node.data is not None:
           self.tree_node(self.root_node)
        return self.tree

    def tree_node(self, node):
        if node is not None:
            self.tree_node(node.left)
            self.tree.append(node.data)
            self.tree_node(node.right)


class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def binary_tree(arr):
    pass

class BinaryTreeTest(unittest.TestCase):

    def test_insert_one(self):
        tree = BinaryTree()
        tree.insert(1)
        self.assertEqual(tree.get_tree(), [1])

    def test_insert_three(self):
        tree = BinaryTree()
        tree.insert(1)
        tree.insert(2)
        tree.insert(3)
        self.assertEqual(tree.get_tree(), [1, 2, 3])

    def test_insert_complex(self):
        """Tree:
                    7
                   / \\
                  6    10
                 / \\    \\
                4    6     12
               / \\ 
              2    5
             / \\
            1    2     
        """
        tree = BinaryTree()
        elements = [7, 6, 6, 4, 5, 2, 2, 1, 10, 12]
        for element in elements:
            tree.insert(element)
        self.assertEqual(tree.get_tree(), [1, 2, 2, 4, 5, 6, 6, 7, 10, 12])


if __name__ == '__main__':
    unittest.main()
