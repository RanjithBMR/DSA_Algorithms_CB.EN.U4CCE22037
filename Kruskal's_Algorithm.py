class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def kruskal_mst(self):
        edges = []
        for i in range(self.vertices):
            for j in range(i + 1, self.vertices):
                if self.graph[i][j] != 0:
                    edges.append((self.graph[i][j], i, j))

        edges.sort()

        parent = [-1] * self.vertices
        mst_edges = []

        def find(v, parent):
            while parent[v] != -1:
                v = parent[v]
            return v

        def union(v1, v2, parent):
            root1 = find(v1, parent)
            root2 = find(v2, parent)

            if root1 != root2:
                parent[root2] = root1

        for weight, v1, v2 in edges:
            if find(v1, parent) != find(v2, parent):
                union(v1, v2, parent)
                mst_edges.append((v1 + 1, v2 + 1, weight))

        return mst_edges

adjacency_matrix = [
    [0, 10, 0, 30, 100],
    [10, 0, 50, 0, 0],
    [0, 50, 0, 20, 10],
    [30, 0, 20, 0, 60],
    [100, 0, 10, 60, 0]
]

g = Graph(len(adjacency_matrix))
g.graph = adjacency_matrix

mst_edges = g.kruskal_mst()

print("Minimum Spanning Tree edges:")
for edge in mst_edges:
    print(f"({edge[0]} - {edge[1]}) with weight {edge[2]}")
