for case in range(1, int(input()) + 1):
    n, l = [int(input()), [int(x) for x in input().split()]]
    currentmax, ret = 0, 0
    for i in range(n):
        if i == 0:
            if i == n - 1:
                ret += 1
            elif i < n - 1:
                if l[i] > l[i + 1]:
                    ret += 1
        elif l[i] > currentmax:
            if i == n - 1:
                ret += 1
            elif i < n - 1:
                if l[i] > l[i + 1]:
                    ret += 1
        currentmax = max(currentmax, l[i])
    print(f"Case #{case}: {ret}")