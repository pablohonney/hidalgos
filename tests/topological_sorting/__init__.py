"""
first vertex is required/depended_on by the second
"""

# https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
DAG1 = [
    (5, 2),
    (5, 0),
    (4, 0),
    (4, 1),
    (2, 3),
    (3, 1),
]

# http://www.techiedelight.com/kahn-topological-sort-algorithm/
DAG2 = [
    (0, 6),
    (1, 2),
    (1, 4),
    (1, 6),
    (3, 0),
    (3, 4),
    (5, 1),
    (7, 0),
    (7, 1),
]

CYCLIC_GRAPH = [
    (0, 1),
    (1, 2),
    (2, 3),
    (2, 0),
]
