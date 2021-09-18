from collections import defaultdict
n = int(input())
l = enumerate([int(x) for x in input().split()])
l = sorted(l, key=lambda x: x[0])
d = defaultdict(int)
for time, cafe in l:
    d[cafe] = time
i = sorted(d.items(), key=lambda x: x[1])
print(i[0][0])