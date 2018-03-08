from random import randint
from functools import reduce


class MatrixError(Exception):
    pass


class MatrixMismatchError(MatrixError):
    pass


class MatrixProportionsError(MatrixError):
    pass


class IrregularMatrixError(MatrixProportionsError):
    pass


class MatrixEqualEdgesError(MatrixProportionsError):
    pass


class Matrix(object):

    @staticmethod
    def check_dimensions(matrix):
        dimensions = map(lambda x: len(x), matrix)

        size = reduce(lambda x, y: x if x == y else None, dimensions)

        if size:
            return size
        else:
            raise IrregularMatrixError

    @property
    def linearize(self):
        return reduce(lambda x, y: x + y, [i for i in self])

    @property
    def max(self):
        return max(self.linearize)

    @property
    def min(self):
        return min(self.linearize)

    @property
    def sum(self):
        return sum(self.linearize)

    @property
    def average(self):
        return self.sum / float(len(self.linearize))

    def __init__(self, multilist=None):

        if isinstance(multilist, (str, bytes)):
            multilist = map(lambda x: map(lambda y: int(y), x.split()), multilist.strip().split('\n'))

        if multilist:
            self.check_dimensions(multilist)
            self._matrix = [[item for item in _list] for _list in multilist]
        else:
            self._matrix = []

    def __call__(self, raw, column):
        return self._matrix[raw][column]

    def __repr__(self):
        size = max(map(lambda x: len(str(x)), [self.max, self.min]))
        l = list(
            map(lambda raw: ' '.join(map(lambda letter: '%{0}s'.format(size) % letter, raw)), self._matrix))

        return '%s(%s)' % (self.__class__.__name__, repr(l))

    def __str__(self):
        size = max(map(lambda x: len(str(x)), [self.max, self.min]))
        return '\n'.join(
            map(lambda raw: ' '.join(map(lambda letter: '%{0}s'.format(size) % letter, raw)), self._matrix))
        # return '\n'.join(map(lambda raw: str(raw), self._matrix))

    def __len__(self):
        return len(self._matrix)

    def __getitem__(self, item):
        return self._matrix[item]

    @property
    def delta(self):
        raw_size = len(self)
        column_size = self.check_dimensions(self)

        if raw_size != column_size:
            raise MatrixEqualEdgesError

        if raw_size == column_size == 2:
            return self(0, 0) * self(1, 1) - self(1, 0) * self(0, 1)

        head = self[0]
        body = self._matrix[1:]

        delta = 0

        for i, raw in enumerate(self._matrix):
            delta += (-1) ** i * head[i] * Matrix(map(lambda x: x[:i] + x[i + 1:], body)).delta

        return delta

    # -------- ITERATIONS --------

    def raws(self):
        return iter(self._matrix)

    def columns(self):
        return iter(map(lambda x: list(x), zip(*self._matrix)))

    def __iter__(self):
        return self.raws()

    # -------- COMPARISONS --------

    def compare_size(self, other):
        if len(self) != len(other):
            return False

        if self.check_dimensions(self) != self.check_dimensions(other):
            return False

        return True

    def __eq__(self, other):
        if not self.compare_size(other):
            return False

        return all(map(lambda x: x[0] == x[1], zip(self, other)))

    def __ne__(self, other):
        return not self != other

    def op(self, other, func):

        if isinstance(other, (int, float)):
            return Matrix([[func(self(i, j), other) for j, _ in enumerate(raw)] for i, raw in enumerate(self)])

        if not self.compare_size(other):
            raise MatrixMismatchError

        return Matrix([[func(self(i, j), other(i, j)) for j, _ in enumerate(raw)] for i, raw in enumerate(self)])

    def __add__(self, other):
        return self.op(other, lambda x, y: x + y)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self.op(other, lambda x, y: x - y)

    def __mul__(self, other):
        return self.op(other, lambda x, y: x * y)

    def __rmul__(self, other):
        return self * other

    def __div__(self, other):
        return self.op(other, lambda x, y: x / y)

    def __floordiv__(self, other):
        return self.op(other, lambda x, y: x // y)

    def __mod__(self, other):
        return self.op(other, lambda x, y: x % y)

    def __pow__(self, power, modulo=None):
        return self.op(power, lambda x, y: x ** y)


class DefaultMatrix(Matrix):
    SYMBOL = ''

    def __init__(self, rows, columns, symbol=SYMBOL):
        self.row_count = rows
        self.col_count = columns
        self.symbol = symbol
        self._matrix = [[self.symbol for _ in range(self.col_count)] for _ in range(self.row_count)]

    def __repr__(self):
        return '%s(%s, %s, %s)' % (self.__class__.__name__, self.row_count, self.col_count, self.symbol)


class OneSymbolMatrix(DefaultMatrix):
    SYMBOL = NotImplemented

    def __init__(self, rows, columns):
        if self.SYMBOL is NotImplemented:
            raise NotADirectoryError

        super(OneSymbolMatrix, self).__init__(rows, columns, self.SYMBOL)

    def __repr__(self):
        return '%s(%s, %s)' % (self.__class__.__name__, self.row_count, self.col_count)


class Zeros(OneSymbolMatrix):
    SYMBOL = 0


class Ones(OneSymbolMatrix):
    SYMBOL = 1


class RandomMatrix(Matrix):

    def __init__(self, row_count, col_count, min_value, max_value):
        self._matrix = [[randint(min_value, max_value) for _ in range(col_count)] for _ in range(row_count)]
