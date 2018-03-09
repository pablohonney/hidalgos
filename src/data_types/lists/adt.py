class ListADT(object):
    """
    List abstract data type

    First implement general methods.

    Special version can be built on top of them.
    But usually have better solutions.
    """

    # TODO should abs(index) > len(self) be valid like with built-ins?
    def insert(self, item, index: int):
        raise NotImplementedError

    def insert_left(self, item):
        self.insert(item, 0)

    def insert_right(self, item):
        self.insert(item, -1)

    def pop(self, index: int):
        raise NotImplementedError

    def pop_left(self):
        return self.pop(0)

    def pop_right(self):
        return self.pop(-1)

    def peek(self, index: int):
        raise NotImplementedError

    def peek_left(self):
        return self.peek(0)

    def peek_right(self):
        return self.peek(-1)

    def remove(self, index: int):
        raise NotImplementedError

    def remove_left(self):
        self.remove(0)

    def remove_right(self):
        self.remove(-1)
