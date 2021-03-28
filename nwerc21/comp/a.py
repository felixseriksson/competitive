from math import ceil
threshhold, cases = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]

bestindexes, best = [None], float("inf")
for i, m in enumerate(l, 1):
    if m/i < best:
        bestindexes = [i]
        best = m/i
    elif m/i == best:
        bestindexes.append(i)

for i in range(threshhold, 2*threshhold + 1):
    best2 = float("inf")
    for j in range(0, i//2 + 1):
        best2 = min(best2, l[i-j-1] + l[j])
    l.append(best2)

for _ in range(cases):
    query = int(input())
    if query <= threshhold * 2:
        print(l[query-1])
        continue
    cost = float("inf")
    for bestindex in bestindexes:
        b = l[bestindex-1]
        num = ceil((query - (threshhold*2))/bestindex)
        cost = min(cost, int(num*b + l[query - num*bestindex -1]))
    print(cost)