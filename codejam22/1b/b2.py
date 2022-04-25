for case in range(1, int(input()) + 1):
    n, p = [int(x) for x in input().split()]
    ps = []
    for _ in range(n):
        ps.append([int(x) for x in input().split()])
    
    minmax = [[0, 0]] + [[min(a), max(a)] for a in ps]
    diff = [b-a for a, b in minmax]
    dp = [[0, 0] for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = diff[i] + min(dp[i-1][0] + abs(minmax[i-1][0] - minmax[i][1]), dp[i-1][1] + abs(minmax[i-1][1] - minmax[i][1]))
        dp[i][1] = diff[i] + min(dp[i-1][0] + abs(minmax[i-1][0] - minmax[i][0]), dp[i-1][1] + abs(minmax[i-1][1] - minmax[i][0]))

    ans = min(dp[n][0], dp[n][1])
    print(f"Case #{case}: {ans}")