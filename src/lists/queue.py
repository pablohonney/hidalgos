"""
To support FIFO behaviour queues need instant O(1) set and get operations on the opposite ends.
"""

from src.lists import Stack
from src.lists import SinglyLinkedList


class QueueViaStack(object):
    def __init__(self, iterable=None):
        self.input = Stack(iterable)
        self.output = Stack()

        self._input_to_output()

    def _input_to_output(self):
        while self.input:
            self.output.push(self.input.pop())

    def push(self, item):
        self.input.push(item)

    def pop(self):
        if not self.output and self.input:
            self._input_to_output()

        return self.output.pop()

    def peek(self):
        if not self.output and self.input:
            self._input_to_output()

        return self.output.peek()

    def __len__(self):
        return len(self.input) + len(self.output)

    def __repr__(self):
        ll = list(self.output.list) + list(self.input.list)[::-1]
        return '%s(%r)' % (self.__class__.__name__, ll)


class QueueViaSinglyLinkedList(object):

    def __init__(self, iterable=None):
        self.list = SinglyLinkedList(iterable)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop(0)

    def peek(self):
        return self.list[0]

    def __len__(self):
        return len(self.list)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, list(self.list))
