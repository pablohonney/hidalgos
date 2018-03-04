"""
Dijkstra's shortest path algorithm

It's greedy. We need the best choice at each step.

Check the vertices with shortest distance.
Because there are no negative edges, the their distance won't change after it was visited.
This is the core principle.

time: O(|E| + |V|log|V|) worst case
"""


def dijkstra(V, E, source, destination):
    # setup
    vertices = {v: (float('inf'), '') for v in V}  # O(|V|) memory
    vertices[source] = (0, '')
    marked_vertices = {}

    # start with source
    current_vertex, (current_distance, _) = source, vertices[source]

    # loop until destination is reached
    while current_vertex != destination:

        for vertex in sorted(filter(lambda x: x[0] == current_vertex, E), key=lambda x: x[2]):  # O(|V|) + O(|V|**2)
            _, dest, distance = vertex
            if current_distance + distance < vertices[dest][0]:
                vertices[dest] = [current_distance + distance, current_vertex]

        marked_vertices[current_vertex] = vertices.pop(current_vertex)
        current_vertex, (current_distance, _) = min(vertices.items(), key=lambda x: x[1][0])  # O(|V|)
    marked_vertices[current_vertex] = vertices.pop(current_vertex)

    # backtrack to the source
    path = [current_vertex]
    while current_vertex != source:
        _, current_vertex = marked_vertices[current_vertex]
        path.append(current_vertex)

    return path[::-1] + [current_distance]
