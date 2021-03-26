from math import ceil
elever, nintervalls, koplatser = [int(x) for x in input().split()]
intervalls = [[int(x) for x in input().split()] for _ in range(nintervalls)]
intervalls.extend([[-2,-1], [koplatser, koplatser+1]])
intervalls = sorted(intervalls)

def distanceworks(d):
    if d == 0:
        return True
    i, ctr, curr = 0, 0, 0
    while i <= nintervalls+1:
        if curr >= intervalls[i][0]:
            i += 1
            continue
        else:
            curr = max(curr, intervalls[i-1][1] + 1)
            people = ceil((intervalls[i][0] - curr)/d)
            ctr, curr, i = ctr + people, curr + people*d, i + 1
    return True if ctr >= elever else False

lo, hi = -1, koplatser+1
while hi > lo:
    mid = lo + (hi - lo) // 2
    if distanceworks(mid) and not distanceworks(mid+1):
        break
    elif distanceworks(mid):
        lo = mid
    else:
        hi = mid
print(mid)