class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def dfs_traversal(self, start):
        def dfs_recursive(v, visited, traversal_path):
            visited[v] = True
            traversal_path.append(v + 1)

            for i in range(self.vertices):
                if self.graph[v][i] != 0 and not visited[i]:
                    dfs_recursive(i, visited, traversal_path)

        visited = [False] * self.vertices
        traversal_path = []

        dfs_recursive(start, visited, traversal_path)
        return traversal_path

g = Graph(5)
g.graph = [
    [0, 10, 0, 30, 100],
    [0, 0, 50, 0, 0],
    [0, 0, 0, 0, 10],
    [0, 0, 20, 0, 60],
    [0, 0, 0, 0, 0]
]

starting_vertex = 0

traversal_path = g.dfs_traversal(starting_vertex)

print("DFS traversal path from vertex", starting_vertex + 1, ":")
print(' --> '.join(str(vertex) for vertex in traversal_path))
