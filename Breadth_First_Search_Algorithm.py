class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def bfs_traversal(self, start):
        visited = [False] * self.vertices
        queue = []
        queue.append(start)
        visited[start] = True
        traversal_path = []

        while queue:
            vertex = queue.pop(0)
            traversal_path.append(vertex + 1)

            for v in range(self.vertices):
                if self.graph[vertex][v] != 0 and not visited[v]:
                    queue.append(v)
                    visited[v] = True

        return traversal_path

# Initialize and define the graph
g = Graph(5)
g.graph = [
    [0, 10, 0, 30, 100],
    [0, 0, 50, 0, 0],
    [0, 0, 0, 0, 10],
    [0, 0, 20, 0, 60],
    [0, 0, 0, 0, 0]
]

starting_vertex = 0

traversal_path = g.bfs_traversal(starting_vertex)

print("BFS traversal path from vertex", starting_vertex + 1, ":")
print(' --> '.join(str(vertex) for vertex in traversal_path))
