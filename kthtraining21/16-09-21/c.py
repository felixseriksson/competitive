# from collections import defaultdict
n, m = [int(x) for x in input().split()]
# beatenby = defaultdict(int)
# beatenby = dic()t
# out = set()
beatenby = [0]*n
for i in range(m):
    l, r, x = [int(c) for c in input().split()]
    for knight in range(l-1, r):
        if knight == x-1:
            continue
        elif beatenby[knight]:
            continue
        else:
            beatenby[knight] = x
print(" ".join([str(beatenby[index]) for index in range(n)]))