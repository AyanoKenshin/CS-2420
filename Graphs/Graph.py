class Graph:
    def __init__(self, numVertices):
        self.neighbors = []

        for i in range(numVertices):
            self.neighbors.append([])

    def AddEdge(self, v1, v2):
        if v2 not in self.neighbors[v1]:
            self.neighbors[v1].append(v2)

    def IsEdge(self, v1, v2):
        return v2 in self.neighbors[v1]

    def GetNeighbors(self, v0):
        return self.neighbors[v0]

    def FindPath(self, v1, v2):
        queue = []
        visited = []

        queue.append([v1])
        visited.append(v1)

        while len(queue) > 0:
            path = queue.pop(0)
            current = path[-1]

            if current == v2:
                return path

            for neighbor in self.GetNeighbors(current):
                if neighbor not in visited:
                    visited.append(neighbor)

                    newPath = path.copy()
                    newPath.append(neighbor)

                    queue.append(newPath)

        return None

    def FindShortestPath(self, v1, v2):
        return self.FindPath(v1, v2)