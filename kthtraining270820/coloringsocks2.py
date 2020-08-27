from collections import deque
socks, cap, diff = [int(x) for x in input().split()]
sockslist = deque(sorted([int(x) for x in input().split()]))
machines = 1
val = sockslist.popleft()
maxval = val + diff
capleft = cap - 1
while sockslist:
    if capleft == 0:
        machines += 1
        capleft = cap
        maxval = None
    new = sockslist.popleft()
    if maxval == None:
        maxval = new + diff
    if new <= maxval:
        capleft -= 1
    else:
        capleft = cap - 1
        maxval = new
        machines += 1

print(machines)