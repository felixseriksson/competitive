import sys
input = sys.stdin.readline

n = int(input())
g = [int(x)-1 for x in input().split()]
unvisited = [True]*n

indegree = [0]*n
for target in g:
    indegree[target] += 1

sources, sinks = [], []

def dfs(node):
    sources.append(node)
    unvisited[node] = False
    nnode = g[node]
    while unvisited[nnode]:
        node = nnode
        unvisited[node] = False
        nnode = g[node]
    sinks.append(node)

for node, idg in enumerate(indegree):
    if idg == 0:
        dfs(node)

onlycycles = False
if len(sources) == 0:
    onlycycles = True
for node in range(n):
    if unvisited[node]:
        dfs(node)

if len(sources) == 1 and onlycycles:
    print(0)
else:
    sinks = sinks[1:] + [sinks[0]]
    print(len(sinks))
    for a, b in zip(sinks, sources):
        print(a+1, b+1)