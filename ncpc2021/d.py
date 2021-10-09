from collections import deque

d = {"N":[-1,0], "S":[1,0], "E":[0,1], "W":[0,-1]}
offsets = [[-1,0], [1,0], [0,1], [0,-1]]

w, h = [int(x) for x in input().split()]
grid = []
finalgrid = []
start = None
for idx in range(h):
    grid.append([char for char in input()])
    finalgrid.append(grid[-1][:])
    if "S" in grid[-1]:
        start = [idx, grid[-1].index("S")]

q = deque([start])
seq = [d[a] for a in input()]
for offset in seq[:-1]:
    r = len(q)
    for _ in range(r):
        curr = q.popleft()
        for o in offsets:
            if o == offset:
                grid[curr[0] + o[0]][curr[1] + o[1]] = "S"
            else:
                new = [curr[0] + o[0], curr[1] + o[1]]
                if grid[new[0]][new[1]] == "S" or grid[new[0]][new[1]] == "#" or grid[new[0]][new[1]] == "!":
                    continue
                else:
                    grid[new[0]][new[1]] = "!"
                    q.append(new)
    # for row in grid:
    #     print("".join(row))
    # print()
offset = seq[-1]
for curr in q:
    for o in offsets:
        if o == offset:
            continue
        else:
            new = [curr[0] + o[0], curr[1] + o[1]]
            if grid[new[0]][new[1]] == "S" or grid[new[0]][new[1]] == "#" or grid[new[0]][new[1]] == "!":
                continue
            else:
                finalgrid[new[0]][new[1]] = "!"

# print()
for row in finalgrid:
    print("".join(row))

"""
11 3
###########
#....S....#
###########
"""