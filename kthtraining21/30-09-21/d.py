from collections import deque

n, k = [int(x) for x in input().split()]
seen = [0]*(2**k)
q = deque()
lastseen = None

for _ in range(n):
    num = int(input(), base=2)
    seen[num] = 1
    q.append(num)
lastseen = num

while q:
    c = q.popleft()
    seen[c] = 1
    lastseen = c
    for i in range(k):
        new = ((1 << i) ^ c)
        if not seen[new]:
            lastseen = new
            q.append(new)
print(format(lastseen, f"0{k}b"))