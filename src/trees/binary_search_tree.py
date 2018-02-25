class BinarySearchTree(object):
    def __init__(self, iterable=None, **mapping):
        self.root = None
        self.length = 0

        # check the (key, value) list possibility
        if iterable:
            if isinstance(iterable, dict):
                for i, j in iterable.items():
                    self[i] = j
            else:
                for i, j in iterable:
                    self[i] = j
        for i, j in mapping.items():
            self[i] = j

    def _add(self, node, key, value):  # recursive
        if node:
            if key == node.key:
                node.value = value
            elif key < node.key:
                if node.left:
                    self._add(node.left, key, value)
                else:
                    node.left = _Node(key, value, node)
                    self.length += 1
            else:
                if node.right:
                    self._add(node.right, key, value)
                else:
                    node.right = _Node(key, value, node)
                    self.length += 1

    def __setitem__(self, key, value):
        if self.root:
            self._add(self.root, key, value)
        else:
            self.root = _Node(key, value, self)
            self.length += 1

    def _get(self, key):  # iterative
        node = self.root
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node
        return None

    def __getitem__(self, item):
        node = self._get(item)
        if node:
            return node.value
        raise KeyError(item)

    def get(self, item, default=None):
        node = self._get(item)
        if node:
            return node.value
        return default

    def remove(self, item):
        node = self._get(item)
        if not node:
            raise KeyError(item)
        elif node == self.root:
            self.root.value = None

        # leaf
        if node.left and node.right:
            # TODO randomize left/right choice
            left_rightmost = self.get_rightmost_node(node.left)

            left_rightmost.right = node.right
            node.right.parent = left_rightmost

            if self.is_left_node(node):
                node.parent.left = node.left
            else:
                node.parent.right = node.left

        elif node.left:
            if self.is_left_node(node):
                node.parent.left = node.left
            else:
                node.parent.right = node.left
            node.left.parent = node.parent
        elif node.right:
            if self.is_left_node(node):
                node.parent.left = node.right
            else:
                node.parent.right = node.right
            node.right.parent = node.parent
        else:  # leaf
            if self.is_left_node(node):
                node.parent.left = None
            else:
                node.parent.right = None

    # sequential access
    def __depth_first_traversal(self, node):
        if node.left:
            yield from self.__depth_first_traversal(node.left)
        yield node
        if node.right:
            yield from self.__depth_first_traversal(node.right)

    def _depth_first_traversal(self):
        if self.root:
            return self.__depth_first_traversal(self.root)
        return []

    def values(self):
        for node in self._depth_first_traversal():
            yield node.value

    def keys(self):
        for node in self._depth_first_traversal():
            yield node.key

    def items(self):
        for node in self._depth_first_traversal():
            yield node.key, node.value

    # priority queue access
    def get_leftmost_node(self, node):
        while node.left:
            node = node.left
        return node

    def get_rightmost_node(self, node):
        while node.right:
            node = node.right
        return node

    def get_smallest_item(self):
        node = self.get_leftmost_node(self.root)
        return node.key, node.value

    def get_biggest_item(self):
        node = self.get_rightmost_node(self.root)
        return node.key, node.value
    
    def is_left_node(self, node):
        return node.parent.left == node

    def is_right_node(self, node):
        return node.parent.right == node

    def __contains__(self, item):
        return True if self._get(item) else False

    def __iter__(self):
        return self.keys()

    def __len__(self):
        return self.length

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, repr(dict(self.items())))


class _Node(object):
    def __init__(self, key, value, parent, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


class _RootNode(object):
    def __init__(self, key, value, parent, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
