import unittest

from src.algorithms.miscellaneous.word_puzzle import (
    PrefixTree,
    WordPuzzle,
    get_trace_matrix,
)

vocabulary = [
    'hell',
    'hello',
    'help',
    'hero',
    'herb',
    'pole',
    'poll',
    'he',
    'she',
    'bolt',
]


class TestSolve(unittest.TestCase):
    VERBOSE = False

    def setUp(self):
        self.trie = PrefixTree(vocabulary)

    def test_2_2(self):
        matrix = [
            ['h', 'e'],
            ['l', 'p'],
        ]
        result_list = WordPuzzle(self.trie, matrix).solve()

        self.assertEqual(result_list, {
            'help': [(0, 0), (0, 1), (1, 0), (1, 1)],
            'he': [(0, 0), (0, 1)]
        })

    def test_3_3(self):
        matrix = [
            ['h', 'e', 'u'],
            ['b', 'l', 'p'],
            ['t', 'o', 'l'],
        ]

        solver = WordPuzzle(self.trie, matrix)
        result_list = solver.solve()

        if self.VERBOSE:
            for _, trace in result_list.items():
                m = get_trace_matrix(solver.rows_count, solver.cols_count, trace)
                for row in m:
                    print(row)
                print('')

        # check words
        self.assertListEqual(
            sorted([
                'he',
                'hell',
                'hello',
                'help',
                'pole',
                'poll',
                'bolt',
            ]),
            sorted(result_list.keys())
        )

        # check traces
        for expected_word, trace in result_list.items():
            word = ''.join(matrix[row][col] for (row, col) in trace)
            self.assertEqual(expected_word, word)
