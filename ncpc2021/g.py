# from random import randint
# n = int(input())
# l = []
# upper, left, right, lower = 10, 10, 0, 0
# for _ in range(n):
#     x, y, r = [int(x) for x in input().split()]
#     upper = max(upper, y+r)
#     left = min(left, x-r)
#     right = max(right, x+r)
#     lower = min(lower, y-r)
#     l.append([x, y, r])

# k = 100000
# s = 0
# for _ in range(k):
#     xi, yi = randint(left, right), randint(lower, upper)
#     for x, y, r in l:
#         if (x-xi)**2 + (y-yi)**2 <= r**2:
#             s += 1
#             break
# print(s/k*(right-left)*(upper-lower))

from math import pi, sqrt, atan2, sin
n = int(input())
l = []
s = 0
for _ in range(n):
    x, y, r = [int(x) for x in input().split()]
    s += pi*r*r
    maxoverlap = 0
    for otherx, othery, otherr in l:
        dx = otherx - x
        dy = othery - y
        d = sqrt(dx**2 + dy**2)
        if d > r + otherr:
            continue
        elif d < abs(r - otherr):
            minr = min(r, otherr)
            maxoverlap
            s -= pi*minr*minr
        elif d == 0 and r == otherr:
            s -= pi*r*r
        else:
            if d == r + otherr or d == r - otherr:
                continue
            else:
                chorddistance = (r**2 - otherr**2 + d**2)/(2*d)
                halfchordlength = sqrt(r**2 - chorddistance**2)
                chordmidx = x + (chorddistance*dx)/d
                chordmidy = y + (chordmidx*dy)/d
                i1 = [chordmidx + halfchordlength*dy/d, chordmidy - halfchordlength*dx/d]
                theta1 = atan2(i1[1] - y, i1[0] - x)
                i2 = [chordmidx - halfchordlength*dy/d, chordmidy + halfchordlength*dx/d]
                theta2 = atan2(i2[1] - y, i2[0] - x)
                dtheta = abs(theta1 - theta2)
                A1 = abs((r**2)/2*(theta1 - sin(theta1)))
                A2 = abs((otherr**2)/2*(theta2 - sin(theta2)))
                s -= A1
                s -= A2
    l.append([x, y, r])
print(s)