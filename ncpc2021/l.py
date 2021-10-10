from math import gcd
n = int(input())
m = 100000000000
for _ in range(n):
    a, b, c = [int(x) for x in input().split()]
    m = min(m, a + b*c/gcd(b,c))
print(int(m))