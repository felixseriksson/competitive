from random import randint
n = int(input())
l = []
upper, left, right, lower = 10, 10, 0, 0
for _ in range(n):
    x, y, r = [int(x) for x in input().split()]
    upper = max(upper, y+r)
    left = min(left, x-r)
    right = max(right, x+r)
    lower = min(lower, y-r)
    l.append([x, y, r])

k = 250
c = 0
xstep = (right - left)/k
ystep = (upper - lower)/k
for i in range(k):
    for j in range(k):
        xc, yc = left + i*xstep, lower + j*ystep
        for xu, yu, ru in l:
            if (xu - xc)**2 + (yu - yc)**2 <= ru**2:
                c += 1
                break
totalarea = (upper-lower)*(right-left)
prop = c/(k*k)
print(prop*totalarea)