inp = """......##
####.#..
.##....#
.##.#..#
........
.#.#.###
#.##....
####.#.."""

# part 1

# inp = [[char for char in line] for line in inp.split("\n")]
# grid = []
# for i in range(6):
#     tmp = [["." for _ in range(20)] for _ in range(20)]
#     grid.append(tmp)

# tmp = []
# for _ in range(6):
#     tmp.append(["." for _ in range(20)])

# for i in range(8):
#     tmp.append([])
#     tmp[-1].extend(["." for _ in range(6)])
#     tmp[-1].extend(inp[i])
#     tmp[-1].extend(["." for _ in range(6)])

# for _ in range(6):
#     tmp.append(["." for _ in range(20)])

# grid.append(tmp)

# for i in range(6):
#     tmp = [["." for _ in range(20)] for _ in range(20)]
#     grid.append(tmp)

# for plane in grid:
#     for row in plane:
#         print(row)
#     print()

# for cycle in range(6):
#     newgrid = [[[0 for col in row] for row in plane] for plane in grid]
#     for plane in range(len(grid)):
#         for row in range(len(grid[0])):
#             for col in range(len(grid[0][0])):
#                 cnter = 0
#                 state = grid[plane][row][col]
#                 for offset in [[1,1,1], [1,1,0], [1,1,-1], [1, 0,1], [1,0,0], [1,0,-1], [1,-1,1], [1,-1,0], [1,-1,-1], [-1,1,1], [-1,1,0], [-1,1,-1], [-1, 0,1], [-1,0,0], [-1,0,-1], [-1,-1,1], [-1,-1,0], [-1,-1,-1], [0,1,1], [0,1,0], [0,1,-1], [0,0,1], [0,0,-1], [0,-1,1], [0,-1,0], [0,-1,-1]]:
#                     try:
#                         cnter += 1 if grid[plane+offset[0]][row+offset[1]][col+offset[2]] == "#" else 0
#                     except:
#                         pass
#                 if state == "#":
#                     if cnter == 2 or cnter == 3:
#                         newgrid[plane][row][col] = "#"
#                     else:
#                         newgrid[plane][row][col] = "."
#                 elif state == ".":
#                     if cnter == 3:
#                         newgrid[plane][row][col] = "#"
#                     else:
#                         newgrid[plane][row][col] = "."
#     grid = newgrid

# ret = 0
# for plane in grid:
#     for row in plane:
#         ret += row.count("#")
# print(ret) # output: 426

# part 2
# "." for _ in x for _ in y for _ in z for _ in w

hypercube = [[[["." for _ in range(20)] for _ in range(20)] for _ in range(13)] for _ in range(13)]
inp = inp.split("\n")
for i in range(len(inp)):
    for j in range(len(inp[0])):
        hypercube[6][6][6+i][6+j] = inp[i][j]

for cycle in range(6):
    newhypercube = [[[["." for _ in range(20)] for _ in range(20)] for _ in range(13)] for _ in range(13)]
    for w in range(13):
        for z in range(13):
            for y in range(20):
                for x in range(20):
                    cnter = 0
                    state = hypercube[w][z][y][x]
                    for woffset in [-1, 0, 1]:
                        for zoffset in [-1, 0, 1]:
                            for yoffset in [-1, 0, 1]:
                                for xoffset in [-1, 0, 1]:
                                    if (woffset, zoffset, yoffset, xoffset) == (0,0,0,0):
                                        continue
                                    try:
                                        cnter += 1 if hypercube[w+woffset][z+zoffset][y+yoffset][x+xoffset] == "#" else 0
                                    except:
                                        pass
                    if state == "#":
                        if cnter == 2 or cnter == 3:
                            newhypercube[w][z][y][x] = "#"
                        else:
                            newhypercube[w][z][y][x] = "."
                    elif state == ".":
                        if cnter == 3:
                            newhypercube[w][z][y][x] = "#"
                        else:
                            newhypercube[w][z][y][x] = "."
    hypercube = newhypercube

ret = 0
for w in range(13):
    for z in range(13):
        for y in range(20):
            for x in range(20):
                ret += 1 if hypercube[w][z][y][x] == "#" else 0
print(ret) # output: 1892