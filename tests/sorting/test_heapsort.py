import unittest

from hypothesis import strategies as st, given

from src.algorithms.sorting import heap_sort


class TestHeapSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_increasing(self, arr):
        expected = sorted(arr)
        self.assertListEqual(list(heap_sort(arr)), expected)

    @given(st.lists(st.integers()))
    def test_decreasing(self, arr):
        expected = sorted(arr, reverse=True)
        self.assertListEqual(list(heap_sort(arr, reverse=True)), expected)
