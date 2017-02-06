#!python

from trees import BinaryTree
import unittest


class TestRecursion(unittest.TestCase):
    def test_insertion(self):
        tree = BinaryTree()
        tree.insert(10)
        with self.assertRaises(KeyError):
            tree.insert(10)

    def test_search(self):
        tree = BinaryTree([10,50,5,9,1,3,2])
        assert tree.search(10).data is 10
        assert tree.search(50).data is 50
        assert tree.search(5).data is 5
        assert tree.search(9).data is 9
        assert tree.search(1).data is 1
        assert tree.search(3).data is 3
        assert tree.search(2).data is 2

        assert tree.search(-1) is None

    def test_deletion_left_side(self):
        tree = BinaryTree([10,50,5,9,1,3,2])

        tree.delete(10)

        assert tree.search(10) is None
        assert tree.search(50).data is 50
        assert tree.search(5).data is 5
        assert tree.search(9).data is 9
        assert tree.search(1).data is 1
        assert tree.search(3).data is 3
        assert tree.search(2).data is 2



    def test_deletion_right_side(self):
        tree = BinaryTree([10, 20, 15, 25, 23, 22, 30])

        tree.delete(25)

        assert tree.search(25) is None
        assert tree.search(20).data is 20
        assert tree.search(15).data is 15
        assert tree.search(10).data is 10
        assert tree.search(23).data is 23
        assert tree.search(22).data is 22
        assert tree.search(30).data is 30

if __name__ == '__main__':
    unittest.main()
