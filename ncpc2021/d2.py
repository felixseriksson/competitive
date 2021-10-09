from collections import deque

def exchange(k, l):
    if grid[k][l] == "#":
        return "#"
    elif grid[k][l] == ".":
        return "."
    elif grid[k][l] == 0:
        return "S"
    elif grid[k][l] == d[k][l] and grid[k][l] == seqlength:
        return "!"
    else:
        return "."

di = {"N":[-1,0], "S":[1,0], "E":[0,1], "W":[0,-1]}
offsets = [[-1,0], [1,0], [0,1], [0,-1]]

w, h = [int(x) for x in input().split()]
grid = []
d = []
start = None
for idx in range(h):
    grid.append([char for char in input()])
    d.append(grid[-1][:])
    if "S" in grid[-1]:
        start = [idx, grid[-1].index("S")]

d[start[0]][start[1]] = 0
dq = deque([start])
while dq:
    curr = dq.popleft()
    for o in offsets:
        if d[curr[0] + o[0]][curr[1] + o[1]] == "#":
            continue
        elif d[curr[0] + o[0]][curr[1] + o[1]] == ".":
            d[curr[0] + o[0]][curr[1] + o[1]] = d[curr[0]][curr[1]] + 1
            dq.append([curr[0] + o[0], curr[1] + o[1]])
        else:
            continue

grid[start[0]][start[1]] = 0
q = deque([start])
seq = [di[a] for a in input()]
seqlength = len(seq)
while q:
    curr = q.popleft()
    steps = d[curr[0]][curr[1]]
    for o in offsets:
        if steps >= seqlength:
            continue
        elif o == seq[steps]:
            continue
        elif grid[curr[0] + o[0]][curr[1] + o[1]] == "#":
            continue
        elif grid[curr[0] + o[0]][curr[1] + o[1]] == ".":
            if d[curr[0] + o[0]][curr[1] + o[1]] == d[curr[0]][curr[1]] + 1:
                grid[curr[0] + o[0]][curr[1] + o[1]] = grid[curr[0]][curr[1]] + 1
                q.append([curr[0] + o[0], curr[1] + o[1]])

for i in range(len(grid)):
    for j in range(len(grid[0])):
        grid[i][j] = exchange(i, j)

for row in grid:
    print("".join([str(a) for a in row]))
