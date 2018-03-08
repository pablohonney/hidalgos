"""
The priority queue interface happens to be exactly as that of the Heap.

It'd be easier to inherit from heap they are different types.
Type composition with field promotion would fit best here, but python doesn't support it natively.
Thus I ended up duplicating things around :/
"""

from src.commons import key_fun
from src.data_types.trees.heaps import MinHeap
from src.data_types.trees.heaps import MaxHeap


class PriorityQueue(object):
    Heap = NotImplemented

    def __init__(self, sequence=None, key=key_fun):
        self.heap = self.Heap(sequence, key)

    def peek(self):
        return self.heap.peek()

    def push(self, item):
        self.heap.push(item)

    def pop(self):
        return self.heap.pop()

    def update_priority(self, old, new):
        self.heap.update_priority(old, new)

    def __len__(self):
        return len(self.heap)


class MinPriorityQueue(PriorityQueue):
    Heap = MinHeap


class MaxPriorityQueue(PriorityQueue):
    Heap = MaxHeap
