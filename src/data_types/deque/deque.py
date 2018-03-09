from src.data_types.lists import DoublyLinkedList


class Deque(object):
    def __init__(self, iterable=None):
        self.list = DoublyLinkedList(iterable)

    def push_left(self, item):
        self.list.insert_left(item)

    def push_right(self, item):
        self.list.insert_right(item)

    def pop_left(self):
        return self.list.pop_left()

    def pop_right(self):
        return self.list.pop_right()

    def peek_left(self):
        return self.list.peek_left()

    def peek_right(self):
        return self.list.peek_right()

    def __len__(self):
        return len(self.list)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, list(self.list))