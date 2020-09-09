from collections import Counter
socks, cap, diff = [int(x) for x in input().split()]
sockslist = Counter([int(x) for x in input().split()])
# print(sockslist)
machines = 0
capleft = 0
overlap = 0
for key in sorted(sockslist.keys()):
    if capleft == 0:
        capleft = cap-overlap
        machines += 1
        maxval = None
    num = sockslist[key]
    if maxval == None:
        maxval = key + diff
    if key > maxval:
        machines += 1
        maxval = key + diff
    if num <= capleft:
        capleft -= num
    else:
        overlap = num - capleft
        capleft = 0

print(machines)


n = int(input("Skriv in n: "))
dlist = []
qlist = []
for num in range(n):
    d = input("Skriv in ett d: ")
    dlist.append(d)
for num in range(n):
    q = input("Skriv in ett q: ")
    qlist.append(q)
# görfinmattemedräntor(dlist, qlist)