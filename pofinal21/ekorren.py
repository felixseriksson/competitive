from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N, K = [int(x) for x in input().split()]
nuts = set([int(x) for x in input().split()])
edges = defaultdict(list)
visited = set()
for _ in range(N-1):
    a, b = [int(x) for x in input().split()]
    edges[a].append(b)
    edges[b].append(a)

ctr = -2

def nutchase(node):
    global ctr
    if node in visited:
        return False
    visited.add(node)
    
    subtrees = False
    for child in edges[node]:
        if nutchase(child):
            subtrees = True
    
    if subtrees or node in nuts:
        ctr += 2
        return True

    return False

nutchase(1)
print(ctr)