for case in range(1, int(input()) + 1):
    n = int(input())
    d = sorted([int(x) for x in input().split()])
    m = 0
    cur = 1
    for val in d:
        if cur <= val:
            m += 1
            cur += 1
    print(f"Case #{case}: {m}")