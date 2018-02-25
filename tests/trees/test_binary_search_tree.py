import unittest

from hypothesis import strategies as st, given

from src.trees import BinarySearchTree


# force bigger values to avoid small values clustering
MIN_KEY_SIZE = 10000
MAX_DICT_SIZE = 10


class TestBinarySearchTree(unittest.TestCase):

    @given(st.dictionaries(st.integers(max_value=MIN_KEY_SIZE), st.characters(), max_size=MAX_DICT_SIZE))
    def test_add_and_length(self, d):
        bst = BinarySearchTree(d)
        self.assertEqual(len(d), len(bst))

    @given(st.dictionaries(st.integers(max_value=MIN_KEY_SIZE), st.integers(), max_size=MAX_DICT_SIZE))
    def test_remove(self, d):
        bst = BinarySearchTree(d)

        for key, value in d.items():
            self.assertEqual(bst[key], value)
            del bst[key]
            with self.assertRaises(KeyError):
                _ = bst[key]

        self.assertEqual(len(bst), 0)

    @given(st.dictionaries(st.integers(max_value=MIN_KEY_SIZE), st.characters(), max_size=MAX_DICT_SIZE))
    def test_serialization(self, d):
        serialized = repr(BinarySearchTree(d))
        bst = eval(serialized)

        self.assertEqual(d, dict(bst.items()))

    @given(st.dictionaries(st.integers(max_value=MIN_KEY_SIZE), st.characters(), max_size=MAX_DICT_SIZE))
    def test_sequential_access(self, d):
        bst = BinarySearchTree(d)
        sorted_items = sorted(d.items(), key=lambda x: x[0])
        sorted_keys = [x for x, _ in sorted_items]
        sorted_values = [y for _, y in sorted_items]

        self.assertListEqual(list(bst), sorted_keys)
        self.assertListEqual(list(bst.keys()), sorted_keys)
        self.assertListEqual(list(bst.values()), sorted_values)
        self.assertListEqual(list(bst.items()), sorted_items)

    @given(st.dictionaries(st.integers(max_value=MIN_KEY_SIZE), st.characters(), max_size=MAX_DICT_SIZE))
    def test_membership(self, d):
        bst = BinarySearchTree(d)
        for key in d:
            self.assertIn(key, bst)
        if d:
            self.assertNotIn(max(d) + 1, bst)

    @given(st.dictionaries(st.integers(max_value=MIN_KEY_SIZE), st.characters(), max_size=MAX_DICT_SIZE))
    def test_random_access(self, d):
        bst = BinarySearchTree(d)
        for key, value in d.items():
            self.assertEqual(bst[key], value)

        if d:
            with self.assertRaises(KeyError):
                _ = bst[max(d) + 1]

    @given(st.dictionaries(st.integers(max_value=MIN_KEY_SIZE), st.characters(), max_size=MAX_DICT_SIZE))
    def test_smallest_item(self, d):
        bst = BinarySearchTree(d)

        for expected in sorted(d.items(), key=lambda x: x[0]):
            item = bst.get_smallest_item()
            self.assertEqual(expected, item)

            item = bst.pop_smallest_item()
            self.assertEqual(expected, item)

        self.assertEqual(0, len(bst))

    @given(st.dictionaries(st.integers(max_value=MIN_KEY_SIZE), st.characters(), max_size=MAX_DICT_SIZE))
    def test_biggest_item(self, d):
        bst = BinarySearchTree(d)

        for expected in sorted(d.items(), key=lambda x: x[0], reverse=True):
            item = bst.get_biggest_item()
            self.assertEqual(expected, item)

            item = bst.pop_biggest_item()
            self.assertEqual(expected, item)

        self.assertEqual(0, len(bst))

    def test_is_left_node(self):
        bst = BinarySearchTree([(5, 25), (3, 9), (4, 16)])
        expected_left = bst.root.get(3)
        self.assertTrue(expected_left.is_left_node)
        self.assertFalse(expected_left.is_right_node)

    def test_is_right_node(self):
        bst = BinarySearchTree([(5, 25), (3, 9), (4, 16)])
        expected_right = bst.root.get(4)
        self.assertTrue(expected_right.is_right_node)
        self.assertFalse(expected_right.is_left_node)
