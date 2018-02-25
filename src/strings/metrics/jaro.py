"""
beginning in __init__.py

Jaro uses only swap (aka transposition).
    swap costs 1

Since it doesn't support add/remove. the string must be of same length.
This condition can be checked right away.
"""
from functools import reduce
import collections
from itertools import combinations_with_replacement


def jaro(str1, str2):
    pass


dd = map(''.join, combinations_with_replacement('ABC', 2))
print(dd)
print(collections.Counter(dd))
# msets = map(collections.Counter, dd)
# print msets
print(reduce(lambda acc, x: acc + x, dd, ''))


class D(collections.deque):
    def __init__(self, iterable=(), maxlen=None, base=101):
        super(D, self).__init__(iterable=iterable, maxlen=maxlen)

        self.base = base
        self.value = 0
        for power, char in enumerate(self):
            self.value += ord(char) * (base ** power)

    def append(self, *args, **kwargs):
        super(D, self).append(*args, **kwargs)

        # self.value -
