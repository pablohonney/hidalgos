import unittest
from itertools import islice

from hypothesis import strategies as st, given

from src.algorithms.compression import encode
from src.algorithms.compression import get_shannon_table
from src.algorithms.compression import decode


class TestShannon(unittest.TestCase):

    def test_wiki_example(self):
        plain_text = 36 * 'a' + 18 * 'b' + 17 * 'c' + 12 * 'd' + 9 * 'e' + 7 * 'f'
        expected_table = {
            'a': '00',
            'b': '010',
            'c': '100',
            'd': '1011',
            'e': '1101',
            'f': '1110',
        }

        encoding_table = get_shannon_table(plain_text)
        self.assertDictEqual(encoding_table, expected_table)

    @given(st.text())
    def test_prefix_code(self, plain_text):
        encoding_table = get_shannon_table(plain_text)

        items = sorted(encoding_table.values(), key=len)
        for i, item in enumerate(items):
            for rest in items[i + 1:]:
                self.assertFalse(rest.startswith(item))

    def test_hello_world(self):
        plain_text = "hello world"

        table = get_shannon_table(plain_text)
        code = ''.join(list(encode(plain_text, table)))
        restored = decode(code, table)

        self.assertEqual(plain_text, restored)

    @given(st.text())
    def test_data_driven(self, plain_text):
        encoding_table = get_shannon_table(plain_text)
        code = ''.join(list(encode(plain_text, encoding_table)))
        restored = decode(code, encoding_table)

        self.assertEqual(plain_text, restored)
