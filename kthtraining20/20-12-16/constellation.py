numpoints = int(input())
points = []
for i in range(1, numpoints+1):
    points.append([*[int(k) for k in input().split()], i])
points = sorted(points)
p1 = points[0]
p2 = points[1]
for point in points[2:]:
    if not 0.5*(p1[0]*(p2[1] - point[1]) + p2[0]*(point[1] - p1[1]) + point[0]*(p1[1] - p2[1])) == 0:
        p3 = point
        break
print(*[p[2] for p in [p1, p2, p3]])