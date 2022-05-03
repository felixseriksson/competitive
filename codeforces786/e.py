from math import ceil

def calc(a, b):
    i = ceil(2*a/3 - b/3)
    j = ceil(-a/3 + 2*b/3)
    cands = [(i-1, j-1), (i-1, j), (i, j-1), (i, j)]
    for ic, jc in cands:
        if ic >= 0 and jc >= 0 and 2*ic + jc >= a and ic + 2*jc >= b:
            return ic+jc
    m = max(a, b)
    return m//2 if not m % 2 else m//2 + 1

n = int(input())
d = [int(x) for x in input().split()]
m1, m2 = sorted(d)[:2]
# Shoot two smallest separately
op1 = (m1//2 if not m1 % 2 else m1//2 + 1) + (m2//2 if not m2 % 2 else m2//2 + 1)

# Shoot one only and hope both adjacent die
if len(d) > 2:
    op2 = min([max(x, y) for x, y in zip(d[:-1], d[2:])])
else:
    op2 = float("inf")

# Shoot two adjacent
op3 = min([calc(x, y) for x, y in zip(d[:], d[1:])])
r = min(op1, op2)
r = min(r, op3)
print(r)