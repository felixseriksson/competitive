import sys
sys.setrecursionlimit(10**7)

def solve(minmax, curr, i):
    try:
        _ = minmax[i]
    except:
        return 0
    global r
    c1 = abs(minmax[i][0] - curr)
    c2 = abs(minmax[i][1] - curr)
    diff = minmax[i][1] - minmax[i][0]
    if r[i][0] == None:
        r1 = solve(minmax, minmax[i][1], i+1)
        r2 = solve(minmax, minmax[i][0], i+1)
        r[i][1] = r1
        r[i][0] = r2
    else:
        r1 = r[i][1]
        r2 = r[i][0]
    return diff + min(c1 + r1, c2 + r2)

for case in range(1, int(input()) + 1):
    n, p = [int(x) for x in input().split()]
    ps = []
    for _ in range(n):
        ps.append([int(x) for x in input().split()])
    
    minmax = [[min(a), max(a)] for a in ps]
    r = [[None, None] for _ in range(n)]
    ans = solve(minmax, 0, 0)

    print(f"Case #{case}: {ans}")