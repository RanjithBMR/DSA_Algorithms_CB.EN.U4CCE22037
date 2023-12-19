class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def display(self, distance):
        print("Vertex \t Distance from Source")
        for node in range(self.vertices):
            print(node, "\t\t", distance[node])

    def minDistance(self, distance, verticesset):
        min = 1e7
        for v in range(self.vertices):
            if distance[v] < min and verticesset[v] == False:
                min = distance[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [1e7] * self.vertices
        dist[src] = 0
        sptSet = [False] * self.vertices
        for i in range(self.vertices):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.vertices):
                if (self.graph[u][v] > 0 and
                        sptSet[v] == False and
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
        self.display(dist)


g = Graph(5)
g.graph = [[1, 3, 0, 0, 0],
           [0, 6, 9, 13, 0],
           [22, 0, 14, 7, 6],
           [8, 0, 5, 13, 0],
           [12, 0, 14, 9, 15]
           ]

g.dijkstra(2)
