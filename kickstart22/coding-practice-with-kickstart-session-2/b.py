for case in range(1, int(input()) + 1):
    l, r = [int(x) for x in input().split()]
    print(f"Case #{case}: {(min(l, r)*min(l, r) + min(l, r))//2}")