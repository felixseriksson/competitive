from itertools import permutations
lists = [[False for _ in range(60)] for _ in range(8)]

def listcost(l, n):
    cost = 0
    for i in range(0, n-1):
        j = l.index(min(l[i:])) + 1
        l[i:j] = list(reversed(l[i:j]))
        cost += j - i
    return cost

for n in range(2, 8):
    p = permutations(list(range(1, n+1)))
    for per in p:
        c = listcost(list(per), n)
        if not lists[n][c]:
            lists[n][c] = per

for case in range(1, int(input())+1):
    reqlength, reqcost = [int(x) for x in input().split()]
    try:
        if lists[reqlength][reqcost]:
            s = " ".join([str(char) for char in lists[reqlength][reqcost]])
            print("Case #{}: {}".format(case, s))
        else:
            print("Case #{}: IMPOSSIBLE".format(case))
    except:
        print("Case #{}: IMPOSSIBLE".format(case))