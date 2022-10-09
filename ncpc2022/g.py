from functools import reduce

n, k = [int(x) for x in input().split()]

p = list(sorted([float(x) for x in input().split()], reverse = True))

if n == k:
    print(reduce(lambda x, y: x * y, p, 1))
else:
    dp = [[0 for _ in range(2 * n + 1)] for _ in range(n + 1)]
    
    for j in range(0, n + 1):
        dp[0][j] = 1

    for i in range(1, n + 1):
        dp[i][n - i] = 1
        dp[i][n + i] = p[i-1]*dp[i-1][n + i -1]
        for j in range(n - i + 1, n + i):
            dp[i][j] = p[i-1]*dp[i-1][j-1] + (1-p[i-1])*dp[i-1][j+1]

    print(max([dp[i][n + k] for i in range(n+1)]))