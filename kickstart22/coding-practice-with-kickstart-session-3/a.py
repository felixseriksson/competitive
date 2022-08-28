for case in range(1, int(input()) + 1):
    n, m = [int(x) for x in input().split()]
    c = sum([int(x) for x in input().split()])
    print(f"Case #{case}: {c % m}")