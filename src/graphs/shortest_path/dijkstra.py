"""
Dijkstra's shortest path algorithm

It's greedy. We need the best choice at each step.

Check the vertices with shortest distance.
Because there are no negative edges, the their distance won't change after it was visited.
This is the core principle.

time: O(|E| + |V|log|V|) worst case
"""
# TODO priorities be update-able !!
from src.lists import MinPriorityQueue


def dijkstra(V, E, source, destination):
    # setup
    distances = {v: float('inf') for v in V}  # O(|V|) memory
    distances[source] = 0
    sources = {source: ''}

    # start with source
    current_vertex, current_distance = source, distances[source]

    # loop until destination is reached. Enables fast exit.
    while current_vertex != destination:

        for vertex in sorted(filter(lambda x: x[0] == current_vertex, E), key=lambda x: x[2]):  # O(|V|) + O(|V|**2)
            _, dest, distance = vertex

            if current_distance + distance < distances[dest]:
                distances[dest] = current_distance + distance
                sources[dest] = current_vertex

        distances.pop(current_vertex)
        current_vertex, current_distance = min(distances.items(), key=lambda x: x[1])  # O(|V|)

    # backtrack to the source
    path = [current_vertex]
    while current_vertex != source:
        current_vertex = sources[current_vertex]
        path.append(current_vertex)

    return path[::-1] + [current_distance]
