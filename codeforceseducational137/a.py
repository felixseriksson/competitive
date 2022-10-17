from math import factorial

def choose(a, b):
    return factorial(a)//(factorial(b)*factorial(a - b))

t = int(input())
for _ in range(t):
    n = 10 - int(input())
    l = [int(x) for x in input().split()]
    print(choose(n, 2) * 6)