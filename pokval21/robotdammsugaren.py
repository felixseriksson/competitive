rows, cols, commands = [int(x) for x in input().split()]
commandseq = input()
grid = [[char for char in input()] for _ in range(rows)]
visited = [[False for _ in range(cols)] for _ in range(rows)]
br = False
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "O":
            row, col = r, c
            br = True
            break
    if br:
        break

visited[row][col] = True
clean = 1
for cmd in commandseq:
    if cmd == "^":
        while grid[row-1][col] != "#":
            row -= 1
            if not visited[row][col]:
                visited[row][col] = True
                clean += 1
    elif cmd == ">":
        while grid[row][col+1] != "#":
            col += 1
            if not visited[row][col]:
                visited[row][col] = True
                clean += 1
    elif cmd == "v":
        while grid[row+1][col] != "#":
            row += 1
            if not visited[row][col]:
                visited[row][col] = True
                clean += 1
    elif cmd == "<":
        while grid[row][col-1] != "#":
            col -= 1
            if not visited[row][col]:
                visited[row][col] = True
                clean += 1
    else:
        print("oops")

print(clean)