import unittest

from hypothesis import strategies as st, given

from src.lists import MinPriorityQueue
from src.lists import MaxPriorityQueue


class TestPriorityQueue(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_increasing(self, arr):
        expected = sorted(arr)
        queue = MinPriorityQueue(arr)

        actual = []
        while queue:
            actual.append(queue.pop())
        self.assertListEqual(actual, expected)

    @given(st.lists(st.integers()))
    def test_decreasing(self, arr):
        expected = sorted(arr, reverse=True)
        queue = MaxPriorityQueue(arr)

        actual = []
        while queue:
            actual.append(queue.pop())
        self.assertListEqual(actual, expected)
