graph = {}
visited = set()

def addedge(x,y):
    if x not in graph.keys():
        graph[x] = [y]
    else:
        graph[x].append(y)
    if y not in graph.keys():
        graph[y] = [x]
    else:
        graph[y].append(x)

def DFS(visited, graph, start):
    if start not in visited:
        print(start, end="")
        visited.add(start)
        for i in graph[start]:
            DFS(visited, graph, i)

addedge(5, 1)
addedge(5, 3)
addedge(1, 6)
addedge(3, 2)
addedge(3, 4)
addedge(8, 0)
addedge(1, 8)
addedge(4, 8)

DFS(visited, graph, 5)