from math import ceil
cases = int(input())
for case in range(1, cases + 1):
    deployments = 0
    n, k = [int(x) for x in input().split()]
    intervals = sorted([[int(x) for x in input().split()] for _ in range(n)])
    lasttime = 0
    c = intervals.pop(0)
    needed = ceil((c[1]-c[0])/k)
    deployments += needed
    lasttime = max(lasttime, c[0]) + needed*k
    while intervals:
        d = intervals.pop(0)
        if d[1] <= lasttime:
            continue
        elif d[0] >= lasttime:
            needed = ceil((d[1] - d[0])/k)
            deployments += needed
            lasttime = max(lasttime, d[0]) + needed*k
        else:
            needed = ceil((d[1] - lasttime)/k)
            deployments += needed
            lasttime = max(lasttime, d[0]) + needed*k

    print("Case #{}: {}".format(case, deployments))