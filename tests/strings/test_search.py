import unittest
from string import ascii_lowercase as letters
from random import randint

from hypothesis import strategies as st, given, assume

from src.strings.search import naive_search
from src.strings.search import rabin_karp
from src.strings.search.rabin_karp import rabin_fingerprint


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


class TestRabinKarp(unittest.TestCase):

    def test_rabin_fingerprint(self):
        print(rabin_fingerprint('world'))

    def test_dummy(self):
        print(rabin_karp('hello world', 'world'))
    #
    # @given(st.text(letters))
    # def test_hit(self, text):
    #     start = randint(0, len(text))
    #     end = randint(start, len(text))
    #
    #     phrase = text[start: end]
    #     self.assertGreaterEqual(text.find(phrase), 0)
    #
    #     self.assertEqual(rabin_karp(text, phrase), text.find(phrase))
    #
    # @given(st.text(letters), st.text(letters))
    # def test_miss(self, text, phrase):
    #     assume(text.find(phrase) == -1)
    #     self.assertEqual(rabin_karp(text, phrase), text.find(phrase))
