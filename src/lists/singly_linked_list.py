class SinglyLinkedList(object):
    def __init__(self, iterable=None):
        self.root = _RootNode()
        self.length = 0

        # support instant read access on both ends
        self.head = self.root

        if iterable:
            # insert at index 0 takes O(1) time, but it reverses the input order
            if isinstance(iterable, range):
                # can't help about this
                for item in iterable:
                    self.append(item)
            else:
                # we can cheat by double reversing.

                # if iterable is random access, we get O(1) access and O(1) insert.
                # if iterable its sequential, we get O(n) access and O(1) insert.
                # which is bad, but we'd get it with append() anyway
                for i in range(len(iterable) - 1, -1, -1):
                    self.insert(iterable[i], 0)

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

    # deque-like interface
    def append(self, item):
        self.insert(item, len(self))

    def prepend(self, item):
        self.insert(item, 0)

    def insert(self, item, index: int = -1):
        prev, head = self._get_nth_item(index)

        node = _Node(item)
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


class _Node(object):
    def __init__(self, value):
        self.next = None
        self.value = value

    def __str__(self):
        return str(self.value)


class _RootNode(_Node):
    """
    A sentinel node.

    It's just a trick for better internal organization.
    While note carrying any data, it implies uniformity to our code.
    So that we don't need to check for any special cases when the node is the root.
    """

    def __init__(self):
        super(_RootNode, self).__init__(None)
