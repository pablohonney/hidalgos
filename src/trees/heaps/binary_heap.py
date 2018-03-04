"""
Properties:
    binary property.

    heap property: defines a relation between parent and children.
    Unlike search tree property it doesn't specify relation between siblings.
    As such it's looser property and it leaves more freedom for
    the shaping of the tree which leeds to next prop.

    shape/complete_tree property: tree is filled left-right until the level is complete.
    Only then is the next level populated. This means there's always strict relation between
    the parent/children positions.
    This allows heaps to be internally implemented as array - this is very space-efficient
    Navigation is done with mathematical calculations rather than algorithmically - which is very fast.


Implementation notes:
    0 based indexing implies +1/+2 for children and -1//2 for parent funcs
    1 based indexing implies +0/+1 for children and //2 for parent funcs

    Heap should be able to work on pre-existent list in-place.
    Simply rub heapify to impose the heap property on the input.

    heapify start with the last branch node. It puts the branches down.
    cf. It moves in a similar but inverted manner to insertion sort. the navigation policy is also different.

    In doing so heapify utilizes the shape prop. Any complete binary tree is half leaves and half branches.
    So heapify can start just in the middle of the underlying array.
"""
from src.commons import key_fun


# TODO implement down and up with less swaps. cf. similar insertion sort optimization/
class BinaryHeap(object):
    def __init__(self, sequence=None, key=key_fun):
        self.key = key
        if sequence:
            self.list = sequence
            self.heapify()
        else:
            self.list = []

    def compare(self, i, j):
        raise NotImplementedError

    def get_parent(self, index):
        return (index - 1) // 2

    # because the heap prop doesn't specify relations between siblings
    # we need to mane an additional check to return the proper min/max child
    def get_child(self, index):
        left = index * 2 + 1
        right = left + 1
        if right >= len(self):
            return left
        elif self.compare(self.key(self.list[left]), self.key(self.list[right])):
            return left
        else:
            return right

    def up(self, index):
        while True:
            parent_index = self.get_parent(index)
            if parent_index >= 0 and self.compare(self.key(self.list[index]), self.key(self.list[parent_index])):
                self.list[parent_index], self.list[index] = self.list[index], self.list[parent_index]
                index = parent_index
            else:
                break

    def down(self, index):
        while True:
            child_index = self.get_child(index)
            if child_index < len(self) and self.compare(self.key(self.list[child_index]), self.key(self.list[index])):
                self.list[child_index], self.list[index] = self.list[index], self.list[child_index]
                index = child_index
            else:
                break

    def peek(self):
        return self.list[0]

    # swap the first and last. pop the new last. push the new first down.
    def pop(self):
        popped = self.list[0]
        self.list[0] = self.list[len(self) - 1]

        self.list.pop()
        self.down(0)

        return popped

    def push(self, item):
        self.list.append(item)
        self.up(len(self) - 1)

    def heapify(self):
        for i in range(len(self) // 2, -1, -1):
            self.down(i)

    def __len__(self):
        return len(self.list)


class MinHeap(BinaryHeap):
    def compare(self, i, j):
        return i < j


class MaxHeap(BinaryHeap):
    def compare(self, i, j):
        return i > j

