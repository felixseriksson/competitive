'''
from itertools import accumulate
testcases = int(input())

for n in range(1, testcases+1):
    stacks, perstack, totalplates = [int(x) for x in input().split()]
    dp = [[0 for j in range(perstack+1)] for i in range(stacks+1)]
    summa = [[0 for k in range(perstack)]]
    for t in range(stacks):
        summa.append(list(accumulate([int(x) for x in input().split()])))
    for i in range(1, stacks+1):
        for j in range(1, perstack+1):
            for offset in range(0, min(j, perstack)):
                dp[i][j] = max(dp[i][min(j, perstack)], summa[i][offset]+dp[i-1][min(j, perstack)-offset])

    print("Case #{}: {}".format(n, dp[stacks][perstack]))
'''
#nåt fuffens med denna orkar inte fixa
