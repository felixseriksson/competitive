from collections import defaultdict
leafchildren = defaultdict(set)
parent = defaultdict(int)
for i in range(2, int(input())+1):
    p = int(input())
    leafchildren[p].add(i)
    parent[i] = p
    try:
        leafchildren[parent[p]].remove(p)
    except:
        pass
vals = set([len(a) for a in leafchildren.values()])
if 1 in vals or 2 in vals:
    print("No")
else:
    print("Yes")