MOD = 10**9 + 7
for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][1] = 1
    for j in range(k+1):
        dp[0][j] = 1

    for kval in range(2, k+1):
        dp[1][kval] = (dp[-2][kval-1] + 1) % MOD
        for nval in range(2, n+1):
            dp[nval][kval] = (dp[nval-1][kval] + dp[n-nval][kval-1]) % MOD
            
    print(dp[n][k])