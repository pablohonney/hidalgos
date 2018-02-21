import unittest
from string import ascii_letters as letters

from hypothesis import strategies as st, given

from src.source_coding import encode_run_length
from src.source_coding import decode_run_length


class TestRunLengthEncoding(unittest.TestCase):
    def test_www(self):
        self.assertEqual('3w', encode_run_length('www'))

    @given(st.text(alphabet=letters))
    def test_round_trip(self, plain_text):
        self.assertEqual(decode_run_length(encode_run_length(plain_text)), plain_text)
