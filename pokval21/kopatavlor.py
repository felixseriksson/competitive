# import bisect
n, k = [int(x) for x in input().split()]
time = [int(x) for x in input().split()]
minval = float("inf")
if k == 1:
    minval = min(time)
else:
    for length in range(k, n+1):
        left = 0
        right = length

        runningsum = time[left] + time[right - 1]
        sublist = time[left + 1:right - 1]
        runningsum += sum(sorted(sublist)[:k-2])
        runningsum += length - 1
        minval = min(minval, runningsum)

        for offset in range(1, n-length+1):
            runningsum = time[left + offset] + time[right + offset - 1]
            if time[left + offset] in sublist:
                sublist.remove(time[left + offset])
            if sublist:
                sublist.append(time[right + offset-2])
            runningsum += sum(sorted(sublist)[:k-2])
            runningsum += length - 1
            minval = min(minval, runningsum)

print(minval)