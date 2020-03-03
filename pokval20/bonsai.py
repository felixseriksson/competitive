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

'''
def parents(edgelist):
    dic = {n: [] for n in range(len(edgelist)+1)}
    for edge in edgelist:
        dic[edge[1]] = [edge[0]]
    return dic
'''

def getchildren(edgelist, node, dictionary, checked, checkable, values):
    nodechildren = set()
    for edge in edgelist:
        if node == edge[0]:
            if edge[1] not in dictionary.keys():
                nodechildren.add(edge[1])
        if node == edge[1]:
            if edge[0] not in dictionary.keys():
                nodechildren.add(edge[0])
    dictionary[node] = list(nodechildren)
    values[node] = 1
    checked.append(node)
    checkable.extend(dictionary[node])
    return dictionary, checked, checkable, values

knölarN = int(input())

kanter = []
for n in range(knölarN):
    for val in input().split()[1:]:
        if [int(val), n, 1] not in kanter and [n, int(val), 1] not in kanter:
            kanter.append([n, int(val), 1])
            kanter.append([int(val), n, 1])

centre = float("inf")
centresum = float("inf")
centredepth = 0
for fr in range(knölarN):
    summa = 0
    depthmax = 0
    for to in range(knölarN):
        depth = dijkstra(kanter, fr, to)[0]
        summa += depth
        depthmax = max(depthmax, depth)
    if summa < centresum:
        centre = fr
        centresum = summa
        centredepth = depthmax

children = {}
checked = []
checkable = []
timevalues = {}
children, checked, checkable, timevalues = getchildren(kanter, centre, children, checked, checkable, timevalues)
while checkable != []:
    nodetocheck = checkable.pop(0)
    children, checked, checkable, timevalues = getchildren(kanter, nodetocheck, children, checked, checkable, timevalues)

# print(children)
# print(timevalues)

'''
while True:
    todelete = []
    for item in children:
        if children[item] == []:
            timevalues[item] = 0
            todelete.append(item)
    for item in todelete:
        del children[item]
        for n in range(len(children)):
            if item in children[n]:
                children[n].remove(item)
                break
'''
for leaf in children:
        if children[leaf] == []:
            timevalues[leaf] = 1

tabort = []

while len(children) != len(children[centre])+1:
    for leaf in children:
        if leaf not in children[centre] and children[leaf] == []:
            tabort.append(leaf)
    while tabort != []:
        grej = tabort.pop(0)
        del children[grej]
        for potentialparent in children:
            if grej in children[potentialparent]:
                children[potentialparent].remove(grej)
                timevalues[potentialparent] += timevalues[grej]
        del timevalues[grej]

timevalues.pop(centre)
times = list(timevalues.values())
times.sort(reverse=True)
times = [times[n]+n for n in range(len(times))]
print(max(times))