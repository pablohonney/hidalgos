import unittest

from hypothesis import strategies as st, given

from src.trees import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_add(self, arr):
        bst = BinarySearchTree()
        for i in arr:
            bst.add(i)

    def test_remove(self):
        pass

    def test_serialization(self):
        pass

    def test_length(self):
        pass

    def test_sequential_access(self):
        pass

    def test_membership(self):
        pass

    def test_random_access(self):
        pass

    def test_deque_access(self):
        pass
