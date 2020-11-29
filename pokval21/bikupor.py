from collections import defaultdict, deque
from heapq import heapify, heappop, heappush
noder, kanter, k = [int(x) for x in input().split()]
graf = defaultdict(set)
for _ in range(kanter):
    a, b = [int(x) for x in input().split()]
    graf[a].add(b)
    graf[b].add(a)

def kcalc(origk, orign, roundwetake, roundnodes, tak, neighb, av):
    ret = origk
    # ret -= (orign - upper)
    ret -= len(tak)
    if roundnodes:
        mini = min(min(roundwetake), -1*max(roundnodes))
        maxi = max(max(roundwetake), -1*min(roundnodes))
    else:
        mini = min(roundwetake)
        maxi = max(roundwetake)
    ret -= sum([1 for k in range(mini, maxi+1) if k not in roundwetake and -1*k not in roundnodes])
    return ret

def whenitdidntworkwithmax(mx, tak, neighb, av):
    tak.add(mx)
    if mx in available:
        available.remove(mx)
    if mx in neighb:
        neighb.remove(mx)
    for nb in graf[mx]:
        neighb.add(nb)
        if nb in av:
            av.remove(nb)
    return tak, neighb, av

available = set(range(1, noder+1))
neighbourtotaken = set()
taken = set()
valid = False

while available:
    source = max(available)
    roundnodes = [-source]
    heapify(roundnodes)
    roundwetake = set([])
    cantake = min(len(available), noder - k - 1)
    if valid:
        break
    while roundnodes:
        # if cantake < len(roundnodes):
        #     valid = False
        #     taken, neighbourtotaken, available = whenitdidntworkwithmax(source, taken, neighbourtotaken, available)
        rnode = -1* heappop(roundnodes)
        roundwetake.add(rnode)
        nbs = graf[rnode]
        valid = True
        for nb in nbs:
            if nb in roundwetake or -nb in roundnodes: # eller i taken eller i neighbourtotaken?
                continue
            if nb in taken:
                taken, neighbourtotaken, available = whenitdidntworkwithmax(source, taken, neighbourtotaken, available)
                break
            if nb in neighbourtotaken:
                if nb >= min(roundwetake) - kcalc(k, noder, roundwetake, roundnodes, taken, neighbourtotaken, available):
                    taken, neighbourtotaken, available = whenitdidntworkwithmax(source, taken, neighbourtotaken, available)
                    break
                else:
                    continue
            if nb >= min(roundwetake) - kcalc(k, noder, roundwetake, roundnodes, taken, neighbourtotaken, available):
                # kan möjligen behålla roundk och bara räkna om den när det behövs
                valid = False
                if cantake > 0:
                    heappush(roundnodes, -nb)
                    cantake -= 1
                else:
                    taken, neighbourtotaken, available = whenitdidntworkwithmax(source, taken, neighbourtotaken, available)
                    break
        if not roundnodes and valid:
            newk = kcalc(k, noder, roundwetake, roundnodes, taken, neighbourtotaken, available)
            newroundnodes = set()
            newmin = min(roundwetake)
            for node in roundwetake:
                tmpnbs = graf[node]
                for newnb in tmpnbs:
                    if newnb in roundwetake or -1*newnb in newroundnodes or newnb < newmin - newk:
                        continue
                    else:
                        newroundnodes.add(-1*newnb)
            if len(newroundnodes) == 0:
                valid = True
                break
            if len(newroundnodes) > cantake:
                valid = False
                taken, neighbourtotaken, available = whenitdidntworkwithmax(source, taken, neighbourtotaken, available)
                break
            else:
                valid = False
                cantake -= len(newroundnodes)
                roundnodes = [item for item in newroundnodes]
                heapify(roundnodes)
    if valid:
        validsubset = [k for k in roundwetake]
        break
if valid:
    print(len(validsubset))
    print(*validsubset)
else:
    print(-1)