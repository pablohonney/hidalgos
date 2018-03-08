from typing import List


def dft_sort(V, E) -> List:
    """
    post-order depth first traversal

    How can we check for cycles here?
    Maybe use a separate cycle detection first. Kahn wins here.
    """

    marked_vertices = set()
    dependencies = {v: [] for v in V}  # DAG as multiset
    for source, destination in E:
        dependencies[destination].append(source)

    sorted_list = []
    for dependent in dependencies:
        sorted_list.extend(_dfs_sort(dependencies, marked_vertices, dependent))
    return sorted_list


def _dfs_sort(dependencies, marked_vertices, dependent):
    for vertex in dependencies[dependent]:
        yield from _dfs_sort(dependencies, marked_vertices, vertex)

    if dependent not in marked_vertices:
        marked_vertices.add(dependent)
        yield dependent
