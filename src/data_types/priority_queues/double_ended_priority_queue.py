from src.data_types.trees.search_trees import BinarySearchTree


class DoubleEndedPriorityQueue(object):
    def __init__(self):
        self.queue = BinarySearchTree()
