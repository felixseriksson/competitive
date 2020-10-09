pushes = int(input())
pushdays = [int(x) for x in input().split()]
cleanups = 0
active = [pushdays.pop(0)]
nextcleanup = active[0] + 19
while pushdays:
    nextpush = pushdays.pop(0)
    if nextpush > nextcleanup:
        cleanups += 1
        active = [nextpush]
        nextcleanup = active[0] + 19
    elif nextpush == nextcleanup:
        cleanups += 1
        active = []
        nextcleanup = float("inf")
    else:
        active.append(nextpush)
        for k in range(21):
            n = active[-1] + k
            dirtiness = sum([n - x for x in active])
            if dirtiness >= 20:
                nextcleanup = active[-1] + k - 1
                break

print(cleanups + 1 if active else cleanups)