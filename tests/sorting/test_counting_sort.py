import unittest

from hypothesis import strategies as st, given

from src.sorting.counting_sort import counter_sort
from src.sorting.counting_sort import counter_sort_inplace


class TestCountingSort(unittest.TestCase):

    @given(st.lists(st.integers(min_value=0, max_value=10 ** 3)))
    def test_counting_sort(self, arr):
        expected = sorted(arr)
        result = counter_sort(arr)
        self.assertListEqual(result, expected)

    @given(st.lists(st.integers(min_value=0, max_value=10 ** 3)))
    def test_counting_sort_inplace(self, arr):
        expected = sorted(arr)
        counter_sort_inplace(arr)
        self.assertListEqual(arr, expected)
