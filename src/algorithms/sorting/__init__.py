"""
Concepts:

order:
sortedness:

when we sort things we usually
key:
satellite data:



Sorting properties

Stability:

how does one sort words? Seems trivial? Ok, then how does one sort kanji.
"""

# exchange sorts
from .bubble_sort import bubble_sort
from .bubble_sort import shaker_sort
from .bubble_sort import comb_sort
from .quick_sort import QuickSortHoare as QuickSort

# selections sorts
from .selection_sort import selection_sort
from .heap_sort import heap_sort

# insertions sorts
from .insertion_sort import insertion_sort
from .insertion_sort import shell_sort
from .tree_sort import tree_sort

# distribution/integer sorts
from .counting_sort import counter_sort
from .counting_sort import counter_sort_inplace

# merge sorts
from .merge_sort import MergeSort

# other
from .pancake_sort import pancake_sort
from .pancake_sort import pancake_sort_slice
