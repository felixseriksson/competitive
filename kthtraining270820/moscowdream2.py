a, b, c, n = [int(x) for x in input().split()]
if a == 0:
    print("NO")
    exit(0)
if b == 0:
    print("NO")
    exit(0)
if c == 0:
    print("NO")
    exit(0)
totalproblems = a + b + c
if n > totalproblems:
    print("NO")
    exit(0)
if n == 1 or n == 2:
    print("NO")
    exit(0)
print("YES")