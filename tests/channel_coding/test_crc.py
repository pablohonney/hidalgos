import unittest

import hypothesis as hypo
from hypothesis import strategies as st

from src.channel_coding.crc import crc
from src.channel_coding.crc import binary_length


class TestCrc(unittest.TestCase):

    def test_110110_1011(self):
        code = crc(0b110110, 0b1011)
        self.assertEqual(code, 2)
        self.assertEqual(crc(0b110110, 0b1011, code), 0)

    @hypo.given(st.integers(min_value=1), st.integers(min_value=1))
    def test_property(self, data, divisor):
        code = crc(data, divisor)
        self.assertEqual(crc(data, divisor, code), 0)


class TestBinaryLength(unittest.TestCase):

    @hypo.given(st.integers(min_value=1))
    def test_length(self, number):

        binary_string = bin(number)[2:]
        hypo.assume(binary_string[0] == '1')

        expected_length = len(binary_string)
        self.assertEqual(binary_length(number), expected_length)

    def test_zero(self):
        self.assertEqual(binary_length(0b000), 0)

    def test_leading_zeroes(self):
        self.assertEqual(binary_length(0b000111), 3)
