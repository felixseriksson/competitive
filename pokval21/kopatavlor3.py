n, k = [int(x) for x in input().split()]
time = [int(x) for x in input().split()]
used = list(range(k))
runningsum = sum([time[q] for q in used]) + k - 1
#print(used)
#print(runningsum)
if k == 1:
    print(min(time))
    exit(0)
else:
    for nextcandidate in range(k, n):
        potential = time[nextcandidate]
        sumifexchanged = [(runningsum - time[used[0]] + potential - abs(used[0] - used[-1])  + abs(used[1] - nextcandidate))]
        for u in range(1, k):
            sumifexchanged.append(runningsum - time[used[u]] + potential - abs(used[0] - used[-1]) + abs(used[0] - nextcandidate))
        #print(sumifexchanged)
        mindex = sumifexchanged.index(min(sumifexchanged))
        #print(mindex)
        if sumifexchanged[mindex] < runningsum:
            runningsum = sumifexchanged[mindex]
            del used[mindex]
            used.append(nextcandidate)
        #print(used)
        #print(runningsum)
print(runningsum)