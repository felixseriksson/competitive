n, k = [int(x) for x in input().split()]
time = [int(x) for x in input().split()]
minval = float("inf")
loss = []
if k == 1:
    print(min(time))
    exit(0)
else:
    if k == 2:
        runningsum = sum(time[:k])
        loss.append((0, 1, runningsum + k - 1, 0))
        for offset in range(n-k):
            runningsum -= time[offset]
            runningsum += time[offset + 2]
            loss.append((offset + 1, offset + 2, runningsum + k - 1, 0))
    else:
        for offset in range(n-k+1):
            runningsum = sum(time[offset:k + offset])
            maxused = max(time[offset + 1:k + offset - 1])
            loss.append((offset, offset + k - 1, runningsum + k - 1, maxused))
minval = min(minval, *[k[2] for k in loss])
for l in range(k+1, n+1):
    newloss = []
    for old in loss[:-1]:
        newa = old[0]
        newb = old[1] + 1
        newrunningsum = old[2] + 1 - time[old[1]] - old[3] + time[newb] + min(old[3], old[1])
        # obs detta funkar ju typ inte eftersom det inte är säkert att den nya är större än de andra, bara att den är mindre än den gamla största
        # !!!!!!!!!!!!!!!!!!!!
        newmaxused = "fan"
        newloss.append((newa, newb, newrunningsum, newmaxused))