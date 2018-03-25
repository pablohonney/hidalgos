import unittest

from hypothesis import strategies as st, given

from src.algorithms.compression import lzw_compress
from src.algorithms.compression import lzw_decompress


class TestLempelZivWelch(unittest.TestCase):

    def test_10a(self):
        plain_text = 10 * 'a'
        alphabet = set('a')
        expected = [0, 1, 2, 3]  # 'a aa aaa aaaa'

        code = lzw_compress(plain_text, alphabet)
        self.assertEqual(expected, code)

        restored = lzw_decompress(code, alphabet)
        self.assertEqual(plain_text, restored)

    def test_5ab(self):
        plain_text = 5 * 'ab'
        alphabet = set('ab')
        expected = [0, 1, 2, 4, 3, 1]  # 'a b ab aba ba b'

        code = lzw_compress(plain_text, alphabet)
        self.assertEqual(expected, code)

        restored = lzw_decompress(code, alphabet)
        self.assertEqual(plain_text, restored)

    def test_abacaba(self):
        plain_text = 'abacaba'
        alphabet = set('abcd')
        expected = [0, 1, 0, 2, 4, 0]

        code = lzw_compress(plain_text, alphabet)
        self.assertEqual(expected, code)

        restored = lzw_decompress(code, alphabet)
        self.assertEqual(plain_text, restored)

    @given(st.text())
    def test_data_driven(self, plain_text):
        alphabet = set(plain_text)
        code = lzw_compress(plain_text, alphabet)
        restored = lzw_decompress(code, alphabet)

        self.assertEqual(plain_text, restored)
