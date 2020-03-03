from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf")

# edges = [
#     ("0", "1", 2),
#     ("1", "0", 2),
#     ("1", "2", 2),
#     ("2", "1", 2),
#     ("2", "3", 2),
#     ("3", "2", 2),
#     ("3", "4", 2),
#     ("4", "3", 2),
#     ("4", "5", 2),
#     ("5", "4", 2),
#     ("5", "6", 2),
#     ("6", "5", 2),
#     ("6", "7", 2),
#     ("7", "6", 2),
#     ("7", "8", 2),
#     ("8", "7", 2),
#     ("8", "9", 2),
#     ("9", "8", 2),
#     ("1", "7", 8),
#     ("2", "5", 5),
#     ("4", "7", 4),
#     ("6", "9", 2)
# ]

# print("=== Dijkstra ===")
# print(edges)
# print("0 -> 9:")

inputline1 = [int(char) for char in input().split()]
N, M, g = inputline1[0], inputline1[1], inputline1[2]

edges = []
edges.append(("0", "1", g))
edges.append(("1", "0", g))
edges.append((str(M), str(M-1), g))
for n in range(M)[1:]:
    edges.append((str(n), str(n+1), g))
    edges.append((str(n+1), str(n), g))
for n in range(N):
    templist = [char for char in input().split()]
    templist[2] = int(templist[2])
    if int(templist[2]) < g*(int(templist[1])-int(templist[0])):
        edges.append(tuple(templist))

print(dijkstra(edges, "0", str(M))[0])