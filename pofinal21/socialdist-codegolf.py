from math import ceil
elever, nintervalls, koplatser = [int(x) for x in input().split()]
cont, lo, hi, intervalls = [True, -1, koplatser+1, [[-2, -1]] + sorted([[int(x) for x in input().split()] for _ in range(nintervalls)]) + [[koplatser, koplatser+1]]]
def distanceworks(d, i = 0, ctr = 0, curr = 0):
    if d == 0: return True
    while i <= nintervalls+1: ctr, curr, i = (ctr, curr, i + 1) if curr >= intervalls[i][0] else (ctr + ceil((intervalls[i][0] - max(curr, intervalls[i-1][1] + 1))/d), max(curr, intervalls[i-1][1] + 1) + ceil((intervalls[i][0] - max(curr, intervalls[i-1][1] + 1))/d)*d, i + 1)
    return True if ctr >= elever else False
while hi > lo and cont == True: lo, hi, cont = (lambda x: (lo, hi, False) if (distanceworks(x) and not distanceworks(x + 1)) else (x, hi, True) if distanceworks(x) else (lo, x, True))(lo + (hi - lo) // 2)
print(lo + (hi - lo) // 2)