for case in range(int(input())):
    n = int(input())
    p = [0] + [int(x) for x in input().split()]
    pset = set(p)

    # handle degenerate tree separately
    if n == 1:
        print(1)
        print(1)
        print(1)
        print()
        continue

    leaves = [i for i in range(1, n+1) if not i in pset]
    seen = set()
    print(len(leaves))
    for l in leaves:
        path = []
        c = l
        while p[c] != c:
            path.append(c)
            seen.add(c)
            newc = p[c]
            p[c] = c
            c = newc
        if not c in seen:
            path.append(c)
            seen.add(c)
        print(len(path))
        print(" ".join([str(ch) for ch in path[::-1]]))
    print()