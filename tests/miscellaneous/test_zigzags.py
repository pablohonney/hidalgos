import unittest

from src.algorithms.miscellaneous.zigzags import (
    zigzags,
    LongestRunHandler,
    AllRunsHandler,
)

REGRESSION = 1


def regression(method):
    return unittest.skipUnless(REGRESSION, 'regression test')(method)


def get_longest_run(seq):
    return zigzags(seq, LongestRunHandler())


def get_all_runs(seq):
    return zigzags(seq, AllRunsHandler())


class TestGetLongestRun(unittest.TestCase):
    def test_0_1_2(self):
        self.assertEqual((0, 0), get_longest_run([]))
        self.assertEqual((0, 0), get_longest_run([1]))
        self.assertEqual((0, 0), get_longest_run([1, 2]))

    def test_3_up(self):
        given = [1, 2, 3]
        expected = (0, 0)

        got = get_longest_run(given)
        self.assertEqual(expected, got)

    def test_3_down(self):
        given = [3, 2, 1]
        expected = (0, 0)

        got = get_longest_run(given)
        self.assertEqual(expected, got)

    def test_3_up_down(self):
        given = [1, 3, 2]
        expected = (0, 3)

        got = get_longest_run(given)
        self.assertEqual(expected, got)

    def test_4_up_down(self):
        given = [1, 3, 2, 4]
        expected = (0, 4)

        got = get_longest_run(given)
        self.assertEqual(expected, got)

    def test_7_with_2_runs(self):
        given = [5, 2, 3, 4, 2, 5, 3]
        expected = (2, 7)

        got = get_longest_run(given)
        self.assertEqual(expected, got)

    def test_second_of_2(self):
        given = [1, 4, 2, 5, 6, 7, 4, 9, 2, 5]
        expected = (4, 10)

        got = get_longest_run(given)
        self.assertEqual(expected, got)

    def test_first_of_2(self):
        given = [1, 4, 2, 5, 2, 6, 7, 4, 9]
        expected = (0, 6)

        got = get_longest_run(given)
        self.assertEqual(expected, got)

    def test_middle_of_3(self):
        given = [5, 4, 7, 5, 1, 4, 2, 6, 1, 5, 2, 6, 7, 4, 9]
        expected = (3, 12)

        got = get_longest_run(given)
        self.assertEqual(expected, got)

    def test_exercise(self):
        given = [1, 3, 2, 8, 5, 7, 6, 4, 3]
        expected = (0, 7)

        got = get_longest_run(given)
        self.assertEqual(expected, got)


class TestGetAllRuns(unittest.TestCase):
    def test_4_up_down(self):
        given = [1, 3, 2, 4]
        expected = [(0, 4)]

        got = get_all_runs(given)
        self.assertEqual(expected, got)

    def test_7_with_2_runs(self):
        given = [5, 2, 3, 4, 2, 5, 3]
        expected = [(0, 3), (2, 7)]

        got = get_all_runs(given)
        self.assertEqual(expected, got)

    def test_second_of_2(self):
        given = [1, 4, 2, 5, 6, 7, 4, 9, 2, 5]
        expected = [(0, 4), (4, 10)]

        got = get_all_runs(given)
        self.assertEqual(expected, got)

    def test_first_of_2(self):
        given = [1, 4, 2, 5, 2, 6, 7, 4, 9]
        expected = [(0, 6), (5, 9)]

        got = get_all_runs(given)
        self.assertEqual(expected, got)

    def test_middle_of_3(self):
        given = [5, 4, 7, 5, 1, 4, 2, 6, 1, 5, 2, 6, 7, 4, 9]
        expected = [(0, 4), (3, 12), (11, 15)]

        got = get_all_runs(given)
        self.assertEqual(expected, got)
