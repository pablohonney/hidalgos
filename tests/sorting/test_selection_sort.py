import unittest

from hypothesis import strategies as st, given

from src.sorting.selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_bubble_sort(self, arr):
        expected = sorted(arr)
        selection_sort(arr)
        self.assertListEqual(arr, expected)
