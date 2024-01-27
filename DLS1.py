from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def addNode(self, v, visited, depth_limit):
        if depth_limit == 0:
            return
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.addNode(neighbour, visited, depth_limit - 1)
    def DFS(self, v, depth_limit):
        visited = set()
        self.addNode(v, visited, depth_limit)
my_graph = Graph()
v = int(input("Enter number of nodes: "))
for _ in range(v - 1):
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    my_graph.addEdge(x, y)

print("Depth-Limited Search:")
my_graph.DFS(1, 3)
