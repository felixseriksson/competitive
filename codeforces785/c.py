def checkpalindrome(integer):
    return str(integer) == str(integer)[::-1]

MOD = 10**9 + 7
palindromes = [i for i in range(1, 4*10**4 + 1) if checkpalindrome(i)]

dp = dp = [[0 for _ in range(len(palindromes) + 1)] for _ in range(4*10**4 + 1)]

for i in range(len(palindromes) + 1):
    dp[0][i] = 1
    dp[1][i] = 1
for i in range(4*10**4 + 1):
    dp[i][0] = 1

for i in range(2, 4*10**4 + 1):
    for j in range(1, len(palindromes)):
        if palindromes[j] <= i:
            dp[i][j] = (dp[i][j-1] + dp[i-palindromes[j]][j]) % MOD
        else:
            dp[i][j] = dp[i][j-1]

with open("codeforces785/c_precomp.txt", "w") as f:
    for n in range(4*10**4 + 1):
        f.write(f"{dp[n][-2]},\n")