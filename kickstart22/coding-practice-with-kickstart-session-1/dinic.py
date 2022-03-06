from collections import deque

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

# # Test 1:
# g = DinicGraph(6, 0, 5)
# g.addedge(0, 1, 10)
# g.addedge(0, 2, 10)
# g.addedge(1, 2, 2)
# g.addedge(1, 3, 4)
# g.addedge(1, 4, 8)
# g.addedge(2, 4, 9)
# g.addedge(3, 5, 10)
# g.addedge(4, 3, 6)
# g.addedge(4, 5, 10)

# # Should be 19
# print(g.maxflow())

# Test 2:
# g = DinicGraph(6, 0, 5)
# g.addedge(0, 1, 16)
# g.addedge(0, 2, 13)
# g.addedge(1, 2, 10)
# g.addedge(1, 3, 12)
# g.addedge(2, 1, 4)
# g.addedge(2, 4, 14)
# g.addedge(3, 2, 9)
# g.addedge(3, 5, 20)
# g.addedge(4, 3, 7)
# g.addedge(4, 5, 4)

# # Should be 23
# print(g.maxflow())