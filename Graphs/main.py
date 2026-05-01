from Graph import Graph


def main():
    filename = "MyGraphData.txt"

    file = open(filename, "r")

    numVertices = int(file.readline())
    numEdges = int(file.readline())

    graph = Graph(numVertices)

    for i in range(numEdges):
        line = file.readline().split()

        v1 = int(line[0])
        v2 = int(line[1])

        graph.AddEdge(v1, v2)

    numTests = int(file.readline())

    tests = []

    for i in range(numTests):
        line = file.readline().split()

        v1 = int(line[0])
        v2 = int(line[1])

        tests.append([v1, v2])

    file.close()

    print("Neighbor list:")
    print(graph.neighbors)
    print()

    for test in tests:
        v1 = test[0]
        v2 = test[1]

        path = graph.FindShortestPath(v1, v2)

        print("From", v1, "to", v2, ":", path)


main()