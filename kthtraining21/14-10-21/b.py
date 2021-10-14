"""
Given a directed graph, find_SCC returns a list of lists containing 
the strongly connected components in topological order.
Note that this implementation can be also be used to check if a directed graph is a
DAG, and in that case it can be used to find the topological ordering of the nodes.
"""
import sys
input = sys.stdin.readline

def find_SCC(graph):
    SCC, S, P = [], [], []
    depth = [0] * len(graph)
 
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            d = depth[~node] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                del S[d:], P[-1]
                for node in SCC[-1]:
                    depth[node] = -1
        elif depth[node] > 0:
            while P[-1] > depth[node]:
                P.pop()
        elif depth[node] == 0:
            S.append(node)
            P.append(len(S))
            depth[node] = len(S)
            stack.append(~node)
            stack += graph[node]
    return SCC[::-1]
n = int(input())

g = [[] for _ in range(n)]
cost = [int(x) for x in input().split()]
for _ in range(int(input())):
    e = [int(x)-1 for x in input().split()]
    g[e[0]].append(e[1])

sccs = find_SCC(g)

mincost = 0
ways = 1

for scc in sccs:
    costs = [cost[i] for i in scc]
    m = min(costs)
    num = sum([1 if i == m else 0 for i in costs])
    mincost += m
    ways *= num
    ways %= 1000000007

print(mincost, ways)
"""
3
1 2 2
4
1 2
2 3
3 2
3 1
"""