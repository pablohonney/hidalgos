"""
Disjoint set aka union-find set aka merge-find set.

Keeps unique sets that don't overlap.
"""


class DisjointSet(object):

    def __init__(self):
        self._sets = []

    def add(self, item):
        if not self.find_set(item):
            self._sets.append({item})

    def find_set(self, item):
        for _set in self._sets:
            if item in _set:
                return _set

    def join(self, item1, item2):
        set1 = self.find_set(item1)
        set2 = self.find_set(item2)

        if set1 is not set2:
            set1.update(set2)
            self._sets.remove(set2)
