from typing import List

from src.lists import Queue


def kahn_sort(V, E) -> List:

    dependency_counter = {v: 0 for v in V}
    for _, b in E:
        dependency_counter[b] += 1

    # if there're no cycles in the graph all the vertices will eventually be reached
    queue = Queue(x for x, y in dependency_counter.items() if y == 0)
    sorted_list = []
    while queue:
        free = queue.pop()
        sorted_list.append(free)
        for x, dependent in E:
            if x is free:
                dependency_counter[dependent] -= 1
                if dependency_counter[dependent] == 0:
                    queue.push(dependent)  # dependent no more )

    # if the free vertices' queue gets empty before all the dependencies are resolved
    # there must have been cycles in the graph. we've been fooled... Alarm.
    if sum(dependency_counter.values()):
        raise TypeError('Not a DAG')

    return sorted_list
