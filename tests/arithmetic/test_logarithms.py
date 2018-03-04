import unittest

from src.arithmetic import iterative_log2


class TestIterativeLog(unittest.TestCase):

    def runTest(self):
        self.assertEqual(iterative_log2(2 ** 0), 0)
        for i in range(1, 5):
            self.assertEqual(iterative_log2(2 ** (2 ** (i - 1))), i)
