n = int(input())
hmin, hmax, out = dict(), dict(), dict()
althmin, althmax, altout = dict(), dict(), dict()
for i in range(1, n + 1):
    a, b, c = [int(x) for x in input().split()]
    out[i] = a
    hmin[i] = b
    hmax[i] = c
    
    if i == 1:
        altout[i] = a
        althmin[n] = b
        althmax[n] = c
    else:
        altout[n-i+2] = a
        althmin[n-i+1] = b
        althmax[n-i+1] = c

best = float("inf")
if out[1] != 0:
    best = 122 - out[1]

curr = 122
currbest = 0
for i in range(1, n):
    if curr < hmin[i]:
        currbest += hmin[i] - curr
        curr = hmin[i]
    elif curr > hmax[i]:
        currbest += curr - hmax[i]
        curr = hmax[i]
    if out[i+1] == 0:
        continue
    elif out[i+1] >= curr:
        best = min(best, currbest)
    else:
        best = min(best, currbest + curr - out[i+1])

curr = 122
currbest = 0
for i in range(1, n):
    if curr < althmin[i]:
        currbest += althmin[i] - curr
        curr = althmin[i]
    elif curr > althmax[i]:
        currbest += curr - althmax[i]
        curr = althmax[i]
    if altout[i+1] == 0:
        continue
    elif altout[i+1] >= curr:
        best = min(best, currbest)
    else:
        best = min(best, currbest + curr - altout[i+1])
print(best)