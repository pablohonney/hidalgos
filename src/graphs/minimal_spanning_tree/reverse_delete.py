"""
Another 'smart data structures and dumb code' algorithm.

properties:
  greedy
  in-place

dependency:
  connectivity checker
"""
from collections import deque


# BFS version
# TODO improve. it'd work better on more structured graph input.
def are_connected(E, start, end):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for u, v, _ in E:
            if u != vertex and v == vertex:
                u, v = v, u

            if u == vertex:
                if v == end:
                    return True
                elif v not in visited:
                    queue.append(v)

    return False


def reverse_delete(E):

    for edge in sorted(E, key=lambda x: x[2], reverse=True):  # O(n*log(n))
        u, v, _ = edge
        E.remove(edge)
        if not are_connected(E, u, v):
            E.add(edge)

    return E
