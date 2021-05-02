from collections import defaultdict
l, k, s = [int(x) for x in input().split()]
# l reggade tider, k rundor krävs, s deltagare
qualified = defaultdict(int)
times = defaultdict(int)
for _ in range(l):
    p, t = input().split()
    p = int(p)
    t = t.split(".")
    t = int(t[0])*60 + int(t[1])
    qualified[p] += 1
    times[p] += t

# print(times.items())
persons = [a for a in sorted(times.items(), key= lambda x: x[0]) if qualified[a[0]] >= k]
persons = sorted(persons, key= lambda x: x[1])
for p in persons:
    print(p[0])