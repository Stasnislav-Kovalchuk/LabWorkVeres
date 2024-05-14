import unittest
from src.BinaryTreeFirstMax import searching_first_biggest
from src.BinaryTreeFirstMax import Node


class TestOfInorderTraversal(unittest.TestCase):
    def test_1(self):
        root = Node(10)
        root.left = Node(10)
        root.left.parent = root
        root.right = Node(10)
        root.right.parent = root
        root.left.right = Node(10)
        root.left.right.parent = root.left
        root.left.left = Node(10)
        root.left.left.parent = root.left
        root.right.right = Node(10)
        root.right.right.parent = root.right
        root.right.left = Node(10)
        root.right.left.parent = root.right

        node = root.left.left

        expected_result = 10
        self.assertEqual(searching_first_biggest(root, node), expected_result)

    def test_2(self):
        root = Node(10)
        root.left = Node(5)
        root.left.parent = root
        root.right = Node(15)
        root.right.parent = root
        root.left.right = Node(7)
        root.left.right.parent = root.left
        root.left.left = Node(3)
        root.left.left.parent = root.left
        root.right.right = Node(20)
        root.right.right.parent = root.right
        root.right.left = Node(12)
        root.right.left.parent = root.right

        node = root.right.right

        expected_result = 20
        self.assertEqual(searching_first_biggest(root, node), expected_result)

    def test_3(self):
        root = Node(10)
        root.left = Node(5)
        root.left.parent = root
        root.right = Node(15)
        root.right.parent = root
        root.left.right = Node(7)
        root.left.right.parent = root.left
        root.left.left = Node(3)
        root.left.left.parent = root.left
        root.right.right = Node(20)
        root.right.right.parent = root.right
        root.right.left = Node(12)
        root.right.left.parent = root.right

        node = root

        expected_result = 12
        self.assertEqual(searching_first_biggest(root, node), expected_result)
