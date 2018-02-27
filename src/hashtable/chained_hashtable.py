from src.lists import SinglyLinkedList

from src.hashtable.rehashed_hashtable import RehashedHashTable
from src.hashtable.rehashed_hashtable import empty


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
