"""
Another 'smart data structures and dumb code' algorithm.

properties:
  greedy

dependency:
  disjoint_set
"""

from src.sets import DisjointSet


def kruskal(V, E):
    ds = DisjointSet()

    for vertex in V:
        ds.add(vertex)

    minimum_spanning_tree = set()

    for edge in sorted(E, key=lambda x: x[2]):
        u, v, _ = edge
        if ds.find_set(u) is not ds.find_set(v):
            ds.join(u, v)
            minimum_spanning_tree.add(edge)

    return minimum_spanning_tree
