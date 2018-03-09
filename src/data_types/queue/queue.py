"""
To support FIFO behaviour queues need instant O(1) set and get operations on the opposite ends.
"""

from src.data_types.stacks import Stack
from src.data_types.lists import SinglyLinkedList


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
        self.list.insert_right(item)

    def pop(self):
        return self.list.pop(0)

    def peek(self):
        return self.list[0]

    def __len__(self):
        return len(self.list)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, list(self.list))


class QueueViaArray(object):
    """
    Use modular arithmetic to imitate a ring.

       tail          head
        |              |
    ----xxxxxxxxxxxxxxxx----------


       head          tail
        |              |
    xxxxx--------------xxxxxxxxxxx
    """

    def __init__(self, size: int, iterable=None):
        self.size = size
        self.list = [None]*size
        self.head = 0
        self.tail = 0

        if iterable:
            for item in iterable:
                self.push(item)

    def push(self, item):
        self.list[self.head] = item
        self.head = (self.head + 1) % self.size

    def pop(self):
        value = self.list[self.tail]
        del self.list[self.tail]
        self.tail = (self.tail + 1) % self.size
        return value

    def peek(self):
        return self.list[self.tail]

    def __len__(self):
        if self.tail > self.head:
            return self.tail - self.head
        else:
            return len(self.list) - self.tail - self.head

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, list(self.list))
