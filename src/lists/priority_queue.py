"""
The priority queue interface happens to be exactly as that of the Heap.

It'd be easier to inherit from heap they are different types.
Type composition with field promotion would fit best here, but python doesn't support it natively.
Thus I ended up duplicate things around :/
"""

from src.commons import key_fun
from src.trees.heaps import MinHeap
from src.trees.heaps import MaxHeap


class PriorityQueue(object):
    Heap = NotImplemented

    def __init__(self, sequence=None, key=key_fun):
        self.heap = self.Heap(sequence, key)

    def push(self, item):
        self.heap.push(item)

    def pop(self):
        return self.heap.pop()

    def change_priority(self):
        raise NotImplementedError

    def __len__(self):
        return len(self.heap)


class MinPriorityQueue(PriorityQueue):
    Heap = MinHeap


class MaxPriorityQueue(PriorityQueue):
    Heap = MaxHeap
