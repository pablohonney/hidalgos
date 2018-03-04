import unittest

from src.encoding import soundex
from src.encoding import refined_soundex
from src.encoding import daitch_mokotoff


class TestSoundex(unittest.TestCase):

    def runTest(self):
        cases = {
            'R163': 'Rupert Robert',
            'R150': 'Rubin',
            'A261': 'Ashcroft Ashcroft',
            'T522': 'Tymczak',
            'P236': 'pfister',
            'H555': 'Honeyman',
            'F234': 'Fusedale',
            'G535': 'Genthner Gentner Gianettini Gunton',
            'G640': 'Garlee Garley Garwell Garwill Gerrell Gerrill Giral Gorelli Gorioli Gourlay Gourley '
                    'Gourlie Graal Grahl Grayley Grealey Greally Grealy Grioli Groll Grolle Guerola Gurley',
            'H326': 'Hadcroft Hadgraft Hatchard Hatcher Hatzar Hedger Hitscher Hodcroft Hutchcraft',
            'P630': 'Parade Pardew Pardey Pardi Pardie Pardoe Pardue Pardy Parradye Parratt Parrett Parrot '
                    'Parrott Pearde Peart Peaurt Peert Perdue Peret Perett Perot Perott Perotti Perrat '
                    'Perrett Perritt Perrot Perrott Pert Perutto Pirdue Pirdy Pirot Pirouet Pirt Porrett '
                    'Porritt Port Porte Portt Prate Prati Pratt Pratte Pratty Preddy Preedy Preto Pretti '
                    'Pretty Prewett Priddey Priddie Priddy Pride Pridie Pritty Prott Proud Prout Pryde '
                    'Prydie Purdey Purdie Purdy',
        }

        for code, case in cases.items():
            for name in case.split(' '):
                with self.subTest(name):
                    self.assertEqual(soundex(name), code)


class TestRefinedSoundex(unittest.TestCase):

    def runTest(self):
        cases = {
            'B1905': 'Braz Broz',
            'C30908': 'Caren Caron Carren Charon Corain Coram Corran Corrin '
                      'Corwin Curran Curreen Currin Currom Currum Curwen',
            'H093': 'Hairs Hark Hars Hayers Heers Hiers',
            'L7081096': 'Lambard Lambart Lambert Lambird Lampaert Lampard Lampart '
                        'Lamperd Lampert Lamport Limbert Lombard',
            'N807608': 'Nolton Noulton',
        }

        for code, case in cases.items():
            for name in case.split(' '):
                with self.subTest(name):
                    self.assertEqual(refined_soundex(name), code)


class TestDaitchMokotoff(unittest.TestCase):

    @unittest.skip('TODO jewish soundex')
    def runTest(self):
        cases = {
            '147740': 'Iozefovich Jacobovitch Jacobovitz Jacobowicz Jacobowits Jacobowitz Josefovic Josefowicz '
                      'Josifovic Josifovitz Josipovic Josipovitz Josofovitz Jozefowicz Yezafovich',
            '147750': 'Iozefovich Josefovic Josifovic Josipovic Yezafovich',
            '345750': 'Dashkovich Djakovic Djekovic Djokovic',
            '783940': 'Baldrick Fielders Walters Weldrick Wolters',
            '783950': 'Baldrick Weldrake Weldrick Welldrake',
            '964660': 'Runchman Runcieman Runciman',
            '965660': 'Runchman Runcieman Runciman',
            '596490': 'Grancher Greenacre',
            '596590': 'Gehringer Grainger Grancher Granger Grangier Greenacre Grunguer',
        }
        for code, case in cases.items():
            for name in case.split(' '):
                with self.subTest(name):
                    self.assertEqual(daitch_mokotoff(name), code)
