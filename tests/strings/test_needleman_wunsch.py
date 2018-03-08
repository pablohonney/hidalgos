import unittest

from src.algorithms.strings.alignment import needleman_wunsch


class TestNeedlemanWunsch(unittest.TestCase):

    @unittest.skip('TODO needleman wunsch')
    def test_GCATGCU_GATTACA(self):
        actual = needleman_wunsch('GCATGCU', 'GATTACA')
        print(actual)