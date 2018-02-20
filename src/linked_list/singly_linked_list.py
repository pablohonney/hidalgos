class SLList(object):
    def __init__(self):
        self.root = _RootNode()

        self.head = self.root
        self.neck = self.root

    # deque behaviour
    def append(self, item):
        self.head.next = _Node(item)
        self.head = self.head.next

    def pop(self, index: int = -1):
        node = self.head
        prev = self.root
        while prev and prev.next == node:
            prev = node

    # random access
    def __setitem__(self, key, value):
        pass

    def __getitem__(self, item):
        pass

    def __delitem__(self, key):
        pass

    # iterable/iterator
    def __iter__(self):
        node = self.root.next
        while node:
            yield node.value
            node = node.next


class _Node(object):
    def __init__(self, value):
        self.next = None
        self.value = value


class _RootNode(_Node):
    def __init__(self):
        super(_RootNode, self).__init__(None)
