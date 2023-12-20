class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def prim_mst(self, start):
        visited = [False] * self.vertices
        min_weight = [float('inf')] * self.vertices
        min_weight[start] = 0
        parent = [-1] * self.vertices

        for _ in range(self.vertices):
            min_vertex = -1
            for v in range(self.vertices):
                if not visited[v] and (min_vertex == -1 or min_weight[v] < min_weight[min_vertex]):
                    min_vertex = v

            visited[min_vertex] = True

            for u in range(self.vertices):
                if self.graph[min_vertex][u] != 0 and not visited[u] and self.graph[min_vertex][u] < min_weight[u]:
                    min_weight[u] = self.graph[min_vertex][u]
                    parent[u] = min_vertex

        mst_edges = []
        for v in range(self.vertices):
            if parent[v] != -1:
                mst_edges.append((parent[v] + 1, v + 1, self.graph[parent[v]][v]))

        return mst_edges

g = Graph(5)
g.graph = [
    [0, 10, 0, 30, 100],
    [10, 0, 50, 0, 0],
    [0, 50, 0, 20, 10],
    [30, 0, 20, 0, 60],
    [100, 0, 10, 60, 0]
]

starting_vertex = 0

mst_edges = g.prim_mst(starting_vertex)

print("Minimum Spanning Tree edges:")
for edge in mst_edges:
    print(f"({edge[0]} - {edge[1]}) with weight {edge[2]}")
