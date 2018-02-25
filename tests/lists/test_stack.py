import unittest

from hypothesis import strategies as st, given

from src.lists import Stack


class TestStack(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_stack(self, arr):
        stack = Stack(arr)

        self.assertEqual(len(stack), len(arr))

        for i in arr[::-1]:
            self.assertEqual(stack.peek(), i)
            self.assertEqual(stack.pop(), i)

        self.assertEqual(len(stack), 0)

    @given(st.lists(st.integers()))
    def test_serialization(self, arr):
        serialized = repr(Stack(arr))
        stack = eval(serialized)

        contents = [stack.pop() for _ in range(len(stack))][::-1]
        self.assertListEqual(contents, arr)
