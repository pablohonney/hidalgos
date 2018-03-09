import unittest

from hypothesis import strategies as st, given

# private
from src.data_types.deque import Deque


class TestDeque(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_right_stack(self, arr):
        dq = Deque(arr)
        actual = [dq.pop_right() for _ in arr]
        self.assertListEqual(arr[::-1], actual)

    @given(st.lists(st.integers()))
    def test_left_stack(self, arr):
        dq = Deque()
        for item in arr:
            dq.push_left(item)

        actual = [dq.pop_left() for _ in arr]
        self.assertListEqual(arr[::-1], actual)

    @given(st.lists(st.integers()))
    def test_right_left_queue(self, arr):
        dq = Deque(arr)

        actual = [dq.pop_left() for _ in arr]
        self.assertListEqual(arr, actual)

    @given(st.lists(st.integers()))
    def test_left_right_queue(self, arr):
        dq = Deque()
        for item in arr:
            dq.push_left(item)

        actual = [dq.pop_right() for _ in arr]
        self.assertListEqual(arr, actual)

    @given(st.lists(st.integers()))
    def test_serialization(self, arr):
        serialized = repr(Deque(arr))
        queue = eval(serialized)

        contents = [queue.pop_left() for _ in range(len(queue))]
        self.assertListEqual(contents, arr)
