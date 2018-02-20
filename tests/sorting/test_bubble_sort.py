import unittest

from hypothesis import strategies as st, given

from src.sorting.bubble_sort import bubble_sort, comb_sort, shaker_sort


class TestBubbleSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_bubble_sort(self, arr):
        expected = sorted(arr)
        bubble_sort(arr)
        self.assertListEqual(arr, expected)

    @given(st.lists(st.integers()))
    def test_shaker_sort(self, arr):
        expected = sorted(arr)
        shaker_sort(arr)
        self.assertListEqual(arr, expected)

    @given(st.lists(st.integers()))
    def test_comb_sort(self, arr):
        expected = sorted(arr)
        comb_sort(arr)
        self.assertListEqual(arr, expected)
