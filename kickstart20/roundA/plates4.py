testcases = int(input())
for case in range(1, testcases+1):
    n, k, p = [int(x) for x in input().split()]
    a = []
    dp = [[0 for n in range(1500)] for m in range(50)]
    for i in range(n):
        dp[i+1] = dp[i].copy()
        jlist = [int(x) for x in input().split()]
        a.append(jlist)
        s = 0
        for j in range(k):
            s += a[i][j]
            for l in range(p-j+1):
                dp[i+1][l+j+1] = max(dp[i][l]+s, dp[i+1][l+j+1])
    print("Case # {}: {}".format(case, dp[n][p]))