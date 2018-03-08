empty = object()  # never used. safe to stop here
dummy = (object(), 'dummy_value')  # previously used. remove/get must continue rehashing.


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
                self.put(item[0], item[1])
        self.size = old_size

    def hash(self, key):  # overridable
        return hash(key)

    def index(self, key):
        return self.hash(key) % self.capacity

    # aka rehash. linear probing.
    def reindex(self, key, index):  # overridable
        return (index + 1) % self.capacity

    def put(self, key, value):
        i = self.index(key)
        while self.list[i] not in [empty, dummy]:
            if self.list[i][0] == key:
                break
            else:
                i = self.reindex(key, i)

        self.list[i] = (key, value)
        self.size += 1

        if self.size / self.capacity > self.UPSCALE_LOAD_FACTOR:
            self.reallocate(upscale=True)

    def get(self, key):
        i = self.index(key)
        while self.list[i] is not empty:
            if self.list[i][0] == key:
                return self.list[i]
            else:
                i = self.reindex(key, i)

        raise KeyError(key)

    def remove(self, key):
        i = self.index(key)
        while self.list[i] is not empty:
            if self.list[i][0] == key:
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

