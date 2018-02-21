import unittest

from src.source_coding import nysiis


class TestSoundex(unittest.TestCase):
    def test_rupert_robert(self):
        self.assertEqual(soundex('Rupert'), 'R163')
        self.assertEqual(soundex('Robert'), 'R163')

    def test_rubin(self):
        self.assertEqual(soundex('Rubin'), 'R150')

    def test_ashcraft_ashcroft(self):
        self.assertEqual(soundex('Ashcraft'), 'A261')
        self.assertEqual(soundex('ashcroft'), 'A261')

    def test_tymczak(self):
        self.assertEqual(soundex('Tymczak'), 'T522')

    def test_pfister(self):
        self.assertEqual(soundex('pfister'), 'P236')

    def test_honeyman(self):
        self.assertEqual(soundex('Honeyman'), 'H555')
