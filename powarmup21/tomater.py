n, d = [int(x) for x in input().split()]
a = sorted([[max(1, t-d), min(n, t+d)] for t in [int(x) for x in input().split()]])
b = [a.pop(0)]
for rng in a:
    if rng[0] <= b[-1][1] + 1:
        b[-1][1] = rng[1]
    else:
        b.append(rng)
print(sum([k[1]-k[0] + 1 for k in b]))