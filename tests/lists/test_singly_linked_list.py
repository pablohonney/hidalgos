import unittest
from random import randint

from hypothesis import strategies as st, given

from src.data_types.lists import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    def test_insert(self):
        expected = []
        ll = SinglyLinkedList()
        for index in range(100):
            expected.insert(len(expected)//2, index)
            ll.insert(index, len(ll)//2)

        self.assertListEqual(expected, list(ll))

    def test_insert_left_right(self):
        ll1 = SinglyLinkedList()
        ll2 = SinglyLinkedList()
        for i in range(100):
            ll1.insert_left(i)
            ll2.insert_right(i)

        self.assertTrue(len(ll1), 100)
        self.assertEqual(len(ll2), 100)
        self.assertListEqual(list(ll1), list(ll2)[::-1])

    def test_pop(self):
        control = list(range(100))
        ll = SinglyLinkedList(range(100))

        expected = []
        while control:
            expected.append(control.pop(len(control)//2))

        actual = []
        while ll:
            actual.append(ll.pop(len(ll)//2))

        self.assertListEqual(expected, actual)

    def test_pop_left_right(self):
        control = list(range(100))
        ll = SinglyLinkedList(range(100))

        expected = []
        actual = []
        for i in range(100):
            if i % 2:
                expected.append(control.pop(0))
                actual.append(ll.pop_left())
            else:
                expected.append(control.pop(-1))
                actual.append(ll.pop_right())

        self.assertListEqual(expected, actual)

    def test_peek(self):
        pass


    @given(st.lists(st.integers()))
    def test_queue_pop(self, arr):
        ll = SinglyLinkedList(arr)

        self.assertListEqual([ll.pop(0) for _ in range(len(ll))], arr)
        self.assertEqual(len(ll), 0)
        with self.assertRaises(IndexError):
            ll.pop()

    @given(st.lists(st.integers()))
    def test_stack_pop(self, arr):
        ll = SinglyLinkedList(arr)

        self.assertListEqual([ll.pop() for _ in range(len(ll))], arr[::-1])
        self.assertEqual(len(ll), 0)
        with self.assertRaises(IndexError):
            ll.pop()

    def test_membership(self):
        arr = list(range(100))
        ll = SinglyLinkedList(arr)

        for i in arr:
            self.assertIn(i, ll)

        for i in range(100, 200):
            self.assertNotIn(i, ll)

    @given(st.lists(st.integers()))
    def test_random_pop(self, arr):
        ll = SinglyLinkedList(arr)

        permutation = []
        for _ in range(len(arr)):
            permutation.append(ll.pop(randint(0, len(ll) - 1)))

        self.assertEqual(len(ll), 0)
        self.assertListEqual(sorted(permutation), sorted(arr))

    def test_tail(self):
        ll = SinglyLinkedList(range(10))
        self.assertEqual(ll.tail.value, 9)
        ll.pop()
        self.assertEqual(ll.tail.value, 8)
        ll.insert_right(15)
        self.assertEqual(ll.tail.value, 15)

    def test_random_access(self):
        ll = SinglyLinkedList(range(10))
        for i in range(10):
            self.assertEqual(ll[i], i)  # get
            ll[i] = i ** 2  # set
            self.assertEqual(ll[i], i ** 2)  # get
        for i in range(10, 20):
            try:
                self.assertEqual(ll[i], i)
            except IndexError:
                pass

    @given(st.lists(st.integers()))
    def test_serialization(self, arr):
        serialized = repr(SinglyLinkedList(arr))
        ll = eval(serialized)

        self.assertListEqual(list(ll), arr)

    @given(st.lists(st.integers()))
    def test_sequential_access(self, arr):
        ll = SinglyLinkedList(arr)
        self.assertListEqual(list(ll), arr)
