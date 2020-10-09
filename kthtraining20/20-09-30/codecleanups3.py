pushes = int(input())
pushdays = [int(x) for x in input().split()]
cleanups = 0
active = [pushdays.pop(0)]
cleanupbefore = active[0] + 20
while pushdays:
    nextpush = pushdays.pop(0)
    if nextpush >= cleanupbefore:
        cleanups += 1
        active = [nextpush]
        cleanupbefore = active[0] + 20
    else:
        if nextpush == cleanupbefore - 1:
            pass
        else:
            pass