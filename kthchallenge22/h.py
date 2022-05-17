from collections import defaultdict

n = int(input())
grid = [[int(c) for c in input()] for _ in range(n)]

ro, co = defaultdict(int), defaultdict(int)
for r in range(n):
    for c in range(n):
        if grid[r][c]:
            ro[r] += 1
            co[c] += 1
try:
    maxcol, maxcolones = max([(key, val) for key, val in co.items()], key = lambda x: x[1])
    colrestones = sum([val for key, val in co.items() if key != maxcol])
except:
    maxcolones = 0
    colrestones = 0
colneededones = n - maxcolones + colrestones

try:
    maxrow, maxrowones = max([(key, val) for key, val in ro.items()], key = lambda x: x[1])
    rowrestones = sum([val for key, val in ro.items() if key != maxrow])
except:
    maxrowones = 0
    rowrestones = 0
rowneededones = n - maxrowones + rowrestones

if colneededones <= n and rowneededones <= n:
    print("+")
elif colneededones <= n:
    print("|")
else:
    print("-")