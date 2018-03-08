"""
beginning in __init__.py

Plain old binary search tree.

In addition to search property there's the binary property.
binary:      branching factor = 2
               i.e. there are up to two children only.

No subtree balancing is done internally.
The internal tree-like structure strongly depends on the input.

input [2, 1, 3]
  2
1   3

input [1, 2, 3]
1
  2
    3

input [3, 2, 1]
    3
  2
1

"""


class BinarySearchTree(object):
    def __init__(self, iterable=None, **mapping):
        self.root = _RootNode()
        self.length = 0

        if iterable:
            if isinstance(iterable, dict):
                for i, j in iterable.items():
                    self[i] = j
            else:
                for i, j in iterable:
                    self[i] = j
        for i, j in mapping.items():
            self[i] = j

    def __setitem__(self, key, value):
        self.root.add(key, value)

    def __getitem__(self, item):
        node = self.root.get(item)
        if node:
            return node.value
        raise KeyError(item)

    def __delitem__(self, key):
        self.pop(key)

    def pop(self, key):
        node = self.root.get(key)
        if node:
            node.remove()
        else:
            raise KeyError(key)

        return node

    def get(self, item, default=None):
        node = self.root.get(item)
        if node:
            return node.value
        return default

    def get_smallest_item(self):
        node = self.root.get_leftmost()
        return node.key, node.value

    def get_biggest_item(self):
        node = self.root.get_rightmost()
        return node.key, node.value

    def pop_smallest_item(self):
        node = self.root.pop_leftmost()
        if node:
            return node.key, node.value
        else:
            raise KeyError('empty')

    def pop_biggest_item(self):
        node = self.root.pop_rightmost()
        if node:
            return node.key, node.value
        else:
            raise KeyError('empty')

    def __contains__(self, item):
        return True if self.root.get(item) else False

    def __iter__(self):
        return self.keys()

    def __len__(self):
        return len(self.root)

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, repr(dict(self.items())))

    # these might go into tree-backed dict implementation
    def values(self):
        for node in self.root.depth_first_traversal():
            yield node.value

    def keys(self):
        for node in self.root.depth_first_traversal():
            yield node.key

    def items(self):
        for node in self.root.depth_first_traversal():
            yield node.key, node.value


class _Node(object):
    def __init__(self, key, value, parent, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __len__(self):
        length = 1
        if self.left:
            length += len(self.left)
        if self.right:
            length += len(self.right)
        return length

    def __str__(self):
        return '%s key: %s left: %s right: %s' % (
            type(self).__name__, self.key,
            self.left.key if self.left else None,
            self.right.key if self.right else None,
        )

    def add(self, key, value):
        node = self

        while node:
            if key == node.key:
                node.value = value
                break
            elif key < node.key:
                if node.left:
                    node = node.left
                else:
                    node.left = _Node(key, value, node)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = _Node(key, value, node)
                    break

    def get(self, key):
        node = self

        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node
        return None

    def remove(self):
        node = self

        # leaf
        if node.left and node.right:
            # TODO randomize left/right choice
            left_rightmost = node.left.get_rightmost()

            left_rightmost.right = node.right
            node.right.parent = left_rightmost

            if node.is_left_node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
            node.left.parent = node.parent

        elif node.left:
            if node.is_left_node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
            node.left.parent = node.parent
        elif node.right:
            if node.is_left_node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
            node.right.parent = node.parent
        else:  # leaf
            if node.is_left_node:
                node.parent.left = None
            else:
                node.parent.right = None

    @property
    def is_left_node(self):
        return self.parent.left == self

    @property
    def is_right_node(self):
        return self.parent.right == self

    # priority queue access
    def get_leftmost(self):
        node = self

        while node.left:
            node = node.left
        return node

    def get_rightmost(self):
        node = self

        while node.right:
            node = node.right
        return node

    def pop_leftmost(self):
        node = self.get_leftmost()
        if node:
            node.remove()
        return node

    def pop_rightmost(self):
        node = self.get_rightmost()
        if node:
            node.remove()
        return node

    # sequential access
    def depth_first_traversal(self):
        if self.left:
            yield from self.left.depth_first_traversal()
        yield self
        if self.right:
            yield from self.right.depth_first_traversal()


class _RootNode(_Node):

    def __init__(self):
        super(_RootNode, self).__init__(None, None, None)
        self.child = None

    def __len__(self):
        # return super(_RootNode, self).__len__() - 1
        if self.child:
            return len(self.child)
        else:
            return 0

    @property
    def is_left_node(self):
        return True

    @property
    def left(self):
        return self.child

    @left.setter
    def left(self, item):
        self.child = item

    @property
    def right(self):
        return self.child

    @right.setter
    def right(self, item):
        self.child = item

    def add(self, key, value):
        if self.child:
            self.child.add(key, value)
        else:
            self.child = _Node(key, value, self)

    def get(self, key):
        if self.child:
            return self.child.get(key)
        else:
            return None

    def depth_first_traversal(self):
        if self.child:
            return self.child.depth_first_traversal()
        else:
            return []
