"""
MergeSort

Asymptotic properties...
recursion depth is fixed at O(log(n))
merging at each level takes O(n) time and O(n) space
this results in O(n*log(n)) time and O(n) auxiliary space for all cases (best, average, worst)

Other properties...
Stable: equal elements keep initial relative order. Implementation sensitive. [1(A), 8, 1(B)] -> [1(A), 1(B), 8]
On-line: doesn't need all the data at once. thus good for external sorting. compare to quick-sort
Lacks in-placement: Can be imitated with linked lists.

Some optimizations...
Runtime: minimize comparisons
    - observation: one of the halves may exhaust much earlier. no need for

Runtime: use simpler algorithm deeper in recursion tree.
    - observation 1: data in the wild is usually semi-sorted. smaller input chunks deeper in the tree may
        be fast-exited. We need a fast-exit algorithm here.
    - observation 2: simpler algorithms with no recursion overhead may beat heavy-weight algos for smaller inputs.
        consider O(n**2) with C1 vs O(n*log(n)) with C2. where C1 < C2.
        e.g for C2 = 4*C1, n = [5, 10, 15, 20]
            5  -> 25*C1  < 11*4*C1  simple sort wins
            10 -> 100*C1 < 33*4*C1
            15 -> 225*C1 < 58*4*C1
            20 -> 400*C1 > 86*4*C1  O(n*log(n)) wins from here on

            The exact threshold size is configured by the C1/C2 ratio, which is implementation dependent
    - cf. timsort = mergesort + insertion sort (O(n**2) with low C and fast-exit, it's also in-place).

Memory impact: n/2 auxiliary continuous space  // better solution seems possible, might need some creepy code
Memory impact: Can be solved with constant auxiliary space with linked-list. Coming soon :)
"""

from math import ceil

from src.commons import cmp_fun
from src.commons import key_fun


class MergeSort(object):
    CUT_OFF = 2  # merge sort base case

    def __init__(self, cmp=cmp_fun, key=key_fun, cut_off=CUT_OFF, callback=None):
        self.cmp = cmp
        self.key = key
        self.callback = callback if callback else None
        self.cut_off = cut_off

    def sort(self, arr):
        self._sort(arr, 0, len(arr))

    def _sort(self, arr, start, end):
        """
        base cases
        [] -> []
        [a] -> [a]

        recursive cases
        [a, b] -> [a] + [b]
        [a, b, c] -> [a] + [b, c]
        [a, b, c, d] -> [a, b] + [c, d]
        [a, b, c, d, e] -> [a, b] + [c, d, e]
        etc
        """

        if end - start < self.cut_off:
            if self.callback:
                self.callback(arr, start, end, self.cmp, self.key)
            return

        mid = ceil((start + end) / 2)
        self._sort(arr, start, mid)
        self._sort(arr, mid, end)
        self._merge(arr, start, mid, end)

    # O(n) time [n/2 more operation], O(n) space [n/2 less space, the rest is in-place]
    # left & right halves should be equal !
    def _merge(self, arr, start, mid, end):
        left = arr[start:mid]
        l_size = mid - start
        r_size = end - mid

        i, j = 0, 0
        while i < l_size and j < r_size:
            if self.cmp(self.key(left[i]), self.key(arr[mid + j])) < 1:
                arr[start + i + j] = left[i]
                i += 1
            else:
                arr[start + i + j] = arr[mid + j]
                j += 1

        while i < l_size:
            arr[start + i + j] = left[i]
            i += 1

        while j < r_size:
            arr[start + i + j] = arr[mid + j]
            j += 1


# O(n) time, O(n) space
def sort_online(left, right):

    while left and right:
        if left[-1] <= right[-1]:
            yield left.pop()
        else:
            yield right.pop()

    while left:
        yield left.pop()

    while right:
        yield right.pop()


