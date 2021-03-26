for case in range(int(input())):
    n, l = int(input()), [int(x) for x in input().split()]
    cost = 0
    for i in range(0, n-1):
        j = l.index(min(l[i:])) + 1
        l[i:j] = list(reversed(l[i:j]))
        cost += j - i
    print("Case #{}: {}".format(case+1, cost))