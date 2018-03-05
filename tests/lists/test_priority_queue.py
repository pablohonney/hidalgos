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

    def test_increasing_update_priority(self):
        arr = [('last', 3), ('first', 1), ('middle', 4)]
        queue = MinPriorityQueue(arr, key=lambda x: x[1])

        self.assertEqual(queue.pop(), ('first', 1))
        self.assertEqual(queue.peek(), ('last', 3))

        queue.update_priority(('middle', 4), ('middle', 2))

        self.assertEqual(queue.pop(), ('middle', 2))
        self.assertEqual(queue.pop(), ('last', 3))

    @given(st.lists(st.integers()))
    def test_decreasing(self, arr):
        expected = sorted(arr, reverse=True)
        queue = MaxPriorityQueue(arr)

        actual = []
        while queue:
            actual.append(queue.pop())
        self.assertListEqual(actual, expected)
