björnar, dagaride = [int(x) for x in input().split()]
dagarmånad = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dates = set()
arbetstid = 364-dagaride
bd, bm = [int(x) for x in input().split("/")]
bdag = (sum(dagarmånad[:bm-1]) + bd -1) + dagaride
dates.add(bdag-bdag)
for n in range(björnar-1):
    d, m = [int(x) for x in input().split("/")]
    dag = (sum(dagarmånad[:m-1]) + d -1)
    dates.add((dag + dagaride - bdag) % 365)
dates = sorted(list(dates))
length = len(dates)
#print(dates)
dates.append(1000)
counter = 0
broke = False
failed = False
leftbound = 0
rightbound = arbetstid + 1
for index in range(1, length+1):
    last = dates[index-1]
    current = dates[index]
    if last >= leftbound and last <= rightbound and current > rightbound:
        counter += 1
        leftbound = last
        rightbound = last + arbetstid + 1
    if rightbound >= 365:
        broke = True
        break
if broke:
    print(counter)
else:
    print(-1)