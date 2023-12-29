                                                     CSP PROBLEM 


def is_safe(vertex, color, graph, c):
    for i in range(len(graph)):
        if graph[vertex][i] and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, colors, color, v):
    if v == len(graph):
        return True

    for c in colors:
        if is_safe(v, color, graph, c):
            color[v] = c
            if graph_coloring_util(graph, colors, color, v + 1):
                return True
            color[v] = None

    return False

def graph_coloring(graph, colors):
    color = [None] * len(graph)

    if not graph_coloring_util(graph, colors, color, 0):
        print("Solution does not exist.")
        return

    print("Solution:")
    for v in range(len(graph)):
        print(f"Vertex {v + 1} is assigned color {color[v]}")

if __name__ == "__main__":
   
    num_vertices = int(input("Enter the number of vertices: "))


    print("Enter the adjacency matrix:")
    graph = []
    for _ in range(num_vertices):
        row = list(map(int, input().split()))
        graph.append(row)

    colors = input("Enter the colors (e.g., red green blue): ").split()

    graph_coloring(graph, colors)


OUTPUT:

Enter the number of vertices: 4
Enter the adjacency matrix:
0 1 1 0
 1 0 1 1
 1 1 0 1
 0 1 1 0
Enter the colors (e.g., red green blue): red green blue
Solution:
Vertex 1 is assigned color red
Vertex 2 is assigned color green
Vertex 3 is assigned color blue
Vertex 4 is assigned color red
