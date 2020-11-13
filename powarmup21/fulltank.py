n = int(input())
lower, upper = (-1)*float("inf"), float("inf")
for _ in range(n):
    vol, pr = [int(x) for x in input().split()]
    l = (pr-5)/vol
    u = (pr+5)/vol
    lower = max(lower, l)
    upper = min(upper, u)
estimate = (lower + upper)/2
final = int(input())
print(int(round(final*estimate, -1)))