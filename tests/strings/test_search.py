import unittest
from string import ascii_lowercase as letters
from random import randint

from hypothesis import strategies as st, given, assume

from src.algorithms.strings.search import naive_search


class TestNaiveSearch(unittest.TestCase):
    @given(st.text(letters))
    def test_hit(self, text):
        start = randint(0, len(text))
        end = randint(start, len(text))

        phrase = text[start: end]
        self.assertGreaterEqual(text.find(phrase), 0)

        self.assertEqual(naive_search(text, phrase), text.find(phrase))

    @given(st.text(letters), st.text(letters))
    def test_miss(self, text, phrase):
        assume(text.find(phrase) == -1)
        self.assertEqual(naive_search(text, phrase), text.find(phrase))
