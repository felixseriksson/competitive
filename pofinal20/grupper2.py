from collections import defaultdict
from heapq import heapify, heappop, heappush

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

def makereadable(foundpath):
    # tar in input direkt från djikstras
    path = []
    for n in str(foundpath):
        if n.isalnum():
            path.append(n)
    lengthofpath = path.pop(0)
    return lengthofpath, reversed(path)
    # returnerar längden på kortaste stigen, en lista med noderna i den kortaste stigen som strings

# graphen görs av en kantlista där varje entry är en tuple på formen (från, till, vikt)
# där alltså från och till kan vara ints eller strings men vikt är en int
# edges = [
#         ("A", "B", 1),
#         ("B", "C", 1),
#         ("C", "A", 1),
#         #("A", "B", 5)
#     ]

antalstolar, antalstolpar = [int(x) for x in input().split()]
edges = []
for n in range(antalstolar):
    if n % 2 == 1:
        edges.append((n, n+1, False))
        edges.append((n+1, n, False))

for n in range(antalstolpar):
    stola, stolb = [int(x) for x in input().split()]
    edges.append((stola, stolb, True))
    edges.append((stolb, stola, True))

print(edges)