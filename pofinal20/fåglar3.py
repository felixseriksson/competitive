from collections import defaultdict
import sys

nodantal, fågelantal, k = [int(x) for x in input().split()]
graf = defaultdict(list)

for n in range(nodantal-1):
    a, b = [int(x) for x in input().split()]
    graf[a].append(b)
    graf[b].append(a)

def dfs(root, grafdict):
    for child in grafdict[root]:
        if len(orderlist) == fågelantal-1:
            return
        graf[child].remove(root)
        graf[root].remove(child)
        counterlist.append(0)
        orderlist[root] = max(orderlist[root], len(counterlist))
        dfs(child, grafdict)
    counterlist.append(0)
    orderlist[root] = max(orderlist[root], len(counterlist))
    return

childrentotestfrom = graf[k]
graf[k] = []
for cchild in childrentotestfrom:
    graf[cchild].remove(k)
    counterlist = []
    orderlist = defaultdict(int)
    dfs(cchild, graf)
    if len(orderlist) < fågelantal-1:
        continue
    string = " ".join(str(x) for x in sorted(orderlist, key=orderlist.get, reverse=True))
    string = string + " " + str(k)
    print(string)
    exit()
else:
    print(-1)
