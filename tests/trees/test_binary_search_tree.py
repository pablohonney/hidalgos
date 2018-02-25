import unittest

from hypothesis import strategies as st, given

from src.trees import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    @given(st.dictionaries(st.integers(), st.characters()))
    def test_add_and_length(self, d):
        bst = BinarySearchTree(d)
        self.assertEqual(len(bst), len(d))

    @unittest.skip('TODO remove on BST')
    # @given(st.dictionaries(st.integers(), st.characters(), min_size=1))
    def test_remove(self, d=0):
        d = {5: 8, 1: 5, 2: 4, 11: 9}
        key, *_ = d.keys()
        bst = BinarySearchTree(d)
        print(bst.get(key))
        bst.remove(key)
        print(bst.get(key))

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

    @given(st.dictionaries(st.integers(), st.characters(), min_size=1))
    def test_smallest_item(self, d):
        bst = BinarySearchTree(d)
        expected = min(d.items(), key=lambda x: x[0])
        item = bst.get_smallest_item()
        self.assertEqual(item, expected)

    @given(st.dictionaries(st.integers(), st.characters(), min_size=1))
    def test_biggest_item(self, d):
        bst = BinarySearchTree(d)
        expected = max(d.items(), key=lambda x: x[0])
        item = bst.get_biggest_item()
        self.assertEqual(item, expected)

    def test_is_left_node(self):
        bst = BinarySearchTree([(5, 25), (3, 9), (4, 16)])
        expected_left = bst._get(3)
        self.assertTrue(bst.is_left_node(expected_left))
        self.assertFalse(bst.is_right_node(expected_left))

    def test_is_right_node(self):
        bst = BinarySearchTree([(5, 25), (3, 9), (4, 16)])
        expected_right = bst._get(4)
        self.assertTrue(bst.is_right_node(expected_right))
        self.assertFalse(bst.is_left_node(expected_right))
