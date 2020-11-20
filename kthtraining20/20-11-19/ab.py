ctr = 0
res = 0
for ch in input()[::-1]:
    if ch == "a":
        res += ctr
        ctr *= 2
    else:
        ctr += 1
    ctr %= (10**9 + 7)
print(res % (10**9 + 7))