import unittest
from binarytree import Node

class BinaryTreeTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(BinaryTreeTests, self).__init__(*args, **kwargs)

        self.root = Node(10)
        self.root.add(5)
        self.root.add(3)
        self.root.add(7)
        self.root.add(2)
        self.root.add(4)
        self.root.add(15)
        self.root.add(13)
        self.root.add(17)

    def test_adds_nodes(self):
        self.assertEqual(self.root.info, 10)
        self.assertIsNotNone(self.root.left)
        self.assertEqual(self.root.left.info, 5)
        self.assertIsNotNone(self.root.right)
        self.assertEqual(self.root.right.info, 15)

    def test_add_same_info_throws(self):
        with self.assertRaises(ValueError):
            self.root.add(13)

if __name__ == '__main__':
    unittest.main()