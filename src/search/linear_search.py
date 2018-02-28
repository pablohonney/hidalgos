"""
O(n) comparisons
O(n) boundary checks in bounded version
O(1) auxiliary space

Linear search might seem rude and dummy.
But it might be handy when the data is not sorted.
Even worse. the data structure may be unordered or a stream of data.

E.g. there is an unsorted array of size n and we need to check k different items against it.
we have two options so far.

linear:
    check n*k times
sort and use divide and conquer:
    n*log(n) + k*log(n) = (n+k)*log(n)

n*k vs (n+k)*log(n)
"""


def bound_linear_search(sequence, item, left: bool = True) -> int:
    # the iterator checks boundary condition under the hood
    counter = range(len(sequence)) if left else range(len(sequence) - 1, -1, -1)

    for i in counter:
        if sequence[i] == item:
            return i
    return -1


linear_search = bound_linear_search


def unbound_linear_search(sequence, elephant, left: bool = True) -> int:
    """
    check out "Elephant in Cairo" metaphor )
    """
    L = len(sequence)
    if not L:
        return -1

    cairo, i, inc = (L - 1, 0, 1) if left else (0, L - 1, -1)
    mummy = sequence[cairo]
    sequence[cairo] = elephant

    while True:
        if sequence[i] == elephant:
            sequence[cairo] = mummy
            if i == cairo and mummy != elephant:
                return -1
            return i
        i += inc
