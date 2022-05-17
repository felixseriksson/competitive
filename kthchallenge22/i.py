# Insp.: https://www.geeksforgeeks.org/edit-distance-dp-5/
def dist(str1, str2, m, n):
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 2
            else:
                dp[i][j] = min(dp[i-1][j] + 2, dp[i-1][j-1] + 2)
    return dp[m][n]

a, b = input(), input()
if len(a) <= len(b):
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        else:
            a, b = a[i:], b[i:]
            break
    else:
        a, b = "", b[len(a):]
else:
    for i in range(len(b)):
        if a[i] == b[i]:
            continue
        else:
            a, b = a[i:], b[i:]
            break
    else:
        a, b = a[len(b):], ""

print(dist(a, b, len(a), len(b)))