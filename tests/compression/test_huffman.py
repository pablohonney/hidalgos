import unittest

from hypothesis import strategies as st, given

from src.algorithms.compression import get_huffman_table
from src.algorithms.compression import encode_var_code as encode
from src.algorithms.compression import decode_var_code as decode


class TestHuffman(unittest.TestCase):

    @given(st.text())
    def test_prefix_code(self, plain_text):
        encoding_table = get_huffman_table(plain_text)

        items = sorted(encoding_table.values(), key=len)
        for i, item in enumerate(items):
            for rest in items[i + 1:]:
                self.assertFalse(rest.startswith(item))

    def test_hello_world(self):
        plain_text = "hello world"

        table = get_huffman_table(plain_text)
        code = ''.join(list(encode(plain_text, table)))
        restored = decode(code, table)

        self.assertEqual(plain_text, restored)

    @given(st.text())
    def test_data_driven(self, plain_text):
        encoding_table = get_huffman_table(plain_text)
        code = ''.join(list(encode(plain_text, encoding_table)))
        restored = decode(code, encoding_table)

        self.assertEqual(plain_text, restored)
