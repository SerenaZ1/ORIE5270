import unittest
from tree.print_tree import Tree, Node


class TestTree(unittest.TestCase):

    def setUp(self):
        self.answer1 = [['1']]
        self.answer2 = [['|', '|', '|', '1', '|', '|', '|'],
                        ['|', '2', '|', '|', '|', '3', '|'],
                        ['4', '|', '5', '|', '6', '|', '7']]
        self.answer3 = [['|', '|', '|', '|', '|', '|', '|', '1', '|', '|', '|', '|', '|', '|', '|'],
                        ['|', '|', '|', '2', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                        ['|', '3', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                        ['4', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]
        self.answer4 = [['|', '|', '|', '|', '|', '|', '|', '1', '|', '|', '|', '|', '|', '|', '|'],
                        ['|', '|', '|', '2', '|', '|', '|', '|', '|', '|', '|', '3', '|', '|', '|'],
                        ['|', '|', '|', '|', '|', '4', '|', '|', '|', '5', '|', '|', '|', '|', '|'],
                        ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '6', '|', '|', '|', '|']]

    def test_tree1(self):
        a = Node(1, None, None)
        tree1 = Tree(a)
        assert tree1.printTree(tree1.get_height(a)) == self.answer1

    def test_tree2(self):
        a = Node(1, None, None)
        b = Node(2, None, None)
        c = Node(3, None, None)
        d = Node(4, None, None)
        e = Node(5, None, None)
        f = Node(6, None, None)
        g = Node(7, None, None)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.left = f
        c.right = g

        tree2 = Tree(a)
        assert tree2.printTree(tree2.get_height(a)) == self.answer2

    def test_tree3(self):
        a = Node(1, None, None)
        b = Node(2, None, None)
        c = Node(3, None, None)
        d = Node(4, None, None)

        a.left = b
        b.left = c
        c.left = d

        tree3 = Tree(a)
        assert tree3.printTree(tree3.get_height(a)) == self.answer3

    def test_tree4(self):
        a = Node(1, None, None)
        b = Node(2, None, None)
        c = Node(3, None, None)
        d = Node(4, None, None)
        e = Node(5, None, None)
        f = Node(6, None, None)

        a.left = b
        a.right = c
        b.right = d
        c.left = e
        e.right = f

        tree4 = Tree(a)
        assert tree4.printTree(tree4.get_height(a)) == self.answer4
