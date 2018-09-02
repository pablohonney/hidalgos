import unittest
from string import ascii_lowercase as lowercase

from hypothesis import given, strategies as st

from src.algorithms.compression import encode_move_to_front
from src.algorithms.compression import decode_move_to_front


class TestMoveToFront(unittest.TestCase):

    def test_encode_bananaaa(self):
        plain_text = 'bananaaa'
        expected = [1, 1, 13, 1, 1, 1, 0, 0]
        code = encode_move_to_front(plain_text, lowercase)
        self.assertEqual(code, expected)

    def test_decode_bananaaa(self):
        code = [1, 1, 13, 1, 1, 1, 0, 0]
        expected = 'bananaaa'
        plain_text = decode_move_to_front(code, lowercase)
        self.assertEqual(plain_text, expected)

    def test_mtf_empty(self):
        code = encode_move_to_front('', '')
        self.assertEqual(code, [])

        plain_text = decode_move_to_front([], '')
        self.assertEqual(plain_text, '')

    @given(st.text())
    def test_property(self, plain_text):
        code = encode_move_to_front(plain_text, set(plain_text))
        restored = decode_move_to_front(code, set(plain_text))

        self.assertEqual(restored, plain_text)
