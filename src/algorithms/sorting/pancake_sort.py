"""
Pancake sort in it's simplest form is like selection sort with swapping procedure changed.

e.g. sort [4 2 1 3]. | is the sorted/unsorted border. <> is the selected min data.

            ----- reversals ----->
    source_reversal     destination_reversal
| 4 2 <1> 3    ->    | 4 2 3 <1>    ->    | 1 3 2 4     |  outer loop
1 | 3 <2> 4    ->    1 | 3 4 <2>    ->    1 | 2 4 3     |
1 2 | 4 <3>    ->  already in place ->    1 2 | 3 4     |
1 2 3 | 4                                              \/

time: O(n**2). reversals cost higher constant than swaps in selection sort.


PS. it'd be interesting to implement one with DoublyLinkedList to minimize reversal cost.
TODO extend from election sort?
"""

from src.commons import key_fun
from src.commons import get_min


def pancake_sort(sequence, key=key_fun):
    pancake_sort_slice(sequence, 0, len(sequence), key)


# supports slice sort protocol
def pancake_sort_slice(sequence, start, end, key=key_fun):
    for destination in range(start, end-1):  # safe to skip the last element  # O(n)
        source = get_min(sequence, destination, end, key)  # O(n)

        if source != destination:  # sort if not in order
            if source != end - 1:
                sequence[source:] = sequence[source:][::-1]  # O(1)
            sequence[destination:] = sequence[destination:][::-1]  # O(1)
