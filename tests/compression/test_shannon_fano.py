import unittest

from hypothesis import strategies as st, given

# public
from src.algorithms.compression import get_shannon_fano_table
from src.algorithms.compression import encode
from src.algorithms.compression import decode

# private
from src.algorithms.compression.shannon_fano import get_middle_index_of_equal_sums


class TestGetEqualSumsDividingIndex(unittest.TestCase):

    # https://en.wikipedia.org/wiki/Shannon%E2%80%93Fano_coding
    def test_wiki_example(self):
        values = [0.38461538, 0.17948718, 0.15384615, 0.15384615, 0.12820513]
        index = get_middle_index_of_equal_sums(values)
        self.assertEqual(index, 2)

    def test_2(self):
        values = [1, 2, 3, 4, 5]
        index = get_middle_index_of_equal_sums(values)
        self.assertEqual(index, 3)

    def test_3(self):
        values = [1, 2, 3, 3, 3, 9, 10]
        index = get_middle_index_of_equal_sums(values)
        self.assertEqual(index, 5)


class TestShannonFano(unittest.TestCase):

    @given(st.text())
    def test_prefix_code(self, plain_text):
        encoding_table = get_shannon_fano_table(plain_text)

        items = sorted(encoding_table.values(), key=len)
        for i, item in enumerate(items):
            for rest in items[i + 1:]:
                self.assertFalse(rest.startswith(item))

    # https://en.wikipedia.org/wiki/Shannon%E2%80%93Fano_coding
    # readjusted B, C, D figures to avoid equivalent encodings.
    def test_wiki_example(self):
        plain_text = 15*'A' + 8*'B' + 7*'C' + 6*'D' + 5*'E'
        expected = {'A': '00', 'B': '01', 'C': '10', 'D': '110', 'E': '111'}

        encoding_table = get_shannon_fano_table(plain_text)
        self.assertDictEqual(encoding_table, expected)

    def test_hello_world(self):
        plain_text = "hello world"

        encoding_table = get_shannon_fano_table(plain_text)
        code = ''.join(list(encode(plain_text, encoding_table)))
        restored = decode(code, encoding_table)

        self.assertEqual(plain_text, restored)

    @given(st.text())
    def test_data_driven(self, plain_text):
        encoding_table = get_shannon_fano_table(plain_text)
        code = ''.join(list(encode(plain_text, encoding_table)))
        restored = decode(code, encoding_table)

        self.assertEqual(plain_text, restored)
