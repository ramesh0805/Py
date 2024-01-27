from queue import PriorityQueue
v = 5
graph = [[] for _ in range(v)]
def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))
def heuristic(node, target):
    return abs(node - target)
def aStarSearch(source, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, source, heuristic(source, target), [source]))  
    visited[source] = True
    while not pq.empty():
        _, u, _, path = pq.get()
        if u == target:
            return path  
        visited[u] = True
        for v, c in graph[u]:
            if not visited[v]:
                new_cost = c
                new_path = path + [v]  
                pq.put((new_cost, v, new_cost + heuristic(v, target), new_path))
    return []  
addedge(0, 1, 4)
addedge(0, 2, 5)
addedge(1, 3, 2)
addedge(2, 4, 8)
addedge(3, 4, 6)
source = 0
target = 4
path = aStarSearch(source, target, v)
if path:
    print("A* Path:", path)
else:
    print("No path found.")
