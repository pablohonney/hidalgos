"""
         head                        tail
          |                           |
root ---> a <--> b <--> c <--> d <--> e

      add O(1)       add O(n)      add O(1)
     peek O(1)      peek O(n)     peek O(1)
      pop O(1)       pop O(n)      pop O(1)

  * while locating elements may take O(n), add/pop proper is always O(1)
"""
from .adt import ListADT


class DoublyLinkedList(ListADT):

    def __init__(self, iterable=None):
        self.head = RootNode()
        self.tail = self.head
        self.size = 0

        if iterable:
            for item in iterable:
                self.insert_right(item)

    def _normalize_index(self, index):
        if index < 0:
            index += len(self)

        if index < 0:
            raise IndexError(index - len(self))

        return index

    def _get_node(self, index: int):
        index = self._normalize_index(index)
        node = self.head
        for _ in range(index):
            if node:
                node = node.next
            else:
                break

        if not node:
            raise IndexError

        return node

    # TODO count from head/tail depending on index
    def insert(self, item, index: int):
        node = self._get_node(index)

        new_node = Node(item)

        # four-way linking
        if node.next:
            new_node.next = node.next
            node.next.prev = new_node

        new_node.prev = node
        node.next = new_node

        if node is self.tail:
            self.tail = new_node

        self.size += 1

    def insert_right(self, item):
        node = Node(item)

        # two-way linking
        node.prev = self.tail
        self.tail.next = node

        # update tail
        self.tail = node

        self.size += 1

    def pop(self, index: int):
        node = self._get_node(index)
        node = node.next
        if not node:
            raise IndexError(index)

        # two-way linking
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        if node is self.tail:
            self.tail = node.prev

        self.size -= 1

        return node.value

    def peek(self, index: int):
        node = self._get_node(index)
        node = node.next
        if not node:
            raise IndexError(index)

        return node.value

    # supports __contains__ quite well
    def __iter__(self):
        node = self.head.next
        while node:
            yield node.value
            node = node.next

    def __setitem__(self, index, value):
        node = self._get_node(index)
        node = node.next
        if not node:
            raise IndexError(index)

        node.value = value

    def __getitem__(self, index):
        return self.peek(index)

    def __len__(self):
        return self.size

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, repr(list(self)))


class Node(object):
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

    def __str__(self):
        return str(self.value)

    __repr__ = __str__


class RootNode(Node):
    """
    A sentinel node.

    It's just a trick for better internal organization.
    While note carrying any data, it implies uniformity to our code.
    So that we don't need to check for any special cases when the node is the root.
    """

    def __init__(self):
        super(RootNode, self).__init__(None)
