from src.commons import key_fun


class DivideConquerSearch(object):
    """
    Base class for divide and conquer searches
    """
    def __init__(self, key=key_fun):
        self.key = key

    def get_pivot(self, low, high):
        raise NotImplementedError

    def search(self, sequence, item, left=True):
        """
        :param sequence:
        :param item:
        :param left: if True return the position of the leftmost matching item, rightmost otherwise
        """
        return self._search(sequence, item, 0, len(sequence), left)

    def _search(self, sequence, item, low, high, left):
        if low == high:
            return -1

        index = low + int(self.get_pivot(low, high))

        k = self.key(item)
        if k > self.key(sequence[index]):
            return self._search(sequence, item, index + 1, high, left)
        elif k < self.key(sequence[index]):
            return self._search(sequence, item, low, index, left)

        # TODO this might degrade on long spans
        # rewrite with recursion
        if left:
            while index and self.key(sequence[index - 1]) == k:
                index -= 1
        else:
            while index < high - 1 and self.key(sequence[index + 1]) == k:
                index += 1

        return index


class BinarySearch(DivideConquerSearch):
    def get_pivot(self, low, high):
        return (high - low) / 2


class GoldenSectionSearch(DivideConquerSearch):
    GOLDEN_SECTION_RATIO = (1 + 5 ** .5) / 2

    def get_pivot(self, low, high):
        return (high - low) / self.GOLDEN_SECTION_RATIO


# TODO need heavy revision
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fib(n):
    val = 0
    for val in fib_iter(n + 1):
        pass
    return val


def ge_fib(x):
    for i, val in enumerate(fib_iter(100)):
        if val >= x:
            return i
    return 0


class FibonacciSearch(DivideConquerSearch):
    def get_pivot(self, low, high):
        return fib(ge_fib(high - low) - 2)


# TODO
class InterpolationSearch(DivideConquerSearch):
    def get_pivot(self, low, high):
        raise NotImplementedError
