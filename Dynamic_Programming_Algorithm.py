class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[]] * vertices

    def dynamic_programming(self, destination):
        optimal_paths = []
        for i in range(self.vertices):
            optimal_paths.append([])

        destination -= 1  # Adjust destination to 0-index

        optimal_paths[destination] = [destination + 1]  # Destination vertex's path is itself

        while True:
            updated = False
            for i in range(self.vertices):
                if i != destination:
                    for j in range(self.vertices):
                        if self.graph[i][j] != 0 and optimal_paths[j]:
                            if not optimal_paths[i] or len(optimal_paths[i]) > len(optimal_paths[j]) + 1:
                                optimal_paths[i] = optimal_paths[j] + [i + 1]
                                updated = True

            if not updated:
                break

        return optimal_paths

g = Graph(5)
g.graph = [
    [0, 10, 0, 30, 100],
    [0, 0, 50, 0, 0],
    [0, 0, 0, 0, 10],
    [0, 0, 20, 0, 60],
    [0, 0, 0, 0, 0]
]

destination_vertex = 5
optimal_paths = g.dynamic_programming(destination_vertex)

vertex = 1
for path in optimal_paths:
    if path:
        print(f"Shortest path from vertex {vertex} to the destination {destination_vertex}: ", end="")
        for i in range(len(path)):
            print(path[i], end="")
            if i != len(path) - 1:
                print(' <-- ', end='')
        print()
    else:
        print(f"No path from vertex {vertex} to the destination {destination_vertex}")
    vertex += 1
