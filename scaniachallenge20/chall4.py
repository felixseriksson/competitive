from collections import deque
graph = [[0]*1002]
with open("C:\\Users\\felix\\Documents\\GitHub\\competitive\\scaniachallenge20\\islands.txt", "r") as file:
    for line in file:
        row = [0]
        row.extend([int(k) for k in line if k != "\n"])
        row.append(0)
        graph.append(row)
graph.append([0]*1002)

def bfs(queue, grid):
    while queue:
        currentrow, currentcol = queue.popleft()
        grid[currentrow][currentcol] = 2
        for nb in [(currentrow-1, currentcol), (currentrow+1, currentcol), (currentrow, currentcol-1), (currentrow, currentcol+1)]:
            if grid[nb[0]][nb[1]] == 1:
                queue.append(nb)
    return grid

islands = 0
for row in range(1, 1001):
    for col in range(1, 1001):
        coord = graph[row][col]
        if coord == 0 or coord == 2:
            continue
        else:
            queue = deque([(row, col)])
            islands += 1
            graph = bfs(queue, graph)

print(islands)