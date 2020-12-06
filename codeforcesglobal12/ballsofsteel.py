def dist(a, b):
    return(abs(a[0]-b[0]) + abs(a[1]-b[1]))

for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    coords = []
    for _ in range(n):
        coords.append([int(x) for x in input().split()])
    inrange = []
    for point in coords:
        inrange.append(sum([1 for otherpoint in coords if dist(point, otherpoint) <= k]))
    if len(coords) in inrange:
        print(1)
    else:
        print(-1)