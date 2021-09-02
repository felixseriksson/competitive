from collections import defaultdict
from heapq import heapify, heappop, heappush

with open("c1/test1.txt", "r") as inputfile:
    inp = [line.strip() for line in inputfile]

cases = int(inp[0])
i = 1
out = []

def solve(index):
    n = int(inp[index])
    value = [int(val) for val in inp[index+1].split(" ")]
    value.insert(0, 0)
    fromto = defaultdict(set)
    rootval = value[1]
    for offset in range(1, n):
        f, t = [int(node) for node in inp[index+1+offset].split(" ")]
        fromto[f].add(t)
        fromto[t].add(f)
                # (node, k, edges, nodesinpath)
    q = [(1, 1, fromto, set([1]))]
    heapify(q)
    while q:
        node, k, edges, nodesinpath = heappop(q)
        if node == 1:
            rootval = max(rootval, sum([value[node] for node in nodesinpath]))
        candidates = edges[node]
        if len(candidates) > 0:
            for cand in candidates:
                newedges = {key:set([item for item in val]) for key, val in edges.items()}
                newedges[node].remove(cand)
                newedges[cand].remove(node)
                newnodesinpath = set([m for m in nodesinpath])
                newnodesinpath.add(cand)
                heappush(q, (cand, k, newedges, newnodesinpath))
        if k > 0:
            for knode in range(1, n+1):
                if knode == node:
                    pass
                newnodesinpath = set([m for m in nodesinpath])
                newnodesinpath.add(node)
                heappush(q, (knode, k-1, edges, newnodesinpath))

    return rootval, index+n+1

for ind in range(1,cases+1):
    gold, i = solve(i)
    out.append(f"Case #{ind}: {gold}")


with open("c1/test1-out.txt", "w") as outfile:
    for line in out:
        outfile.write(line + "\n")