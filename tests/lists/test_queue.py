import unittest

from hypothesis import strategies as st, given

from src.lists.queue import QueueViaStack
from src.lists.queue import QueueViaSinglyLinkedList


class TestQueueViaStack(unittest.TestCase):
    @given(st.lists(st.integers()))
    def test_is_working(self, arr):
        queue = QueueViaStack(arr)

        self.assertEqual(len(queue), len(arr))

        for i in arr:
            self.assertEqual(queue.peek(), i)
            self.assertEqual(queue.pop(), i)

        self.assertEqual(len(queue), 0)

    @given(st.lists(st.integers()))
    def test_serialization(self, arr):
        serialized = repr(QueueViaStack(arr))
        queue = eval(serialized)

        contents = [queue.pop() for _ in range(len(queue))]
        self.assertListEqual(contents, arr)


class TestQueueViaSinglyLikedList(unittest.TestCase):
    def test(self):
        arr = list(range(5))

        queue = QueueViaSinglyLinkedList(arr)

        self.assertEqual(len(queue), len(arr))

        for i in arr:
            self.assertEqual(queue.peek(), i)
            self.assertEqual(queue.pop(), i)

        self.assertEqual(len(queue), 0)

    @given(st.lists(st.integers()))
    def test_is_working(self, arr):
        queue = QueueViaSinglyLinkedList(arr)

        self.assertEqual(len(queue), len(arr))

        for i in arr:
            self.assertEqual(queue.peek(), i)
            self.assertEqual(queue.pop(), i)

        self.assertEqual(len(queue), 0)

    @given(st.lists(st.integers()))
    def test_serialization(self, arr):
        serialized = repr(QueueViaSinglyLinkedList(arr))
        queue = eval(serialized)

        contents = [queue.pop() for _ in range(len(queue))]
        self.assertListEqual(contents, arr)
