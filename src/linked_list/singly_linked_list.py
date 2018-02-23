class SinglyLinkedList(object):
    def __init__(self, sequence=None):
        self.root = _RootNode()
        self.head = self.root
        self.length = 0

        if sequence:
            for item in sequence:
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

    # deque behaviour
    def append(self, item):
        self.head.next = _Node(item)
        self.head = self.head.next
        self.length += 1

    def pop(self, index: int = -1):
        # head pop optimization

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


class _RootNode(_Node):  # sentinel node
    def __init__(self):
        super(_RootNode, self).__init__(None)
