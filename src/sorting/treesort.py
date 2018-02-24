"""
Tree sort is a nice example of the 'smart data structures and dumb code' principle.

TODO Right now the implementation is intimidating.

Our BST was designed with map interface in mind so it doesn't count for duplicates.
We can only sort distinct elements now.
"""

from src.trees import BinarySearchTree
from src.commons import key_fun


def tree_sort(arr, key=key_fun):
    bst = BinarySearchTree()
    for value in arr:
        bst[key(value)] = value
    return bst.values()
