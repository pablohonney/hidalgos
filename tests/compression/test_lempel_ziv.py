import unittest

from hypothesis import strategies as st, given

from src.algorithms.compression import lzw_compress
from src.algorithms.compression import lzw_decompress


class TestLempelZiv(unittest.TestCase):
    def test_abacaba(self):
        plain_text = 'abacaba'
        alphabet = set('abcd')
        expected = [0, 1, 0, 2, 4, 0]
        code = lzw_compress(plain_text, alphabet)

        self.assertEqual(code, expected)

        # @given(st.text())
        # def test_data_driven(self, plain_text):
        #     alphabet = set(plain_text)
        #     code = lzw_compress(plain_text, alphabet)
        #     restored = lzw_decompress(code, alphabet)
        #
        #     self.assertEqual(plain_text, restored)
