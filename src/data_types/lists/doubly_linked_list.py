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

    def insert(self, item, index: int = 0):
        index = self.normalize_index(index)
        head = self.head

        for i in range(index):
            if head:
                head.next = head

        node = Node(item)

        node.next = head.next  # two way linking
        node.prev = head

        self.size += 1

    def insert_right(self, item):
        tail = Node(item)

        self.tail.next = tail  # two way linking
        tail.prev = self.tail

        self.tail = tail  # update tail

        self.size += 1

    def insert_left(self, item):
        head = Node(item)

        head.next = self.head.next  # two way linking
        head.prev = self.head
        self.head.next = head  # update tail

        self.size += 1

    def normalize_index(self, index):
        if index < 0:
            index += len(self)

        if index < 0:
            raise IndexError(index - len(self))

        return index

    def get_node(self, index):
        pass


    def pop(self):
        pass

    def __iter__(self):
        node = self.head.next
        while node:
            yield node.value
            node = node.next

    def __getitem__(self, item):
        pass

    def __len__(self):
        return self.size

    def __repr__(self):
        pass


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
