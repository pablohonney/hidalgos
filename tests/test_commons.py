import unittest

from hypothesis import strategies as st, given, assume

from src.commons import binary_length


class TestBinaryLength(unittest.TestCase):

    @given(st.integers(min_value=1))
    def test_length(self, number):
        binary_string = bin(number)[2:]
        assume(binary_string[0] == '1')

        expected_length = len(binary_string)
        self.assertEqual(binary_length(number), expected_length)

    def test_zero(self):
        self.assertEqual(binary_length(0b000), 0)

    def test_leading_zeroes(self):
        self.assertEqual(binary_length(0b000111), 3)
