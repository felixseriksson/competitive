testcases = int(input())
for case in range(1, testcases+1):
    n, k, p = [int(x) for x in input().split()]
    dp = [[0 for i in range(p+1)] for j in range(n+1)]
    a = [[] for ind in range(n)]
    a.insert(0, [0 for i in range(k)])
    for i in range(n):
        s = 0
        tmp = [int(x) for x in input().split()]
        for kk in tmp:
            s += kk
            a[i+1].append(s)
        a[i+1].insert(0,0)
    for i in range(1, n+1):
        for j in range(p+1):
            for x in range(min(j, k)+1):
                dp[i][j] = max(dp[i][j], dp[i-1][j-x] + a[i][x])
    print("Case #{}: {}".format(case, dp[n][p]))