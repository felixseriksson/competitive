from math import ceil

testcases = int(input())

for case in range(1, testcases+1):
    n, k = [int(x) for x in input().split()]
    times = [int(x) for x in input().split()]
    dlower = 1
    dupper = times[-1] - times[0]
    ksum = 0
    while dupper != dlower:
        dopt = (dlower + dupper) // 2
        ksum = 0
        for i in range(n-1):
            ki = ceil((times[i+1]-times[i])/dopt)-1
            ksum += ki
        if ksum < k:
            dupper = dopt
        elif ksum > k:
            dlower = dopt +1
        elif k == ksum:
            break
    while k == ksum:
        dlast = dopt
        dopt -= 1
        ksum = 0
        for i in range(n-1):
            ki = ceil((times[i+1]-times[i])/dopt)-1
            ksum += ki
        
        
    # alts = [dopt - 1, dopt, dopt + 1]
    # last = float("inf")
    # for k in alts:
    #     for i in range(n-1):
    #         ki = ceil((times[i+1]-times[i])/dopt)-1
    #         ksum += ki
    #     if last <
    # while k == ksum:
    #     dlast = dopt
    #     dopt -= 1
    #     ksum = 0
    #     for i in range(n-1):
    #         ki = ceil((times[i+1]-times[i])/dopt)-1
    #         ksum += ki
    print("Case #{}: {}".format(case, dlast))#dlast))