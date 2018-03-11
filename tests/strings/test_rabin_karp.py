import unittest
from string import ascii_lowercase as letters
from random import randint

from hypothesis import strategies as st, given, assume

# private
from src.algorithms.strings.search.rabin_karp import rabin_karp
from src.algorithms.strings.search.rabin_karp import rabin_fingerprint
from src.algorithms.strings.search.rabin_karp import rabin_roller
from src.algorithms.strings.search.rabin_karp import BASE


class TestRabinKarp(unittest.TestCase):

    def test_rabin_fingerprint(self):
        expected = ord('c') + ord('a') * BASE + ord('t') * (BASE ** 2)
        self.assertEqual(rabin_fingerprint('cat'), expected)

    def test_rabin_roller_byte_sequence(self):
        self.assertListEqual(list(rabin_roller('abcde', 1)), [97, 98, 99, 100, 101])

    def test_rabin_roller_same_letters(self):
        for code in rabin_roller('aaaaaaaaaaa', 3):
            self.assertEqual(rabin_fingerprint('aaa'), code)

    def test_rabin_roller(self):
        roller = iter(rabin_roller('python', 3))
        self.assertEqual(rabin_fingerprint('pyt'), next(roller))
        self.assertEqual(rabin_fingerprint('yth'), next(roller))
        self.assertEqual(rabin_fingerprint('tho'), next(roller))
        self.assertEqual(rabin_fingerprint('hon'), next(roller))

    def test_rabin_roller_whitespace(self):
        roller = iter(rabin_roller('pyt hon', 5))
        self.assertEqual(rabin_fingerprint('pyt h'), next(roller))
        self.assertEqual(rabin_fingerprint('yt ho'), next(roller))
        self.assertEqual(rabin_fingerprint('t hon'), next(roller))

    @given(st.text(letters))
    def test_hit(self, text):
        start = randint(0, len(text))
        end = randint(start, len(text))

        phrase = text[start: end]
        self.assertGreaterEqual(text.find(phrase), 0)

        self.assertEqual(rabin_karp(text, phrase), text.find(phrase))

    @given(st.text(letters), st.text(letters))
    def test_miss(self, text, phrase):
        assume(text.find(phrase) == -1)
        self.assertEqual(rabin_karp(text, phrase), text.find(phrase))

    @given(st.text(letters, min_size=10))
    def test_multiple_hit(self, text):
        size = randint(1, 7)
        assume(size < len(text))

        phrases = []
        for _ in range(5):
            start = randint(0, len(text))
            end = randint(start, len(text))

            phrase = text[start: end]
            self.assertGreaterEqual(text.find(phrase), 0)
            phrases.append(phrase[:size].zfill(20))

        self.assertEqual(rabin_karp(text, *phrases), min(map(text.find, phrases)))
