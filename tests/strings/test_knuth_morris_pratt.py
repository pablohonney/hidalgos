import unittest
from random import randint
from string import ascii_letters as letters

from hypothesis import strategies as st, given
from hypothesis import assume

from src.algorithms.strings.search import knuth_morris_pratt

# private
from src.algorithms.strings.search.knuth_morris_pratt import get_suffix_to_prefix_jump_table
from src.algorithms.strings.search.knuth_morris_pratt import get_suffix_to_prefix_jump_table_naive


class TestGetSuffixToPrefixJumpTable(unittest.TestCase):

    @given(st.text('abcdefg'))
    def runTest(self, phrase):
        self.assertListEqual(
            get_suffix_to_prefix_jump_table(phrase),
            get_suffix_to_prefix_jump_table_naive(phrase),
        )


# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
@unittest.skip('')
class TestGetSuffixToPrefixJumpTable(unittest.TestCase):

    def test_ABCABCCC(self):
        phrase = 'ABCDABCD'
        expected = [-1, 0, 0, -1, 0, -1, -1, -1]

        table = get_suffix_to_prefix_jump_table(phrase)
        print(table)
        # self.assertDictEqual(table, expected)

    def test_wiki_1(self):
        phrase = 'ABCDABD'
        expected = [-1, 0, 0, 0, -1, 0, 2]

        table = get_suffix_to_prefix_jump_table(phrase)
        self.assertDictEqual(table, expected)

    def test_wiki_2(self):
        phrase = 'ABACABABC'
        expected = [-1, 0, -1, 1, -1, 0, -1, 3, 2]

        table = get_suffix_to_prefix_jump_table(phrase)
        self.assertDictEqual(table, expected)

    def test_wiki_3(self):
        phrase = 'PARTICIPATE IN PARACHUTE'
        expected = [
            -1, 0, 0, 0, 0, 0, 0, -1, 0, 2, 10, 10, 10,
            10, 10, 1 - 1, 10, 10, 13, 10, 20, 20, 20, 20
        ]

        table = get_suffix_to_prefix_jump_table(phrase)
        self.assertDictEqual(table, expected)


class TestKnuthMorrisPratt(unittest.TestCase):

    @given(st.text(letters))
    def test_hit(self, text):
        start = randint(0, len(text))
        end = randint(start, len(text))

        phrase = text[start: end]
        self.assertGreaterEqual(text.find(phrase), 0)

        self.assertEqual(knuth_morris_pratt(text, phrase), text.find(phrase))

    @given(st.text(letters), st.text(letters))
    def test_miss(self, text, phrase):
        assume(text.find(phrase) == -1)
        self.assertEqual(knuth_morris_pratt(text, phrase), text.find(phrase))
