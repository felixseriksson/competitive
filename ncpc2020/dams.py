from collections import defaultdict, deque
dams, waterneeded = [int(x) for x in input().split()]
children = defaultdict(list)
vals = [None]*(dams + 1)
vals[0] = [waterneeded, 0, waterneeded, waterneeded]
for dam in range(1, dams+1):
    parent, neededtobreak, there = [int(x) for x in input().split()]
    children[parent].append(dam)
    vals[dam] = [neededtobreak, there, None, None] # neededtobreak, there, neededtosupply, supplied
queue = deque([0])
havetosupply = waterneeded
best = waterneeded
while queue:
    node = queue.popleft()
    for k in children[node]:
        queue.append(k)
    needed = vals[node][2]
    there = vals[node][1]
    neededtobreak = vals[node][0]
    supplied = abs(max(neededtobreak, needed) - there)
    vals[node][3] = supplied
    for c in children[node]:
        vals[c][2] = supplied
    best = min(best, supplied)

print(best)