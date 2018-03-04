import unittest

from src.encoding import nysiis


# @unittest.skip('TODO nysiis. use NIST specs')
class TestNysiis(unittest.TestCase):
    def runTest(self):
        cases = {
            # 'DAGAL': 'Diggell Dougal Doughill Dougill Dowgill Dugall Dugall',
            'GLAND': 'Glinde',
            # 'PLANRAG': 'Plumridge',
            # 'SANAC': 'Chinnick Chinnock Chinnock Chomicki Chomicz Schimek Shimuk Simak Simek Simic Sinnock '
            #          'Sinnocke Sunnex Sunnucks Sunock',
            # 'WABARLY': 'Webberley Wibberley',
        }

        for code, case in cases.items():
            for name in case.split(' '):
                with self.subTest(name):
                    self.assertEqual(nysiis(name), code)
