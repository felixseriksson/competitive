from math import sqrt
def dist(a, b):
    xs = a[0] - b[0] if a[0] >= b[0] else b[0] - a[0]
    ys = a[1] - b[1] if a[1] >= b[1] else b[1] - a[1]
    return sqrt(xs**2 + ys**2)

def cross(a, b):
    return a[0]*b[1] - a[1]*b[0]

def orient(a, b, c):
    newb = [b[0] - a[0], b[1] - a[1]]
    newc = [c[0] - a[0], c[1] - a[1]]
    return cross(newb, newc)

def above(a, p):
    return p[1] >= a[1]

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def indisk(a, b, p):
    newa = [a[0] - p[0], a[1] - p[1]]
    newb = [b[0] - p[0], b[1] - p[1]]
    return dot(newa, newb) <= 0

def onsegment(a, b, p):
    return orient(a, b, p) == 0 and indisk(a, b, p)

def crossesray(a, p, q):
    d1 = 1 if above(a, q) else 0
    d2 = 1 if above(a, p) else 0
    return (d1 - d2)*orient(a, p, q) > 0

def intriangle(p1, p2, p3, p):
    numcrossings = 0
    if onsegment(p1, p2, p) or onsegment(p2, p3, p) or onsegment(p3, p1, p):
        return False
    if crossesray(p, p1, p2):
        numcrossings += 1
    if crossesray(p, p2, p3):
        numcrossings += 1
    if crossesray(p, p3, p1):
        numcrossings += 1
    if numcrossings % 2 == 0:
        return False
    else:
        return True

def inrectangle(p1, p2, p3, p4, p):
    numcrossings = 0
    if onsegment(p1, p2, p) or onsegment(p2, p3, p) or onsegment(p3, p1, p):
        return False
    if crossesray(p, p1, p2):
        numcrossings += 1
    if crossesray(p, p2, p3):
        numcrossings += 1
    if crossesray(p, p3, p1):
        numcrossings += 1
    if numcrossings % 2 == 0:
        return False
    else:
        return True

for case in range(1, int(input())+1):
    n = int(input())
    points = []
    for _ in range(n):
        p = [int(x) for x in input().split()]
        points.append(p)
    star = [int(x) for x in input().split()]
    notfound = True
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                p1, p2, p3 = points[i], points[j], points[k]
                if intriangle(p1, p2, p3, star):
                    perimeter = dist(p1, p2) + dist(p2, p3) + dist(p3, p1)
                    if notfound:
                        notfound = False
                        minperimeter = perimeter
                    else:
                        minperimeter = min(perimeter, minperimeter)
    if n >= 4:
        for i in range(n-3):
            for j in range(i+1,n-2):
                for k in range(j+1,n-1):
                    for l in range(k+1,n):
                        p1, p2, p3, p4 = points[i], points[j], points[k], points[l]
                        if inrectangle(p1, p2, p3, p4, star):
                            perimeter = dist(p1, p2) + dist(p2, p3) + dist(p3, p4) + dist(p4, p1)
                            if notfound:
                                notfound = False
                                minperimeter = perimeter
                            else:
                                minperimeter = min(perimeter, minperimeter)
    if notfound:
        print(f"Case #{case}: IMPOSSIBLE")
    else:
        print(f"Case #{case}: {minperimeter}")