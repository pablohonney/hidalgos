"""
To support FIFO behaviour queues need instant O(1) set and get operations on the opposite ends.

It'd be easy with DoublyLinkedList class.
DLL is overkill though. It's got some nice features we don't really need that also imply memory overhead.
We'd keep it for a deque behaviour rather.

As for plain queues, we can combine two stacks to imitate one.
"""

from src.lists import Stack


class Queue(object):
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
        return '%s(%s)' % (self.__class__.__name__, repr(ll))


class QueueViaSinglyLinkedList(object):
    pass