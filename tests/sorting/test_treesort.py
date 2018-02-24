import unittest

from hypothesis import strategies as st, given

from src.sorting import tree_sort


class TestTreeSort(unittest.TestCase):

    @given(st.sets(st.integers()))
    def test_distinct_keys(self, arr):
        expected = sorted(arr)
        self.assertListEqual(expected, list(tree_sort(arr)))
