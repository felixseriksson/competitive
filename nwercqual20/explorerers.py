from collections import Counter
from math import floor, ceil
cases = int(input())
for _ in range(cases):
    num = int(input())
    levels = Counter(sorted([int(x) for x in input().split()]))
    teams = 0
    minn = min(levels.keys())
    teams += levels[minn]
    del levels[minn]
    for val in levels:
        maxx = max(levels.keys())
        teams += floor(levels[maxx]/maxx)
        levels[maxx] %= maxx
