from math import floor
pushes = int(input())
days = [int(x) for x in input().split()]
cleanups = 0
pushes = [days.pop(0)]
nextcleanup = pushes[0] + 19
while days:
    # pushes.append(days.pop(0))
    # nextcleanup = -1*(len(pushes)-1)*(pushes[0]+20) + sum(pushes[1:]) if len(pushes) != 1 else pushes[0] + 19
    # if nextcleanup < pushes[-1]:
    #     cleanups += 1
    #     pushes = []
    # else:
    #     continue
    # nextpush = days.pop(0)
    # if nextpush == nextcleanup:
    #     cleanups += 1
    #     continue
    # elif nextpush > nextcleanup:
    #     cleanups += 1
    #     nextcleanup = nextpush + 19
    # else:
    #     pushes.append(nextpush)
    #     nextcleanup = -1*(len(pushes)-1)*(pushes[0]+19)
    if len(pushes) == 0:
        pushes = [days.pop(0)]
        nextcleanup = pushes[0] + 19
    try:
        nextpush = days.pop(0)
    except:
        continue

    if nextpush > nextcleanup:
        cleanups += 1
        nextcleanup = nextpush + 19
        pushes = [nextpush]
        continue
    elif nextpush == nextcleanup:
        cleanups += 1
        pushes = []
        continue
    else:
        pushes.append(nextpush)
        k = floor((20 + sum(pushes[:-1]) - len(pushes)*pushes[-1])/len(pushes))
        nextcleanup = pushes[-1] + k
print(cleanups + 1 if pushes else cleanups)