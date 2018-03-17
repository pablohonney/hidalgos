import unittest

from hypothesis import strategies as st, given

from src.algorithms.compression import get_tunstall_table
from src.algorithms.compression import encode_var_word as encode
from src.algorithms.compression import decode_var_word as decode


class TestTunstall(unittest.TestCase):

    # http://balapon.blogspot.am/2014/11/tunstall-code-python.html
    def test_abc(self):
        plain_text = 7 * 'a' + 2 * 'b' + 1 * 'c'
        expected_table = [
            ['b', '000'], ['c', '001'], ['ab', '010'], ['ac', '011'], ['aaa', '100'], ['aab', '101'], ['aac', '110']
        ]
        expected_keys = sorted(key for key, _ in expected_table)

        actual_table = get_tunstall_table(plain_text, 3)
        actual_keys = sorted(actual_table.keys())

        self.assertListEqual(actual_keys, expected_keys)

    # https://en.wikipedia.org/wiki/Tunstall_coding
    def test_hello_world(self):
        plain_text = 'hello, world'

        encoding_table = get_tunstall_table(plain_text, 5)
        code = encode(plain_text, encoding_table)
        restored = decode(code, encoding_table)

        self.assertEqual(restored, plain_text)

    @unittest.skip('TODO Tunstall')
    @given(st.text())
    def test_data_driven(self, plain_text):
        encoding_table = get_tunstall_table(plain_text, 3)
        code = encode(plain_text, encoding_table)
        restored = decode(code, encoding_table)

        self.assertEqual(plain_text, restored)
