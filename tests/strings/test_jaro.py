import unittest

from src.algorithms.strings.metrics import jaro_similarity

PRECISION = 5  # places


@unittest.skip('TODO jaro')
class TestJaroSimilarity(unittest.TestCase):
    # https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance
    def test_crate_trace(self):
        self.assertAlmostEqual(jaro_similarity('crate', 'trace'), 1, places=PRECISION)

    def test_DwayNE_DuANE(self):
        self.assertAlmostEqual(jaro_similarity('dwayne', 'duane '), 0, places=PRECISION)

    # https://rosettacode.org/wiki/Jaro_distance
    def test_martha_marhta(self):
        self.assertAlmostEqual(jaro_similarity('martha', 'marhta'), 0.944444444444, places=PRECISION)

    def test_dixon_dicksonx(self):
        self.assertAlmostEqual(jaro_similarity('dixon', 'dicksonx'), 0.7666666, places=PRECISION)

    def test_jellyfish_smellyfish(self):
        self.assertAlmostEqual(jaro_similarity('jellyfish', 'smellyfish'), 0.8962962962, places=PRECISION)


@unittest.skip('TODO TestJaroWinklerSimilarity')
class TestJaroWinklerSimilarity(unittest.TestCase):
    pass
