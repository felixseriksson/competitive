from math import ceil

testcases = int(input())

for case in range(1, testcases+1):
    n, k = [int(x) for x in input().split()]
    times = [int(x) for x in input().split()]
    dlower = 1 
    dupper = max(times)
    while dupper - dlower >= 1:
        dopt = (dlower + dupper) // 2
        ksum = 0
        for i in range(n-1):
            ki = ceil((times[i+1]-times[i])/dopt)-1
            ksum += ki
        if ksum >= k:
            dlower = dopt
        elif ksum < k:
            dupper = dopt
    print("Case #{}: {}".format(case, dopt))