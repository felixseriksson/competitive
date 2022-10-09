from math import sqrt

r = int(input())
r2 = r**2

y = r+1
x = 0
mind = r+1
coords = (r+1,0)

while y >= 0:
    d = sqrt(x*x + y*y)
    if mind > d:
        mind = d
        coords = (x, y)
    if (y-1)**2 + x**2 > r2:
        y -= 1
    else:
        x += 1

print(coords[0], coords[1])

# r = int(input())

# print(1, r)
