"""
Insertion sort consists of the loops.

External loop walks the length of the array.
Internal loop is an insertion function* (in-lined here)

Each next item from the list (outer loop iteration) is inserted into a
growing sorted list.

* The insertion function is usually implemented as a right-to-left loop.
  This way the item will be inserted after any other occurrence of the same item.
  This renders the implementation stable

  sorted
----------  <- stream

Sorted list can be

- an array (classic version).
    O(log(n)) to find
    O(n) to insert

- a linked list
    O(n) to find
    O(1) to insert

- a search tree (e.g. self-balanced BST).
  This is known as tree sort (see the )
    O(log(n)) to find
    O(log(n)) to insert
"""
from src.commons import key_fun

from src.algorithms.sorting.bubble_sort import bubble_with_gaps


def insertion_sort(arr, key=key_fun):
    insertion_sort_slice(arr, 0, len(arr), key)


# supports slice sort protocol
def insertion_sort_slice(arr, start, end, key=key_fun):
    for i in range(start + 1, end):
        value = arr[i]
        tmp = key(value)
        while i > start and key(arr[i - 1]) > tmp:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = tmp


def shell_sort(arr):
    bubble_with_gaps(arr)
    insertion_sort(arr)
