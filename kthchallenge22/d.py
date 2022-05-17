from collections import defaultdict, deque

n, m = [int(x) for x in input().split()]

d = defaultdict(list)

for _ in range(m):
    u, v = [int(x) for x in input().split()]
    d[u].append(v)

alive = defaultdict(int)
c = 1
q = deque([c])
while d[c]:
    