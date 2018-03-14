import unittest

from src.algorithms.strings.metrics import jaro_similarity


@unittest.skip('TODO jaro')
class TestJaroSimilarity(unittest.TestCase):

    def test_crate_trace(self):
        self.assertEqual(jaro_similarity('crate', 'trace'), 1)

    def test_DwayNE_DuANE(self):
        self.assertEqual(jaro_similarity('dwayne', 'duane '), 0)
