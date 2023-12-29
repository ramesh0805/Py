from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.ver = vertices
        self.graphlist = defaultdict(list)

    def EdgeAddition(self, u, v):
        self.graphlist[u].append(v)

    def DLS(self, s, t, d):
        if s == t:
            return True
        if d <= 0:
            return False
        for i in self.graphlist[s]:
            if self.DLS(i, t, d - 1):
                return True
        return False

    def IDDFS(self, s, t, d):
        for i in range(d + 1):
            if self.DLS(s, t, i):
                return True
        return False

# Taking input from the user
tot_ver = int(input('Enter a number of vertices: '))
g = Graph(tot_ver)

for i in range(tot_ver):
    x = int(input('Enter 1st value: '))
    y = int(input('Enter 2nd value: '))
    g.EdgeAddition(x, y)

s = int(input('Enter value of source point: '))
t = int(input('Enter target point: '))
d = int(input('Enter depth value: '))

if g.IDDFS(s, t, d):
    print('Target reachable')
else:
    for i in range(tot_ver):
        d = int(input('Enter depth limit: '))
        if g.IDDFS(s, t, d):
            print('Target reachable')
            break
        else:
            print('Target is not reachable')
    else:
        print("Target is not reachable within limit")



OUTPUT:


Enter a number of vertices: 6
Enter 1st value: 0
Enter 2nd value: 1
Enter 1st value: 0
Enter 2nd value: 2
Enter 1st value: 1
Enter 2nd value: 3
Enter 1st value: 1
Enter 2nd value: 4
Enter 1st value: 2
Enter 2nd value: 5
Enter 1st value: 2
Enter 2nd value: 6
Enter value of source point: 0
Enter target point: 6
Enter depth value: 2
Target reachable
