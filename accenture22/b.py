def dist(l, x0, y0):
    x1, y1 = l
    return (x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0)

x0, y0 = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for _ in range(6)]
b = [[int(x) for x in input().split()] for _ in range(6)]

adists = [dist(x, x0, y0) for x in a]
bdists = [dist(x, x0, y0) for x in b]
aclosest = min(adists)
bclosest = min(bdists)

if aclosest == bclosest:
    print("TIE")
elif aclosest < bclosest:
    count = 0
    for d in adists:
        if d < bclosest:
            count += 1
    print("JONNA")
    print(count)
else:
    count = 0
    for d in bdists:
        if d < aclosest:
            count += 1
    print("OPPONENTS")
    print(count)