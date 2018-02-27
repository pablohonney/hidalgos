from src.hashtable import RehashedHashTable


class HashTableSet(set):
    def __init__(self):
        self.hashtable = RehashedHashTable()

    def add(self, element):
        self.hashtable.put(element)

    def pop(self):
        self.hashtable

    def __contains__(self, item):
        try:
            self.hashtable.get(item)
            return True
        except KeyError:
            return False