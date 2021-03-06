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
    - indexing
        0 based indexing implies +1/+2 for children and -1//2 for parent funcs
        1 based indexing implies +0/+1 for children and //2 for parent funcs

    - heapify
        Heap should be able to work on pre-existent list in-place.
        Simply use heapify to impose the heap property on the input.

        heapify starts with the last branch node. It puts the branches down.
        cf. It moves in a similar but inverted manner to insertion sort. the navigation policy is also different.

        In doing so heapify utilizes the shape prop. Any complete binary tree is half leaves and half branches.
        So heapify can start just in the middle of the underlying array.
        This movement is somewhat similar to insertion sorting.

                     | --->
        --------------------------
              | --->
        --------------------------
        | --->
        --------------------------
          branches     leaves

    - down
        Heap property doesn't specify relations between siblings. But we need this information when swapping
        parent with the a child. Consider a MinHeap example.

        Normal

            A
          >   <
        B   ?   C

        Wrong

            A
          <   >
        B   ?   C

        Let's swap A with B.

            B
          >   ?
        A   >   C

        While A > C relation is irrelevant (and we loose some info here), B ? C relation which was of no value
        previously becomes important. We need to check B against C now. If B happens to be bigger..

            B
          >   >
        A   ?   C

        swap again

            C
          >   <
        A   ?   B

        We could rather check B against C first, than swap the smaller with A.

            C
          >   <
        B   ?   A

"""
from src.commons import key_fun


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

    # takes O(n), needs research.
    def update_priority(self, old, new):
        for index, j in enumerate(self.list):
            if j == old:
                self.list[index] = new
                if self.compare(self.key(new), self.key(old)):
                    self.up(index)
                else:
                    self.down(index)
                break

    def heapify(self):
        for i in range(len(self) // 2, -1, -1):
            self.down(i)

    def __len__(self):
        return len(self.list)


class OptimizedBinaryHeap(BinaryHeap):

    # minimize swaps. cf insertion sort
    def up(self, index):
        item = self.list[index]
        key = self.key(item)
        parent_index = self.get_parent(index)

        while parent_index >= 0:
            if self.compare(key, self.key(self.list[parent_index])):
                self.list[index] = self.list[parent_index]
                index = parent_index
                parent_index = self.get_parent(index)
            else:
                break

        self.list[index] = item

    # minimize swaps. cf insertion sort
    def down(self, index):
        child_index = self.get_child(index)
        if child_index >= len(self):
            return
        item = self.list[index]
        key = self.key(item)

        while child_index < len(self):
            if self.compare(self.key(self.list[child_index]), key):
                self.list[index] = self.list[child_index]
                index = child_index
                child_index = self.get_child(index)
            else:
                break

        self.list[index] = item


class MinHeap(OptimizedBinaryHeap):
    def compare(self, i, j):
        return i < j


class MaxHeap(OptimizedBinaryHeap):
    def compare(self, i, j):
        return i > j
