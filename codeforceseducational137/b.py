for _ in range(int(input())):
    n = int(input())
    print(" ".join(["1", str(n), *[str(x) for x in list(range(2, n))]]))