import unittest

from hypothesis import strategies as st, given

from src.trees import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    @given(st.dictionaries(st.integers(), st.characters()))
    def test_add_and_length(self, d):
        bst = BinarySearchTree(d)
        self.assertEqual(len(bst), len(d))

    @given(st.dictionaries(st.integers(), st.characters()))
    def test_remove(self, d):
        bst = BinarySearchTree(d)

    @given(st.dictionaries(st.integers(), st.characters()))
    def test_serialization(self, d):
        serialized = repr(BinarySearchTree(d))
        bst = eval(serialized)

        self.assertEqual(dict(bst.items()), d)

    @given(st.dictionaries(st.integers(), st.characters()))
    def test_sequential_access(self, d):
        bst = BinarySearchTree(d)
        sorted_items = sorted(d.items(), key=lambda x: x[0])
        sorted_keys = [x for x, _ in sorted_items]
        sorted_values = [y for _, y in sorted_items]

        self.assertListEqual(list(bst), sorted_keys)
        self.assertListEqual(list(bst.keys()), sorted_keys)
        self.assertListEqual(list(bst.values()), sorted_values)
        self.assertListEqual(list(bst.items()), sorted_items)

    @given(st.dictionaries(st.integers(), st.characters()))
    def test_membership(self, d):
        bst = BinarySearchTree(d)
        for key in d:
            self.assertIn(key, bst)
        if d:
            self.assertNotIn(max(d) + 1, bst)

    @given(st.dictionaries(st.integers(), st.characters()))
    def test_random_access(self, d):
        bst = BinarySearchTree(d)
        for key, value in d.items():
            self.assertEqual(bst[key], value)

        if d:
            with self.assertRaises(KeyError):
                _ = bst[max(d) + 1]

    def test_deque_access(self):
        pass
