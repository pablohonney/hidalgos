import unittest

from src.strings.metrics import jaro


@unittest.skip('TODO jaro')
class TestJaroDistance(unittest.TestCase):

    def test_crate_trace(self):
        self.assertEqual(jaro('crate', 'trace'), 1)

    def test_DwayNE_DuANE(self):
        self.assertEqual(jaro('dwayne', 'duane '), 0)
