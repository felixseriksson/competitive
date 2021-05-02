from collections import defaultdict
l, k, s = [int(x) for x in input().split()]
times = defaultdict(float)
counts = defaultdict(int)

for _ in range(l):
    person, time = input().split()
    time = time.split(".")
    time = int(time[0])*60+int(time[1])
    times[person] += time
    counts[person] += 1

finished = [a for a in sorted(counts.keys()) if counts[a] >= k]
sortedfinished = sorted(finished, key= lambda x: times[x])
for p in sortedfinished:
    print(p)