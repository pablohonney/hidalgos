import unittest

from hypothesis import strategies as st, given

from src.lists import Queue


class TestQueue(unittest.TestCase):

    @given(st.lists(st.integers()))
    def runTest(self, arr):
        queue = Queue(arr)

        self.assertEqual(len(queue), len(arr))

        for i in arr:
            self.assertEqual(queue.peek(), i)
            self.assertEqual(queue.pop(), i)

        self.assertEqual(len(queue), 0)

    @given(st.lists(st.integers()))
    def test_serialization(self, arr):
        serialized = repr(Queue(arr))
        queue = eval(serialized)

        contents = [queue.pop() for _ in range(len(queue))]
        self.assertListEqual(contents, arr)
