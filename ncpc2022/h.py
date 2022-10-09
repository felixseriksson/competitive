n = int(input())

l = [int(x) for x in input().split()]
mintoleftof = [float("inf") for _ in range(n)]
mintorightof = [float("inf") for _ in range(n)]

cmin = l[0]
for i in range(1, n):
    if l[i] < l[i-1]:
        cmin = l[i]
    mintoleftof[i] = cmin

cmin = l[-1]
for i in range(1, n):
    if l[-1 * i - 1] < l[-1 * i]:
        cmin = l[-1 * i - 1]
    mintorightof[-1 * i - 1] = cmin

maxx = 0
for i in range(1, n-1):
    maxx = max(maxx, min(l[i] - mintoleftof[i], l[i] - mintorightof[i]))

print(maxx)