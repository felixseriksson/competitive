from collections import deque

OFFSETS = [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1), (0, -1)]

class FlowEdge():
    """
        Directed edge from u to v with flow flow out
        of a possible cap capacity.
    """
    def __init__(self, u, v, cap, flow = 0):
        self.u = u
        self.v = v
        self.cap = cap
        self.flow = flow

class DinicGraph():
    """
        Dinic's algorithm. Computes maximum flow from node s to node t in O(VE^2) in general,
        but in O(min(V^(2/3), E^(1/2))*E) for unit flow capacities.

        # TODO check if this is only for unit flow capacities or also float

        See https://cp-algorithms.com/graph/dinic.html and https://en.wikipedia.org/wiki/Dinic%27s_algorithm

        Usage: TODO fill in
    """
    def __init__(self, n, s, t):
        """
            # TODO: Add description
        """
        self.flowinf = float("inf")
        self.n = n
        self.m = 0
        self.s = s
        self.t = t

        self.edges = []
        self.adj = [[] for _ in range(n)]
        self.level = []
        self.ptr = []
        self.q = deque([])


    def addedge(self, u, v, cap):
        """
            # TODO Add description
        """
        self.edges.append(FlowEdge(u, v, cap))
        self.edges.append(FlowEdge(v, u, 0))
        self.adj[u].append(self.m)
        self.adj[v].append(self.m + 1)
        self.m += 2

    def bfs(self):
        """
            # TODO Add description
        """
        while self.q:
            u = self.q.popleft()
            for ind in self.adj[u]:
                if self.edges[ind].cap - self.edges[ind].flow < 1:
                    continue
                if self.level[self.edges[ind].v] != -1:
                    continue
                self.level[self.edges[ind].v] = self.level[u] + 1
                self.q.append(self.edges[ind].v)
        return self.level[self.t] != -1

    def dfs(self, u, pushed):
        """
            # TODO Add description
        """
        if pushed == 0:
            return 0
        if u == self.t:
            return pushed
        for cind in range(self.ptr[u], len(self.adj[u])):
            ind = self.adj[u][cind]
            v = self.edges[ind].v
            if self.level[u] + 1 != self.level[v] or self.edges[ind].cap - self.edges[ind].flow < 1:
                continue
            tr = self.dfs(v, min(pushed, self.edges[ind].cap - self.edges[ind].flow))
            if tr == 0:
                continue
            self.edges[ind].flow += tr
            if ind % 2:
                self.edges[ind-1].flow -= tr
            else:
                self.edges[ind+1].flow -= tr
            
            return tr
        
        return 0


    def maxflow(self):
        """
            # TODO Add description
        """
        if len(self.edges) == 0:
            return 0

        f = 0
        while True:
            self.level = [-1]*self.n
            self.level[self.s] = 0
            self.q.append(self.s)
            if not self.bfs():
                break
            self.ptr = [0]*self.n
            pushed = self.dfs(self.s, self.flowinf)
            while pushed:
                f += pushed
                pushed = self.dfs(self.s, self.flowinf)
        
        return f

def makemaingraph(g, d):
    nodes = d.keys()
    for ci, cj in nodes:
        for oi, oj in OFFSETS:
            ni, nj = ci + oi, cj + oj
            if (ni, nj) in nodes:
                fridx = d[(ci, cj)]
                toidx = d[ni, nj]
                g.addedge(fridx, toidx, 1)
    return g

for case in range(1, int(input()) + 1):
    n = int(input())
    grid = [[char for char in input()] for _ in range(n)]

    blueindex, redindex, bidx, ridx = dict(), dict(), 0, 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "B":
                blueindex[(i, j)] = bidx
                bidx += 1
            elif grid[i][j] == "R":
                redindex[(i, j)] = ridx
                ridx += 1
    
    nblue, nred = len(blueindex), len(redindex)
    if nblue > nred + 1 or nred > nblue + 1:
        print(f"Case #{case}: Impossible")
        continue

    blues, bluet, reds, redt = bidx, bidx+1, ridx, ridx+1

    bluegraph = DinicGraph(nblue + 2, blues, bluet)
    bluegraph = makemaingraph(bluegraph, blueindex)
    
    for node in [node for node in blueindex.keys() if node[1] == 0]:
        bluegraph.addedge(blues, blueindex[node], 1)
    
    for node in [node for node in blueindex.keys() if node[1] == n-1]:
        bluegraph.addedge(blueindex[node], bluet, 1)

    blueflow = bluegraph.maxflow()
    if blueflow >= 2:
        print(f"Case #{case}: Impossible")
    else:
        bluecanwin = True if blueflow == 1 else False
        
        redgraph = DinicGraph(nred + 2, reds, redt)
        redgraph = makemaingraph(redgraph, redindex)
        
        for node in [node for node in redindex.keys() if node[0] == 0]:
            redgraph.addedge(reds, redindex[node], 1)
        
        for node in [node for node in redindex.keys() if node[0] == n-1]:
            redgraph.addedge(redindex[node], redt, 1)
        
        redflow = redgraph.maxflow()
        if redflow >= 2:
            print(f"Case #{case}: Impossible")
        else:
            redcanwin = True if redflow == 1 else False

            if bluecanwin and nred > nblue:
                print(f"Case #{case}: Impossible")
            elif redcanwin and nblue > nred:
                print(f"Case #{case}: Impossible")
            else:
                if bluecanwin and redcanwin:
                    print(f"Case #{case}: Impossible")
                elif bluecanwin and not redcanwin:
                    print(f"Case #{case}: Blue wins")
                elif not bluecanwin and redcanwin:
                    print(f"Case #{case}: Red wins")
                else:
                    print(f"Case #{case}: Nobody wins")