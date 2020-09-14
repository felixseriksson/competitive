from collections import Counter
from math import floor, ceil
cases = int(input())
for _ in range(cases):
    num = int(input())
    levels = Counter(sorted([int(x) for x in input().split()]))
    teams = 0
    for val in levels.keys():
        teams += floor(levels[val]/val)
        levels[val] %= val

    kvar = sorted(levels.elements())
    team = []
    while kvar:
        last = kvar.pop(-1)
        team.append(last)
        if len(team) == last:
            teams += 1
            team = []