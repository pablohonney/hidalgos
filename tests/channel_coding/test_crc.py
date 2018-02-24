import unittest

from hypothesis import strategies as st, given

from src.channel_coding import crc


class TestCrc(unittest.TestCase):

    def test_110110_1011(self):
        code = crc(0b110110, 0b1011)
        self.assertEqual(code, 2)
        self.assertEqual(crc(0b110110, 0b1011, code), 0)

    @given(st.integers(min_value=1), st.integers(min_value=1))
    def test_property(self, plain_text, divisor):
        code = crc(plain_text, divisor)
        self.assertEqual(crc(plain_text, divisor, code), 0)
