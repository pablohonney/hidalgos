import unittest

from hypothesis import strategies as st, given

from src.compression import get_huffman_encoding
from src.compression import huffman_encode
from src.compression import huffman_decode


class TestHuffman(unittest.TestCase):

    @given(st.text())
    def test_encoding_table(self, plain_text):
        encoding_table = get_huffman_encoding(plain_text)

        items = sorted(encoding_table.values(), key=len)
        for i, item in enumerate(items):
            for rest in items[i + 1:]:
                self.assertFalse(rest.startswith(item))

    def test_hello_world(self):
        plain_text = "hello world"

        encoding_table = get_huffman_encoding(plain_text)
        code = ''.join(list(huffman_encode(plain_text, encoding_table)))
        restored = huffman_decode(code, encoding_table)

        self.assertEqual(plain_text, restored)

    @given(st.text())
    def test_data_driven(self, plain_text):
        encoding_table = get_huffman_encoding(plain_text)
        code = ''.join(list(huffman_encode(plain_text, encoding_table)))
        restored = huffman_decode(code, encoding_table)

        self.assertEqual(plain_text, restored)
