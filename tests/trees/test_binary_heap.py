import unittest

from hypothesis import strategies as st, given

from src.trees.heaps import MinHeap
from src.trees.heaps import MaxHeap


class TestBinaryHeap(unittest.TestCase):

    def test_simple_min_heap(self):
        bh = MinHeap()
        for i in range(9, -1, -1):
            bh.push(i)

        self.assertListEqual(bh.list, [0, 1, 4, 3, 2, 8, 5, 9, 6, 7])
        self.assertEqual(len(bh), 10)

        for i in range(10):
            self.assertEqual(bh.peek(), i)
            self.assertEqual(bh.pop(), i)

        self.assertEqual(len(bh), 0)

    @given(st.lists(st.integers()))
    def test_min_heap(self, arr):
        bh = MinHeap(arr)

        self.assertEqual(len(bh), len(arr))

        for i in sorted(arr):
            self.assertEqual(bh.peek(), i)
            self.assertEqual(bh.pop(), i)

        self.assertEqual(len(bh), 0)

    @given(st.lists(st.integers()))
    def test_max_heap(self, arr):
        bh = MaxHeap(arr)

        self.assertEqual(len(bh), len(arr))

        for i in sorted(arr, reverse=True):
            self.assertEqual(bh.peek(), i)
            self.assertEqual(bh.pop(), i)

        self.assertEqual(len(bh), 0)
