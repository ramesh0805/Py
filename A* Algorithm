
import heapq
import math

class Node:
    def __init__(self, x, y, cost, heuristic, parent=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = heuristic
        self.parent = parent  # Added parent attribute to store the parent node

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def heuristic(node, goal):
    return math.sqrt((node.x - goal.x)**2 + (node.y - goal.y)**2)

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    start_node = Node(start[0], start[1], 0, heuristic(Node(start[0], start[1], 0, 0), Node(goal[0], goal[1], 0, 0)))
    priority_queue = [start_node]

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if current_node.x == goal[0] and current_node.y == goal[1]:
            path = reconstruct_path(current_node)  # Reconstruct the path from the goal node
            return int(current_node.cost), path  # Return both the cost and path

        if visited[current_node.x][current_node.y]:
            continue

        visited[current_node.x][current_node.y] = True

        neighbors = [
            (current_node.x - 1, current_node.y),
            (current_node.x + 1, current_node.y),
            (current_node.x, current_node.y - 1),
            (current_node.x, current_node.y + 1),
            (current_node.x - 1, current_node.y - 1),
            (current_node.x - 1, current_node.y + 1),
            (current_node.x + 1, current_node.y - 1),
            (current_node.x + 1, current_node.y + 1)
        ]

        for neighbor_x, neighbor_y in neighbors:
            if 0 <= neighbor_x < rows and 0 <= neighbor_y < cols and not visited[neighbor_x][neighbor_y] and grid[neighbor_x][neighbor_y] != 1:
                cost = current_node.cost + 1 if (current_node.x == neighbor_x or current_node.y == neighbor_y) else current_node.cost + math.sqrt(2)
                neighbor_node = Node(neighbor_x, neighbor_y, cost, heuristic(Node(neighbor_x, neighbor_y, 0, 0), Node(goal[0], goal[1], 0, 0)), parent=current_node)
                heapq.heappush(priority_queue, neighbor_node)

    return -1, []  # No path found, return -1 for cost and an empty path

def reconstruct_path(node):
    path = []
    while node:
        path.append((node.x, node.y))
        node = node.parent
    return path[::-1]  # Reverse the path to start from the beginning

def get_dynamic_input():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    grid = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} (0 for walkable, 1 for obstacle): ").split()))
        grid.append(row)

    start_node = tuple(map(int, input("Enter the start node (row col): ").split()))
    goal_node = tuple(map(int, input("Enter the goal node (row col): ").split()))
    goal_node = (goal_node[0], goal_node[1])  # No need to adjust for 0-indexing

    return grid, start_node, goal_node

if __name__ == "__main__":
    grid, start_node, goal_node = get_dynamic_input()

    result, path = astar(grid, start_node, goal_node)

    if result != -1:
        print(f"Shortest path length from {start_node} to {goal_node}: {result}")
        print("Path:", path)
    else:
        print("No path found.")




OUTPUT:




Enter the number of rows: 4
Enter the number of columns: 4
Enter row 1 (0 for walkable, 1 for obstacle): 0 0 1 0
Enter row 2 (0 for walkable, 1 for obstacle): 0 0 0 0
Enter row 3 (0 for walkable, 1 for obstacle): 0 0 0 1
Enter row 4 (0 for walkable, 1 for obstacle): 0 1 0 1
Enter the start node (row col): 0 3
Enter the goal node (row col): 3 2
Shortest path length from (0, 3) to (3, 2): 3
Path: [(0, 3), (1, 3), (2, 2), (3, 2)]
