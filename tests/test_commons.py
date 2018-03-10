import unittest
from itertools import islice

from hypothesis import strategies as st, given, assume

from src.commons import binary_length
from src.commons import float_to_binary


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


class TestFloatToBinary(unittest.TestCase):

    def test_36(self):
        digits = []
        for digit in islice(float_to_binary(0.36), 4):
            digits.append(digit)

        self.assertListEqual(digits, [0, 1, 0, 1])

    # https://en.wikipedia.org/wiki/Shannon_coding
    def test_wiki_example(self):
        float_to_binary_table = {
            0.0: '0000',
            0.36: '0101',
            0.54: '1000',
            0.72: '1011',
            0.84: '1101',
            0.93: '1110',
        }

        for float_, expected in float_to_binary_table.items():
            digits = []
            for digit in islice(float_to_binary(float_), len(expected)):
                digits.append(str(digit))

            self.assertEqual(''.join(digits), expected)
