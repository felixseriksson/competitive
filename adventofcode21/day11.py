inp = """1172728874
6751454281
2612343533
1884877511
7574346247
2117413745
7766736517
4331783444
4841215828
6857766273"""
inp = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

inp = inp.split("\n")
inp = [[int(a) for a in line] for line in inp]
H = len(inp)
W = len(inp[0])
offsets = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def updatefirst(grid):
    for i in range(H):
        for j in range(W):
            grid[i][j] += 1
    return grid

def updatelevels(grid):
    change = False
    for i in range(H):
        for j in range(W):
            if not seen[i][j] and grid[i][j] > 9:
                change = True
                seen[i][j] = 1
                for oy, ox in offsets:
                    if i+oy >= 0 and i+oy < H and j+ox >= 0 and j + ox < W:
                        grid[i+oy][j+ox] += 1
    return grid, change

def evaluateflashes(grid):
    t = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] > 9:
                grid[i][j] = 0
                t += 1
    return grid, t

def printgrid(grid):
    for line in grid:
        print(line)
    print("\n")

# part 1
# ans = 0
# for _ in range(100):
#     seen = [[0 for _ in line] for line in inp]
#     inp = updatefirst(inp)
#     flag = True
#     while flag:
#         inp, flag = updatelevels(inp)
#     # printgrid(inp)
#     inp, t = evaluateflashes(inp)
#     # printgrid(inp)
#     ans += t

# print(ans)

def checkallzeros(grid):
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0:
                return False
    return True

# part 2
i = 1
while True:
    seen = [[0 for _ in line] for line in inp]
    inp = updatefirst(inp)
    flag = True
    while flag:
        inp, flag = updatelevels(inp)
    inp, t = evaluateflashes(inp)
    if checkallzeros(inp):
        print(i)
        break
    i += 1