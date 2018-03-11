import unittest
from random import randint
from string import ascii_letters as letters

from hypothesis import strategies as st, given
from hypothesis import assume

from src.algorithms.strings.search import knuth_morris_pratt

# private
from src.algorithms.strings.search.knuth_morris_pratt import get_suffix_to_prefix_jump_table

from src.algorithms.strings.search.knuth_morris_pratt import get_table_active_state


# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
class TestGetSuffixToPrefixJumpTable(unittest.TestCase):

    def test_get_table_active_state(self):
        phrase = 'ABABABE'
        print(list(get_suffix_to_prefix_jump_table(phrase).keys()))
        print(get_table_active_state(phrase))

    def test_1(self):
        phrase = 'ABABAB'
        table = get_suffix_to_prefix_jump_table(phrase)
        print([i for _, i in sorted(table.items(), key=lambda x:x[0])])

    def test_AAA(self):
        phrase = 'AAA'
        expected = {
            0: -1,
            1: -1,
            2: -1,
        }

        table = get_suffix_to_prefix_jump_table(phrase)
        self.assertDictEqual(table, expected)

    def test_ABCABCCC(self):
        phrase = 'ABCDABCD'
        expected = {
            0: -1,  # A
            1: 0,  # B
            2: 0,  # C
            3: -1,  # A
            4: 0,  # B
            5: -1,  # C
            6: -1,  # C
            7: -1,  # C
        }

        table = get_suffix_to_prefix_jump_table(phrase)
        print(table)
        # self.assertDictEqual(table, expected)

    def test_wiki_1(self):
        phrase = 'ABCDABD'
        expected = {
            0: -1,  # A
            1: 0,  # B
            2: 0,  # C
            3: 0,  # D
            4: -1,  # A
            5: 0,  # B
            6: 2,  # D
        }

        table = get_suffix_to_prefix_jump_table(phrase)
        self.assertDictEqual(table, expected)

    def test_wiki_2(self):
        phrase = 'ABACABABC'
        expected = {
            0: -1,  # A
            1: 0,  # B
            2: -1,  # A
            3: 1,  # C
            4: -1,  # A
            5: 0,  # B
            6: -1,  # A
            7: 3,  # B
            8: 2,  # C
        }

        table = get_suffix_to_prefix_jump_table(phrase)
        self.assertDictEqual(table, expected)

    def test_wiki_3(self):
        phrase = 'PARTICIPATE IN PARACHUTE'
        expected = {
            0: -1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: -1, 8: 0, 9: 2, 10: 0, 11: 0, 12: 0,
            13: 0, 14: 0, 15: -1, 16: 0, 17: 0, 18: 3, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0
        }

        table = get_suffix_to_prefix_jump_table(phrase)
        self.assertDictEqual(table, expected)


@unittest.skip('TODO KMP')
class TestKnuthMorrisPratt(unittest.TestCase):

    @given(st.text(letters))
    def test_hit(self, text):
        start = randint(0, len(text))
        end = randint(start, len(text))

        phrase = text[start: end]
        self.assertGreaterEqual(text.find(phrase), 0)

        print(knuth_morris_pratt(text, phrase))
        print(text.find(phrase))
        # self.assertEqual(knuth_morris_pratt(text, phrase), text.find(phrase))

    @given(st.text(letters), st.text(letters))
    def test_miss(self, text, phrase):
        assume(text.find(phrase) == -1)
        self.assertEqual(knuth_morris_pratt(text, phrase), text.find(phrase))
