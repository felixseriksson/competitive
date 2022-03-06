from collections import deque

def countcolours(g):
    nb, nr = 0, 0
    for line in g:
        for c in line:
            if c == "B":
                nb += 1
            elif c == "R":
                nr += 1
            else:
                pass
    return nb, nr

def findcomponents(g):
    offsets = [(0, -1), (-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1)]
    ret = []
    seen = set()
    for i in range(1, len(g)):
        for j in range(1, len(g)):
            if (i, j) in seen or g[i][j] == "." or g[i][j] == "#":
                continue
            else:
                comp = [(i, j)]
                seen.add((i, j))
                q = deque([(i, j)])
                char = g[i][j]
                while len(q) > 0:
                    ci, cj = q.popleft()
                    for oi, oj in offsets:
                        if (ci + oi, cj + oj) in seen or g[ci+oi][cj+oj] != char:
                            continue
                        else:
                            seen.add((ci + oi, cj + oj))
                            q.append((ci + oi, cj + oj))
                            comp.append((ci + oi, cj + oj))
                ret.append(comp)
    return ret

def potentialwinningpaths(cs, g, clr):
    ret = []
    n = len(g) - 2
    for c in cs:
        if len(c) == 0:
            continue
        elif clr == "B" and g[c[0][0]][c[0][1]] == "B":
            lc = [c[i] for i in range(len(c)) if c[i][1] == 1]
            rc = [c[i] for i in range(len(c)) if c[i][1] == n]
        elif clr == "R" and g[c[0][0]][c[0][1]] == "R":
            lc = [c[i] for i in range(len(c)) if c[i][0] == 1]
            rc = [c[i] for i in range(len(c)) if c[i][0] == n]
        else:
            continue

        if len(lc) > 0 and len(rc) > 0:
            ret.append(c)
    
    return ret

def gridcopy(g):
    ret = []
    for line in g:
        newline = line[:]
        ret.append(newline)
    return ret

for ind in range(int(input())):
    n = int(input())
    grid = [["#" for _ in range(n+2)]]
    for _ in range(n):
        l = ["#"]
        l.extend([char for char in input()])
        l.append("#")
        grid.append(l)
    grid.append(["#" for _ in range(n+2)])

    nblue, nred = countcolours(grid)
    if nblue > nred+1 or nred > nblue + 1:
        print(f"Case #{ind+1}: Impossible")
    else:
        components = findcomponents(grid)
        bluevalidcomponents = potentialwinningpaths(components, grid, "B")
        redvalidcomponents = potentialwinningpaths(components, grid, "R")
        if nblue >= nred and len(bluevalidcomponents) > 0:
            clr = "B"
        elif nred >= nblue and len(redvalidcomponents) > 0:
            clr = "R"
        else:
            print(f"Case #{ind+1}: Nobody wins")
            continue

        valid = False
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid)-1):
                if grid[i][j] == clr:
                    newgrid = gridcopy(grid)
                    newgrid[i][j] = "."
                    newcomponents = findcomponents(newgrid)
                    validcomponents = potentialwinningpaths(newcomponents, newgrid, clr)
                    if len(validcomponents) == 0:
                        valid = True
        
        if valid:
            clr = "Blue" if clr == "B" else "Red"
            print(f"Case #{ind+1}: {clr} wins")
        else:
            print(f"Case #{ind+1}: Impossible")