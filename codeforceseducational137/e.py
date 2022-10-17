p1, t1 = [int(x) for x in input().split()]
p2, t2 = [int(x) for x in input().split()]
h, s = [int(x) for x in input().split()]

# WLOG t1 <= t2
if t1 > t2:
    t1, t2 = t2, t1
    p1, p2 = p2, p1

r1, r2, r3 = p1 - s, p2 - s, p1 + p2 - s
t3 = max(t1, t2)

maxnum = h // r3 if not h % r3 else h // r3 + 1
mintime = float("inf")
for i in range(maxnum + 1):
    hi = h - i * r3
    j = hi // r1 if not hi % r1 else hi // r1 + 1
    mintime = min(mintime, i * t3 + j * t1)
print(mintime)