from fractions import Fraction
from math import ceil
n = int(input())
h = [int(x) for x in input().split()]
hmax = max(h)
hmaxindex = h.index(hmax)
h = h[:hmaxindex+1]
if len(h) == 1:
    print(0)
    exit()
incline = Fraction(100000, 1)
for i in range(1,len(h)):
    tempinc = Fraction(hmax - h[-i-1], i)
    incline = min(incline, tempinc)

# l = 0
# height = h[0]+4
# while True:
#     if Fraction(hmax - height, hmaxindex+l) < incline:
#         print(l)
#         break
#     else:
#         l+=1
l = ceil((hmax - h[0] - 4)/incline) - hmaxindex
if l <= 0:
    l = 0
if Fraction((hmax - h[0] - 4), l + hmaxindex) == incline:
    print(l+1)
else:
    print(l)