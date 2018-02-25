"""
Divide and conquer approach significantly improves over linear search.
But it requires that input be sorted.

time O(log(n))
space O(1) all cases

If one's has some extra knowledge about the input characteristics,
the division policy can be customized to make a better guess of the pivot.
"""

from src.commons import key_fun


class DivideConquerSearch(object):
    """
    Base class for divide and conquer searches
    """

    def __init__(self, key=key_fun):
        self.key = key

    def get_pivot(self, low, high):
        raise NotImplementedError

    def search(self, sequence, item, left: bool = True):
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
    """
    Values in the Fibonacci sequence have a bizarre property, they relate to
    each other with a ratio that approaches the golden section.

    lim(fib(n)/fib(n-1)) -> golden section

    Theoretically it might be easier to use these numbers to locate the 'golden' pivot
    than use the golden_section constant per se.

    As such this algorithm is a variant of GoldenSectionSearch
    """

    def get_pivot(self, low, high):
        return fib(ge_fib(high - low) - 2)


class InterpolationSearch(DivideConquerSearch):
    """
    We can try to to find closer pivot values if we know the input values are evenly distributed.

    This is a highly opinionated approach. It strongly relies on the input.
    For exponentially increasing values we'll come up locating sequential pivots that'll
    degrade the performance to linear search or even worse, given the high D&C constant.
    """
    def get_pivot_extended(self, low, high, seq, item):
        return int((item - seq[low]) * (high - low) / (seq[high] - seq[low]))

    def search(self, sequence, item, left: bool = True):
        if len(sequence) == 1:
            return 0 if self.key(sequence[0]) == item else -1

        return self._search(sequence, item, 0, len(sequence) - 1, left)

    def _search(self, sequence, item, low, high, left):
        if low >= high:
            return -1

        # check uniformity condition
        if not sequence[low] <= item <= sequence[high]:
            return -1

        index = low + int(self.get_pivot_extended(low, high, sequence, item))

        k = self.key(item)
        if k > self.key(sequence[index]):
            return self._search(sequence, item, index + 1, high, left)
        elif k < self.key(sequence[index]):
            return self._search(sequence, item, low, index - 1, left)

        return index
