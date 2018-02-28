import unittest

from src.hashes.fletcher import fletcher16_optimized


class TestFletcher(unittest.TestCase):

    @unittest.skip('TODO fletcher')
    def test_fletcher_16(self):
        self.assertEqual(fletcher16_optimized('abcde', 16), 4031760169)
        # self.assertEqual(fletcher16_optimized('abcdef', 6), 1448095018)
        # self.assertEqual(fletcher16_optimized('abcdefgh', 8), 3957429649)
