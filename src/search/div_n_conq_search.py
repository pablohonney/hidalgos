class DivideConquerSearch(object):
    """
    Generates a customizable search function based on the pivot configuration

    :param left: if True return the position of the leftmost matching item, rightmost otherwise
    :return: search function
    """

    def indexer(self, low, high):
        raise NotImplementedError

    def search(self, arr, x, left=True):
        return self._search(arr, x, 0, len(arr), left)

    def _search(self, arr, x, low, high, left):
        if low == high:
            return -1

        index = low + int(self.indexer(low, high))

        if x > arr[index]:
            return self._search(arr, x, index + 1, high, left)
        elif x < arr[index]:
            return self._search(arr, x, low, index, left)

        # TODO this might degrade on long spans
        if left:
            while index and arr[index - 1] == x:
                index -= 1
        else:
            while index < high - 1 and arr[index + 1] == x:
                index += 1
            index += 1

        return index


class BinarySearch(DivideConquerSearch):
    def indexer(self, low, high):
        return (high - low) / 2


class GoldenSectionSearch(DivideConquerSearch):
    GOLDEN_SECTION_RATIO = (1 + 5 ** .5) / 2

    def indexer(self, low, high):
        return (high - low) / self.GOLDEN_SECTION_RATIO


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
    def indexer(self, low, high):
        return fib(ge_fib(high - low) - 2)


class InterpolationSearch(DivideConquerSearch):
    pass
