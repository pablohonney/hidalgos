class BinarySearchTree(object):
    def __init__(self):
        self.root = _Node(None)

    def _add(self, node, key, value):
        if node:
            if key == node.value:
                node.value = value
            elif key < node.value:
                if node.left:
                    self._add(node.left, key, value)
                else:
                    node.left = _Node(value)
            else:
                if node.right:
                    self._add(node.right, key, value)
                else:
                    node.right = _Node(value)

    def __setitem__(self, key, value):
        if self.root:
            self._add(self.root)
        else:
            self.root = _Node(value)


class _Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

