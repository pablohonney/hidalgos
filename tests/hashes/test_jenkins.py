import unittest

from src.algorithms.hashes import jenkins


class TestJenkins(unittest.TestCase):

    @unittest.skip('TODO find jenkins test data')
    def runTest(self):
        # plaintext = "Four score and seven years ago"
        # print(jenkins(plaintext))

        plaintext = "Apple"
        print(jenkins(plaintext))
