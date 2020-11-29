n, k = [int(x) for x in input().split()]
times = [int(x) for x in input().split()]
current = [0]*n
offset = 1
if k == 1:
    print(min(times))
    exit(0)
for it in range(k-1):
    runningsum = times[offset-1] + current[offset-1]
    newcurrent = [0]*n
    for no in range(offset, n):
        runningsum = min(runningsum, times[no-1] + current[no-1]) + 1
        newcurrent[no] = runningsum
    current = newcurrent
    offset += 1
print(min([current[ind] + times[ind] for ind in range(n) if current[ind]]))