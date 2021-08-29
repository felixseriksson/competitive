from heapq import heapify, heappop, heappush
from collections import defaultdict
import math

with open("a2/main.txt", "r") as inputfile:
    inp = [line.strip() for line in inputfile]

cases = int(inp[0])
i = 1
out = []

for ind in range(1,cases+1):
    # string = [char for char in inp[i]]
    # i += 1
    # k = inp[i]
    # i += 1
    # fromto = []
    # for _ in range(int(k)):
    #     f, t = [char for char in inp[i]]
    #     i += 1
    #     fromto.append((f, t))

    # seen = set(["".join(string)])
    # q = [(string, 0)]
    # heapify(q)
    # found = False
    # while q:
    #     cstring, cost = heappop(q)
    #     if len(set([char for char in cstring])) == 1:
    #         found = True
    #         final = cost
    #         break
    #     for index, c in enumerate(cstring):
    #         for f, t in fromto:
    #             if f == c:
    #                 newstring = cstring[:]
    #                 newstring[index] = t
    #                 if "".join(newstring) in seen:
    #                     continue
    #                 newcost = cost + 1
    #                 heappush(q, (newstring, newcost))
    #                 seen.add("".join(newstring))
    # if found:
    #     out.append(f"Case #{ind}: {final}")
    # else:
    #     out.append(f"Case #{ind}: -1")
    string = [char for char in inp[i]]
    i += 1
    k = inp[i]
    i += 1
    fromto = defaultdict(set)
    cost = defaultdict(int)
    for _ in range(int(k)):
        f, t = [char for char in inp[i]]
        i += 1
        fromto[f].add(t)
        cost[(f, t)] = 1

    if len(set([char for char in string])) == 1:
        out.append(f"Case #{ind}: 0")
        continue
    
    already = []
    for key in fromto.keys():
        for value in fromto[key]:
            already.append((key, value))
    already = set(already)
    for a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if (a, b) not in already:
                fromto[a].add(b)
                cost[(a, b)] = float("inf")

    addedone = True
    while addedone:
        addedone = False
        for source, destinationset in fromto.items():
            for intermediate in destinationset:
                for cand in fromto[intermediate]:
                    previouscost = cost[(source, cand)]
                    intermediatecost = cost[(source, intermediate)]
                    extra = cost[(intermediate, cand)]
                    if previouscost <= intermediatecost + extra:
                        pass
                    else:
                        cost[(source, cand)] = intermediatecost + extra
                        addedone = True
    
    mincost = float("inf")
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        currcost = 0
        for sourceletter in string:
            if sourceletter != letter:
                currcost += cost[(sourceletter, letter)]
        mincost = min(mincost, currcost)
    
    if math.isinf(mincost):
        out.append(f"Case #{ind}: -1")
    else:
        out.append(f"Case #{ind}: {mincost}")

with open("a2/main-out.txt", "w") as outfile:
    for line in out:
        outfile.write(line + "\n")