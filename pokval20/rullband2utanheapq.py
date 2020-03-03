from collections import namedtuple, deque
from pprint import pprint as pp
 
 
inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])
 
class Graph():
    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        # print(dir(self.edges[0]))
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}
 
    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
        #pp(neighbours)
 
        while q:
            # pp(q)
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:                                  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        #pp(previous)
        s, u, pathdist = deque(), dest, dist[dest]
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s, pathdist
 
 
# graph = Graph([("0", "1", 2),  ("1", "0", 2),  ("1", "2", 2), ("1", "7", 8),
#                ("2", "1", 2),  ("2", "3", 2), ("2", "5", 5),  ("3", "2", 2),
#                ("3", "4", 2),  ("4", "3", 2),  ("4", "5", 2),  ("5", "4", 2),
#                ("5", "6", 2),  ("6", "5", 2),  ("6", "7", 2),  ("6", "9", 2),
#                ("7", "6", 2),  ("7", "8", 2),  ("8", "7", 2),  ("8", "9", 2),  
#                ("9", "8", 2)])
# pp(graph.dijkstra("0", "9")[1])

inputline1 = [int(char) for char in input().split()]
N, M, g = inputline1[0], inputline1[1], inputline1[2]
baraframåt = False #sätt till True för att testa fallen där man bara behöver gå framåt
graphlist = []
if baraframåt == False:
    graphlist.append(("0", "1", g))
    graphlist.append(("1", "0", g))
    graphlist.append((str(M), str(M-1), g))
    for n in range(M)[1:]:
        graphlist.append((str(n), str(n+1), g))
        graphlist.append((str(n+1), str(n), g))
else:
    graphlist.append(("0", "1", g))
    for n in range(M)[1:]:
        graphlist.append((str(n), str(n+1), g))

for n in range(N):
    templist = [char for char in input().split()]
    templist[2] = int(templist[2])
    graphlist.append(tuple(templist))

graph = Graph(graphlist)
shortestpath, shortestpathdistance = graph.dijkstra("0", str(M))
#print("shortest path ", shortestpath, "with distance/time ", shortestpathdistance)
print(shortestpathdistance)