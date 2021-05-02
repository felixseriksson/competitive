def gcd(a, b):
    return b if a == 0 else gcd(b%a, a)

def digitsum(a):
    return sum([int(x) for x in str(a)])

for _ in range(int(input())):
    n = int(input())
    while gcd(n, digitsum(n)) == 1:
        n += 1
    print(n)