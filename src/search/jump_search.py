"""
Let's use a metaphor to see how it works.
Consider magnetic tape cassettes of the old days.

1. To find a movie episode one would fast-forward to skip several minutes without checking the content.
2. Then the tape is played. If it's too early yet, go to step 1 and forward again.
3. if it's too late we know the upper and lower boundaries. it's between the old and new pivots.

As such jump search goes well with bidirectional sequential access data structures (e.g. doubly linked lists)

TODO with random access data structure it's no different from D&C algos.
to better illustrate the use case we need a doubly linked list.
"""


def jump_search(sequence, item, left: bool = True):
    low = 0
    high = len(sequence)

    pivot = int((high-low)**.5)

    # if sequence[pivot] < item:
    #     high <