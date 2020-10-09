from collections import deque

def bfs(initialrow, initialcol):
    queue = deque()
    queue.append((initialrow, initialcol))
    while queue:
        rowindex, colindex = queue.popleft()
        material = grid[rowindex][colindex]
        grid[rowindex][colindex] = "#"
        if material == "W":
            continue
        elif material == "L" or material == "C":
            queue.append((rowindex-1, colindex))
            queue.append((rowindex, colindex-1))
            queue.append((rowindex+1, colindex))
            queue.append((rowindex, colindex+1))


rows, columns = [int(x) for x in input().split()]
grid = [["#"]*(columns+2)]
for row in range(rows):
    r = [char for char in input()]
    r.insert(0, "#")
    r.append("#")
    grid.append(r)
grid.append(["#"]*(columns+2))
#print(grid)

ctr = 0
for rowindex in range(rows+2):
    for columnindex in range(columns+2):
        if grid[rowindex][columnindex] == "L":
            ctr += 1
            bfs(rowindex, columnindex)
print(ctr)