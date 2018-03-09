from src.data_types.lists import SinglyLinkedList


class Stack(object):
    def __init__(self, iterable=None):
        self.list = SinglyLinkedList()

        if iterable:
            for item in iterable:
                self.push(item)

    def push(self, item):
        self.list.insert(item, 0)

    def pop(self):
        return self.list.pop(0)

    def peek(self):
        return self.list[0]

    def __len__(self):
        return len(self.list)

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, repr(list(self.list)[::-1]))
