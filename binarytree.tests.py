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

    def test_add_same_info_twice_throws(self):
        with self.assertRaises(ValueError):
            self.root.add(13)

    def test_in_order(self):
        actual = self.root.in_order()
        self.assertEqual(actual, [2, 3, 4, 5, 7, 10, 13, 15, 17])

    def test_max_height(self):
        actual = self.root.max_height()
        self.assertEqual(actual, 4)

    def test_min_height(self):
        actual = self.root.min_height()
        self.assertEqual(actual, 3)


if __name__ == '__main__':
    unittest.main()
