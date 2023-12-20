class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        for i in range(vertices):
            row = []
            for j in range(vertices):
                row.append(0)
            self.graph.append(row)

    def floyd_warshall(self):
        A = []
        for i in range(self.vertices):
            row = []
            for j in range(self.vertices):
                if i == j:
                    row.append(0)
                else:
                    row.append(float('inf'))
            A.append(row)

        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.graph[i][j] != 0:
                    A[i][j] = self.graph[i][j]

        for k in range(self.vertices):
            for i in range(self.vertices):
                for j in range(self.vertices):
                    if A[i][k] + A[k][j] < A[i][j]:
                        A[i][j] = A[i][k] + A[k][j]

        for i in range(self.vertices):
            for j in range(self.vertices):
                if i==j:
                    A[i][j]=0

        return A

g = Graph(3)
g.graph = [
    [2, 8, 5],
    [3, 0, 0],
    [0, 2, 0]
]

optimal_paths = g.floyd_warshall()

print("Final matrix A after Floyd's algorithm:")
for row in optimal_paths:
    print(row)
