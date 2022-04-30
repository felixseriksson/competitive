from os import getcwd

def checkpalindrome(integer):
    return str(integer) == str(integer)[::-1]

def getpartitions(numset, biggernum):
    size_numset = len(numset)
    dp = [[0 for _ in range(biggernum + 1)] for _ in range(size_numset + 1)]
    dp[0][0] = 1

    for c in range (1, biggernum+1):
        dp[0][c] = 0

    for r in range (1, size_numset+1):
        dp[r][0] = 1 

    for r in range (1, size_numset+1):
        for c in range (1, biggernum+1):
            if c >= numset[r-1]:
               dp[r][c] = (dp[r-1][c] + dp[r][c-numset[r-1]]) % MOD
            else:
               dp[r][c] = dp[r-1][c] % MOD

    return dp[size_numset][biggernum] % MOD

MOD = 10**9 + 7
palindrome = [checkpalindrome(i) for i in range(4*10**4 + 1)]

res = []

with open("c_precomp.txt", "w") as f:
    for n in range(4*10**4 + 1):
        nums = [i for i in range(1, n+1) if palindrome[i]]
        f.write(f"{getpartitions(nums, n)}\n")
        if n % 1000 == 0:
            print(n)