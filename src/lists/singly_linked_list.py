"""
         head                         tail
          |                            |
root ---> a ---> b ---> c ---> d ---> e

      add O(1)                     add O(1)
     peek O(1)                    peek O(1)
      pop O(1)                     pop O(n)


Optimization:
    keep a tail pointer.

    Without the tail, append would take O(n). It could be mitigated this way.

    for i in range(len(iterable) - 1, -1, -1):
        self.insert(iterable[i], 0)

    If iterable is random access, we get O(1) iterable access and O(1) list insertion.
    If iterable is one-way sequential, we get O(n) on next element access and O(1) on list insertion.
    If iterable is two-way sequential, we get O(1) on next element access and O(1) on list insertion.
"""


class SinglyLinkedList(object):
    def __init__(self, iterable=None):
        self.root = RootNode()
        self.length = 0

        # support instant read access on both ends
        self.head = self.root

        if iterable:
            for item in iterable:
                self.append(item)

    def _normalize_index(self, index):
        if index < 0:
            index = len(self) + index

        if index < 0:
            raise IndexError()

        return index

    def _get_nth_item(self, index):
        index = self._normalize_index(index)

        prev = self.root
        node = prev.next

        while index and node:
            prev = node
            node = node.next
            index -= 1

        return prev, node

    # --- DEQUE-LIKE INTERFACE ---

    # like self.insert(item, len(self)), but takes O(1) time
    def append(self, item):
        self.head.next = Node(item)
        self.head = self.head.next
        self.length += 1

    # O(1) time
    def prepend(self, item):
        self.insert(item, 0)

    # iterates the list. O(n) time
    def insert(self, item, index: int = -1):
        prev, head = self._get_nth_item(index)

        node = Node(item)
        prev.next = node
        if head:
            node.next = head
        else:
            self.head = node

        self.length += 1

    def pop(self, index: int = -1):
        prev, head = self._get_nth_item(index)
        if not head:
            raise IndexError()

        prev.next = head.next
        if self._normalize_index(index) == len(self) - 1:
            self.head = prev
        self.length -= 1
        return head.value

    # random access
    def __setitem__(self, key, value):
        prev, head = self._get_nth_item(key)
        if head:
            head.value = value
        else:
            raise IndexError(key)

    def __getitem__(self, item):
        prev, head = self._get_nth_item(item)
        if head:
            return head.value
        else:
            raise IndexError(item)

    def __delitem__(self, key):
        self.pop(key)

    # membership
    def __contains__(self, item):
        node = self.root
        while node:
            if node.value == item:
                return 1
            node = node.next
        return False

    # iterable/iterator
    def __iter__(self):
        node = self.root.next
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
