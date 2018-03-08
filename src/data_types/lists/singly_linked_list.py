"""
         head                        tail
          |                           |
root ---> a ---> b ---> c ---> d ---> e

      add O(1)       add O(n)      add O(1)
     peek O(1)      peek O(n)     peek O(1)
      pop O(1)       pop O(n)      pop O(n)

    * while locating elements may take O(n), add/pop proper is always O(1)


Optimization:
    keep a tail pointer.

    Without the tail, append would take O(n). It could be mitigated this way.

    for i in range(len(iterable) - 1, -1, -1):
        self.insert(iterable[i], 0)

    If iterable is random access, we get O(1) iterable access and O(1) list insertion.
    If iterable is one-way sequential, we get O(n) on next element access and O(1) on list insertion.
    If iterable is two-way sequential, we get O(1) on next element access and O(1) on list insertion.
"""
from .adt import ListADT


class SinglyLinkedList(ListADT):
    def __init__(self, iterable=None):
        self.head = RootNode()
        self.length = 0

        # support instant peek/add on tail
        self.tail = self.head

        if iterable:
            for item in iterable:
                self.insert_right(item)

    # support negative indices
    def _normalize_index(self, index: int) -> int:
        if index < 0:
            index += len(self)

        if index < 0:
            raise IndexError(index - len(self))

        return index

    def _get_nth_item(self, index: int):
        index = self._normalize_index(index)

        prev = self.head
        node = prev.next

        while index and node:
            prev = node
            node = node.next
            index -= 1

        return prev, node

    # iterates the list. O(n) time
    def insert(self, item, index: int):
        prev, tail = self._get_nth_item(index)

        node = Node(item)
        prev.next = node
        if tail:
            node.next = tail
        else:
            self.tail = node

        self.length += 1

    # like self.insert(item, len(self)), but takes O(1) time
    def insert_right(self, item):
        self.tail.next = Node(item)
        self.tail = self.tail.next
        self.length += 1

    def pop(self, index: int = -1):
        prev, tail = self._get_nth_item(index)
        if not tail:
            raise IndexError()

        prev.next = tail.next
        if self._normalize_index(index) == len(self) - 1:
            self.tail = prev
        self.length -= 1
        return tail.value

    def peek(self, index: int):  # O(n) time
        prev, tail = self._get_nth_item(index)
        if not tail:
            raise IndexError()

        return tail.value

    def peek_right(self):  # O(1) time
        return self.tail.value

    # random access
    def __setitem__(self, key, value):
        prev, tail = self._get_nth_item(key)
        if tail:
            tail.value = value
        else:
            raise IndexError(key)

    def __getitem__(self, item):
        prev, tail = self._get_nth_item(item)
        if tail:
            return tail.value
        else:
            raise IndexError(item)

    def __delitem__(self, key):
        self.pop(key)

    # membership
    def __contains__(self, item):
        node = self.head
        while node:
            if node.value == item:
                return 1
            node = node.next
        return False

    # iterable/iterator
    def __iter__(self):
        node = self.head.next
        while node:
            yield node.value
            node = node.next

    # commons
    def __len__(self):
        return self.length

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, repr(list(self)))


class Node(object):
    def __init__(self, value):
        self.next = None
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
