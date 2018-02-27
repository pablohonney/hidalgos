from src.hashtable import RehashedHashTable


class HashTableDict(object):
    def __init__(self, iterable, **mapping):
        self.hashtable = RehashedHashTable()

        if iterable:
            if isinstance(iterable, dict):
                for k, v in iterable.items():
                    self.hashtable.put(k, v)
            else:
                for k, v in iterable:
                    self.hashtable.put(k, v)

        if mapping:
            for k, v in mapping.items():
                self.hashtable.put(k, v)

    def __setitem__(self, key, value):
        self.hashtable.put(key, value)

    def __getitem__(self, item):
        return self.hashtable.get(item)[1]

    def __delitem__(self, key):
        self.hashtable.remove(key)

    def get(self, key, default=None):
        try:
            return self.hashtable.get(key)
        except KeyError:
            return default

    def keys(self):
        raise NotImplementedError

    def values(self):
        raise NotImplementedError

    def items(self):
        raise NotImplementedError

    def __len__(self):
        return len(self.hashtable)
