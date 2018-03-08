"""
Another 'smart data structures and dumb code' algorithm.

time: O(n*log(n)). evaluates lazily
space: in-place

Properties:
    lazy evaluation
    non-stable
"""
from src.commons import key_fun
from src.data_types.priority_queue import MinPriorityQueue
from src.data_types.priority_queue import MaxPriorityQueue


def heap_sort(sequence, key=key_fun, reverse=False):
    if reverse:
        queue = MaxPriorityQueue(sequence, key)
    else:
        queue = MinPriorityQueue(sequence, key)

    while queue:
        yield queue.pop()
