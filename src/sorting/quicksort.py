"""
TODO description
"""
from src.commons import swap
from src.commons import key_fun


def get_median_of_three(sequence, lo, hi, key=key_fun):
    """
    This little func proved to be puzzling. It was hard to keep all pieces in memory.
    Thus I first wrote it in combinatorial form. Which is redundant in comparisons.

    if sequence[lo] < sequence[mid] < sequence[hi]:
        pivot = mid
    elif sequence[lo] > sequence[mid] > sequence[hi]:
        pivot = mid
    elif sequence[lo] < sequence[mid] > sequence[hi]:
        pivot = lo if sequence[lo] > sequence[hi] else hi
    elif sequence[lo] > sequence[mid] < sequence[hi]:
        pivot = lo if sequence[lo] < sequence[hi] else hi

    Than only factored out the repetitions ).

    P.S. Median of three should be more randomized, but then it'd be hard to test.
    """
    mid = (hi + lo) // 2

    lo_val = key(sequence[lo])
    mid_val = key(sequence[mid])
    high_val = key(sequence[hi])

    if lo_val < mid_val:
        if mid_val < high_val:
            pivot = mid
        elif lo_val > high_val:
            pivot = lo
        else:
            pivot = hi
    else:
        if mid_val > high_val:
            pivot = mid
        elif lo_val < high_val:
            pivot = lo
        else:
            pivot = hi

    return pivot


class BaseQuickSort(object):
    CUT_OFF = 2

    def __init__(self, key=key_fun, get_pivot=get_median_of_three, cut_off=CUT_OFF, callback=None):
        self.key = key
        self.get_pivot = get_pivot
        self.callback = callback if callback else None
        self.cut_off = cut_off

    def sort(self, sequence):
        self._sort(sequence, 0, len(sequence))

    def _sort(self, sequence, lo, hi):
        if hi - lo < self.cut_off:
            if self.callback:
                self.callback(sequence, lo, hi, self.key)
            return

        pivot = self.get_pivot(sequence, lo, hi - 1, self.key)

        pivot_lo, pivot_hi = self.partition(sequence, lo, hi-1, pivot)

        self._sort(sequence, lo, pivot_lo)
        self._sort(sequence, pivot_hi, hi)

    def partition(self, sequence, lo, hi, pivot):
        raise NotImplementedError


class QuickSortLomuto(BaseQuickSort):

    def partition(self, sequence, lo, hi, pivot):
        """
        ... lo-> ... j-> ??? | pivot

        Putting the pivot at the end is just a matter of tradition.
        """
        p_value = self.key(sequence[pivot])
        swap(sequence, pivot, hi)

        for j in range(lo, hi):
            if sequence[j] < p_value:
                swap(sequence, lo, j)
                lo += 1
        swap(sequence, lo, hi)
        return lo, lo+1


class QuickSortHoare(BaseQuickSort):

    def partition(self, sequence, lo, hi, pivot):
        """
        pivot | ... lo-> ??? <-hi ...

        This is the original quick-sort. Takes less swaps.
        """
        swap(sequence, pivot, lo)
        pivot = lo
        p_value = self.key(sequence[pivot])

        lo += 1
        while hi > lo:
            if self.key(sequence[lo]) > p_value:
                swap(sequence, lo, hi)
                hi -= 1
            else:
                lo += 1

        # depends on the which pointer had been changed the last time.
        # design flaw? Control flow should be more uniform.
        if self.key(sequence[lo]) > p_value:
            lo -= 1

        swap(sequence, pivot, lo)
        pivot = lo

        return pivot, pivot+1


class QuickSortWithEquals(BaseQuickSort):

    def partition(self, sequence, lo, hi, pivot):
        """
        pivot | ... lo-> ... eq-> ??? <-hi ...

        Prevents the values equal to the pivot from degrading the binary recursion tree.
        """
        swap(sequence, pivot, lo)
        pivot = lo
        p_value = self.key(sequence[pivot])

        lower, equal, higher = lo + 1, lo + 1, hi - 1
        while higher >= equal:
            if self.key(sequence[equal]) > p_value:
                swap(sequence, equal, higher)
                higher -= 1
            elif self.key(sequence[equal]) == p_value:
                equal += 1
            else:
                swap(sequence, lower, equal)
                lower += 1
                equal += 1

        # depends on the which pointer had been changed the last time.
        # design flaw? Control flow should be more uniform.
        if self.key(sequence[lower]) > p_value:
            lower -= 1
        if equal == len(sequence):
            equal -= 1
        if self.key(sequence[equal]) > p_value:
            equal -= 1

        swap(sequence, pivot, equal)

        return lower, equal
