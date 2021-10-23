import networkx.algorithms.approximation.traveling_salesman as tsp
import networkx as nx
datafile = "data.txt"

def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

points = []

with open(datafile, "r") as da:
    for index, line in enumerate(da):
        point = [int(l) for l in line.strip().split()]
        points.append(point)


total = 1000000
for _ in range(100):
    G = nx.Graph()
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            p1, p2 = points[i], points[j]
            d = dist(p1, p2)
            G.add_edge(i, j, weight=dist(p1, p2))
    a = tsp.christofides(G)
    temp = 0
    l = len(a)
    for i in range(l):
        n = a[i]
        m = a[(i+1)%l]
        p1 = points[n]
        p2 = points[m]
        temp += dist(p1, p2)
    print(temp)
    total = min(total, temp)
    points = points[1:] + [points[0]]
print("best:")
print(total)