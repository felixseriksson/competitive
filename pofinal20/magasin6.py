björnar, dagaride = [int(x) for x in input().split()]
dagarmånad = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
worklist = []
arbetstid = 365-dagaride
björned, björnem = [int(x) for x in input().split("/")]
björnedag = (sum(dagarmånad[:björnem-1]) + björned - 1)
björnesovtuple = ((björnedag ) % 365, (björnedag + dagaride) % 365)
for n in range(björnar-1):
    d, m = [int(x) for x in input().split("/")]
    dag = (sum(dagarmånad[:m-1]) + d - 1)
    worklist.append(((dag + dagaride)%365 ,(dag) % 365))
length = len(worklist)

worklist.append(björnesovtuple)
worklist = sorted(worklist, key=lambda x: x[0])
#print(worklist)

björneindex = worklist.index(björnesovtuple)
del worklist[björneindex]
#print(worklist)
startingindex = (björneindex - 1) % (length)
#print(björneindex, startingindex)
startpoint, goalpoint = [x for x in björnesovtuple]
if startpoint > goalpoint:
    goalflipped = True
else:
    goalflipped = False
#print(startpoint, goalpoint)
counter = 1
index = startingindex
leftbound = worklist[startingindex][0]
rightbound = worklist[startingindex][1]
broke = False
failed = False
while True:
    if goalflipped:
        if rightbound < startpoint and rightbound > goalpoint:
            broke = True
            break
    else:
        if not(rightbound > startpoint and rightbound < goalpoint):
            broke = True
            break
    if failed == True:
        break
    currentstart, currentstop = worklist[index][0],worklist[index][1]
    additive = 0
    while additive <= length:
        additive += 1
        nextstart, nextstop = worklist[(index + additive) % length][0], worklist[(index + additive) % length][1]
        if leftbound < rightbound:
            if (not (nextstart >= leftbound and nextstart <= rightbound)) and additive == 1:
                failed = True
                break
            if nextstart > leftbound and nextstart <= rightbound:
                continue
            else:
                counter += 1
                index = (index + additive-1) % length
                leftbound = worklist[index][0]
                rightbound = worklist[index][1]
                break
        else:
            if (not ((nextstart >= leftbound and nextstart <= 364) or (nextstart >= 0 and nextstart <= rightbound))) and additive == 1:
                failed = True
                break
            if not (nextstart > rightbound and nextstart < leftbound):
                continue
            else:
                counter += 1
                index = (index + additive - 1) % length
                leftbound = worklist[index][0]
                rightbound = worklist[index][1]
                break
if broke:
    print(counter)
else:
    print(-1)