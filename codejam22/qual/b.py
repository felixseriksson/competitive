for case in range(1, int(input()) + 1):
    c, m, y, k = 10**6, 10**6, 10**6, 10**6
    for _ in range(3):
        colors = [int(x) for x in input().split()]
        c = min(c, colors[0])
        m = min(m, colors[1])
        y = min(y, colors[2])
        k = min(k, colors[3])
    if c + m + y + k < 10**6:
        print(f"Case #{case}: IMPOSSIBLE")
    else:
        c = min(c, 10**6)
        m = min(m, 10**6 - c)
        y = min(y, 10**6 - c - m)
        k = min(k, 10**6 - c - m - y)
        print(f"Case #{case}: {c} {m} {y} {k}")