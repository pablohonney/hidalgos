"""
Hash collisions can be solved in two ways.
  1. open hashing aka chaining
     easier to implement. breaks the O(n) guaranty
  2. closed hashing aka rehashing
     2.1 linear probing
     2.2 quadratic probing
     2.3 double hashing

When rehashing we get a rehash path that needs to be walked each time
the key is looked for.

Removing elements may leave gaps in these rehash paths. consider this:

array of size 3, e is empty, <> is the checked index
hashing is modulus, rehashing is linear probing,

put 1      -hash> [<e>, e, e] -put> [1, e, e]
put 4      -hash> [<1>, e, e] -rehash> [1, <e>, e] -put> [1, 4, e]
get 4      -hash> [<1>, 4, e] -rehash> [1, <4>, e] -get> 4
remove 1   -hash> [<1>, 4, e] -remove> [e, 4, e]
get 4      -hash> [<e>, 4, e] -error> couldn't find

solutions?
1: rehash all values on remove. bad.
2: rehash round robin on get/put/remove. bad.
3: damn, any ideas ?  Gotcha. use chaining for a while.

------------------------------------

Base hash-table class with polymorphic closed rehashing

write a custom hash function. should support salting !

Imitate sparse_index/dense_entry solution
"""

from src.lists import SinglyLinkedList

empty = object()  # never used. safe to stop here
dummy = object()  # previously used. remove/get must continue rehashing.


class RehashedHashTable(object):
    DEFAULT_CAPACITY = 8
    UPSCALE_LOAD_FACTOR = 0.7
    DOWNSCALE_LOAD_FACTOR = 0.2
    RESIZE_POLICY = 2  # make this more flexible

    # elaborate on this
    if UPSCALE_LOAD_FACTOR < DOWNSCALE_LOAD_FACTOR:
        raise RuntimeError

    def __init__(self):

        self.capacity = self.DEFAULT_CAPACITY
        self.size = 0.0
        self.list = [empty] * self.capacity

    def reallocate(self, upscale: bool = True):
        old_list = self.list
        old_size = len(self)

        if upscale:
            self.capacity *= self.RESIZE_POLICY
        else:
            self.capacity /= self.RESIZE_POLICY
        if self.capacity < self.DEFAULT_CAPACITY:
            self.capacity = self.DEFAULT_CAPACITY

        self.capacity = int(self.capacity)
        self.list = [empty] * self.capacity

        # put increments the size.
        # reassign the old size to avoid corruption.
        for item in old_list:
            if item not in [empty, dummy]:
                self.put(item)
        self.size = old_size

    def hash(self, key):  # overridable
        return hash(key)

    def index(self, key):
        return self.hash(key) % self.capacity

    # aka rehash. linear probing.
    def reindex(self, key, index):  # overridable
        return (index + 1) % self.capacity

    def put(self, key):
        i = self.index(key)
        while self.list[i] not in [empty, dummy]:
            if self.list[i] == key:
                break
            else:
                i = self.reindex(key, i)

        self.list[i] = key
        self.size += 1

        if self.size / self.capacity > self.UPSCALE_LOAD_FACTOR:
            self.reallocate(upscale=True)

    def get(self, key):
        i = self.index(key)
        while self.list[i] is not empty:
            if self.list[i] == key:
                return self.list[i]
            else:
                i = self.reindex(key, i)

        raise KeyError(key)

    def remove(self, key):
        i = self.index(key)
        while self.list[i] is not empty:
            if self.list[i] == key:
                self.list[i] = dummy
                self.size -= 1

                if self.size / self.capacity < self.DOWNSCALE_LOAD_FACTOR:
                    self.reallocate(upscale=False)
                return
            else:
                i = self.reindex(key, i)

        raise KeyError(key)

    def __len__(self):
        return int(self.size)


class ChainedHashTable(RehashedHashTable):

    DEFAULT_CAPACITY = 20

    def put(self, key):
        i = self.index(key)
        if self.list[i] is empty:
            self.list[i] = SinglyLinkedList()

        for j, item in enumerate(self.list[i]):
            if item == key:
                self.list[i][j] = item
                break
        else:
            self.list[i].prepend(key)
            self.size += 1

        # if self.size / self.capacity > self.UPSCALE_LOAD_FACTOR:
        #     self.reallocate(upscale=True)

    def get(self, key):
        i = self.index(key)
        if self.list[i] is empty:
            raise KeyError(key)
        else:
            for item in self.list[i]:
                if item == key:
                    return item
            raise KeyError(key)

    def remove(self, key):
        i = self.index(key)
        while self.list[i] is empty:
            raise KeyError(key)

        for j, item in enumerate(self.list[i]):
            if item == key:
                del self.list[i][j]
                self.size -= 1

                if not self.list[i]:
                    self.list[i] = empty
                break
