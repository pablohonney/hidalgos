"""
Bubble sort.
    properties:
        - in-place
        - off-line
        - stable?  [prove it with loop invariants. That'll be really nerdy :)]
        - fast-exit
        - requires random access data

observations on input cases:
    Average case: unsorted array
    O(n**2) comparisons
    O(n**2) swaps

    Best case: sorted array
    [1, 2, 3] -> [1, 2, 3]
    O(n) comparisons
    no swaps

    Worst case turned into best case:  reverse sorted array
    This goes like extra unsorted to the naive naives.
    [3, 2, 1] -> [2, 1, 3] -> [1, 2, 3]
    Unless we oscillate the direction.
    I strongly believe we can use some heuristics here. like running through the array twice in both directions
    and gathering some stats on the degree of sortedness from the two perspectives. Then we can go with the cheaper
    direction and reverse the direction if needed in the end. The latter is gonna take T(n/2) swaps.

    Bubble sort runs L2R. So the sorted values build up from the right side in descending order.
    This brings us to the rabbits and turtles problem.

    biggest values move intentionally. smaller ones move occasionally as a side effect. Thus the "bubble" metaphor.
    Lets discuss the border cases.

    A rabbit at the beginning
    [4, 1, 2, 3] -> [1, 2, 3, 4] takes a single run with O(n) comps and O(n) swaps

    a turtle at the end
    [2, 3, 4, 1] -> [2, 3, 1, 4] -> [2, 1, 3, 4] -> [1, 2, 3, 4] takes n runs with O(n**2) comps and O(n) swaps
    This can be cured with oscillation and gaps


P.S. I've been told bubble sort is stupid and kept in zoos to entertain the young.
Is it? It'd be nice to find some real habitats.
"""
from src.commons import key_fun
from src.commons import swap


def bubble_sort(sequence, key=key_fun):
    is_over = False

    while not is_over:
        is_over = True
        for i in range(1, len(sequence)):
            if key(sequence[i - 1] > key(sequence[i])):
                swap(sequence, i - 1, i)
                is_over = False


def shaker_sort(sequence, key=key_fun):
    is_over = False
    counter = 0
    ll = len(sequence)

    while not is_over:
        counter += 1
        is_over = True
        for i in range(1, ll) if counter % 2 else range(ll - 1, 0, -1):
            if key(sequence[i - 1]) > key(sequence[i]):
                swap(sequence, i - 1, i)
                is_over = False


def bubble_with_gaps(sequence, key=key_fun):
    """
    Mitigate turtles problem.
    """
    gap = len(sequence) // 2

    while gap > 1:
        for i in range(len(sequence) - gap):
            if key(sequence[i]) > key(sequence[i + gap]):
                swap(sequence, i, i + gap)
        gap //= 2


def comb_sort(sequence, key=key_fun):
    bubble_with_gaps(sequence, key)
    bubble_sort(sequence, key)
