from math import factorial
MOD = 10**9 + 7
n, k = [int(x) for x in input().split()]
for _ in range(n-1):
    input()
total = 0
for x in range(k+1):
    add = (-1)**(k-x)*(factorial(k)//(factorial(x)*factorial(k-x)))*(x)*(x-1)**(n-1) % MOD
    total += add
    total %= MOD
print(total)