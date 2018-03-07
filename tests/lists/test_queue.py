import unittest

from hypothesis import strategies as st, given

from src.lists.queue import QueueViaStack
from src.lists.queue import QueueViaSinglyLinkedList
from src.lists.queue import QueueViaArray


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


class TestQueueViaArray(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_is_working(self, arr):
        queue = QueueViaArray(len(arr), arr)

        self.assertEqual(len(queue), len(arr))

        for i in arr:
            self.assertEqual(queue.peek(), i)
            self.assertEqual(queue.pop(), i)

        self.assertEqual(len(queue), 0)

    @given(st.lists(st.integers()))
    def test_serialization(self, arr):
        serialized = repr(QueueViaArray(arr))
        queue = eval(serialized)

        contents = [queue.pop() for _ in range(len(queue))]
        self.assertListEqual(contents, arr)


