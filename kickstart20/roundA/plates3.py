testcases = int(input())
for n in range(1, testcases+1):
    n, k, p = [int(x) for x in input().split()]
    dp = [[0 for i in range(p)] for j in range(n+1)]
    a = [[] for ind in range(n)]
    a.insert(0, [0 for o in range(k+1)])
    for i in range(n):
        s = 0
        tmp = [int(x) for x in input().split()]
        for kk in tmp:
            s += kk
            a[i+1].append(s)
        a[i+1].insert(0,0)
    for availablestacks in range(0, n+1):
        for usedplates in range(0, k+1):
            #for l in range((usedplates+1)):
            #    dp[availablestacks][usedplates] = max(dp[availablestacks][usedplates], a[availablestacks][usedplates-l] + dp[availablestacks-1][l])#dp[availablestacks][usedplates], dp[availablestacks][platesnotfromthisstack]+a[availablestacks][usedplates])
            for l in range(k-usedplates):
                dp[availablestacks][usedplates+l] = max(dp[availablestacks][l]+a[availablestacks][usedplates], dp[availablestacks+1][usedplates+l+1])

    print(a)
    print(dp)
