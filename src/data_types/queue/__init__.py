"""
To support FIFO behaviour queues need instant O(1) set and get operations on the opposite ends.
"""

from .queue import QueueViaSinglyLinkedList as Queue
# from .queue import QueueViaStack
# from .queue import QueueViaArray
