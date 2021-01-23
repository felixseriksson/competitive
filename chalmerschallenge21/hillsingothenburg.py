nodes, edges = [int(x) for x in input().split()]
start, end = [int(x) for x in input().split()]
heights = [int(x) for x in input().split()]

from collections import defaultdict
from heapq import heapify, heappop, heappush

def dijkstra(g, f, t):

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
graph = defaultdict(list)
for _ in range(edges):
    fr, to = input().split()
    if heights[int(fr)-1] == heights[int(to)-1]:
        graph[fr].append((0, to))
        graph[to].append((0, fr))
    elif heights[int(fr)-1] < heights[int(to)-1]:
        diff = heights[int(to)-1] - heights[int(fr)-1]
        graph[fr].append((diff, to))
        graph[to].append((0, fr))
    else:
        diff = heights[int(fr)-1] - heights[int(to)-1]
        graph[to].append((diff, fr))
        graph[fr].append((0, to))

# output ges på formen (vikt, (sista noden,(näst sista noden,(...,(första noden,())))))
#print(edges)
res = dijkstra(graph, str(start), str(end))
#print(res)
print(int(makereadable(res)[0]))