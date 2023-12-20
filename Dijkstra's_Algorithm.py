class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def dijkstra(self):
        source_vertex = 0
        distance = [float('inf')] * self.vertices
        distance[source_vertex] = 0
        final_set = set()

        for i in range(self.vertices):
            min_distance = float('inf')
            next_vertex = -1

            for v in range(self.vertices):
                if v not in final_set and distance[v] < min_distance:
                    min_distance = distance[v]
                    next_vertex = v

            if next_vertex != -1:
                final_set.add(next_vertex)
                for v in range(self.vertices):
                    if v not in final_set and self.graph[next_vertex][v] != 0:
                        distance[v] = min(distance[v], distance[next_vertex] + self.graph[next_vertex][v])

        final_vertices = [v + 1 for v in sorted(final_set)]
        return final_vertices

g = Graph(5)
g.graph = [
    [0, 10, 0, 30, 100],
    [0, 0, 50, 0, 0],
    [0, 0, 0, 0, 10],
    [0, 0, 20, 0, 60],
    [0, 0, 0, 0, 0]
]

final_vertices = g.dijkstra()
print("S =", final_vertices)
