import unittest

from hypothesis import strategies as st, given

from src.data_types.lists import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    List = SinglyLinkedList

    @given(st.lists(st.integers()))
    def test_insert(self, control):
        expected = []
        ll = self.List()
        for index, _ in enumerate(control):
            expected.insert(len(expected) // 2, index)
            ll.insert(index, len(ll) // 2)

        self.assertListEqual(expected, list(ll))

    @given(st.lists(st.integers()))
    def test_insert_left_right(self, control):
        ll1 = self.List()
        ll2 = self.List()
        for item in control:
            ll1.insert_left(item)
            ll2.insert_right(item)

        self.assertEqual(len(ll1), len(control))
        self.assertEqual(len(ll2), len(control))
        self.assertListEqual(list(ll1), list(ll2)[::-1])

    @given(st.lists(st.integers()))
    def test_pop(self, control):
        ll = self.List(control)

        expected = []
        while control:
            expected.append(control.pop(len(control) // 2))

        actual = []
        while ll:
            actual.append(ll.pop(len(ll) // 2))

        self.assertListEqual(expected, actual)

    @given(st.lists(st.integers()))
    def test_pop_left_right(self, control):
        ll = self.List(control)

        expected = []
        actual = []
        for i, _ in enumerate(control):
            if i % 2:
                expected.append(control.pop(0))
                actual.append(ll.pop_left())
            else:
                expected.append(control.pop(-1))
                actual.append(ll.pop_right())

        self.assertListEqual(expected, actual)

    def test_pop_empty(self):
        ll = self.List()

        with self.assertRaises(IndexError):
            ll.pop(0)
        with self.assertRaises(IndexError):
            ll.pop_left()
        with self.assertRaises(IndexError):
            ll.pop_right()

    @given(st.lists(st.integers()), st.lists(st.integers()))
    def test_peek(self, arr1, arr2):
        ll = self.List()
        for item in arr1:
            ll.insert_left(item)
            self.assertEqual(ll.peek_left(), item)

        for item in arr2:
            ll.insert_right(item)
            self.assertEqual(ll.peek_right(), item)

        for index, item in enumerate(arr1[::-1] + arr2):
            self.assertEqual(ll.peek(index), item)

    def test_peek_empty(self):
        ll = self.List()

        with self.assertRaises(IndexError):
            ll.peek(0)
        with self.assertRaises(IndexError):
            ll.peek_left()
        with self.assertRaises(IndexError):
            ll.peek_right()

    def test_membership(self):
        arr = list(range(100))
        ll = self.List(arr)

        for i in arr:
            self.assertIn(i, ll)

        for i in range(100, 200):
            self.assertNotIn(i, ll)

    def test_random_access(self):
        ll = self.List(range(10))
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
    def test_serial_access(self, arr):
        ll = self.List(arr)
        self.assertListEqual(list(ll), arr)

    @given(st.lists(st.integers()))
    def test_serialization(self, arr):
        serialized = repr(self.List(arr))
        ll = eval(serialized)

        self.assertListEqual(list(ll), arr)
