import unittest

from src.strings.metrics.levenshtein import levenshtein_recursive
from src.strings.metrics.levenshtein import levenshtein_matrix
from src.strings.metrics.levenshtein import levenshtein_compressed_matrix


cases = [
    # ['kitten', 'sitten', 1],
    ['sitten', 'sittin', 1],
    # ['sittin', 'sitting', 1],
    # ['hello', '', 5],
    # ['hello', 'world', 4],
]


class TestHammingDistance(unittest.TestCase):

    def test_recursive(self):
        for s1, s2, dist in cases:
            with self.subTest('%s_%s' % (s1, s2)):
                self.assertEqual(levenshtein_recursive(s1, s2), dist)
                self.assertEqual(levenshtein_recursive(s2, s1), dist)

    def test_matrix(self):
        for s1, s2, dist in cases:
            with self.subTest('%s_%s' % (s1, s2)):
                self.assertEqual(levenshtein_matrix(s1, s2), dist)
                # self.assertEqual(levenshtein_matrix(s2, s1), dist)

    def test_compressed_matrix(self):
        for s1, s2, dist in cases:
            with self.subTest('%s_%s' % (s1, s2)):
                self.assertEqual(levenshtein_compressed_matrix(s1, s2), dist)
                # self.assertEqual(levenshtein_compressed_matrix(s2, s1), dist)
