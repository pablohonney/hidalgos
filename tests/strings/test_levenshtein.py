import unittest

# private
from src.algorithms.strings.metrics.levenshtein import levenshtein_recursive
from src.algorithms.strings.metrics.levenshtein import levenshtein_matrix
from src.algorithms.strings.metrics.levenshtein import levenshtein_compressed_matrix
from src.algorithms.strings.metrics.levenshtein import wagner_fischer_compressed_matrix
from src.algorithms.strings.metrics.levenshtein import damerau_levenshtein_recursive
from src.algorithms.strings.metrics.levenshtein import damerau_levenshtein_matrix

cases = [
    ['the', 'teh', 2],
    ['kitten', 'sitten', 1],
    ['sitten', 'sittin', 1],
    ['sittin', 'sitting', 1],
    ['kitten', 'sitting', 3],
    ['saturday', 'sunday', 3],
    ['hello', '', 5],
    ['hello', 'world', 4],
    ['wiki', 'wiki', 0]
]


class TestLevenshteinDistance(unittest.TestCase):

    def test_recursive(self):
        for s1, s2, dist in cases:
            with self.subTest('%s_%s' % (s1, s2)):
                self.assertEqual(levenshtein_recursive(s1, s2), dist)
                self.assertEqual(levenshtein_recursive(s2, s1), dist)

    def test_matrix(self):
        for s1, s2, dist in cases:
            with self.subTest('%s_%s' % (s1, s2)):
                self.assertEqual(levenshtein_matrix(s1, s2), dist)
                self.assertEqual(levenshtein_matrix(s2, s1), dist)

    def test_compressed_matrix(self):
        for s1, s2, dist in cases:
            with self.subTest('%s_%s' % (s1, s2)):
                self.assertEqual(levenshtein_compressed_matrix(s1, s2), dist)
                self.assertEqual(levenshtein_compressed_matrix(s2, s1), dist)

    def test_wagner_fischer(self):
        for s1, s2, dist in cases:
            with self.subTest('%s_%s' % (s1, s2)):
                self.assertEqual(wagner_fischer_compressed_matrix(s1, s2), dist)
                self.assertEqual(wagner_fischer_compressed_matrix(s2, s1), dist)


damerau_cases = [
    ['the', 'teh', 1],
    ['ca', 'abc', 3],
    # ['sittin', 'sitting', 1],
    # ['kitten', 'sitting', 3],
    # ['saturday', 'sunday', 3],
    # ['hello', '', 5],
    # ['helo', 'hola', 2],
    # ['wiki', 'wiki', 0]
]


class TestDamerauLevenshteinDistance(unittest.TestCase):

    def test_recursive(self):
        for s1, s2, dist in damerau_cases:
            with self.subTest('%s_%s' % (s1, s2)):
                self.assertEqual(damerau_levenshtein_recursive(s1, s2), dist)
                self.assertEqual(damerau_levenshtein_recursive(s2, s1), dist)

    def test_matrix(self):
        for s1, s2, dist in damerau_cases:
            with self.subTest('%s_%s' % (s1, s2)):
                self.assertEqual(damerau_levenshtein_matrix(s1, s2), dist)
                self.assertEqual(damerau_levenshtein_matrix(s2, s1), dist)
