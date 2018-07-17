from src.data_types.trees.tries import Trie


class PrefixTree(object):
    """
    Adapter class
    """

    def __init__(self, vocabulary):
        self.trie = Trie(vocabulary)

    def has_prefix(self, s):
        return bool(self.trie.words_starting_with(s))

    def has_word(self, s):
        return s in self.trie


class WordPuzzle(object):

    def __init__(self, trie, matrix):
        self.trie = trie
        self.words = {}
        self.matrix = matrix

        self.rows_count = len(self.matrix)
        self.cols_count = len(self.matrix[0])

    def solve(self):  # smells like java :)

        for row in range(self.rows_count):
            for col in range(self.cols_count):
                self.traverse(row, col, '', [])

        return self.words

    def traverse(self, row, col, prefix, trace):
        pos = row, col

        # trace is a double thing. It serves also as a marked pos set.
        # O(n), but easier to maintain.
        if pos in trace:
            return

        char = self.matrix[row][col]
        prefix += char

        if self.trie.has_word(prefix):
            self.words[prefix] = trace + [pos]
        if not self.trie.has_prefix(prefix):
            return

        for d_row in [0, 1, -1]:
            for d_col in [0, 1, -1]:
                if d_row == d_col == 0:
                    continue

                new_row = row + d_row
                new_col = col + d_col

                if not (0 <= new_row < self.rows_count):
                    continue

                if not (0 <= new_col < self.cols_count):
                    continue

                self.traverse(new_row, new_col, prefix, trace + [pos])


def get_trace_matrix(rows_count, cols_count, trace, matrix=None):
    m = [['_' for _ in range(cols_count)] for _ in range(rows_count)]
    for i, (row, col) in enumerate(trace):
        if matrix:
            m[row][col] = matrix[row][col]
        else:
            m[row][col] = str(i)

    return m
